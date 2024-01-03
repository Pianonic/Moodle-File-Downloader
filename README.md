# Moodle File Downloader

![GitHub license](https://img.shields.io/badge/license-GPL--3.0-blue.svg)

## Description

The **Moodle File Downloader** is a Python script designed exclusively for downloading files from a Moodle course page on moodle.bbbaden.ch. It organizes the files into a zip archive using web scraping techniques to extract information from the course page.

## Features

- Automatic extraction of file names from Moodle course page
- Sanitization of file names for legal and safe use
- Creation of a zip archive for organized file storage

## Requirements

- Python 3.x
- Requests library
- BeautifulSoup library

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/PianoNic/Moodle-File-Downloader.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the script:

   ```bash
   python moodle_file_downloader.py
   ```

## Configuration

- Modify the `url` variable in the script to point to your Moodle course page.
- Set the `cookie` variable with your Moodle session cookie.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Requests](https://docs.python-requests.org/en/latest/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [ZipFile](https://docs.python.org/3/library/zipfile.html)
