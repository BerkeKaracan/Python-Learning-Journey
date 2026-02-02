# 🚀 Internet Speed Test Tool

A lightweight Python CLI tool to check your internet connection speed directly from the terminal. It measures Download, Upload, and Ping latency using the best available server.

## ⚡ Features

- **Auto-Server Select:** Automatically finds the best and closest server for accurate results.
- **Comprehensive Metrics:** Measures **Download Speed**, **Upload Speed**, and **Ping**.
- **Clean Output:** displays results in a readable format converted to **Mbps** (Megabits per second).
- **No Browser Needed:** Runs entirely in the command line, avoiding ads and heavy web pages.

## 🛠️ Requirements

You need Python installed and the `speedtest-cli` library.

To install the required library, run:

    pip install speedtest-cli

## 🎮 How to Use

1.  **Run the Script:**
    Open your terminal and run:

        python main.py

2.  **Wait for Analysis:**
    The tool will sequentially:
    - Find the best server...
    - Measure Download speed...
    - Measure Upload speed...

3.  **View Results:**
    You will see a report like this:

        Your connection speed :
        Download Speed : 85.42 Mbps
        Upload Speed : 7.89 Mbps
        Ping : 12.0 ms

## 📂 Project Structure

    ├── main.py          # The source code
    ├── README.md        # Documentation
    └── .gitignore       # Git configuration

---

_Developed by [BerkeKaracan]_
