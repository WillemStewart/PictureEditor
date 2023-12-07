""" 
    Uses a module "images" by Kenneth Lambert that helps 
    process image files
"""

import images

def blackAndWhite(Image):
    blackPixel = (0, 0, 0)
    whitePixel = (255, 255, 255)
    for y in range(myImage.getHeight()):
        for x in range(myImage.getWidth()):
            (r, g, b) = myImage.getPixel(x, y)
            average = (r + g + b) // 3
            if average < 128:
                Image.setPixel(x, y, blackPixel)
            else:
                Image.setPixel(x, y, whitePixel)
    Image.draw()

def grayScale(Image):
    for y in range(Image.getHeight()):
        for x in range(Image.getWidth()):
            (r, g, b) = Image.getPixel(x, y)
            r = int(r * 0.299)
            g = int(g * 0.587)
            b = int(b * 0.114)
            lum = r + g + b
            Image.setPixel(x, y, (lum, lum, lum))
    Image.draw()        

def shrink(Image, factor):
    width = Image.getWidth()
    height = Image.getHeight()
    new = images.Image(width // factor, height // factor)
    oldY = 0
    newY = 0
    while oldY < height - factor:
        oldX = 0
        newX = 0
        while oldX < width - factor:
            oldP = Image.getPixel(oldX, oldY)
            new.setPixel(newX, newY, oldP)
            oldX += factor
            newX += 1
        oldY += factor
        newY += 1
    new.draw()

print("*" * 30)
print("*  Picture Conversion Program")
print("*" * 30)
print("")

myString = input("Please enter the name of the image file to be modified: ")
myImage = images.Image(myString)
myImage.draw()
baseImage = myImage.clone()

print("")
print("Options: ")
print("(1) Black and White Filter")
print("(2) Grayscale Filter")
print("(3) Image Shrink")
print("")
print("(x) Exit")
print("")
userInput = input("Please enter your selection: ")

while userInput != 'x':
    if userInput == '1':
        blackAndWhite(myImage)
        myImage = baseImage
        userInput = input("Please enter your selection: ")

    elif userInput == '2':
        grayScale(myImage)
        myImage = baseImage
        userInput = input("Please enter your selection: ")

    elif userInput == '3':
        myFactor = int(input("Reduce by what factor?"))
        shrink(myImage, myFactor)
        myImage = baseImage
        userInput = input("Please enter your selection: ")

    else:
        print("Incorrect input, please try again")
        userInput = input("Please enter your selection: ")

print("Ending program")
