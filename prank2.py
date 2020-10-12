import time
import random
import pyautogui

def moveMouse(hlis):
    startTime = time.time()
    timeElapsed = time.time() - startTime
    xSize, ySize = pyautogui.size()

    while timeElapsed < hlis:
        x, y = random.randrange(xSize), random.randrange(ySize)
        pyautogui.moveTo(x, y, duration=0.2)
        timeElapsed = time.time() - startTime

if __name__ == "__main__":
    pyautogui.alert("Update Completed!")
    moveMouse(120)
