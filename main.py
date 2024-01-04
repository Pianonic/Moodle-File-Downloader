import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
import re

def sanitize_filename(filename):
    illegal_chars_regex = r'[\\/:"*?<>|]'
    sanitized_filename = re.sub(illegal_chars_regex, '', filename)
    sanitized_filename = sanitized_filename.replace(' ', '_')

    return sanitized_filename

url = "https://moodle.bbbaden.ch/course/view.php?id="
cookie = {"MoodleSession": ""}

response = requests.get(url, cookies=cookie)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    div_tag = soup.find('div', class_='page-header-headings')
    h1_tag = div_tag.find('h1', class_='h2')
    title = h1_tag.get_text(strip=True)

    sanitized_title = sanitize_filename(title)
    activity_divs = soup.find_all('div', class_='activityname')

    zip_file_path = sanitized_title + ".zip"

    with ZipFile(zip_file_path, 'w') as zip_file:
        for div in activity_divs:
            anchor = div.find('a', class_='aalink stretched-link')
            if anchor:
                href = anchor.get('href')
                if "mod/resource" in href:
                    file_response = requests.get(href, cookies=cookie)
                    if file_response.status_code == 200:
                        contentHeader = file_response.headers['content-disposition']
                        file_name = re.findall('filename="(.+)"', contentHeader)[0]
                        zip_file.writestr(file_name, file_response.content)
                        print("Downloaded and added to zip:", file_name)
                    else:
                        print("Failed to download file. Status code:", file_response.status_code)

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
