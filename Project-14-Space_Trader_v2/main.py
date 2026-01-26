import random
import os
import json
import time

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
password  = random.randint(100000000,9999999999)
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def save_game():
    save_data ={
        "Player Data" : player,
        "Ship Inventory" : ship,
        "Game Tasks" : game_tasks,
        "Faction" : faction
    }
    try:
        with open("savefile.json", "w") as f :
            json.dump(save_data, f)
        print("\n[✔] GAME SAVED SUCCESSFULLY!")
    except Exception as e:
        print(f"\n[!] Error saving game:{e}")
def load_game():
    global game_tasks
    global faction
    try:
        with open("savefile.json", "r") as f :
            data = json.load(f)
            player.update(data["Player Data"])
            ship.update(data["Ship Inventory"])
            game_tasks[:] = data["Game Tasks"]
            faction = data.get("Faction", "INDEPENDENT")
            if "visited_planets" not in player:
                player["visited_planets"] = [player["location"]]
        print("\n[✔] SAVE LOADED! Continuing mission.")

    except FileNotFoundError:
        print("\n[!] No save file found.")
    except KeyError:
        print("\n[!] Save file structure is outdated. Some data might be reset.")
def check_status_tasks():
    for task in game_tasks:
        if task['completed'] == True :
            continue
        mission_done = False
        if  task['id'] == 1  and player['location'] == "Mars" :
            mission_done = True
        elif task['id'] == 2 and player['credit'] >= 5100 :
            mission_done = True
        elif task['id'] == 3 and player['ship'] != "A0000" :
            mission_done = True
        elif task['id'] == 4 and player['location'] == "Jupiter" :
            mission_done = True
        elif task['id'] == 5 and player['fuel'] >= 600 :
            mission_done = True
        elif task['id'] == 6 and player['location'] == "Saturn" :
            mission_done = True
        elif task['id'] == 7 and player['prestige'] == 50 :
            mission_done = True
        elif task['id'] == 8 and player['location'] == "Venus" :
            mission_done = True
        if mission_done :
            task['completed'] = True
            player['credit'] += task['reward']
            print("\n" + "*" * 40)
            print(f"★ MISSION COMPLETED! ★")
            print(f"Task: {task['en']}")
            print(f"Reward: +{task['reward']} Credits added to your account!")
            print("*" * 40 + "\n")

def ship_getting():
    repair= input("[R] REPAIR SHIP (Cost: 10 Credits per %1 Hull)").upper()
    if repair == "R":
        if player['hull'] == 100:
            print("You didn't have any damage ")
        else:
            p = 100 - player['hull']
            p *= 10
            if player['credit'] >= p :
                player['credit'] -=p
                player['hull'] =100
                print("Your ship fixed")
            else:
                print("You don't have enough credits")
    ship_list = list(ships.keys())
    for i, ship_key in enumerate(ship_list, 1):
        capacity = ships[ship_key]["Capacity"]
        value = ships[ship_key]["Value"]
        print(f"\n {i} . {ship_key}  - Capacity : {capacity} - Value {value}")
    try:
        choice = int(input("What do you want to buy ? (For exit '0')"))
        if choice == 0:
            return
        selected_item = ship_list[choice - 1]
        ship_capacity = ships[selected_item]["Capacity"]
        ship_value = ships[selected_item]["Value"]
        print(f" Selected Item :  {selected_item}  Capacity : {ship_capacity} Price : {ship_value}")
        if player['credit'] >= ship_value:
            player['credit'] -= ship_value
            player['ship'] = selected_item
            player['capacity'] = ship_capacity
            print(f"{selected_item} bought !! ")
            print(f" Your new capacity : {player['capacity']}")
        else:
            print(Fore.YELLOW +  "Your balance is not enough !!!")
    except (ValueError, KeyError, IndexError):
        print(Fore.RED + "Please enter a valid option")
