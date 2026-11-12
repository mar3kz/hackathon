from PIL import Image
import pytesseract
import requests

url = "http://10.10.1.5:8080/fotka3.jpg"
picture = "project/pictures/picture.png"

response = requests.get(url)

if response.status_code == 200:
    # binary write
    with open(picture, "wb") as file:
        file.write(response.content)
else:
    print("neco spatne")

print(pytesseract.image_to_string(Image.open(picture)))