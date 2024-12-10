import requests
from bs4 import BeautifulSoup
import csv
import os

# Helper function to convert DMS (Degrees, Minutes, Seconds) format to decimal
def dms_to_decimal(coord):
    try:
        parts = coord.split()  # Split by spaces
        degrees = float(parts[0][:-1])  # Remove the last character (N/S/E/W) from degrees
        minutes = float(parts[1][:-1]) if len(parts) > 1 else 0  # Remove the last character (')
        seconds = float(parts[2][:-1]) if len(parts) > 2 else 0  # Remove the last character (")
        direction = parts[-1]  # Get the direction (N/S/E/W)
        
        # Convert to decimal
        decimal = degrees + (minutes / 60) + (seconds / 3600)
        
        # Adjust for direction
        if direction in ['S', 'W']:
            decimal = -decimal
        
        return round(decimal, 6)  # Round to 6 decimal places for API precision
    except (IndexError, ValueError):
        return None  # Return None if the format is invalid

# Read country codes from a CSV file
country_codes_file = 'country_codes.csv'

# Ensure the file exists
if not os.path.exists(country_codes_file):
    print(f"File '{country_codes_file}' not found!")
    exit()

# Read the Alpha-2 codes and country names from the file
countries = []
with open(country_codes_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        countries.append({
            'Alpha-2': row['Alpha-2 code'],
            'Country': row['Country']
        })

# Base URL
base_url = 'https://opennav.com/waypoint/'

# List to store all scraped data
all_scraped_data = []

# Loop through all countries
for country in countries:
    country_code = country['Alpha-2']
    country_name = country['Country']
    print(f"Fetching waypoints for country: {country_name} ({country_code})")
    url = base_url + country_code  # Construct URL for the current country
    
    try:
        # Send GET request to fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()
        
        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the table element with class 'datagrid fullwidth'
        table = soup.find('table', class_='datagrid fullwidth')
        if not table:
            print(f"No data found for {country_name} ({country_code})")
            continue

        # Find all table rows (<tr>) inside the table
        rows = table.find_all('tr')

        # Loop through each row in the table
        for row in rows:
            # Find all table data cells (<td>) in the row
            cols = row.find_all('td')
            
            # Skip rows that don't contain enough data
            if len(cols) < 5:  # Ensure there are at least 5 columns
                continue
            
            # Extract the IDENT, LATITUDE, and LONGITUDE values
            ident = cols[0].text.strip()  # The first column contains IDENT
            raw_latitude = cols[2].text.strip()  # The third column contains LATITUDE
            raw_longitude = cols[4].text.strip()  # The fifth column contains LONGITUDE
            
            # Format the latitude and longitude
            latitude = dms_to_decimal(raw_latitude)
            longitude = dms_to_decimal(raw_longitude)
            
            # Check if the row has valid data
            if ident and latitude is not None and longitude is not None:
                all_scraped_data.append({
                    'IDENT': ident,
                    'COUNTRY_CODE': country_code,
                    'COUNTRY_NAME': country_name,
                    'LATITUDE': latitude,
                    'LONGITUDE': longitude
                })

    except Exception as e:
        print(f"An error occurred for {country_name} ({country_code}): {e}")

# Save all the scraped data into one CSV file
if all_scraped_data:
    with open('global_aviation_waypoints.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['COUNTRY_CODE', 'COUNTRY_NAME', 'IDENT', 'LATITUDE', 'LONGITUDE']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # Write the header row
        writer.writerows(all_scraped_data)  # Write all data rows
    print("Data saved to 'all_waypoints.csv'")
else:
    print("No data to save.")
