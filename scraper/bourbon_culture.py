import requests
from bs4 import BeautifulSoup
import csv

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to fetch page. Status code: {response.status_code}")

def parse_page(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def extract_data(soup):
    headers = soup.find_all(lambda tag: tag.name == 'h2' and tag.get('id') and tag['id'].split(':')[0].isdigit())

    if headers:
        data_list = []

        for header in headers:
            header_id = header['id']
            print(f"ID: {header_id}")
            header_text = header.text.strip()

            
            ranked = header.find_all_next('p')

            if ranked:
                # Loop through each <p> tag and extract the content
                for paragraph in ranked:
                    split_result = paragraph.text.split('–', 1)
                    
                    if len(split_result) >= 2:
                        rank, title = map(str.strip, split_result)
                        data_list.append({'Ranking': rank, 'Title': title})
                    else:
                        print(f"Skipping entry: {paragraph.text}")

                for entry in data_list:
                    print(f"Ranking: {entry['Ranking']}, Title: {entry['Title']}")
                

                csv_filename = 'ranking_data.csv'
                with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
                    fieldnames = ['Ranking', 'Title']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    
                    writer.writeheader()
                    
                    writer.writerows(data_list)

                print(f"\nCSV file '{csv_filename}' created successfully.")
            else:
                print("No <p> tags found after the header.")
    else:
        print("Bourbon ranking headers not found.")
    
    return data_list
    

def run_scraper():
    url = "https://thebourbonculture.com/reviews-by-rating/"
    page_content = fetch_page(url)
    parsed_page = parse_page(page_content)
    data = extract_data(parsed_page)

    for entry in data:
        print(entry)
    # import code; code.interact(local=dict(globals(), **locals()))
