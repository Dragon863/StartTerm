import datetime
import os
import socket
import time
import dotenv

import requests
from startterm import image

os.system("cls")
dotenv.load_dotenv(".env")


def getIp() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    host = s.getsockname()[0]
    s.close()
    return host


def get_weather(city):
    api_key = dotenv.get_key(".env", "OWM_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return f"{data['main']['temp']}°C, {data['weather'][0]['description']}"


def drawText(data: list, text: str, row: int):
    position = len(data[row]) - 1 - (len([*text]))
    print(os.get_terminal_size().columns)
    print(position)

    print()
    for char in [*text]:
        data[row][position] = char + " "
        position += 1


def drawDash():
    data: list = image.renderImageAsBg(
        "assets/tumblr_inline_o29dtaXWxz1rtb73a_1280.jpg"
    )
    time = str(datetime.datetime.now().strftime("%H:%M"))
    drawText(data, time, 1)
    drawText(data, getIp(), 3)
    weather = get_weather(dotenv.get_key(".env", "CITY"))
    drawText(data, weather, 5)

    for row in data:
        for pixel in row:
            print(str(pixel), end="")
        print()


if __name__ == "__main__":
    while True:
        drawDash()
        time.sleep(20)
