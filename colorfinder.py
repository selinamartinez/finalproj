import requests
import re
from bs4 import BeautifulSoup

def colorName(hexadecimal):
    url = "https://www.color-name.com/hex/" + hexadecimal
    # Collect and parse first page
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    # Pull all text from 'color-code color-white' div
    text = soup.find(class_='color-code color-white')

    # Removes <h4> header tags
    text = text.contents[0]

    # Removes unnecessary text
    text = text.replace("Color Name: ", "", 1)

    # Removes tabs and enters
    color = re.sub(r"[\n\t]*", "", text) 
    print(color)
    return color
