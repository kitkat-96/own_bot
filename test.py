from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import random
from bs4 import BeautifulSoup 

# real url - might need replacing
# url = 'https://glastonbury.seetickets.com/content/extras'

# testing urls
glasto_url = 'file:///Users/katielovell/Documents/CodingProjects/glastonbury/own_bot/glasto_site.htm'
queue_url = 'file:///Users/katielovell/Documents/CodingProjects/glastonbury/own_bot/glasto_queue.htm'
site_options = [queue_url, glasto_url]
is_queue_page = True


# will want to set headers 
headers = {}

driver = webdriver.Firefox()

#  throws up test site
def gen_page ():
    page_choice = random.choices(site_options, weights=[0.92, 0.08])[0]
    return str(page_choice)

def refresh_page ():
    num = random.uniform(0,2)
    time.sleep(num)
    driver.get(gen_page())
        # will need to add back in the refresh
        # driver.refresh()
    return num

while is_queue_page == True: # this will change to the while false or something 
    # timeout not working
    num = refresh_page()
    loaded = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    print(num)
    page_html = str(BeautifulSoup(driver.page_source, 'html.parser'))
    # if postcode appears on queue page this will not work. 
    # If postcode does not appear on main page this will not work
    if page_html.__contains__("postcode") or page_html.__contains__("Postcode"):
        is_queue_page = False


    # except NoSuchElementException as exc:
    # #     print(exc)


# look at how to link beautiful soup and selenium
# soup = BeautifulSoup(driver, 'html.parser')
# print(soup)
# # https://www.codecademy.com/article/caupolicandiaz/web-scrape-with-selenium-and-beautiful-soup

# driver.get(random_generator)

# Refreshes the web page