def market_menu():
    current_loc = player['location']
    if current_loc not in planets:
        print(Fore.RED + "Error: Market data not found for this sector.")
        return
    market = planets[current_loc]
    print(f"\nWelcome to {current_loc} Market!")
    product_list = list(market.keys())
    for i, item in enumerate(product_list, 1):
        offer = market[item]
        print(f"{i}. {item} - Price: {offer}")
    try:
        selection = input("\nWhat do you want to buy? (For exit 'Q'): ")
        if selection.upper() == "Q":
            return
        index = int(selection) - 1
        if index < 0 or index >= len(product_list):
            print(Fore.RED + "Invalid selection number!")
            return
        selected_item = product_list[index]
        product_price = market[selected_item]
        print(f"Selected Item: {selected_item} | Price: {product_price}")
        if player['credit'] < product_price:
            print("Insufficient Funds!")
            return
        if not capacity_check():
            return
        player['credit'] -= product_price
        if selected_item in ship:
            ship[selected_item] += 1
        else:
            ship[selected_item] = 1
        print(f"SUCCESS:  {selected_item} purchased! New Balance: {player['credit']}")
    except ValueError:
        print(Fore.YELLOW + "Please enter a valid number.")
    except Exception as e:
        print(f"{Fore.RED } An unexpected error occurred: {e}")

def market_menu_second():
    current_loc = player['location']
    print(f"Welcome to {current_loc} Market  !")
    product_list = list(ship.keys())
    for i , item in enumerate(product_list, 1):
        offer = ship[item]
        print(f"{i} . {item} - Quantity : {offer} ")
    try:
        choice = input("What do you want to sell ? (For exit 'Q') ").upper()
        if choice == "Q":
            return
        choice = int(choice) - 1
        selected_item = product_list[choice]
        if selected_item not in planets[current_loc]:
            print(f"{Fore.YELLOW}This planet does not buy {selected_item}!")
            return
        product_val = planets[current_loc][selected_item]
        print(f"Selected Item : {selected_item} Quantity : {product_val} Price: {planets[current_loc][selected_item]}")
        if ship[selected_item] <= 0:
            return
        player['credit'] += product_val
        ship[selected_item] -= 1
        print(f"{selected_item} sold !! ")
    except(ValueError, KeyError, IndexError):
        pass


def capacity_check():
    total_load = sum(ship.values())
    if total_load >= player['capacity']:
        print(f" {Fore.YELLOW}CARGO FULL! (Load:  {total_load}/{player['capacity']})")
        return False
    return True
def check():
    if player['fuel'] < 0 :
        print(Fore.RED + "Fuel depleted! Life support failing... GAME OVER!")
        quit()
    if player['hull'] <= 0:
        print(Fore.RED + "CRITICAL FAILURE! Hull breach detected... Ship destroyed.")
        print(Fore.RED + "GAME OVER")
        quit()
