# 🕵️‍♂️ Crypto Spy - Smart Price Tracker

A Python-based, real-time cryptocurrency tracker that alerts you when your target price is hit. Unlike simple trackers, this bot features a **"Smart Mode"** that automatically detects whether you are waiting for a dip (buying opportunity) or a pump (selling opportunity).

## 🚀 Features

* **🧠 Smart Mode Logic:** Automatically determines if it should wait for a **RISE** or a **DROP** based on your target price.
* **🔔 Desktop Notifications:** Sends a native Windows notification (via `plyer`) when the target is reached.
* **⚡ Real-Time Data:** Fetches live price data directly from the **Binance API**.
* **🛡️ Error Handling:** Auto-reconnects in case of internet loss or API timeouts.
* **✅ User Friendly:** Handles input errors (like using commas instead of dots) gracefully.

## 🛠️ Tech Stack

* **Python 3.13**
* **Requests** (For API communication)
* **Plyer** (For OS Notifications)

## 📦 Installation

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/BerkeKaracan/Python-Projects.git
    ```

2.  **Install dependencies:**
    ```bash
    pip install requests plyer
    ```

## ▶️ How to Run

1.  Run the script:
    ```bash
    python main.py
    ```
2.  Enter the coin symbol (e.g., `BTC`, `ETH`, `SOL`).
3.  Set your target price.
4.  Sit back! The bot will notify you when the moment comes. 📉📈

## 📸 Preview

> *Example Scenario:*
> * **Current BTC:** $95,000
> * **Your Target:** $89,000
> * **Bot Action:** Activates **DROP Mode** and waits for the price to fall <= $89,000.

---
*Developed by [Berke Karacan]*