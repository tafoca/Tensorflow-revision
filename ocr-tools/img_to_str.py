from PIL import Image
import pytesseract

img = Image.open('test-fr3.png')
text = pytesseract.image_to_string(img,lang='fra') 
print(text)