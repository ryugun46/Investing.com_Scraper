# import needed libraries

from bs4 import BeautifulSoup
import requests
import pandas as pd
import random

URL = "https://www.investing.com/equities/most-active-stocks"

# The user agents used for rotation of user agents

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.188',
    'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0',
    'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
]
# Selects random user agent which helps to rotate the user agents
user_agent = random.choice(user_agent_list)

headers = {'User-Agent': user_agent}
response = requests.get(URL, headers=headers)
main_page_soup = BeautifulSoup(response.content, 'html.parser')


# Function finds the company name and puts them in a list
def find_company_name(soup):
    Company_Name = soup.find_all('a', {
        'class': 'font-semibold text-[#181C21] hover:text-[#1256A0] text-ellipsis whitespace-nowrap overflow-hidden'})
    Company_Name_List = []
    for anchor_tag in Company_Name:
        title_value = anchor_tag['title']
        Company_Name_List.append(title_value)
    return Company_Name_List


# Function finds the company links and puts them in a list
def find_company_url(soup):
    Company_URL = soup.find_all('a', {
        'class': 'font-semibold text-[#181C21] hover:text-[#1256A0] text-ellipsis whitespace-nowrap overflow-hidden'})
    Company_URL_List = []
    for anchor_tag in Company_URL:
        href_value = "https://www.investing.com/" + anchor_tag['href']
        Company_URL_List.append(href_value)
    return Company_URL_List


# Stores company names in a list
company_name_list = (find_company_name(main_page_soup))

# Stores company URLs in a list
company_url_list = (find_company_url(main_page_soup))

# Stores last price data in a list
last_price_list = []
'''
for link in company_url_list:
    link_response = requests.get(link, headers=headers)
    link_soup = BeautifulSoup(link_response.content, 'html.parser')
    last_price = link_soup.find_all('div', {'class': 'text-5xl/9 font-bold md:text-[42px] md:leading-[60px] text-[#232526]'})

    for i in range(len(last_price)):
        last_price_text = last_price[i].text
        last_price_list.append(last_price_text)

for i in range(len(company_name_list)):
    print(f'Company Name:"{company_name_list[i]}" Last Price:"{last_price_list[i]}"')

# Created a dataframe

data = {'Company Name': company_name_list, 'Last Price': last_price_list}
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('trending_stocks.csv', index=False)
'''
for link in company_url_list:
    link_response = requests.get(link, headers=headers)
    link_soup = BeautifulSoup(link_response.content, 'html.parser')
    last_price = link_soup.find_all('div', {'class': 'text-5xl/9 font-bold md:text-[42px] md:leading-[60px] text-[#232526]'})
    PE_ratio = link_soup.find('dd', {'data-test': 'ratio'}).get_text()
    price_change_percent = link_soup.find('span', {'data-test':'instrument-price-change-percent'}).get_text()
    print(PE_ratio)

