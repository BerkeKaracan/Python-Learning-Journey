import requests
import tkinter as tk

window = tk.Tk()
window.title("Weather Situation")
window.geometry("300x250")
title= tk.Label(window, text="Enter location: ")
title.pack(pady=10)
location= tk.Entry(window)
location.pack(pady=5)
result = tk.Label(window, text="Waiting for location...")
result.pack(pady=15)

def main():
    current_location = location.get()
    if not current_location:
        return
    
    api_key = "8789b64d6527c6498e8d8d72ff53a703"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={current_location}&appid={api_key}&units=metric"

    try:
        request1 = requests.get(url)
        if request1.status_code == 200:
            data = request1.json()
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            result.config(text= f"Temperature: {temp} Celsius \n Situation: {weather}")
        else:
            result.config(text= "Location not found.")
        
    except Exception as e:
        result.config(text="Network error!")


button = tk.Button(window, text="Enter" ,command=main)
button.pack(pady= 10)
window.mainloop()