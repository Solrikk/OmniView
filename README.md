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

# OmniView

## Description

**OmniView** is a powerful video viewing and recording application equipped with real-time object detection and screenshot capabilities. The application uses the OpenCV library to connect to cameras and perform video processing, as well as the Darknet API for object detection.

## Key Features

- **Camera Detection**: Automatically detect connected cameras.
- **Live View**: View live video from the selected camera.
- **Video Recording**: Record video stream to a file.
- **Object Detection**: Detect objects in the video using the YOLOv3 model.
- **Screenshots**: Capture screenshots and save them to the selected folder.

## Installation

1. Ensure you have Python 3.10 or higher installed.
2. Clone the repository:
    ```bash
    git clone https://github.com/Solrikk/OmniView.git
    cd OmniView
    ```
3. Install dependencies:
    ```bash
    poetry install
    ```

## Usage

1. Run the application:
    ```bash
    poetry run python main.py
    ```
2. Select a camera from the list and click "View Camera" to start viewing.
3. Use the buttons to start recording, take screenshots, and activate object detection.

## Dependencies

- **Python 3.10 and above**
- **tkinter**: for creating the user interface.
- **OpenCV**: for connecting to cameras and processing video.
- **NumPy**: for working with data arrays.
- **Pillow**: for image processing.
- **Poetry**: for dependency management.
