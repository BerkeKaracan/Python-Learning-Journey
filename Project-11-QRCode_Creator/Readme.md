# 🏭 Python QR Code Generator (CLI)

A robust, backend-focused Python tool that converts URLs or text inputs into scannable QR Code images (`.png`). This project demonstrates functional programming logic, library integration, and file system manipulation via the Command Line Interface.

## 🎯 Project Focus: Backend Logic

> **Note:** This project is intentionally designed without a Graphical User Interface (GUI). It focuses purely on **backend logic implementation**, data validation, and direct interaction with Python's standard and external libraries.

## 🚀 Key Features

* **Instant Generation:** Converts any string or URL into a standard QR code instantly.
* **Custom File Naming:** Users can define specific filenames for their outputs.
* **Smart Automation:** Automatically opens the generated image file using the OS default viewer upon completion.
* **Input Validation:** Prevents errors by checking for empty inputs before processing.
* **Error Handling:** Includes `try-except` blocks to manage file system permissions and unexpected crashes gracefully.

## 🛠️ Tech Stack

* **Python 3.13**
* **qrcode** - *For generating the QR matrix.*
* **Pillow (PIL)** - *Image processing engine used by the qrcode library.*
* **OS & Time** - *Standard libraries for file operations and delays.*

## 💻 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/BerkeKaracan/Python-Projects.git
    cd Python-Projects
    ```

2.  **Install the required library:**
    ```bash
    pip install "qrcode[pil]"
    ```

## ▶️ How to Run

1.  Run the script in your terminal:
    ```bash
    python main.py
    ```
2.  Select **Option 1** to start.
3.  Paste your link/text and choose a filename.
4.  The QR code will be saved and opened automatically! 📷

---
*Developed by Berke Karacan*