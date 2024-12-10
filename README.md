Waypoint Scraper

Overview

📍📍📍 This repository contains a Python script that scrapes waypoint data for countries worldwide and saves the data into a single consolidated CSV file. The waypoints are sourced from OpenNav, a platform providing aeronautical navigation data. The script uses Alpha-2 country codes from a CSV file to fetch data for all countries.

What Are Waypoints?

🛩️🛩️🛩️ Waypoints are predefined geographical coordinates used in aviation and navigation to define routes and positions in airspace. They are critical components of modern navigation systems and are represented by identifiers such as latitude, longitude, and a unique code (IDENT).

Importance of Waypoints:

✈️ Air Traffic Management: Waypoints are used by pilots and air traffic controllers to define flight paths, avoiding obstacles and ensuring safe navigation.

🌍 Route Planning: They help create efficient flight routes, reducing fuel consumption and travel time.

🎯 Precision Navigation: Waypoints are integral to satellite navigation systems (like GPS), ensuring accurate positioning.

🚨 Emergency Handling: In emergencies, waypoints assist in guiding aircraft to alternate routes or safe landing zones.

Features

✨✨✨ - Fetches waypoint data for all countries using their Alpha-2 country codes.

Converts latitude and longitude from DMS (Degrees, Minutes, Seconds) format to decimal format for compatibility with APIs.

Saves all waypoint data into a consolidated CSV file: worldwide_waypoints.csv.

Handles errors gracefully, ensuring uninterrupted processing of other countries if an issue occurs for one.

Dependencies

📦📦📦 The script uses the following Python libraries:

🧾 requests: For making HTTP requests to fetch webpage content.

🧩 BeautifulSoup (bs4): For parsing and extracting data from HTML.

📊 csv: For reading and writing CSV files.

🗂️ os: For file and directory operations.

Usage

Input File

📂📂📂 The script requires a CSV file named country_codes.csv containing country information, including their Alpha-2 codes. The file should follow this format:

Alpha-2 code,Country,Latitude (average),Longitude (average)
AD,Andorra,42.5,1.6
AE,United Arab Emirates,24,54
AF,Afghanistan,33,65
AG,Antigua and Barbuda,17.05,-61.8
AI,Anguilla,18.25,-63.1667

Running the Script

🚀🚀🚀 1. Ensure Python is installed on your system.
2. Install the required dependencies:

pip install requests beautifulsoup4

Place the country_codes.csv file in the same directory as the script.

Run the script:

python waypoint_scraper.py

The script will generate a single CSV file named worldwide_waypoints.csv in the same directory.

Output

🗂️🗂️🗂️ The output CSV file contains the following columns:

COUNTRY_CODE: Alpha-2 code of the country.

COUNTRY_NAME: Full name of the country.

IDENT: Unique identifier for the waypoint.

LATITUDE: Latitude in decimal format.

LONGITUDE: Longitude in decimal format.

Example file: worldwide_waypoints.csv

COUNTRY_CODE,COUNTRY_NAME,IDENT,LATITUDE,LONGITUDE
PK,Pakistan,ABC,33.123456,73.987654
PK,Pakistan,XYZ,34.654321,74.321098

Scale of Data

🌍🌍🌍 The script successfully scrapes over 51,000 waypoints from across the globe, providing a comprehensive dataset for aviation and navigation purposes.

Error Handling

⚠️⚠️⚠️ - If a country does not have waypoint data on the website, the script logs the message: No data found for <Country Name> (<Alpha-2 Code>).

If the website structure changes or an error occurs, the script logs the issue and moves on to the next country.

Contributing

🤝🤝🤝 Contributions to improve the script or add new features are welcome. Please fork the repository, make changes, and create a pull request.

License

📜📜📜 This project is licensed under the MIT License. See the LICENSE file for more details.

Contact

📧📧📧 For questions or suggestions, feel free to open an issue or contact.

