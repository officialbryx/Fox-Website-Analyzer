import requests
from bs4 import BeautifulSoup

news_url = "https://www.foxnews.com/"

def scrape_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract headline text
    headlines = soup.find_all('h3')  # Adjust this if necessary

    # Get the text of each headline, stripping extra whitespace
    headlines_text = [headline.get_text(strip=True) for headline in headlines]

    return headlines_text

def is_valid_headline(headline):
    # Define criteria for a valid headline
    return len(headline) > 10 and not headline.startswith(('Fox Nation', 'Features & Faces', 'Political cartoons of the day'))

def format_headlines(headlines, start_number=1):
    formatted_output = ""
    valid_count = 0

    for idx, headline in enumerate(headlines, start=start_number):
        if is_valid_headline(headline):
            valid_count += 1
            formatted_output += f"{valid_count}. {headline}\n"

    return formatted_output.strip()  # Remove any trailing newline

# Scrape headlines from the site
headline_list = scrape_news(news_url)

# Format headlines starting from a specific number (e.g., 1)
formatted_headlines = format_headlines(headline_list)

# Print the formatted headlines
print(formatted_headlines)
