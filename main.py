import requests
from zipfile import ZipFile
from datetime import datetime

current_year = datetime.now().year  # Hämta nuvarande år
start_year = 2020

for year in range(start_year, current_year + 1):  # inkludera det aktuella året
    file_url = f"https://data.jobtechdev.se/annonser/historiska/2020.json.zip"
    response = requests.get(file_url)
    
    if response.status_code == 200:  # kontrollera om svaret är OK
        file_name = f"data_{year}.zip"
        
        # Spara zip-filen lokalt
        with open(file_name, 'wb') as file:
            file.write(response.content)
        
        # Extrahera innehållet i zip-filen
        with ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(f"data_{year}")
            
        print(f"Data for {year} downloaded and extracted.")
    else:
        print(f"Failed to download data for {year}. Status code: {response.status_code}")
