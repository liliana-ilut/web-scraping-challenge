from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd 

def init_browser():

    #Mac Users
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

#Mars News
#create dictionary
mars_info = {}

def scrape_mars_news():
    try:
        browser= init_browser()

     # URL of page to be scraped
        url = 'https://mars.nasa.gov/news/8744/nasa-engineers-checking-insights-weather-sensors/'
        browser.visit(url)

        soup = BeautifulSoup(response.text, 'lxml')
        news_title = soup.title.text
        news_p = soup.find_all('p')[1].text

     # Dictionary entry from MARS NEWS
        mars_info['news_title'] = news_title
        mars_info['news_paragraph'] = news_p
    
        return mars_info
    
    finally:

        browser.quit()

#Mars Image
def scrape_mars_image():
    try:
        browser= init_browser()
        image_url_featured= 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_url_featured)

        # HTML Object 
        html_image = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html_image, 'html.parser')

        # Retrieve background-image url from style tag 
        featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

        # Website Url 
        main_url = 'https://www.jpl.nasa.gov'

        # Concatenate website url with scrapped route
        featured_image_url = main_url + featured_image_url

        # Display full link to featured image
        featured_image_url
        # Dictionary entry from FEATURED IMAGE
        mars_info['featured_image_url'] = featured_image_url 
        
        return mars_info

    finally:

        browser.quit()

#Mars Facts

def scrape_mars_facts():

    try:
        browser= init_browser()
        space_facts_url= 'https://space-facts.com/mars/'
        browser.visit(space_facts_url)

        space_facts_url = browser.html
        soup = BeautifulSoup(space_facts_url, 'html.parser')
        tables = pd.read_html(space_facts_url)
        
        space_facts_df = tables[0]
        space_facts_df.rows = ['Equatorial Diameter', 'Polar Diameter', 'Mass', 'Moons', 
              'Orbit Distance', 'Orbit Period', 'Surface Temperature:', 'First Record', 
              'Recorded By']

        facts_df = space_facts_df.rename(columns={
                                        0: "Description",
                                        1: "Value"})
        facts_df.set_index("Description", inplace=True)
        html_table = facts_df.to_html()

        # Dictionary entry from MARS FACTS
        mars_info['mars_facts'] = html_table

        return mars_info

#Mars Hemispheres

def scrape_mars_hemispheres():
    try:

        browser = init_browser()

        hemisphere_url= 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemisphere_url)

        # Parse HTML with Beautiful Soup
        hemisphere_url = browser.html
        soup = BeautifulSoup(hemisphere_url, 'html.parser')

        # Retreive all items that contain mars hemispheres information
        items = soup.find_all('div', class_='item')

        # Create empty list for hemisphere urls 
        hemisphere_image_urls = []

        # Store the main_ul 
        hemispheres_main_url = 'https://astrogeology.usgs.gov'

        # Loop through the items previously stored
        for i in items: 
            # Store title
            title = i.find('h3').text
    
            # Store link that leads to full image website
            partial_img_url = i.find('a', class_='itemLink product-item')['href']
    
            # Visit the link that contains the full image website 
            browser.visit(hemispheres_main_url + partial_img_url)
    
            # HTML Object of individual hemisphere information website 
            partial_img_html = browser.html
    
            # Parse HTML with Beautiful Soup for every individual hemisphere information website 
            soup = BeautifulSoup( partial_img_html, 'html.parser')
    
            # Retrieve full image source 
            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
    
            # Append the retreived information into a list of dictionaries 
            hemisphere_image_urls.append({"title" : title, "img_url" : img_url})

        
         mars_info['hemisphere_image_urls'] = hemisphere_image_urls

         return mars_info

    finally:

        browser.quit()






     
