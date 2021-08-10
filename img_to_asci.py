from PIL import Image
import requests
from io import BytesIO

import webbrowser



asci = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
def main(img, newWidth= 200):

    # resizing image 
    image = Image.open(img)
    
    HeightOfImage, widthOfImage = image.size
    ratio = HeightOfImage/widthOfImage
    newHeight = int(newWidth*ratio)
    image = image.resize((newWidth,newHeight))

    # grayify image (turn it into black and white)
    image = image.convert("L")

    pixels = image.getdata()
    chars = ""
    for pixel in pixels:
        chars += asci[pixel//25]

    chars = list(chars)
    str = ''
    for i in range(0, len(chars),newWidth):
        chars[i] = chars[i]+"\n"
    for i in chars:
        str+=i

    # print(str)
    with open('asci.txt' , 'w') as f:
        f.write(str)





while True:
    url = 'https://source.unsplash.com/random/800x800/?img=1'
    response = requests.get(url)
    main(BytesIO(response.content),250)
    webbrowser.open("asci.txt")

    if input('type next to get new one , type exit to stop the code : ')=='exit':
        break