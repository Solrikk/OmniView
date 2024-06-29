<div align="center">
  <img src="https://github.com/Solrikk/OmniView/blob/main/assets/images/techny-machine-vision-icon.png" alt="Logo" />
</div>

<div align="center">
  <h3>
    <a href="https://github.com/Solrikk/OmniView/blob/main/README.md">English</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_RU.md">Russian</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_GE.md">German</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_JP.md">Japanese</a> |
    <a href="README_KR.md">Korean</a> |
    <a href="README_CN.md">⭐Chinese⭐</a>
  </h3>
</div>

-----------------

# OmniView 👁️

## 概述：

**OmniView** 是一个高级的视频观看和录制应用程序，提供 **实时对象检测** 和 **截图** 等功能。该项目使用 **OpenCV库** 用于 **摄像头连接** 和 **视频处理**，确保流畅和高质量的视频流。通过集成 **Darknet API**，OmniView 提供先进的 **对象检测** 功能，能够实时识别和追踪视频流中的各种对象。

![OmniView Demo](https://github.com/Solrikk/OmniView/blob/main/assets/gif/OmniView.gif)

## 功能: ✨

- **摄像头检测** 📷: 自动识别和列出已连接的摄像头。此功能使用 **OpenCV** 扫描所有可用的视频设备，并将检测到的摄像头添加到供用户选择的列表中，无需手动搜索设备。

- **实时流观看** 📺: 实时查看所选摄像头的实时视频流。应用程序使用 **Tkinter** 和 **OpenCV** 直接在用户界面中显示视频流，允许用户无缝监控摄像头的视频流。

- **视频录制** 🎥: 一键将视频流录制到文件中。录制可以随时开始和停止，生成的视频文件会被保存以供以后查看或分析。应用程序使用 **XVID 编解码器** 进行录制，并自动设置帧速率和分辨率。

- **对象检测** 🕵️‍♂️: 使用 **YOLOv3 模型** 实时检测视频流中的对象。该模型突出显示各种类型的对象（例如，人、车、动物），并显示相应的标签和置信度，使识别和追踪帧中的对象变得更加容易。

- **截图** 📸: 拍摄高质量的截图并将其保存到您指定的文件夹。此功能非常适合捕捉重要瞬间或用于进一步分析应用程序会自动在用户的主目录中创建一个文件夹以保存截图（如果该文件夹不存在）。

## 安装: 🛠️

开始使用 OmniView，请按照以下步骤操作：

1. 确认已安装 **Python 3.10** 或更高版本。
2. 克隆存储库：
    ```bash
    git clone https://github.com/Solrikk/OmniView.git
    cd OmniView
    ```
3. 使用 Poetry 安装依赖项：
    ```bash
    poetry install
    ```

## 使用方法: 🚀

按照以下简单步骤使用 OmniView：

1. 启动应用程序：
    ```bash
    poetry run python main.py
    ```
2. 从提供的列表中选择一个摄像头，然后点击“View Camera”以开始查看实时视频流。
3. 使用可用的按钮开始或停止视频录制、拍摄截图以及启用对象检测。

## 依赖项: 📦

OmniView 依赖以下库和工具：

- **Python 3.10 及以上**：应用程序要求 [**Python 3.10**](https://www.python.org/downloads/release/python-3100/) 或更高版本，以利用最新的语言功能并确保与现代库的兼容性。

- **tkinter**: 用于构建用户界面。 [**tkinter**](https://docs.python.org/3/library/tkinter.html) 是 Python 的内置 GUI 工具包，提供了一种简单的方法来创建窗口、对话框、按钮和其他用户界面元素。

- **OpenCV**: 用于管理摄像头连接和视频处理。 [**OpenCV**](https://opencv.org/) 是一个开源的计算机视觉和机器学习软件库，广泛用于实时计算机视觉应用。它可以捕获来自摄像头、视频文件甚至网络流的视频。

- **NumPy**: 处理数据数组的必备工具。 [**NumPy**](https://numpy.org/) 是一个用于科学计算的基本 Python 包，提供强大的数组处理功能。它广泛用于处理图像数据并执行对象检测所需的数学运算。

- **Pillow**: 用于图像处理任务。 [**Pillow**](https://python-pillow.org/) 是 Python Imaging Library (PIL) 的分支，为 Python 解释器添加了易于使用的图像处理功能。它能够打开、操作和保存多种图像文件格式。

- **Poetry**: 有效管理项目依赖项。 [**Poetry**](https://python-poetry.org/) 是一个用于 Python 中的依赖项管理和打包的工具。它有助于声明项目库，确保依赖项彼此兼容，并简化虚拟环境的创建和激活。
