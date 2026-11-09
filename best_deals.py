import csv
import requests
from bs4 import BeautifulSoup

output_filename = "recent_travel_deals.csv"
url = "https://secretflying.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
