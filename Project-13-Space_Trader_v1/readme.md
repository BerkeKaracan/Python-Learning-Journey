# 🌌 SPACE TRADER V1.0

**Space Trader** is a text-based interstellar economy and strategy simulation game written in Python. Become the wealthiest captain in the solar system by trading goods, completing missions, fighting pirates, and managing your fuel and cargo.

## 🚀 Features

* **Dynamic Economy:** Prices fluctuate based on random galactic news events (e.g., "Gold Rush", "Pirate Blockade", "Great Drought").
* **5 Explorable Planets:** Travel between Earth, Mars, Jupiter, Saturn, and Venus. Each planet has unique resources and distances.
* **Trade System:** Buy low, sell high! Trade resources like Water, Provisions, Electronics, Ore, and Luxury Goods.
* **Exclusive Goods:** Rare items like *Saffron (Earth)*, *Rust (Mars)*, or *Ice (Saturn)* can only be bought on specific planets.
* **Combat & Events:** Random encounters with Pirates and Police during travel. Choose to fight, bribe, or flee.
* **Faction System:** Align yourself with **Pirates**, **Police**, or stay **Independent**. Your choice affects gameplay and prestige.
* **Mission System:** Complete contracts (e.g., "Supply Water to Mars") to earn bonus credits.
* **Ship Upgrades:** Buy larger ships with increased cargo capacity from the Shipyard.
* **Save & Load:** Full persistence system using JSON. Save your progress and resume later.

## 📦 Installation & How to Run

You don't need to install any external libraries. The game runs on standard Python.

1.  **Clone the repository** (or download the files):
    ```bash
    git clone https://github.com/BerkeKaracan/Python-Projects.git
    ```
2.  **Navigate to the folder:**
    ```bash
    cd space-trader
    ```
3.  **Run the game:**
    ```bash
    python Space_trader_v1.py
    ```

## 🎮 How to Play

Upon starting, you will be asked to enter your **Captain Name** and choose a **Faction**.

### Main Menu Commands:
* **[1] Planet Info:** Learn about the resources and lore of each planet.
* **[2] Travel:** Move to another planet. *Warning: Consumes Fuel!*
* **[3] Buy Goods:** Purchase items from the local market.
* **[4] Sell Goods:** Sell items from your cargo.
* **[5] Profile:** Check your Credits, Fuel, Ship status, and Rank.
* **[6] Shipyard:** Upgrade your spaceship for more capacity.
* **[7] Tasks:** View active missions to earn rewards.
* **[8] Prestige & Faction:** Check your standing or switch sides.
* **[9] Save Game:** Save your current progress to `savefile.json`.
* **[10] Load Game:** Resume your last saved session.
* **[11] Buy Fuel:** Refuel your ship (Critical for survival!).

### 🌍 The Solar System

| Planet | Cheap Resource | Expensive Resource | Notes |
| :--- | :--- | :--- | :--- |
| **Earth** | Saffron | Antimatter | The starting point. |
| **Mars** | Rust | Nitrogen | The Red Planet. |
| **Jupiter** | Hydrogen | Metal | The largest market. |
| **Saturn** | Helium | Ice | Ringed giant. |
| **Venus** | Java | Oxygen | High risk, high reward. |

## ⚠️ Important Strategy Tips

1.  **Watch Your Fuel:** If your fuel reaches 0 during travel, it's **GAME OVER**. Always refuel at the station (Option 11).
2.  **Unique Goods:** Some items (like Saffron or Rust) are unique to their home planets. You might need to find specific buyers or hold them for future updates (Black Market v2.0).
3.  **News Matters:** Always check the news after traveling. If "Industrial Accident" happens, Electronics prices will skyrocket!

## 🛠 Technologies Used

* **Python 3.13**
* **JSON** (For data persistence)
* **OS/Random** (Standard libraries)

## 🔜 Future Roadmap (v2.0)

* **Black Market:** A place to sell illegal or unique goods anywhere.
* **More Ships:** Advanced cruisers and battleships.
* **Visual Interface:** Enhanced UI elements.

---
*Developed by Captain [Berke Karacan/BerkeKaracan]*