def news(c):
    if c == "Gold Rush":
        print(Fore.CYAN + '''
        Gold Rush: 
        "Rich mineral veins discovered on satellites; 
        miners flock to the region, equipment demand explodes!"
        Electronics prices increased by 5%. 
        Mineral prices dropped by 15%.
        ''')
        j = player['location']
        planets[j]['Electronics'] *= 1.05
        planets[j]['Ore'] *= 0.85
    elif c == "Great Drought" :
        print(Fore.CYAN +'''
        Great Drought: 
        "A major malfunction has occurred in Water treatment plants around the planet; 
        the public is awaiting urgent Water assistance!"
        Water prices surged by 20%.
        Provisions was raised % 5
        Electronics equipment's economy was reduced % 15
        Luxury goods was reduced %5
        ''')
        j = player['location']
        planets[j]['Water'] *= 1.20
        planets[j]['Provisions'] *= 1.05
        planets[j]['Electronics'] *= 0.85
        planets[j]['luxury_goods'] *= 0.95
    elif c == "Technology Fair" :
        print(Fore.CYAN +'''
        Technology Fair: 
        "An interplanetary technology congress is gathering in this region; 
        exorbitant prices are being paid for advanced components!"
        Electronics equipment's economy was raised %10
        Water was reduced % 5 
        ''')
        j = player['location']
        planets[j]['Electronics'] *= 1.10
        planets[j]['Water'] *= 0.95
    elif c == "Harvest Disaster":
        print(Fore.CYAN +'''
        Harvest Disaster: 
        "A mysterious parasite that appeared in agricultural domes destroyed the entire crop; 
        a Provisions crisis is looming!"
        Provisions was raised %35
        Water was raised %5
        Electronics equipment's economy was reduced % 20 
        Luxury goods was reduced %10 
        ''')
        j = player['location']
        planets[j]['Water'] *= 1.05
        planets[j]['Provisions'] *= 1.35
        planets[j]['Electronics'] *= 0.80
        planets[j]['luxury_goods'] *= 1.10
    elif c == "The Feast of the Nobles" :
        print(Fore.CYAN +'''
        The Feast of the Nobles: 
        "The luxury goods market was buzzing due to the lavish ball held in honor of the governor of Venus!"
        Luxuries was raised %15 
        Electronics equipment's economy was raised % 5
        Ore was raised %5 
        Provisions was reduced %5 
        Water was reduced %10
        ''')
        j = player['location']
        planets[j]['Water'] *= 0.90
        planets[j]['Provisions'] *= 0.95
        planets[j]['Electronics'] *= 1.05
        planets[j]['luxury_goods'] *= 1.15
        planets[j]['Ore'] *= 1.05
    elif c == "Pirate Blockade" :
        print(Fore.CYAN +'''
        Pirate Blockade: 
        "Pirate attacks in the sector have disrupted shipping routes; 
        product prices have become uncertain on the black market!"
        Market instability detected! Prices are volatile.
        ''')
        j = player['location']
        planets[j]['Water'] *=  (1 + random.randint(1,50)/100)
        planets[j]['Provisions'] *= (1 + random.randint(1,50)/100)
        planets[j]['Electronics'] *= (1 + random.randint(1,50)/100)
        planets[j]['luxury_goods'] *= (1 + random.randint(1,50)/100)
        planets[j]['Ore'] *= (1 + random.randint(1,50)/100)
    elif c == "New Colony Construction" :
        print(Fore.CYAN +'''
        New Colony Construction: 
        "A new settlement is being established in a remote crater; 
        there are high incentives for construction and raw materials!"
        Water was raised % 5
        Electronics equipment's economy was raised % 10 
        ''')
        j = player['location']
        planets[j]['Electronics'] *= 1.10
        planets[j]['Water'] *= 1.05
    elif c == "Medical Breakthrough" :
        print(Fore.CYAN +'''
        Medical Breakthrough: 
        "A revolutionary drug has been developed in laboratories; 
        rare earth element stocks are rapidly depleting!"
        Ore was raised %50
        Electronics equipment's economy was raised %25 
        Luxuries was raised %15
        Provisions was raised %5
        Water was raised %10 
        ''')
        j = player['location']
        planets[j]['Water'] *= 1.10
        planets[j]['Provisions'] *= 1.05
        planets[j]['Electronics'] *= 1.25
        planets[j]['luxury_goods'] *= 1.15
        planets[j]['Ore'] *= 1.50
    elif c == "Industrial Accident" :
        print(Fore.CYAN +'''
        Industrial Accident: 
        "Explosions at main factories halted production;
        Spare parts are now extremely valuable!
        Technological equipment's economy was raised %100
        Ore was raised %50
        Luxuries was raised %25
        Provisions was reduced %5
        Water was reduced %10
        ''')
        j = player['location']
        planets[j]['Water'] *= 0.90
        planets[j]['Provisions'] *= 0.95
        planets[j]['Electronics'] *= 2.00
        planets[j]['luxury_goods'] *= 1.25
        planets[j]['Ore'] *= 1.50
    elif c == "Peace Festival" :
        print(Fore.CYAN +'''
        Peace Festival: 
        "Interstellar peace festival celebrations have begun; 
        tourists arriving on the planet are searching for souvenirs!"
        Technological equipment's economy was raised %20
        Luxuries was raised %45
        Provisions was reduced %5
        ''')
        j = player['location']
        planets[j]['Provisions'] *= 0.95
        planets[j]['Electronics'] *= 1.20
        planets[j]['luxury_goods'] *= 1.45
    else:
        print(Fore.RED + "IMPOSSIBLE")
