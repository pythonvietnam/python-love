import requests
from PIL import Image
from io import BytesIO


def get_image_size(url):
    data = requests.get(url).content
    im = Image.open(BytesIO(data))    
    return im.size


if __name__ == "__main__":
    url = "http://4.bp.blogspot.com/_A2NamGQmyCc/TO1nWedGQQI/AAAAAAAAAnA/WxBVyEGHxjc/s1600/sbn_pic_2.jpg"
    width, height = get_image_size(url)
    print width, height
