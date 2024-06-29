<div align="center">
  <img src="https://github.com/Solrikk/OmniView/blob/main/assets/images/techny-machine-vision-icon.png" alt="Logo" />
</div>

<div align="center">
  <h3>
    <a href="https://github.com/Solrikk/OmniView/blob/main/README.md">English</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_RU.md">Russian</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_GE.md">⭐German⭐</a> |
    <a href="https://github.com/Solrikk/OmniView/blob/main/README_JP.md">Japanese</a> |
    <a href="README_KR.md">Korean</a> |
    <a href="README_CN.md">Chinese</a>
  </h3>
</div>

-----------------

# OmniView 👁️

## Überblick:

**OmniView** ist eine fortschrittliche Anwendung zur Videoanzeige und -aufzeichnung, die Funktionen wie **Echtzeit-Objekterkennung** und **Screenshot-Erstellung** bietet. Dieses Projekt verwendet die **OpenCV-Bibliothek** für die **Kameraverbindung** und **Videobearbeitung**, um reibungslose und hochqualitative Videostreams zu gewährleisten. Die Integration der **Darknet-API** bietet fortschrittliche **Objekterkennungs**-Funktionen und ermöglicht die Echtzeit-Identifizierung und -Verfolgung verschiedener Objekte im Videostream.

![OmniView Demo](https://github.com/Solrikk/OmniView/blob/main/assets/gif/OmniView.gif)

## Funktionen: ✨

- **Kameraerkennung** 📷: Erkennt und listet automatisch angeschlossene Kameras auf. Diese Funktion verwendet **OpenCV**, um alle verfügbaren Videogeräte zu scannen und fügt die erkannten Kameras zur Auswahl hinzu, wodurch die manuelle Gerätesuche entfällt.

- **Live-Stream-Anzeige** 📺: Sehen Sie sich in Echtzeit den Live-Video-Feed von der ausgewählten Kamera an. Die Anwendung verwendet **Tkinter** und **OpenCV**, um den Videostream direkt in der Benutzeroberfläche anzuzeigen, sodass Benutzer den Feed nahtlos überwachen können.

- **Videoaufzeichnung** 🎥: Zeichnen Sie Videostreams mit einem Klick auf. Die Aufzeichnung kann jederzeit gestartet und gestoppt werden, und die resultierende Videodatei wird zur späteren Ansicht oder Analyse gespeichert. Die Anwendung verwendet den **XVID-Codec** zur Aufzeichnung mit automatischen Einstellungen für Bildrate und Auflösung.

- **Objekterkennung** 🕵️‍♂️: Verwendet das **YOLOv3-Modell** zur Erkennung von Objekten im Videostream in Echtzeit. Dieses Modell hebt verschiedene Objekttypen (z. B. Personen, Autos, Tiere) hervor und zeigt sie mit entsprechenden Beschriftungen und Vertrauensstufen an, was die Identifizierung und Verfolgung von Objekten im Frame erleichtert.

- **Screenshot-Aufnahme** 📸: Machen Sie hochqualitative Screenshots und speichern Sie sie im gewünschten Ordner. Diese Funktion ist ideal, um wichtige Momente festzuhalten oder die Frames für weitere Analysen zu verwenden. Die Anwendung erstellt automatisch einen Ordner im Home-Verzeichnis des Benutzers, um Screenshots zu speichern, falls dieser noch nicht existiert.

## Installation: 🛠️

Um mit OmniView zu beginnen, befolgen Sie diese Schritte:

1. Stellen Sie sicher, dass **Python 3.10** oder höher installiert ist.
2. Klonen Sie das Repository:
    ```bash
    git clone https://github.com/Solrikk/OmniView.git
    cd OmniView
    ```
3. Installieren Sie die Abhängigkeiten mit Poetry:
    ```bash
    poetry install
    ```

## Nutzung: 🚀

Befolgen Sie diese einfachen Schritte, um OmniView zu verwenden:

1. Starten Sie die Anwendung:
    ```bash
    poetry run python main.py
    ```
2. Wählen Sie eine Kamera aus der bereitgestellten Liste aus und klicken Sie auf "View Camera", um den Live-Feed zu starten.
3. Verwenden Sie die verfügbaren Schaltflächen, um die Videoaufzeichnung zu starten oder zu stoppen, Screenshots zu erstellen und die Objekterkennung zu aktivieren.

## Abhängigkeiten: 📦

OmniView verwendet die folgenden Bibliotheken und Werkzeuge:

- **Python 3.10 und höher**: Die Anwendung erfordert [**Python 3.10**](https://www.python.org/downloads/release/python-3100/) oder höher, um die neuesten Sprachfunktionen zu nutzen und die Kompatibilität mit modernen Bibliotheken zu gewährleisten.

- **tkinter**: Für die Erstellung der Benutzeroberfläche. [**tkinter**](https://docs.python.org/3/library/tkinter.html) ist das integrierte GUI-Toolkit für Python, das eine einfache Möglichkeit bietet, Fenster, Dialoge, Schaltflächen und andere Benutzeroberflächenelemente zu erstellen.

- **OpenCV**: Zur Verwaltung der Kameraverbindungen und Videobearbeitung. [**OpenCV**](https://opencv.org/) ist eine Open-Source-Softwarebibliothek für Computer Vision und maschinelles Lernen, die häufig für Anwendungen in Echtzeit verwendet wird. Sie ermöglicht das Erfassen von Videos von Kameras, Videodateien und sogar Netzwerkstreams.

- **NumPy**: Wesentlich für die Handhabung von Datenarrays. [**NumPy**](https://numpy.org/) ist ein grundlegendes Paket für wissenschaftliches Rechnen in Python und bietet leistungsstarke Möglichkeiten zur Array-Verarbeitung. Es wird umfassend zur Handhabung von Bilddaten und zur Durchführung mathematischer Operationen verwendet, die für die Objekterkennung erforderlich sind.

- **Pillow**: Wird für Aufgaben der Bildbearbeitung verwendet. [**Pillow**](https://python-pillow.org/) ist ein Fork der Python Imaging Library (PIL) und fügt Ihrem Python-Interpreter einfach zu bedienende Bildverarbeitungsfunktionen hinzu. Es ermöglicht das Öffnen, Manipulieren und Speichern vieler verschiedener Bilddateiformate.

- **Poetry**: Verwalte Projektabhängigkeiten effizient. [**Poetry**](https://python-poetry.org/) ist ein Tool für Abhängigkeitsmanagement und Paketierung in Python. Es hilft dabei, Projektbibliotheken zu deklarieren, stellt sicher, dass die Abhängigkeiten miteinander kompatibel sind und vereinfacht die Erstellung und Aktivierung virtueller Umgebungen.