game_tasks = [
            {
                "id": 1,
                "en": "Contract: Water Supply for Mars",
                "reward": 500,
                "completed": False
            },
            {
                "id": 2,
                "en": "Milestone: First Fortune (5,000 Credits)",
                "reward": 1000,
                "completed": False
            },
            {
                "id": 3,
                "en": "Objective: Fleet Expansion (Buy a Ship)",
                "reward": 2000,
                "completed": False
            },
            {
                "id": 4,
                "en": "Trade Route: Tech to Jupiter",
                "reward": 1500,
                "completed": False
            },
            {
                "id": 5,
                "en": "Resource: Fuel Stockpile (500 Units)",
                "reward": 250,
                "completed": False
            },
            {
                "id": 6,
                "en": "Ice of Saturn (Buy Ice from Saturn)",
                "reward": 3000,
                "completed": False
            },
            {
                "id": 7,
                "en": "Prestige Master (Reach 50 Prestige)",
                "reward": 5000,
                "completed": False
            },
            {
                "id": 8,
                "en": "Luxury Life (Travel to Venus)",
                "reward": 750,
                "completed": False
            },
            {
                "id": 9,
                "en": "Traveler(Travel to all planets)",
                "reward": "Password of Black Market",
                "completed": False
             }
        ]
planets = {
    "Earth" : {"saffron" : 15 , "antimatter" : 500000 , "Water" : 25 , "Provisions" : 100 , "Electronics" : 1000 , "Ore" : 100000 , "luxury_goods" :  250000},
    "Mars" : { "rust" : 2 ,"nitrogen": 1250000, "Water" : 250 , "Provisions" : 1000 , "Electronics" : 10000 , "Ore" : 1000000 , "luxury_goods" :  250000},
    "Jupiter" : { "hydrogen" : 50 ,"metal" : 1000000 , "Water" : 100 , "Provisions" : 500 , "Electronics" : 10000 , "Ore" : 100000 , "luxury_goods" : 275000 },
    "Saturn" : {"helium" : 1000 , "ice" : 100000 , "Water" : 200 , "Provisions" : 750 , "Electronics" : 30000 , "Ore" : 90000 , "luxury_goods" : 75000},
    "Venus" : {"java" : 30 , "oxygen" : 1000000 , "Water" : 500 , "Provisions" : 1000 , "Electronics" : 100000 , "Ore": 775000 , "luxury_goods" : 250000}
}
black_market_products = {
    "saffron" :{ "price" : 6 , "stock" : 500} ,
    "antimatter" : {"price" : 275000 , "stock" : 10},
    "Water" : {"price" : 125 , "stock" : 10000},
    "Provisions" : {"price" : 75, "stock" : 1000},
    "Electronics" : {"price" : 565 , "stock" : 500},
    "Ore" : {"price" : 45000 , "stock" : 200},
    "luxury_goods" : {"price" : 52500 , "stock" : 185},
    "rust" : {"price" : 1 , "stock" : 100000},
    "hydrogen" : { "price" : 25 , "stock" : 10000},
    "nitrogen" : {"price" : 775000 , "stock" : 5},
    "helium" : {"price" : 775 , "stock" : 960},
    "java" : {"price" : 22 , "stock" : 10000},
    "oxygen" : {"price" : 50000},
    "ice" : {"price" : 10000 , "stock" : 100}
}
ships = {
    "A00001" : {"Capacity" : 5000 , "Value" : 1000},
    "A00002" : {"Capacity" : 10000 , "Value" : 10000},
    "A00003" : {"Capacity" : 25000 , "Value" : 25000},
    "A00004" : {"Capacity" : 50000 , "Value" : 50000},
    "A00005" : {"Capacity" : 100000 , "Value" : 100000}
}
player = {
    "name" : "default",
    "credit" :  100 ,
    "fuel" : 100 ,
    "location" : 'Earth',
    "capacity" : 500 ,
    "prestige" : 0,
    "ship" : "A0000",
    "visited_planets": ["Earth"],
    "hull": 100
}
faction = "INDEPENDENT"
ship = {"Water" : 100,
             "Provisions" : 100,
             "Electronics" : 0,
             "Ore" : 0,
             "luxury_goods" : 0,
             }
