CHAR = "█"


class RGBA:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __repr__(self):
        # Blend the colour with a black background based on alpha
        r = int(self.r * self.a / 255)
        g = int(self.g * self.a / 255)
        b = int(self.b * self.a / 255)

        # This formatting looks awful I know
        # Explanation:
        # \033 is an escape character
        # 38 specifies the foreground colour is being changed
        # 2 means to use "true colour" mode
        # The following characters are the colour, formatted R;G;B;
        # m means the end of the escape sequence
        # The next part is the unicode block
        # Finally, \033[0m resets the colour to default

        return f"\033[38;2;{r};{g};{b}m{CHAR*2}\033[0m"


import math
import os
from PIL import Image


def resizeImage(image_path, size):
    with Image.open(image_path) as img:
        resizedImg = img.resize(size)
    return resizedImg


def imageToRGBAList(image_path, size):
    resizedImg = resizeImage(image_path, size)
    rgba_list = []

    for y in range(resizedImg.height):
        row = []
        for x in range(resizedImg.width):
            values = resizedImg.getpixel((x, y))
            if len(values) == 3:
                r, g, b = values
                a = 255
            else:
                r, g, b, a = values
            row.append(RGBA(r, g, b, a))
        rgba_list.append(row)

    return rgba_list


def convertPngToRGBAList(image_path, size) -> list:
    rgba_list = imageToRGBAList(image_path, size)
    return rgba_list


def renderImage(path: str, size: tuple) -> list:
    rgbaList = convertPngToRGBAList(path, size)
    return rgbaList


def renderImageAsBg(path) -> list:
    termSize = os.get_terminal_size()
    size = (math.floor(termSize.columns / 2), termSize.lines - 1)
    rgbaList = convertPngToRGBAList(path, size)
    return rgbaList
