# fortnite-health-tracker
A python application that tracks your health in fortnite that has an optional nerf gun shooting flask server.

#Credits: Michael Reeves
[Source](https://bitbucket.org/mtreeves808/footnot-health-detection/)

#Setup

The OCR that the program uses is Tesseract OCR you can download it below.
Downloads: [Linux](https://github.com/tesseract-ocr/tesseract/wiki#linux) [Windows](https://github.com/tesseract-ocr/tesseract/wiki#windows)

Make sure you edit the config file in client/ if you dont have or want to setup the server on an RPI for shooting a airsoft/nerf gun then leave it blank.

The configuration file has coordinates which are for locating the health bar you can change those as needed.

#Installation
Open cmd prompt in windows or a terminal in linux and run the following.
```
pip3 install -r requirements.txt
```

#Running
```
python3 main.py
```

**Note: the server is optional it is not required if you are just going to use the health detection then only worry about the client folder.**