distance_from_venus = {
    "Earth" : 24,
    "Mars" : 249,
    "Jupiter" : 602,
    "Saturn" : 1224,
    "Venus" :  0
}
def black_market(user_password):
    if user_password != password:
        print(Fore.RED + "Wrong password (If you want to try , the password has 10 digits.) ")
        return
    else:
        print(Fore.GREEN + "Access granted.")
        print("The black_market system is opening...")
        product_keys = list(black_market_products.keys())
        for index, item_key in enumerate(product_keys, 1):
            item_data = black_market_products[item_key]
            price = item_data['price']
            stock = item_data['stock']
            stock_display = stock if stock > 0 else "OUT OF STOCK"
            print(f"{index}. {item_key.upper()} | Price: {price} | Stock: {stock_display}")
        try:
            buy_bm= int(input("\n Select Item Number :"))
            if buy_bm < 1 or buy_bm > len(product_keys):
                print(Fore.YELLOW + "Wrong Item Number.")
                return
            selected_product = product_keys[buy_bm - 1]
            selected_product_data = black_market_products[selected_product]
            if selected_product_data['stock'] <= 0 :
                print("This product is not available.")
                return
            stock_bm = int(input(f"How many {selected_product} do you want? :  "))
            if selected_product_data['stock'] <= stock_bm :
                print(f"Not enough stock! Only {selected_product_data['stock']} available.")
                return
            total_price = selected_product_data['price'] * stock_bm
            if player['credit'] < total_price:
                print(Fore.YELLOW + "Insufficient funds on encrypted account.")
                return
            if not capacity_check():
                return
            player['credit'] -= total_price
            if selected_product in ship:
                ship[selected_product] += stock_bm
            else:
                ship[selected_product] = stock_bm
            black_market_products[selected_product]['stock'] -= stock_bm
            print(f"{Fore.GREEN} Transaction Complete. {total_price} Credits.")
            catching_possibility = random.randint(1, 3)
            if catching_possibility == 1:
                print(Fore.RED + "\n[!!!] ALERT: COLONY PATROL DETECTED SIGNAL!")
                print(Fore.RED + "Authorities confiscated the illegal goods!")
                player['prestige'] -= 20
                ship[selected_product] -= stock_bm
            else:
                print(Fore.GREEN + "\n[OK] Signal Trace: NEGATIVE. Safe exit.")
        except ValueError:
            print(Fore.YELLOW+"Invalid input detected.")

def instructions(no):
    if no == 1 :
        print( Fore.BLUE + ''' 
            EARTH
                Earth is the planet from which humanity originated.
               It is mostly composed of Water and oxygen.
               Its cheapest substance is saffron and its most expensive substance is antimatter. 
               It has an atmosphere.''')
    elif no == 2 :
        print( Fore.BLUE +''' 
            MARS 
                Mars, also known as the Red Planet, is a ringless planet that is the fourth closest to the Sun in the Solar System.
               It has two moons, Phobos and Deimos.
               Mars is the second smallest planet in the Solar System after Mercury.
               Its cheapest material is rust, and its most expensive is nitrogen.''')
    elif no == 3 :
        print(Fore.BLUE +'''
            JUPITER 
                Jupiter is not only the largest planet in the Solar System, but its mass alone is 2.5 times the combined mass of all the other planets.
               It has the shortest rotation period on its axis.
               It possesses the strongest magnetic field and the largest magnetosphere.
               Its cheapest material is hydrogen, and its most expensive is metal.''')
    elif no == 4 :
        print(Fore.BLUE +'''
            SATURN 
                Saturn is the sixth planet from the Sun and the second largest planet in our solar system. 
               Saturn is a massive ball of hydrogen and helium, surrounded by a magnificent ring system.
               It is the farthest planet from Earth discovered by human eyes.
               Its cheapest material is helium, and its most expensive is ice.''')
    elif no == 5 :
        print(Fore.BLUE +'''
            VENUS    
                Venus, despite not being the closest planet to the Sun, is the hottest.
               This is because it has an atmosphere rich in greenhouse gases.
               This atmosphere consists mainly of clouds containing carbon monoxide and sulfuric acid. 
               These gases trap heat from the Sun. 
               Its cheapest material is lava, and its most expensive is oxygen.''')
