#pip3 install -U selenium


#pip3 install webdriver-manager


from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.firefox.options import Options


#code with headless no browser will open
def no_head():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(),options=options)
    browser.get('https://nidhi.nic.in/HotelDivision/Hotels/ClassifiedLevel1.aspx?StateCode=2&StateName=Tamilnadu')
    print('Title: %s' % browser.title)
    l=browser.find_element("name", "ctl00$MainContent$btnexport")
    l.click()
    time.sleep(10)
    browser.quit()


#code with head browser will open
def head():
    browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    browser.get('https://trendoceans.com/blog')
    print('Title: %s' % browser.title)
    time.sleep(10)
    browser.quit()

no_head()
