import datetime
import json
import os
import socket
import psutil
import dotenv
import sys
import select


import requests
from startterm import image

os.system("cls" if os.name == "nt" else "clear")
dotenv.load_dotenv(".env")


def getIp() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host = s.getsockname()[0]
    s.close()
    return host


def getWeather(city):
    api_key = dotenv.get_key(".env", "OWM_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return f"{data['main']['temp']}°C, {data['weather'][0]['description']}"


def drawTextEnd(data: list, text: str, row: int):
    position = len(data[row]) - 1 - (len([*text]))
    for char in [*text]:
        data[row][position] = char + " "
        position += 1


def drawTextCenter(data: list, text: str, row: int):
    width = len(data[row])
    start = (width - len(text)) // 2
    for i, char in enumerate(text):
        data[row][start + i] = f"\033[1m{char}\033[0m "


def dynamic_greeting() -> str:
    now = datetime.datetime.now()

    if 5 <= now.hour < 12:
        greeting = "Good Morning!"
    elif 12 <= now.hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"

    return greeting


def getBatteryStatus():
    battery = psutil.sensors_battery()
    percent = round(battery.percent) if battery else "N/A"
    return f"Battery: {percent}%"


def drawDash():
    os.system("cls" if os.name == "nt" else "clear")
    data: list = image.renderImageAsBg(
        dotenv.get_key(".env", "IMAGE"),
    )
    time = str(datetime.datetime.now().strftime("%H:%M"))
    weather = getWeather(dotenv.get_key(".env", "CITY"))
    drawTextEnd(data, time, 1)
    drawTextEnd(data, getIp(), 3)
    drawTextEnd(data, getBatteryStatus(), 5)
    drawTextEnd(data, weather, 7)
    drawTextCenter(data, dynamic_greeting(), round(0.5 * len(data)))

    for row in data:
        for pixel in row:
            print(str(pixel), end="")
        print()


with open("shortcuts.json", "r") as f:
    # User-definable presets for commands that could be run :)
    # (example included)
    commands = json.load(f)

if __name__ == "__main__":
    try:
        while True:
            drawDash()
            if sys.stdin in select.select([sys.stdin], [], [], 20)[0]:
                user_input = input().strip()
                if user_input in commands:
                    os.system("cls" if os.name == "nt" else "clear")
                    os.system(commands[user_input])
                elif user_input == "exit" or user_input == "":
                    break
    finally:
        os.system("cls" if os.name == "nt" else "clear")
