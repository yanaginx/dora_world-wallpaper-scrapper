import re
import requests
import os
import time

from bs4 import BeautifulSoup

BASE_URL = 'https://dora-world.com/wallpaper'
ROOT_URL = 'https://dora-world.com/'
DOWNLOAD_DIR = 'wallpapers'

current_path = os.path.dirname(os.path.abspath(__file__))

def extract_wallpaper_urls_from_url(url):
    full_wallpaper_urls = []
    print('Extracting Dora World Wallpaper URLs...')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('div', attrs={'class': 'item'})):
        wallpaper_a = tag.find_all('a') 
        rel_wallpaper_url = wallpaper_a[0].get('href') 
        full_wallpaper_url = ROOT_URL + rel_wallpaper_url
        full_wallpaper_urls.append(full_wallpaper_url)
    return full_wallpaper_urls
    
def download_wallpapers_from_url(base_url):
    urls = extract_wallpaper_urls_from_url(base_url)
    download_path = os.path.join(current_path, DOWNLOAD_DIR)
    if not os.path.exists(download_path):
        os.makedirs(download_path)
        print("Download directory is created!")
    for url in urls:
        filename = url.split('/')[-1]
        print("Downloading " + filename)
        response = requests.get(url, allow_redirects=True)
        full_download_path = os.path.join(download_path, filename)
        open(full_download_path, 'wb').write(response.content)
        print(filename + " downloaded!")

if __name__ == "__main__":
    download_wallpapers_from_url(BASE_URL) 
