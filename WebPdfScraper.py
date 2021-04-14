# Script to scrape Pdf document

###########################################################
# Import packages
import requests
from bs4 import BeautifulSoup
from urllib.request import unquote

# init PDF urls
website =input('Enter web-link: ')
dir = input('Enter directory path: ')

# Define Function
def pdfscrape(website,dir):
    
    response = requests.get(website)

    # Parse content
    content = BeautifulSoup(response.text, "lxml")
    # print(type(content))

    # Extract URLs refering PDF doc
    all_url = content.find_all('a')
    # loop over all urls
    for url in all_url:
        # try url containing "href" attributes
        try:
            # Pick up url containing "pdf" within "href" attributes
            if 'pdf' in url['href']:
                # Initialise pdf url
                pdf_url = ""

                # Append base url if no 'https' available in url
                if "https" not in url['href']:
                    pdf_url = website + url['href']

                    # otherwise use base url 
                
                else:
                    pdf_url = url['href']

                # Make Http request to fetch pdf bytes
                pdf_response = requests.get(pdf_url)
                # print(type(pdf_response.content))

                # Extract filename
                filename = unquote(pdf_response.url).split('/')[-1].replace(' ', '_')
                
                # Write Pdf to local file
                with open(dir + '/' + filename , 'wb') as f:
                    f.write(pdf_response.content)

        # Skip all the other urls
        except:
            pass

pdfscrape(website,dir)