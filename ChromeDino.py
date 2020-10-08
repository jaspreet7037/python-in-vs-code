from os import truncate
import pyautogui
from PIL import Image , ImageGrab
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data): 
    for i in range(300, 415): 
            for j in range(410, 610):
                if data[i , j] < 100:
                    hit("down")
                    return True

    for i in range(300, 415): 
            for j in range(600, 650):
                if data[i , j] < 100:  
                    hit("up")              
                    return True
    return False                     


# def draw():
    
# def  takeScreenshot():
    # return image()

if __name__ == "__main__":
    print("Hey ... Dino game i about to start in 2 seconds")
    time.sleep(2)
    # hit('up')

    while True: 
       #  image = takeScreenshot() 
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
        '''
        # print(asarray(image))
         # Draw the rectangle 
        for i in range(300, 415): 
            for j in range(600, 650):
               data[i , j] = 0
        
        for i in range(300, 415): 
            for j in range(410, 610):
               data[i , j] = 171
        
        image.show()
        break
    
        '''