def menu_travel():
    attack_percent = random.randint(1,10)
    if attack_percent == 1 or attack_percent == 2 :
        if faction == "PIRATES" :
            print(Fore.YELLOW + "Police forces have intercepted you!")
            escaping = input(Fore.BLUE + "Option 1: Attempt Bribe (60% Chance to Escape) \n Option 2: Resist Arrest (40% Chance to Escape)")
            escaping_possibility = random.randint(1,5)
            if escaping == "1" :
                if escaping_possibility == 1 or escaping_possibility == 3 or escaping_possibility == 5 :
                    player['credit'] -= 250
                else:
                    player['credit'] = 0
                    print(Fore.RED + "They arrested you and confiscated your credits. GAME OVER :) Don't drop the soap!")
                    quit()
            elif escaping == "2"  :
                if escaping_possibility == 1 or escaping_possibility == 2:
                    print(Fore.GREEN + "You managed to escape!")
                    player['hull'] -= random.randint(10, 30)
                    print(Fore.RED + f"Hull Damage Taken! Current Integrity: {player['hull']}%")
                else:
                    print(Fore.RED + "You were caught! Sentenced to life in galactic prison. Enjoy your stay :) GAME OVER.")
                    quit()
        elif faction == "POLICE" :
            situation = random.randint(1,2)
            if situation == 1:
                print(Fore.YELLOW + "Pirates are attacking your ship!")
                k = input(Fore.BLUE + "Option 1: Fight Back (50% Chance to Win) \n Option 2 : Lose your dignity(and pants) (%80 : Escape)")
                a = random.randint(1,2)
                b = random.randint(1,5)
                if k == "1":
                    if a == 1:
                        print(Fore.GREEN + "Victory! You defeated the pirates and looted 200 credits.")
                        player['credit'] += 200
                        player['hull'] -= random.randint(10, 30)
                        print(Fore.RED + f"Hull Damage Taken! Current Integrity: {player['hull']}%")
                    elif a == 2:
                        print(Fore.RED + "Killed in action! GAME OVER.")
                        quit()
                elif k == "2":
                    if b == 1 or b == 2 or b==3 or b==4 :
                        print(Fore.BLUE + "They left you stranded, but you are alive.")
                        player['credit'] = 0
                        print(Fore.BLUE + "You were dismissed from your position after this incident.")
                        player['prestige'] = 0
                    else:
                        print(Fore.RED + "They showed no mercy. You were executed on the spot. GAME OVER.")
                        quit()
                else:
                    print(Fore.YELLOW+"Please enter a valid option")
                    return
        else:
            print(Fore.YELLOW+"The pirates attacked you !")
            c = input(Fore.BLUE+"Option 1: Fight Back (20% Chance to Win) \n Option 2: Evasive Maneuvers (30% Chance to Escape, Lose 50% Credits) \n Option 3: Emergency Warp (100% Escape, Risk of Ship Damage) ")
            m = random.randint(1,10)
            if c == "1":
                if m == 1 or m == 2 :
                    print(Fore.GREEN+"Hostiles eliminated! Found 200 credits in the wreckage.")
                    player['credit'] += 200
                else:
                    print(Fore.RED+"Hull critical! Ship destroyed. GAME OVER.")
                    quit()
            elif c == "2":
                if m == 3 or m == 4 or m == 5 :
                    print(Fore.BLUE+"You managed to hide, but they took half your credits.")
                    now_credit = player['credit']
                    player['credit'] -= now_credit/2
                else:
                    print(Fore.RED+"They found your hiding spot. No survivors. GAME OVER.")
                    quit()
            elif c == "3":
                print(Fore.GREEN+"You escaped")
                if m==6 or m==7 or m==8 or m==9 or m==10:
                    print("Critical hit! ")
                    player['hull'] -= random.randint(10, 30)
                    print(Fore.RED + f"Hull Damage Taken! Current Integrity: {player['hull']}%")
                else:
                    print(Fore.GREEN+"Warp successful! Ship integrity is stable.")
            else:
                print(Fore.YELLOW+"Please enter a valid option")
                return
    try:
        travel_choice = int(input('''
                                        1 = Earth
                                        2 = Mars
                                        3 = Jupiter
                                        4 = Saturn
                                        5 = Venus
                                        Which planet do you want to travel ? 
                                        '''))
    except ValueError:
        print(Fore.RED+"Invalid input. Please enter a number.")
        return
    news_list = ["Great Drought", "Gold Rush", "Technology Fair", "Harvest Disaster", "The Feast of the Nobles",
             "Pirate Blockade", "New Colony Construction", "Medical Breakthrough", "Industrial Accident",
             "Peace Festival"]
    k = random.choice(news_list)
    if travel_choice == 1:
        dest_planet= 'Earth'
        curr_planet = player['location']
        dist = abs(distance_from_venus[curr_planet] - distance_from_venus[dest_planet])
        fuel_cost = dist * 0.1
        if player['fuel'] < fuel_cost:
            print(f" Insufficient Fuel! (Required:{fuel_cost:.1f}, Current:  {player['fuel']:.1f})")
            return
        player['fuel'] -= fuel_cost
        check()
        player['location'] = "Earth"
        print("Fuel Consumed:", fuel_cost)
        print(f"Arrival at Sector: {player['location']}")
        news(k)
    elif travel_choice == 2:
        dest_planet= 'Mars'
        curr_planet = player['location']
        dist = abs(distance_from_venus[curr_planet] - distance_from_venus[dest_planet])
        fuel_cost = dist * 0.1
        if player['fuel'] < fuel_cost:
            print(f" Insufficient Fuel! (Required:{fuel_cost:.1f}, Current:  {player['fuel']:.1f})")
            return
        check()
        player['location'] = "Mars"
        print("Fuel Consumed:", fuel_cost)
        print(f"Arrival at Sector: {player['location']}")
        news(k)
    elif travel_choice == 3:
        dest_planet= 'Jupiter'
        curr_planet = player['location']
        dist = abs(distance_from_venus[curr_planet] - distance_from_venus[dest_planet])
        fuel_cost = dist * 0.1
        if player['fuel'] < fuel_cost:
            print(f" Insufficient Fuel! (Required:{fuel_cost:.1f}, Current:  {player['fuel']:.1f})")
            return
        check()
        player['location'] = "Jupiter"
        print("Fuel Consumed:", fuel_cost)
        print(f"Arrival at Sector: {player['location']}")
        news(k)
    elif travel_choice == 4:
        dest_planet= 'Saturn'
        curr_planet = player['location']
        dist = abs(distance_from_venus[curr_planet] - distance_from_venus[dest_planet])
        fuel_cost = dist * 0.1
        if player['fuel'] < fuel_cost:
            print(f" Insufficient Fuel! (Required:{fuel_cost:.1f}, Current:  {player['fuel']:.1f})")
            return
        check()
        player['location'] = "Saturn"
        print("Fuel Consumed:", fuel_cost)
        print(f"Arrival at Sector: {player['location']}")
        news(k)
    elif travel_choice == 5:
        dest_planet= 'Venus'
        curr_planet = player['location']
        dist = abs(distance_from_venus[curr_planet] - distance_from_venus[dest_planet])
        fuel_cost = dist * 0.1
        if player['fuel'] < fuel_cost:
            print(f" Insufficient Fuel! (Required:{fuel_cost:.1f}, Current:  {player['fuel']:.1f})")
            return
        check()
        player['location'] = "Venus"
        print("Fuel Consumed:", fuel_cost)
        print(f"Arrival at Sector: {player['location']}")
        news(k)
    else:
        print("Please enter a valid option.")
    if player['location'] not in player['visited_planets']:
        player['visited_planets'].append(player['location'])
        print(f"\n[System] New Sector Charted: {player['location']}")

    if len(player['visited_planets']) == 5:
        print("\n" + "|" * 40)
        print(Fore.YELLOW+"★ EXPLORER ACHIEVEMENT UNLOCKED! ★")
        print("You have mapped the entire solar system.")
        print("Incoming Encrypted Transmission...")
        print(f"🛑 BLACK MARKET PASSWORD DECODED: {password}")
        print("|" * 40 + "\n")
