import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
import re

def sanitize_filename(filename):
    # Define a regular expression to match illegal characters in filenames
    illegal_chars_regex = r'[\\/:"*?<>|]'
    
    # Replace illegal characters with underscores
    sanitized_filename = re.sub(illegal_chars_regex, '', filename)

    # Replace spaces with a single underscore
    sanitized_filename = sanitized_filename.replace(' ', '_')

    return sanitized_filename

url = "https://moodle.bbbaden.ch/course/view.php?id=1154"
cookie = {"MoodleSession": "2e5o9qdskqn6c0e5eb318l66ap"}

# Send HTTP GET request with the provided cookie
response = requests.get(url, cookies=cookie)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the div with the specified class
    div_tag = soup.find('div', class_='page-header-headings')

    # Find the h1 tag inside the div
    h1_tag = div_tag.find('h1', class_='h2')

    # Extract the text from the h1 tag
    title = h1_tag.get_text(strip=True)

    sanitized_title = sanitize_filename(title)

    # Find all divs with class "activityname"
    activity_divs = soup.find_all('div', class_='activityname')

    # Create a zip file
    zip_file_path = sanitized_title + ".zip"

    with ZipFile(zip_file_path, 'w') as zip_file:
        # Extract href from each anchor inside the activity divs
        for div in activity_divs:
            anchor = div.find('a', class_='aalink stretched-link')
            if anchor:
                href = anchor.get('href')
                # Check if the link contains "mod/resource"
                if "mod/resource" in href:
                    # Download the file
                    file_response = requests.get(href, cookies=cookie)
                    if file_response.status_code == 200:
                        # Extract the file name from the URL
                        contentHeader = file_response.headers['content-disposition']
                        file_name = re.findall('filename="(.+)"', contentHeader)[0]
                        # Write the file to the zip archive
                        zip_file.writestr(file_name, file_response.content)
                        print("Downloaded and added to zip:", file_name)
                    else:
                        print("Failed to download file. Status code:", file_response.status_code)

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
