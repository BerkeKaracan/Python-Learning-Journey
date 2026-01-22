# 🗣️ RoboSpeaker Pro

A Python-based **Text-to-Speech (TTS)** assistant that converts user input into lifelike audio using Google's Speech API. This tool is designed to generate, save, and play audio files seamlessly without cutting off the playback.

## 🚀 Features

* **High-Quality Speech:** Uses Google Text-to-Speech (`gTTS`) API for natural-sounding voice generation.
* **Smart Playback Control:** Integrated with `pygame` to ensure the audio finishes playing completely before the program continues (resolves common "cut-off" issues).
* **Dynamic File Management:** Generates unique filenames using random integers to prevent Windows `PermissionError` (file-in-use) conflicts.
* **Error Handling:** Robust protection against network issues or invalid inputs.
* **Clean CLI Interface:** Simple and interactive command-line menu.

## 🛠️ Tech Stack & Libraries

* **Python 3.13**
* **gTTS** (Google Text-to-Speech) - *For API communication.*
* **Pygame** - *For audio mixer and playback control.*
* **OS & Random** - *For file system operations and unique naming.*

## 💻 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/BerkeKaracan/Python-Projects.git
    cd Python-Projects
    ```

2.  **Install the required libraries:**
    You need to install `gTTS` and `pygame` to run this project.
    ```bash
    pip install gTTS pygame
    ```

## ▶️ How to Run

1.  Run the script in your terminal:
    ```bash
    python main.py
    ```
2.  Select **"1"** from the menu.
3.  Type the text or paragraph you want the robot to read.
4.  Listen to the audio! 🎧
5.  Press **"Q"** to exit the program safely.

## 🧠 Logic Highlights

This project demonstrates advanced handling of asynchronous events in a synchronous script:

* **The "Busy" Loop:**
    Standard media players often run in the background, causing the Python script to finish before the audio does. This project uses a `while` loop to check the mixer status:
    ```python
    # Prevents the script from continuing until the audio finishes
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    ```

* **File Locking Solution:**
    To avoid overwriting files that are currently being played (which causes crashes), the script assigns a random ID to every new audio file (`Speaking_452.mp3`, `Speaking_89.mp3`, etc.).

---
*Created by [BerkeKaracan]*