def buy_fuel():
    cost = 5
    amount = float(input("How many units of Fuel do you want? :"))
    if amount <= 0: print("Invalid amount! Please enter a positive number."); return
    total = cost * amount
    if player['credit'] >= total:
        player['credit'] -= total
        player['fuel'] += amount
        print(f"Tank refueled! Current Fuel: {player['fuel']}")
    else:
        print("Insufficient credits, Captain!")

clear_screen()
def print_header(text):
    print("\n" + Fore.CYAN + Style.BRIGHT + "=" * 40 )
    print(Fore.YELLOW + Style.BRIGHT + f"{text.center(40)}")
    print(Fore.CYAN + Style.BRIGHT + "=" * 40 + "\n" + Style.RESET_ALL)
start_choice = input("Load saved game? (Y/N) : ").upper()
if start_choice == "Y":
    load_game()
else:
    name = input("What is your name, Captain? :")
    player['name'] = name
    faction = input("Select Faction: PIRATES / POLICE / INDEPENDENT : ").upper()
while True:
    time.sleep(2)
    check_status_tasks()
    check()
    print("\n" + Fore.CYAN + "-" * 40)
    print(f"{Fore.WHITE}LOCATION: {Fore.CYAN}{player['location'].ljust(10)} {Fore.WHITE}| "
          f"CREDIT: {Fore.GREEN}${player['credit']} {Fore.WHITE}| "
          f"FUEL: {Fore.RED}{player['fuel']:.1f}")
    print(Fore.CYAN + "-" * 40 + Style.RESET_ALL)

    print(Fore.CYAN + "--- NAVIGATION ---")
    print(f"{Fore.CYAN}1. [?] Planet Info")
    print(f"{Fore.CYAN}2. [✈] Travel")

    print(Fore.GREEN + "\n--- ECONOMY ---")
    print(f"{Fore.GREEN}3. [$] Buy Goods (Market)")
    print(f"{Fore.GREEN}4. [$] Sell Goods")
    print(f"{Fore.GREEN}11.[FUEL] Buy Fuel")

    print(Fore.MAGENTA + "\n--- SHIP & PROFILE ---")
    print(f"{Fore.MAGENTA}5. [i] Profile & Cargo")
    print(f"{Fore.MAGENTA}6. [⚓] Shipyard (Buy Ship)")
    print(f"{Fore.MAGENTA}7. [★] Tasks")
    print(f"{Fore.MAGENTA}8. [♛] Prestige & Faction")

    print(Fore.YELLOW + "\n--- SYSTEM ---")
    print(f"{Fore.YELLOW}9. [S] SAVE GAME")
    print(f"{Fore.YELLOW}10.[L] LOAD GAME")
    print(f"{Fore.RED}0. [X] EXIT")

    print(Fore.BLACK + Style.BRIGHT + "\n--- CLASSIFIED ---")
    print("12.[!] Black Market")
    print("13.[] Password Reveal")

    try:
        choose = int(input("\nSelect Command >> "))
        clear_screen()

        if choose == 1:
            print_header("PLANET INFO")
            pl = int(input("1-Earth 2-Mars 3-Jupiter 4-Saturn 5-Venus\nSelect: "))
            instructions(pl)
            input("\nPress Enter to continue...")

        elif choose == 2:
            menu_travel()
        elif choose == 3:
            market_menu()

        elif choose == 4:
            market_menu_second()

        elif choose == 5:
            print(f"\n--- COMMANDER PROFILE ---")
            print(f"Name: {player['name']}")
            print(f"Rank: {player['prestige']} (Faction: {faction})")
            print(f"Ship: {player['ship']} | Capacity: {player['capacity']}")
            print(f"Fuel: {player['fuel']:.1f} | Credits: {player['credit']}")


        elif choose == 6:
                print(f"Your ship capacity : {player['capacity']}", "|", end="")
                ship_getting()
        elif choose == 7:

            for task in game_tasks:
                print(f" Task id {task['id']} - Task : {task['en']} - Reward : {task['reward']} - Situation : {task['completed']}")
        elif choose == 8:
                print("Your prestige ", player['prestige'])
                faction = input("Select Faction: PIRATES / POLICE / INDEPENDENT : ").upper()
                if faction == "PIRATES":
                    player['prestige'] = 0
                elif faction == "POLICE":
                    player['prestige'] = 100
                else:
                    player['prestige'] = 50

        elif choose == 9:
                save_game()
                input("\nPress Enter to continue......")

        elif choose == 10:
                load_game()
                input("\nPress Enter to continue......")
        elif choose == 11:
            buy_fuel()

        elif choose == 12:
            a = int(input("Enter the password :"))
            black_market(a)

        elif choose == 13:
            if len(player['visited_planets']) == 5:
                print(password)
        elif choose == 0:
                print("Safe travels, Captain!")
                break
    except ValueError:
            print("Please enter a valid number!")
            input("Press Enter to continue......")
    except KeyError:
            print("Data Error detected (KeyError).")
            input("Press Enter to continue......")


















