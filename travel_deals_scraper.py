import csv
import requests
from bs4 import BeautifulSoup
import os

def get_travel_deals():
    url = "https://secretflying.com"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        print("Fetching latest travel deals online...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        deal_cards = soup.find_all('a', class_='title-link')

        if not deal_cards:
            print("No deal cards found.")
            return []
        
        extracted_deals = []

        for card in deal_cards:
            title_text = card.text.strip() if card.text else "Unknown Destination"
            link_url = card.get('href', 'Link unavailable')

            extracted_deals.append({
                "Title" : title_text,
                "Link" : link_url
            })

        return extracted_deals

    except requests.exceptions.RequestException as e:
        print(f"Could not connect: {e}")
        return []

def save_to_spreadsheet(deals, filename="travel_deals.csv"):
    if not deals:
        print("No data saved")
        return

    try:
        file_exists = os.path.isfile(filename)

        with open(filename, mode='a', encoding='utf-8', newline='') as csv_file:
            field_names = ["Title", "Link"]
            writer = csv.DictWriter(csv_file, fieldnames=field_names)

            if not file_exists:
                writer.writeheader()
            for deal in deals:
                writer.writerow(deal)
        print(f"Successfully saved {len(deals)} items into {filename}")

    except IOError as e:
        print(f"Storage error: {e}")

if __name__ == "__main__":
    recent_deals = get_travel_deals()
    save_to_spreadsheet(recent_deals)