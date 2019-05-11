import numpy as np
from PIL import ImageGrab, Image
import cv2
import pytesseract
import math
import requests
import json
import winsound

config = json.loads(open('config.json').read())
numtxt = 0
class Imaging:
    def __init__(self):
        self.currentHealth = 0
        numtxt = 0
        self.ocrErr = False

    def process(self, greyImg):
        self.currentHealth
        global numtxt
        txt = pytesseract.image_to_string(greyImg)
        try:
            numtxt = int(txt)
        except ValueError:
            winsound.Beep(37,0)
        if numtxt != self.currentHealth:
            print(numtxt)
            winsound.PlaySound('yousuck.wav', winsound.SND_FILENAME)
            self.currentHealth = numtxt

def main():
    imaging = Imaging()
    while(True):
        x = config['x_cord']
        y = config['y_cord']
        offx = config['off_x']
        offy = config['off_y']
        
        new_size_x = 300
        new_size_y = 300

        img = ImageGrab.grab(bbox=(x-375, y, x + offx-220, y + offy+105)).convert('L')
        
        #img = img.resize((new_size_x, new_size_y), Image.ANTIALIAS)
        #img = np.float32(img)
        #cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        #helping with image processing
        img = np.array(img, dtype = 'uint8')
        #img = np.float32(img)
        #img = cv2.blur(img, (9,9), img)
        cv2.imshow('Fortnite Health', np.invert(img))
        
        if imaging.process(img):
            winsound.Beep(500,0)
        if cv2.waitKey(25) & 0xFF == ord('q'):  
            cv2.destroyAllWindows()
            
            break

if __name__ == '__main__':
    main()