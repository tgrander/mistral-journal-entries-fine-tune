import requests
from bs4 import BeautifulSoup

# URL of the website
url = 'https://www.nifty.org/nifty/gay/'

# Send a request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract data as needed, e.g., all text
    texts = soup.get_text()
    print(texts)
else:
    print("Failed to retrieve the webpage")

# Add more logic here to navigate and extract specific data