import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# Scrape the below website https://mcds.cs.cmu.edu/directory/all/154/1 
# Extract the data, page count and find the Name, Email, Office and Phone of each professor and print it in XML format

def get_page_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the pagination element and get the last page number
    pager = soup.find('ul', class_='pager')
    last_page = int(pager.find_all('li', class_='pager-item')[-1].text)
    
    return last_page

# Example usage
url = "https://mcds.cs.cmu.edu/directory/all/154/1"
page_count = get_page_count(url)
print(f"Total Pages: {page_count}")

def scrape_professor_data(page_url, total_pages):
    data = []
    
    for page in range(total_pages):
        print(page)
        # TODO: Get the url for each page
        url = None # replace this

        print(url)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # TODO: Look at the page source and identify the right tag to find all professors
        rows = soup.find_all(None)

        for row in rows:
            # Extract the email
            email_tag = row.find('a', href=lambda x: x and x.startswith('mailto:'))
            email = email_tag.get_text(strip=True) if email_tag else 'N/A'

            # Extract the name
            name_tag = None # TODO
            name = None # TODO

            # Extract the office
            office_div = row.find('div', class_=lambda x: x and 'views-field-field-computed-building' in x)
            if office_div:
                office_text = office_div.get_text(separator=' ', strip=True)
                office = office_text.replace('Office:', '').strip()
            else:
                office = 'N/A'
            
            data.append({
                'name': name,
                'email': email,
                'office': office
            })
    return data

# Example usage
# data = scrape_professor_data(url, page_count)

def to_xml(data):
    root = ET.Element("Professors")
    
    for prof in data:
        prof_elem = ET.SubElement(root, "Professor")
        ET.SubElement(prof_elem, "Name").text = prof['name']
        ET.SubElement(prof_elem, "Email").text = prof['email']
        ET.SubElement(prof_elem, "Office").text = prof['office']
    
    return ET.tostring(root, encoding='unicode')

# Example usage
# print("XML Output:")
# print(to_xml(data))

