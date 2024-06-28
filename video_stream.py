import tkinter as tk
from tkinter import messagebox, Label, filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
import os

class CameraApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Camera Viewer")
        self.cameras = self.detect_cameras()
        self.create_widgets()

        prototxt_path = "deploy.prototxt"
        model_path = "mobilenet_iter_73000.caffemodel"
        self.net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)
        self.classNames = {0: 'background', 1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat',
                           5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair', 10: 'cow',
                           11: 'diningtable', 12: 'dog', 13: 'horse', 14: 'motorbike', 15: 'person',
                           16: 'pottedplant', 17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor'}
        self.is_recording = False
        self.output = None

    def detect_cameras(self):
        index = 0
        arr = []
        while True:
            cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
            if not cap.read()[0]:
                break
            else:
                arr.append(index)
            cap.release()
            index += 1
        return arr

    def create_widgets(self):
        if not self.cameras:
            messagebox.showinfo("Info", "No cameras detected.")
            self.master.quit()
            return

        self.label = tk.Label(self.master, text="Select a camera:")
        self.label.pack(pady=10)

        self.camera_var = tk.StringVar(value=self.cameras[0])
        for cam in self.cameras:
            tk.Radiobutton(self.master, text=f"Camera {cam}", variable=self.camera_var, value=cam).pack(anchor=tk.W)

        self.view_button = tk.Button(self.master, text="View Camera", command=self.view_camera)
        self.view_button.pack(pady=10)

        self.record_button = tk.Button(self.master, text="Start Recording", command=self.toggle_recording)
        self.record_button.pack(pady=10)

        self.screenshot_button = tk.Button(self.master, text="Take Screenshot", command=self.take_screenshot)
        self.screenshot_button.pack(pady=10)

        self.snapshot_folder = os.path.join(os.path.expanduser("~"), "camera_snapshots")
        if not os.path.exists(self.snapshot_folder):
            os.makedirs(self.snapshot_folder)
    
    def view_camera(self):
        self.cam_index = int(self.camera_var.get())
        self.cap = cv2.VideoCapture(self.cam_index, cv2.CAP_DSHOW)

        if not self.cap.isOpened():
            messagebox.showerror("Error", "Cannot open camera.")
            return

        self.window = tk.Toplevel(self.master)
        self.window.title(f"Camera {self.cam_index}")
        self.display = Label(self.window)
        self.display.pack()

        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            messagebox.showerror("Error", "Cannot read frame.")
            self.window.destroy()
            return

        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
        self.net.setInput(blob)
        detections = self.net.forward()

        h, w = frame.shape[:2]
        for i in np.arange(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > 0.2:  # Порог уверенности
                idx = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                label = f"{self.classNames[idx]}: {round(confidence * 100, 2)}%"
                cv2.rectangle(frame, (startX, startY), (endX, endY), (255, 0, 0), 2)
                y = startY - 15 if startY - 15 > 15 else startY + 15
                cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        if self.is_recording and self.output:
            self.output.write(frame)

        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.display.imgtk = imgtk
        self.display.configure(image=imgtk)

        self.window.after(10, self.update_frame)

    def toggle_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.record_button.config(text="Stop Recording")
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.output = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
        else:
            self.is_recording = False
            self.record_button.config(text="Start Recording")
            self.output.release()

    def take_screenshot(self):
        if not hasattr(self, 'cap') or not self.cap.isOpened():
            messagebox.showerror("Error", "Camera is not open.")
            return

        ret, frame = self.cap.read()
        if not ret:
            messagebox.showerror("Error", "Cannot read frame.")
            return

        filepath = os.path.join(self.snapshot_folder, "screenshot.png")
        cv2.imwrite(filepath, frame)
        messagebox.showinfo("Info", f"Screenshot saved to {filepath}")

    def on_closing(self):
        if self.is_recording and self.output:
            self.output.release()
        self.cap.release()
        self.window.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = CameraApp(root)
    root.mainloop()