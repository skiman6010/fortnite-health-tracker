import numpy as np
from PIL import ImageGrab, Image
import cv2
import pytesseract
import math
import requests
import json

config = json.loads(open('config.json').read())

class Imaging:
    def __init__(self):
        self.currentHealth = 100
        self.ocrErr = False

    def process(self, greyImg):
        self.currentHealth
        txt = pytesseract.image_to_string(greyImg)
        if not txt == '':
            new_health = ''.join(filter(lambda x: x.isdigit(), txt))
            if not new_health == '':
                if new_health == '01':
                    new_health = '0'
                    print('Health: {}'.format(new_health))
                else:
                    print('Health: {}'.format(new_health))
        try:
            health = int(txt)
            self.ocrErr = False
        except:
            health = self.currentHealth
            if not self.ocrErr:
                health = self.currentHealth - 1
                self.ocrErr = True

        if health < self.currentHealth:
            self.currentHealth = health
            return True
        return False

def main():
    imaging = Imaging()
    while(True):
        x = config['x_cord']
        y = config['y_cord']
        offx = config['off_x']
        offy = config['off_y']
        
        new_size_x = 300
        new_size_y = 100

        img = ImageGrab.grab(bbox=(x, y, x + offx, y + offy)).convert('L')
        img = img.resize((new_size_x, new_size_y), Image.ANTIALIAS)
        #helping with image processing
        img = np.array(img)
        cv2.imshow('Fortnite Health', img)
        
        if imaging.process(img):
            if not config['raspberry_pi_host'] is None:
                requests.get(config['raspberry_pi_host'])

        if cv2.waitKey(25) & 0xFF == ord('q'):  
            cv2.destroyAllWindows()
            break

if __name__ == '__main__':
    main()
