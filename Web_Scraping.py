from selenium import webdriver
from selenium.webdriver.common.by import By
import time



def get_articles(url):
    # Initialize the Chrome Driver
    driver = webdriver.Chrome()

    # Navigate to url
    driver.get(url)

    # Scrape Articles
    main_article = driver.find_elements(By.CSS_SELECTOR, "article h2 a")
    other_articles = driver.find_elements(By.CSS_SELECTOR, "article h3 a")
    articles = main_article + other_articles
    titles = [article.text for article in articles]
    links = [article.get_attribute('href') for article in articles]

    return [titles, links]


def villanovan():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    url = 'http://webcache.googleusercontent.com/search?q=cache:https://villanovan.com/&strip=0&vwsrc=0'
    url_2 = 'https://villanovan.com/'
    driver.get(url_2)
    time.sleep(3)
    #elements = [my_elem for my_elem in driver.find_elements(By.CSS_SELECTOR, "a.homeheadline")]
    #links = [i.get_attribute("href") for i in elements if len(i.text) != 0]
    #titles = [i.text for i in elements if len(i.text) != 0]

    a = driver.find_elements(By.CLASS_NAME, "homeheadline")
    titles = [i.get_attribute('text') for i in a]
    links = [i.get_attribute('href') for i in a]
    return [titles, links]

if __name__ == "__main__":
    print(villanovan())