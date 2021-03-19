from selenium import webdriver
from re import sub
import numpy as np
import statsmodels.stats.api as sms

browser=webdriver.Chrome(executable_path=r'C:\Users\Administrator\Documents\chromedriver.exe')
browser.get("http://www.randhawa.us/games/retailer/nyu.html")

maintain = browser.find_element_by_id("maintainButton")
dc_10 = browser.find_element_by_id("tenButton")
dc_20 = browser.find_element_by_id("twentyButton")
dc_40 = browser.find_element_by_id("fortyButton")
restart = browser.find_element_by_class_name("button")

scores = []

for i in range(1000):
    for tr in browser.find_elements_by_xpath('//table[@id="result-table"]//tr'):
        tds = tr.find_elements_by_tag_name('td')
    sales = int(tds[-2].text)
    if sales < 60:
        dc_40.click()
    elif sales < 80:
        dc_20.click()
        for j in range(10):
            maintain.click()
        dc_40.click()
    elif sales < 100:
        dc_10.click()
        for p in range(6):
            maintain.click()
        dc_20.click()
        for x in range(6):
            maintain.click()
    else:
        for q in range(4):
            maintain.click()
        dc_10.click()
        for g in range(9):
            maintain.click()
    revenue = int(sub(r'[^\d.]', '', browser.find_element_by_id("rev").text))
    perfect = int(sub(r'[^\d.]', '', browser.find_element_by_id("perfect").text))
    scores.append(1 - revenue/perfect)
    restart.click()


print(np.mean(scores))
print(np.std(scores, ddof=1))
print(sms.DescrStatsW(scores).tconfint_mean())

