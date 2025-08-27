import requests
from bs4 import BeautifulSoup
import csv


def extract_data(block):
    a1 = block.find('a', class_="govuk-link")
    title = a1.get_text(strip=True)
    link = a1.get('href')
    publisher_tag = block.find('dd', class_="published_by")
    published_by = publisher_tag.get_text(strip=True) if publisher_tag else "Unknown"
    date_tag = block.find("dt", string="Last updated:")
    published_date = date_tag.find_next("dd").get_text(strip=True) if date_tag else "Null"
    content_tag = block.find('p')
    content = content_tag.get_text(strip=True)
    return title, link, published_by, published_date, content
csv_file = open('uk_data.csv', 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
# header row
csv_writer.writerow([
    'Title',
    'Link',
    'Published_by',
    'Published_date',
    'Content',
    'Dataset_page',
    'Download_link',
    'Format',
    'Date'
])
all_links = []
user_input_1 = input("Enter what do you want for scrapping : \n"
                        "Crime and justice,Defence,Education,Environment,Government,"
                        "spending,Health,Mapping,Society,Towns and cities,"
                        "Transport,Digital,service,performance,reference,data")
if user_input_1 == 'Government':
    user_input_2 = input("Enter 'public' or 'specific': ")
    if user_input_2 == 'public':
        page = 1
        while True:
            url = f"https://www.data.gov.uk/search?filters%5Btopic%5D=Government&page={page}"
            response = requests.get(url)
            if response.status_code != 200:
                break

            soup = BeautifulSoup(response.content, "lxml")
            links = soup.find_all('div', class_="dgu-results__result")
            if not links:
                break

            for block in links:
                title, link, published_by, published_date, content = extract_data(block)
                csv_writer.writerow([
                    title,
                    link,
                    published_by,
                    published_date,
                    content,
                    '',
                    '',
                    '',
                    ''
                ])
            page += 1
    elif user_input_2 == 'specific':
        page = 1
        while True:
            url = f"https://www.data.gov.uk/search?filters%5Btopic%5D=Government&page={page}"
            response = requests.get(url)
            if response.status_code != 200:
                break

            soup = BeautifulSoup(response.content, "lxml")
            links = soup.find_all('div', class_="dgu-results__result")
            if not links:
                break
            for block in links:
                a1 = block.find('a', class_="govuk-link")
                if a1:
                    full_link = f"https://www.data.gov.uk{a1.get('href')}"
                    all_links.append(full_link)
            print(f'Page {page} links collected')
            page += 1
        for link in all_links:
            response = requests.get(link)
            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.content, "lxml")
            title = soup.find('h1', class_="heading-large")
            title = title.get_text(strip=True)
            publisher_tag = soup.find('dd', property="dc:creator")
            published_by = publisher_tag.get_text(strip=True) if publisher_tag else "Unknown"
            date_tag = soup.find("dt", string="Last updated:")
            published_date = date_tag.find_next("dd").get_text(strip=True) if date_tag else "Null"
            content_tag = soup.find('div', class_='js-summary').find('p')
            content = content_tag.get_text(strip=True)
            table_body = soup.find("tbody", class_="govuk-table__body")
            if table_body:
                rows = table_body.find_all("tr")
                for row in rows:
                    tds = row.find_all("td")
                    download_link = tds[0].find("a", attrs={"data-ga-event": "download"})["href"]
                    file_format = tds[1].get_text(strip=True)
                    date = tds[2].get_text(strip=True)
                    csv_writer.writerow([
                        title,
                        link,
                        published_by,
                        published_date,
                        content,
                        link,
                        download_link,
                        file_format,
                        date
                    ])
            else:
                csv_writer.writerow([
                    title,
                    link,
                    published_by,
                    published_date,
                    content,
                    link,
                    '',
                    '',
                    ''
                ])
if user_input_1 == 'Crime and justice':

    user_input_2 = input("Enter 'public' or 'specific': ")
    if user_input_2 == 'public':
        page = 1
        while True:
            url = f"https://www.data.gov.uk/search?filters%5Btopic%5D=Crime+and+justice&page={page}"
            response = requests.get(url)
            if response.status_code != 200:
                break

            soup = BeautifulSoup(response.content, "lxml")
            links = soup.find_all('div', class_="dgu-results__result")
            if not links:
                break

            for block in links:
                title, link, published_by, published_date, content = extract_data(block)
                csv_writer.writerow([
                    title,
                    link,
                    published_by,
                    published_date,
                    content,
                    '',
                    '',
                    '',
                    ''
                ])
            page += 1
    elif user_input_2 == 'specific':
        page = 1
        while True:
            url = f"https://www.data.gov.uk/search.html?filters%5Btopic%5D=Crime+and+justice&page={page}"
            response = requests.get(url)
            if response.status_code != 200:
                break

            soup = BeautifulSoup(response.content, "lxml")
            links = soup.find_all('div', class_="dgu-results__result")
            if not links:
                break
            for block in links:
                a1 = block.find('a', class_="govuk-link")
                if a1:
                    full_link = f"https://www.data.gov.uk{a1.get('href')}"
                    all_links.append(full_link)
            print(f'Page {page} links collected')
            page += 1
        for link in all_links:
            response = requests.get(link)
            if response.status_code != 200:
                continue

            soup = BeautifulSoup(response.content, "lxml")
            title = soup.find('h1', class_="heading-large")
            title = title.get_text(strip=True)
            publisher_tag = soup.find('dd', property="dc:creator")
            published_by = publisher_tag.get_text(strip=True) if publisher_tag else "Unknown"
            date_tag = soup.find("dt", string="Last updated:")
            published_date = date_tag.find_next("dd").get_text(strip=True) if date_tag else "Null"
            content_tag = soup.find('div', class_='js-summary').find('p')
            content = content_tag.get_text(strip=True)
            table_body = soup.find("tbody", class_="govuk-table__body")
            if table_body:
                rows = table_body.find_all("tr")
                for row in rows:
                    tds = row.find_all("td")
                    download_link = tds[0].find("a", attrs={"data-ga-event": "download"})["href"]
                    file_format = tds[1].get_text(strip=True)
                    date = tds[2].get_text(strip=True)
                    csv_writer.writerow([
                        title,
                        link,
                        published_by,
                        published_date,
                        content,
                        link,
                        download_link,
                        file_format,
                        date
                    ])
                else:
                    csv_writer.writerow([
                    title,
                    link,
                    published_by,
                    published_date,
                    content,
                    link,
                    '',
                    '',
                    ''
                ])
csv_file.close()
