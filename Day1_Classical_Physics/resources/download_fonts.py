"""
Download DejaVu fonts required for the presentation
"""

import urllib.request
import os

def download_fonts():
    base_url = "https://github.com/dejavu-fonts/dejavu-fonts/raw/master/ttf/"
    fonts = {
        "DejaVuSansCondensed.ttf": "DejaVuSansCondensed.ttf",
        "DejaVuSansCondensed-Bold.ttf": "DejaVuSansCondensed-Bold.ttf"
    }
    
    for font_file, local_name in fonts.items():
        url = base_url + font_file
        print(f"Downloading {font_file}...")
        urllib.request.urlretrieve(url, local_name)
        print(f"Downloaded {local_name}")

if __name__ == '__main__':
    download_fonts()
