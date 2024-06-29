![Logo](https://github.com/Solrikk/OmniView/blob/main/assets/result/images/orb6.png)

<div align="center">
  <h3>
    <a href="https://github.com/Solrikk/OmniView/blob/main/README.md">⭐English⭐</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_RU.md">Russian</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_GE.md">German</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_JP.md">Japanese</a> |
    <a href="README_KR.md">Korean</a> |
    <a href="README_CN.md">Chinese</a>
  </h3>
</div>

-----------------

# OmniView 👁️

## Overview

**OmniView** is an advanced video viewing and recording application packed with real-time object detection and screenshot features. Utilizing the OpenCV library for camera connection and video processing, alongside the Darknet API for object detection, OmniView is your go-to tool for comprehensive video analysis.

## Key Features ✨

- **Camera Detection** 📷: Automatically identifies and lists connected cameras. This feature utilizes **OpenCV** to scan for all available video devices and adds the detected cameras to a list for user selection, eliminating the need for manual device searching.

- **Live Stream Viewing** 📺: View live video feed from your selected camera in real-time. The application uses **Tkinter** and **OpenCV** to display the video feed directly within the user interface, allowing users to monitor the camera feed seamlessly.

- **Video Recording** 🎥: Record video streams to a file with just a click. The recording can be started and stopped at any time, and the resulting video file is saved for later viewing or analysis. The application uses the **XVID codec** for recording, with automatic settings for frame rate and resolution.

- **Object Detection** 🕵️‍♂️: Leverages the **YOLOv3** model for detecting objects within the video stream in real-time. This model highlights various types of objects (e.g., people, cars, animals) and displays them with corresponding labels and confidence levels, making it easier to identify and track objects in the frame.

- **Screenshot Capture** 📸: Take high-quality screenshots and save them in your desired folder. This feature is ideal for capturing important moments or using the frames for further analysis. The application automatically creates a folder in the user's home directory for storing screenshots if it doesn't already exist.

## Installation 🛠️

To get started with OmniView, follow these steps:

1. Ensure you have **Python 3.10** or higher installed.
2. Clone the repository:
    ```bash
    git clone https://github.com/Solrikk/OmniView.git
    cd OmniView
    ```
3. Install dependencies using Poetry:
    ```bash
    poetry install
    ```

## Usage 🚀

Follow these simple steps to use OmniView:

1. Launch the application:
    ```bash
    poetry run python main.py
    ```
2. Select a camera from the provided list and click "View Camera" to start the live feed.
3. Utilize the buttons available to start or stop video recording, take screenshots, and enable object detection.

## Dependencies 📦

OmniView relies on the following libraries and tools:

- **Python 3.10 and above**
- **tkinter**: For constructing the user interface.
- **OpenCV**: To manage camera connections and process video streams.
- **NumPy**: Essential for handling data arrays.
- **Pillow**: Used for image processing tasks.
- **Poetry**: Manages project dependencies efficiently.
