from startterm import image

if __name__ == "__main__":
    data = image.renderImageAsBg("assets/macos.jpg")
    for row in data:
        for pixel in row:
            print(pixel, end="")
        print()
