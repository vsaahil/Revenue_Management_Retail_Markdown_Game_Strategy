from selenium import webdriver
import pandas as pd
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

raw = pd.read_csv("matrix_input.csv",header=None)

scores = []

for i in range(1000):
    for i in range(14):
        for tr in browser.find_elements_by_xpath('//table[@id="result-table"]//tr'):
            tds = tr.find_elements_by_tag_name('td')
        sales = int(tds[-2].text)
        price = int(tds[-3].text)
        if price == 60:
            if sales < raw.iloc[i,4]:
                dc_40.click()
            elif sales < raw.iloc[i,3]:
                dc_20.click()
            elif sales < raw.iloc[i,2]:
                dc_10.click()
            else:
                maintain.click()
        elif price == 54:
            if sales < raw.iloc[i,7]:
                dc_40.click()
            elif sales < raw.iloc[i,6]:
                dc_20.click()
            else:
                maintain.click()
        elif price == 48:
            if sales < raw.iloc[i,9]:
                dc_40.click()
            else:
                maintain.click()
    revenue = int(sub(r'[^\d.]', '', browser.find_element_by_id("rev").text))
    perfect = int(sub(r'[^\d.]', '', browser.find_element_by_id("perfect").text))
    scores.append(1 - revenue/perfect)
    restart.click()


print(np.mean(scores))
print(np.std(scores, ddof=1))
print(sms.DescrStatsW(scores).tconfint_mean())

