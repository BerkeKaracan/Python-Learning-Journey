# 📂 Smart File Organizer

A Python-based automation tool that instantly organizes chaotic directories into categorized folders. Designed with a focus on user experience, it features **real-time visual feedback** that lets you watch the organization process step-by-step.

## 🚀 Features

* **Universal Compatibility:** Works on any directory path provided by the user.
* **Cinematic Process:** Uses a smart delay (`time.sleep`) to provide satisfying, matrix-style visual feedback as files are moved.
* **Robust Error Handling:** Checks if directories exist and handles file permission errors gracefully without crashing.
* **Auto-Categorization:** Automatically sorts files into:
    * Images 🖼️
    * Documents 📄
    * Videos 🎥
    * Music 🎵
    * Programs 💾
    * Archives 📦
* **Safe Execution:** Cleans up file path inputs (removes extra quotes) and prevents immediate console closure upon completion.

## 🛠️ Built With

* **Python 3.13
* **Libraries: `os`, `shutil`, `time`

## 💻 How to Run

1.  Clone the repository:
    ```bash
    git clone [https://github.com/BerkeKaracan/Python-Projects.git](https://github.com/BerkeKaracan/Python-Projects.git)
    ```
2.  Navigate to the directory:
    ```bash
    cd Python-Projects
    ```
3.  Run the script:
    ```bash
    python organizer.py
    ```
4.  Paste the folder path you want to organize when prompted.

## 🧠 Logic & Code Highlights

This script demonstrates **Automation** and **UX Design** skills:
* **Dictionary Mapping:** Uses Python dictionaries to efficiently map file extensions to target folders.
* **User Feedback Loop:** Implements a visual delay loop to enhance user interaction and trust.
* **Path Manipulation:** robust handling of absolute paths using `os.path.join` for cross-platform compatibility.
