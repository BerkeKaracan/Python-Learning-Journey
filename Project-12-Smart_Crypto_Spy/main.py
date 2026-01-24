import time
import requests
import plyer

print("--- CRYPTO SPY (SMART MODE) 🧠 ---")

type_of_coin = input("Which coin do you want to follow? (e.g., BTC): ").upper()
symbol = type_of_coin + "USDT"

goal_input = input("What is your target price? ($): ").replace(',', '.')
goal_cost = float(goal_input)

try:
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
    initial_data = requests.get(url).json()

    if "price" not in initial_data:
        print(" Coin not found! Please check the symbol and restart.")
        exit()

    start_price = float(initial_data["price"])
    print(f"Current Price: {start_price}")
    mode = ""
    if goal_cost > start_price:
        mode = "RISE"
        print(f" Mode: Awaiting RISE (Target: {goal_cost})")
    else:
        mode = "DROP"
        print(f" Mode: Awaiting DROP (Target: {goal_cost})")

except Exception as e:
    print(f"Initialization Error: {e}")
    exit()

print(" Tracking started...")
while True:
    try:
        data = requests.get(url).json()
        current_price = float(data["price"])
        print(f"Current: {current_price} | Target: {goal_cost}")
        trigger_alarm = False
        if mode == "RISE" and current_price >= goal_cost:
            trigger_alarm = True
        elif mode == "DROP" and current_price <= goal_cost:
            trigger_alarm = True

        if trigger_alarm:
            plyer.notification.notify(
                title=f"{mode} TARGET REACHED! ",
                message=f"{symbol} price is now {current_price}!",
                timeout=10
            )
            print("🔔 Notification sent!")
            time.sleep(20)
            exit()
        time.sleep(3)

    except Exception as e:
        print(f"Error: {e}")
        print("Retrying...")
        time.sleep(5)