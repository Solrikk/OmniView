<div align="center">
  <img src="https://github.com/Solrikk/OmniView/blob/main/assets/images/techny-machine-vision-icon.png" alt="Logo" />
</div>

<div align="center">
  <h3>
    <a href="https://github.com/Solrikk/OmniView/blob/main/README.md">English</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_RU.md">Russian</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_GE.md">German</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_JP.md">Japanese</a> |
    <a href="README_KR.md">⭐Korean⭐</a> |
    <a href="README_CN.md">Chinese</a>
  </h3>
</div>

-----------------

# OmniView 👁️

## 개요:

**OmniView**는 **실시간 객체 감지** 및 **스크린샷 캡처**와 같은 기능을 제공하는 고급 비디오 시청 및 녹화 응용 프로그램입니다. 이 프로젝트는 **카메라 연결** 및 **비디오 처리**를 위해 **OpenCV 라이브러리**를 사용하여 원활하고 고품질의 비디오 스트림을 보장합니다. **Darknet API**를 통합하여 OmniView는 고급 **객체 감지** 기능을 제공하며, 비디오 피드 내 다양한 객체를 실시간으로 식별하고 추적할 수 있습니다.

![OmniView Demo](https://github.com/Solrikk/OmniView/blob/main/assets/gif/OmniView.gif)

## 기능: ✨

- **카메라 감지** 📷: 연결된 카메라를 자동으로 감지하여 목록에 표시합니다. 이 기능은 **OpenCV**를 사용하여 사용 가능한 모든 비디오 장치를 스캔하고 감지된 카메라를 목록에 추가하여 수동으로 검색할 필요를 없앱니다.

- **실시간 스트림 보기** 📺: 선택한 카메라의 실시간 비디오 피드를 실시간으로 볼 수 있습니다. 응용 프로그램은 **Tkinter** 및 **OpenCV**를 사용하여 비디오 피드를 사용자 인터페이스 내에서 직접 표시하여 사용자가 원활하게 피드를 모니터링할 수 있도록 합니다.

- **비디오 녹화** 🎥: 버튼 클릭 한 번으로 비디오 스트림을 파일에 녹화합니다. 녹화는 언제든지 시작하고 중지할 수 있으며, 결과 비디오 파일은 나중에 보기나 분석을 위해 저장됩니다. 응용 프로그램은 **XVID 코덱**을 사용하여 자동 설정으로 녹화합니다(프레임 속도 및 해상도).

- **객체 감지** 🕵️‍♂️: 실시간으로 비디오 스트림 내에서 객체를 감지하기 위해 **YOLOv3 모델**을 사용합니다. 이 모델은 다양한 유형의 객체(예: 사람, 자동차, 동물)를 강조 표시하고 해당 라벨 및 신뢰 수준과 함께 표시하여 프레임 내 객체의 식별 및 추적을 쉽게 합니다.

- **스크린샷 캡처** 📸: 고품질의 스크린샷을 찍어 원하는 폴더에 저장합니다. 이 기능은 중요한 순간을 포착하거나 추가 분석을 위해 프레임을 사용하는 데 적합합니다. 응용 프로그램은 이미 존재하지 않는 경우 사용자의 홈 디렉토리에 스크린샷을 저장할 폴더를 자동으로 만듭니다.

## 설치: 🛠️

OmniView를 시작하려면 다음 단계를 따르세요:

1. **Python 3.10** 이상이 설치되어 있는지 확인하세요.
2. 리포지토리를 클론합니다:
    ```bash
    git clone https://github.com/Solrikk/OmniView.git
    cd OmniView
    ```
3. Poetry로 종속성을 설치합니다:
    ```bash
    poetry install
    ```

## 사용 방법: 🚀

OmniView를 사용하려면 다음 간단한 단계를 따르세요:

1. 응용 프로그램을 실행합니다:
    ```bash
    poetry run python main.py
    ```
2. 제공된 목록에서 카메라를 선택하고 "View Camera"를 클릭하여 라이브 피드를 시작합니다.
3. 비디오 녹화를 시작하거나 중지하고, 스크린샷을 찍으며, 객체 감지를 활성화하는 버튼을 사용합니다.

## 종속성: 📦

OmniView는 다음 라이브러리와 도구에 의존합니다:

- **Python 3.10 이상**: 응용 프로그램은 최신 언어 기능을 활용하고 최신 라이브러리와의 호환성을 유지하기 위해 [**Python 3.10**](https://www.python.org/downloads/release/python-3100/) 이상이 필요합니다.

- **tkinter**: 사용자 인터페이스를 구성하기 위해 사용합니다. [**tkinter**](https://docs.python.org/3/library/tkinter.html)는 Python의 내장 GUI 도구 키트로, 창, 대화 상자, 버튼 및 기타 사용자 인터페이스 요소를 쉽게 만들 수 있습니다.

- **OpenCV**: 카메라 연결 관리 및 비디오 스트림 처리를 위해 사용합니다. [**OpenCV**](https://opencv.org/)는 오픈 소스 컴퓨터 비전 및 머신 러닝 소프트웨어 라이브러리로, 실시간 컴퓨터 비전 응용 프로그램에 널리 사용됩니다. 카메라, 비디오 파일 및 네트워크 스트림에서 비디오를 캡처할 수 있습니다.

- **NumPy**: 데이터 배열을 처리하는 데 필수적입니다. [**NumPy**](https://numpy.org/)는 Python에서 과학 계산을 위한 기본 패키지로, 강력한 배열 처리 기능을 제공합니다. 이미지 데이터 처리 및 객체 감지에 필요한 수학적 작업을 수행하는 데 많이 사용됩니다.

- **Pillow**: 이미지 처리 작업에 사용합니다. [**Pillow**](https://python-pillow.org/)는 Python Imaging Library (PIL)의 포크로, Python 인터프리터에 사용하기 쉬운 이미지 처리 기능을 추가합니다. 다양한 이미지 파일 형식을 열고, 조작하며, 저장할 수 있습니다.

- **Poetry**: 프로젝트 종속성을 효율적으로 관리합니다. [**Poetry**](https://python-poetry.org/)는 Python에서 종속성 관리 및 패키징을 위한 도구입니다. 프로젝트 라이브러리를 선언하고, 종속성이 서로 호환되도록 하고, 가상 환경 생성 및 활성화를 단순화하는 데 도움을 줍니다.
