import csv
import requests
from bs4 import BeautifulSoup

output_filename = "recent_travel_deals.csv"
url = "https://secretflying.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    response = request.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    deals = soup.find_all('artical', class_='entry-card')

    with open(output_filename, mode='w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Deal Title", "Link URL"])

        counter = 0

        for deal in deals:
            title_element = deal.find('h2', class_='entry-title')
            title_text = title_element.text.strip() if title_element else "No title found"

            link_element = title_element.find('a') if title_element else None
            link_url = link_element['href'] if link_element and link_element.has_attr('href') else "No link found"

            writer.writerow([title_text, link_url])
            counter += 1
        
    print(f"Scraped {counter} items and saved them to {output_filename}.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching web data: {e}")
except IOError as e:
    print(f"Could not write data to file: {e}.")