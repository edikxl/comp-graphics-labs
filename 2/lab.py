from typing import List
import sys

import numpy as np
from PIL import Image

def getDataFromFile(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()

def getCordsFromData(data: str) -> set:
    x = []
    y = []

    data = data.split('\n') 
    for string in data:
        if string:
            x_, y_ = string.split(' ')

            x.append(int(x_))
            y.append(int(y_))

    return x, y

def getImageArrayFromCords(x: List[int], y: List[int], color: List[int]) -> list:
    imageArray = np.zeros([ max(y) + 1, max(x) + 1, 4], dtype=np.uint8)

    for i in range(len(x)):
        imageArray[y[i]][x[i]] = color
    
    return imageArray

def enchanceImage(image):
    image = image.resize((540, 960), Image.LANCZOS)
    image = image.rotate(90, expand=True)

    return image

def changeExtToPng(path: str) -> str:
    return path[:path.find('.') + 1] + 'png'

if __name__ == '__main__':
    COLOR = [0, 0, 0, 255]

    datasetPath = sys.argv[1]

    data = getDataFromFile(datasetPath)
    x, y = getCordsFromData(data)
    imageArray = getImageArrayFromCords(x, y, COLOR)

    image = Image.fromarray(imageArray)
    image = enchanceImage(image)
    image.save(changeExtToPng(datasetPath))
