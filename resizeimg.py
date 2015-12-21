#from pythonvietnam
#email: khanhnn@pythonvietnam
#you must install requests and pillow
import requests
from PIL import Image
from io import BytesIO


def get_image_size(url):
    data = requests.get(url).content
    im = Image.open(BytesIO(data))    
    return im.size


if __name__ == "__main__":
    url = "http://pythonvietnam.info/styles/default/xenforo/logo.png"
    width, height = get_image_size(url)
    print width, height
