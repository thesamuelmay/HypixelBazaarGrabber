import requests
import json
import os
from datetime import datetime

BAZAAR_API_URL = 'https://api.hypixel.net/skyblock/bazaar'
DATA_FOLDER = 'data'

def fetch_bazaar_data():
    response = requests.get(BAZAAR_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

def save_bazaar_data_to_file(data, folder):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Generate the filename with the current date and time
    timestamp = datetime.now().strftime('%d%b%y-%H%M')
    filename = os.path.join(folder, f'{timestamp}.json')
    
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    return filename

def main():
    try:
        print("Fetching bazaar data...")
        data = fetch_bazaar_data()
        print("Bazaar data fetched successfully.")
        
        filename = save_bazaar_data_to_file(data, DATA_FOLDER)
        print(f"Bazaar data saved to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
        main()
