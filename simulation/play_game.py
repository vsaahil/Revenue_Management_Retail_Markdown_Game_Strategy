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


thresholds = [[0.452363091, 0.31, 0.035],
             [0.549887472, 0.42, 0.07],
             [0.737434359, 0.62, 0.15]]

accumulated = [133.3, 266.6, 399.9, 533.2, 666.5, 799.8, 933.1, 1066.4,	1199.7, 1333, 1466.3, 1599.6, 1732.9, 1866.2, 2000]

for i in range(1000):
    difference = []
    percent_diff = []
    NEWVAR = 0
    trigger_10 = 0
    trigger_20 = 0
    trigger_40 = 0
    flag = 0
    for i in range(6):
        for tr in browser.find_elements_by_xpath('//table[@id="result-table"]//tr'):
            lds = tr.find_elements_by_tag_name('td')
        sales = int(lds[-2].text)
        NEWVAR += sales
        difference.append(accumulated[i]-NEWVAR)
        percent_diff.append(difference[i]/accumulated[i])
        if percent_diff[i] > thresholds[2][0]:
            dc_40.click()
            trigger_40 = 1
            break
        elif percent_diff[i] > thresholds[1][0]:
            if trigger_20 >= 1:
                maintain.click()
            else:
                dc_20.click()
                trigger_20 += 1
        elif percent_diff[i] > thresholds[0][0]:
            if trigger_20 >= 1 and trigger_10 >= 1:
                maintain.click()
            elif trigger_20 >= 1:
                maintain.click()
            elif flag == 1:
                dc_20.click()
                flag = 0
            elif trigger_10 >= 1:
                maintain.click()
            else:
                dc_10.click()
                trigger_10 += 1
                flag = 1
        else:
            maintain.click()
        flag = 0
    for i in range(5):
        if trigger_40 == 1:
            break
        for xr in browser.find_elements_by_xpath('//table[@id="result-table"]//tr'):
            tds = xr.find_elements_by_tag_name('td')
        sales = int(tds[-2].text)
        NEWVAR += sales
        difference.append(accumulated[6+i]-NEWVAR)
        percent_diff.append(difference[6+i]/accumulated[6+i])
        if percent_diff[6+i] > thresholds[2][1]:
            dc_40.click()
            trigger_40 = 1
            break
        elif percent_diff[6+i] > thresholds[1][1]:
            if trigger_20 >= 1:
                maintain.click()
            else:
                dc_20.click()
                trigger_20 += 1
        elif percent_diff[6+i] > thresholds[0][1]:
            if trigger_20 >= 1 and trigger_10 >= 1:
                maintain.click()
            elif trigger_20 >= 1:
                maintain.click()
            elif flag == 1:
                dc_20.click()
                flag = 0
            elif trigger_10 >= 1:
                maintain.click()
            else:
                dc_10.click()
                trigger_10 += 1
                flag = 1
        else:
            maintain.click()
        flag = 0
    for i in range(3):
        if trigger_40 == 1:
            break
        for gr in browser.find_elements_by_xpath('//table[@id="result-table"]//tr'):
            xds = gr.find_elements_by_tag_name('td')
        sales = int(xds[-2].text)
        NEWVAR += sales
        difference.append(accumulated[11+i]-NEWVAR)
        percent_diff.append(difference[11+i]/accumulated[11+i])
        if percent_diff[11+i] > thresholds[2][2]:
            dc_40.click()
        elif percent_diff[11+i] > thresholds[1][2]:
            if trigger_20 >= 1:
                maintain.click()
            else:
                dc_20.click()
                trigger_20 += 1
        elif percent_diff[11+i] > thresholds[0][2]:
            if trigger_20 >= 1 and trigger_10 >= 1:
                maintain.click()
            elif trigger_20 >= 1:
                maintain.click()
            elif flag == 1:
                dc_20.click()
                flag = 0
            elif trigger_10 >= 1:
                maintain.click()
            else:
                dc_10.click()
                trigger_10 += 1
                flag = 1
        else:
            maintain.click()
        flag = 0
    revenue = int(sub(r'[^\d.]', '', browser.find_element_by_id("rev").text))
    perfect = int(sub(r'[^\d.]', '', browser.find_element_by_id("perfect").text))
    scores.append(1 - revenue/perfect)
    restart.click()


print(np.mean(scores))
print(np.std(scores, ddof=1))
print(sms.DescrStatsW(scores).tconfint_mean())


