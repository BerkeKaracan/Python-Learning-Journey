# 🌌 SPACE TRADER V2.0 - The Neon Frontier Update

**Space Trader** is a text-based interstellar strategy and economy simulation game built with Python. Version 2.0 introduces a living economy, visual enhancements, and dangerous underground trading mechanics.

> **Requirement:** This version requires the `colorama` library for the visual interface.

## 🚀 New Features in V2.0

* **🎨 Visual Interface (HUD):** A completely redesigned interface using `colorama`. Real-time colored status bars for Fuel (Red), Credits (Green), and Location (Cyan).
* **❤️ Hull Integrity & Repair:** Your ship now has **Health (Hull)**. Combat and desperate escapes cause damage. If Hull reaches 0%, the ship explodes.
    * **Repair System:** Visit the **Shipyard [6]** to repair your ship. Cost: **10 Credits per 1% damage**.
* **🕵️ Black Market (Deep Mechanics):** * Access via hidden menu **[12]**.
    * Requires a **10-digit numeric password**.
    * Contains stock-limited goods.
    * **Risk System:** Every transaction has a **33% chance** of a Colony Patrol raid (Goods confiscated + Prestige penalty).
* **🏆 Explorer Achievement:** Visiting all 5 planets (Earth, Mars, Jupiter, Saturn, Venus) unlocks the **Black Market Password** automatically.
* **📜 New Task:** Added Task #9 "Traveler" to guide players toward the password discovery.

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/BerkeKaracan/Python-Projects.git
    ```
2.  **Install Dependencies:**
    ```bash
    pip install colorama
    ```
3.  **Run the Game:**
    ```bash
    python main.py
    ```

## 🎮 Gameplay Guide

### 🌍 Sectors & Economy
* **Dynamic Prices:** Random events (e.g., *Gold Rush*, *Pirate Blockade*) change prices globally.
* **5 Planets:** Each planet buys/sells different goods.
    * *Earth, Mars, Jupiter, Saturn, Venus.*

### ⚔️ Combat & Survival
* **Factions:** Choose between **Pirates**, **Police**, or **Independent**.
* **Encounters:** You may be intercepted while traveling.
    * **Fight:** Risk Hull damage for loot.
    * **Escape:** Risk Hull damage to flee.
    * **Bribe/Surrender:** Lose credits or Prestige.

### 🛑 The Black Market (Classified)
A hidden trading channel for illicit goods.
* **How to Access:** Select Option **12** in the main menu.
* **Password:** Generated randomly at the start of each game. You must find it by exploring the galaxy.
* **Warning:** Police raids are frequent on this channel.

## 🕹️ Command Center (Menu)

| Key | Function | Description |
| :--- | :--- | :--- |
| **1** | **Planet Info** | Learn about resources and lore. |
| **2** | **Travel** | Move between planets (Consumes Fuel). |
| **3** | **Buy Goods** | Purchase legal items from the local market. |
| **4** | **Sell Goods** | Sell your cargo for profit. |
| **5** | **Profile** | View Rank, Cargo, and Ship stats. |
| **6** | **Shipyard** | **Buy Ships** or press **[R] to Repair**. |
| **7** | **Tasks** | View active contracts and missions. |
| **8** | **Prestige** | Check reputation or switch Faction. |
| **9** | **Save Game** | Save progress to `savefile.json`. |
| **10** | **Load Game** | Resume from last save. |
| **11** | **Buy Fuel** | Refuel your tank (5 Credits/Unit). |
| **12** | **Black Market** | Enter the encrypted trading channel. |
| **13** | **Reveal Password** | (Secret) Shows password if all 5 planets are visited. |
| **0** | **Exit** | Close the communication link. |

## 🔮 Roadmap (V3.0)

> *Incoming Transmission...*
> *System Alert: Unknown alien signal detected in Sector 9...*

* **Aliens:** Non-human factions.
* **Weapon Systems:** Upgradeable lasers and shields.
* **More Planets:** Expanding beyond the solar system.

---
*Developed by Captain [Berke Karacan]*