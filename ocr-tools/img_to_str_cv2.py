import requests
import numpy as np
import cv2
import io
import json

key = ""#enter your apikey public here
language = "fre" 
src_image = "capture.jpeg"

def running():
    img = cv2.imread(src_image)
    # print(img.shape)
    heigth, width, _ = img.shape
    #print(heigth, '  - ', width)
    # cutting image
    roi = img[5:heigth, 10:width]
    cv2.imshow("roi", roi)
    # print(roi)
    # communication with a externel serveur
    url_api = "https://api.ocr.space/parse/image"
    _, compressedimage = cv2.imencode(".jpeg", roi, [1, 90])
    file_bytes = io.BytesIO(compressedimage)
    result = requests.post(url_api,
                           files={src_image: file_bytes},
                           data={"apikey": key,"language":language}
                           )

    result = result.content.decode()
    # print(type(result))- > str
    #load in a dictionary , for easy extract for treatment
    result = json.loads(result)
    #print(result)
    parsedText = result.get("ParsedResults")
    #print(parsedText)
    text_detected = parsedText[0].get("ParsedText")
    return text_detected

text_detected = running()
print(text_detected)
