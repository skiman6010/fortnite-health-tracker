import numpy as np
from PIL import ImageGrab, Image
import cv2
import pytesseract
import math
import requests
import json
import winsound

config = json.loads(open('config.json').read())

class Imaging:
    def __init__(self):
        self.currentHealth = 0
        self.ocrErr = False

    def process(self, greyImg):
        self.currentHealth
        txt = pytesseract.image_to_string(greyImg)
        if txt != self.currentHealth:
            print(txt)
            
            self.currentHealth = txt

def main():
    imaging = Imaging()
    while(True):
        x = config['x_cord']
        y = config['y_cord']
        offx = config['off_x']
        offy = config['off_y']
        
        new_size_x = 300
        new_size_y = 300

        img = ImageGrab.grab(bbox=(x-355, y+5, x + offx-220, y + offy+95)).convert('L')
        #img = img.resize((new_size_x, new_size_y), Image.ANTIALIAS)
        #img = np.float32(img)
        #cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        #helping with image processing
        
        img = np.array(img, dtype = 'uint8')
        
        
        cv2.imshow('Fortnite Health', img)
        
        if imaging.process(img):
            winsound.Beep(500,0)
        if cv2.waitKey(25) & 0xFF == ord('q'):  
            cv2.destroyAllWindows()
            
            break

if __name__ == '__main__':
    main()