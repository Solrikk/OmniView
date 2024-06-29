<div align="center">
  <img src="https://github.com/Solrikk/OmniView/blob/main/assets/images/techny-machine-vision-icon.png" alt="Logo" />
</div>

<div align="center">
  <h3>
    <a href="https://github.com/Solrikk/OmniView/blob/main/README.md">English</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_RU.md">Russian</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_GE.md">German</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_JP.md">⭐Japanese⭐</a> |
    <a href="README_KR.md">Korean</a> |
    <a href="README_CN.md">Chinese</a>
  </h3>
</div>

-----------------

# OmniView 👁️

## 概要:

**OmniView** は、**リアルタイムオブジェクト検出** や **スクリーンショットキャプチャ** などの機能を提供する高度なビデオ視聴および録画アプリケーションです。このプロジェクトは、**カメラ接続** および **ビデオ処理** のために **OpenCVライブラリ** を使用し、スムーズで高品質なビデオストリームを保証します。**Darknet API** を統合することで、OmniViewは高度な **オブジェクト検出** 機能を提供し、ビデオフィード内のさまざまなオブジェクトをリアルタイムで識別および追跡することができます。

![OmniView Demo](https://github.com/Solrikk/OmniView/blob/main/assets/gif/OmniView.gif)

## 機能: ✨

- **カメラ検出** 📷: 接続されたカメラを自動的に検出してリストに表示します。この機能は **OpenCV** を使用して利用可能なすべてのビデオデバイスをスキャンし、検出されたカメラをリストに追加して、手動でデバイスを検索する必要をなくします。

- **ライブストリーム視聴** 📺: 選択したカメラのライブビデオフィードをリアルタイムで表示します。アプリケーションは **Tkinter** と **OpenCV** を使用してビデオフィードをユーザーインターフェース内に直接表示し、ユーザーがシームレスにフィードを監視できるようにします。

- **ビデオ録画** 🎥: ボタンをクリックするだけでビデオストリームをファイルに録画します。録画はいつでも開始および停止でき、結果のビデオファイルは後で見るためや分析のために保存されます。アプリケーションは **XVIDコーデック** を使用して録画し、フレームレートや解像度の自動設定を行います。

- **オブジェクト検出** 🕵️‍♂️: リアルタイムでビデオストリーム内のオブジェクトを検出するために **YOLOv3モデル** を使用します。このモデルはさまざまな種類のオブジェクト（例：人、車、動物）を強調表示し、対応するラベルと信頼レベルと共に表示します。これにより、フレーム内のオブジェクトの識別および追跡が容易になります。

- **スクリーンショットキャプチャ** 📸: 高品質のスクリーンショットを撮影し、希望のフォルダに保存します。この機能は重要な瞬間をキャプチャしたり、さらなる分析のためにフレームを使用するのに最適です。アプリケーションは、既に存在しない場合、スクリーンショットを保存するためにユーザーのホームディレクトリ内にフォルダを自動的に作成します。

## インストール: 🛠️

OmniViewを開始するには、以下の手順に従ってください：

1. **Python 3.10** 以上がインストールされていることを確認します。
2. リポジトリをクローンします：
    ```bash
    git clone https://github.com/Solrikk/OmniView.git
    cd OmniView
    ```
3. Poetryで依存関係をインストールします：
    ```bash
    poetry install
    ```

## 使用方法: 🚀

OmniViewを使用するには、以下の簡単な手順に従ってください：

1. アプリケーションを起動します：
    ```bash
    poetry run python main.py
    ```
2. 提供されたリストからカメラを選択し、「View Camera」をクリックしてライブフィードを開始します。
3. ビデオ録画を開始または停止したり、スクリーンショットを撮ったり、オブジェクト検出を有効にしたりするためのボタンを使用します。

## 依存関係: 📦

OmniViewは以下のライブラリとツールに依存しています：

- **Python 3.10以上**: アプリケーションは最新の言語機能を利用し、最新のライブラリとの互換性を保つために [**Python 3.10**](https://www.python.org/downloads/release/python-3100/) 以上を必要とします。

- **tkinter**: ユーザーインターフェースの構築に使用します。 [**tkinter**](https://docs.python.org/3/library/tkinter.html) はPythonの組み込みGUIツールキットで、ウィンドウ、ダイアログ、ボタンなどのユーザーインターフェース要素を簡単に作成できます。

- **OpenCV**: カメラ接続の管理およびビデオストリームの処理に使用します。 [**OpenCV**](https://opencv.org/) はリアルタイムコンピュータビジョンアプリケーションで広く使用されているオープンソースのコンピュータビジョンおよび機械学習ソフトウェアライブラリです。カメラ、ビデオファイル、およびネットワークストリームからビデオをキャプチャすることができます。

- **NumPy**: データ配列の処理に不可欠です。 [**NumPy**](https://numpy.org/) はPythonでの科学計算のための基本的なパッケージであり、強力な配列処理機能を提供します。画像データの処理やオブジェクト検出に必要な数学的操作を実行するために広く使用されています。

- **Pillow**: 画像処理タスクに使用します。 [**Pillow**](https://python-pillow.org/) はPython Imaging Library (PIL) のフォークで、Pythonインタプリタに使いやすい画像処理機能を追加します。さまざまな画像ファイル形式のオープン、操作、および保存を可能にします。

- **Poetry**: プロジェクトの依存関係を効率的に管理します。 [**Poetry**](https://python-poetry.org/) はPythonでの依存関係管理およびパッケージングのためのツールです。プロジェクトライブラリの宣言を支援し、依存関係が互いに互換性があることを確認し、仮想環境の作成と有効化を簡単にします。
