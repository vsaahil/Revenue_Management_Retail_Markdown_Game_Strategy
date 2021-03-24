from selenium import webdriver
from re import sub
import numpy as np
import statsmodels.stats.api as sms
import pulp as plp
from pulp import *

# opens the browser for scraping
browser=webdriver.Chrome(executable_path=r'C:\Users\Administrator\Documents\chromedriver.exe')
browser.get("http://www.randhawa.us/games/retailer/nyu.html")

# finds the buttons to click
maintain = browser.find_element_by_id("maintainButton")
dc_10 = browser.find_element_by_id("tenButton")
dc_20 = browser.find_element_by_id("twentyButton")
dc_40 = browser.find_element_by_id("fortyButton")
restart = browser.find_element_by_class_name("button")

scores = []
prices = [60, 54, 48, 36]

# function to return LP optimized combo, maximizing revenue

def get_weeks(sales):
    prob = LpProblem("LP")
    prob.sense = LpMaximize
    d_at_54 = sales*1.31
    d_at_48 = sales*1.73
    d_at_36 = sales*2.81
    coeff = [sales,d_at_54,d_at_48,d_at_36]
    units_available = 2000 - sales
    variables = ["weeks_60","weeks_54","weeks_48","weeks_36"]
    x_vars = {i:
             LpVariable(name = variables[i], lowBound = 0, upBound=14, cat=LpInteger)
             for i in range(len(variables))}
    # total weeks need to <= 14. need to set to == for this
    prob += lpSum(x_vars) == 14
    # limited inventory constraint
    prob += lpSum(x_vars[i] * coeff[i] for i in range(len(variables))) <= units_available
    # objective and solve
    prob.setObjective(lpSum(x_vars[i] * coeff[i] * prices[i] for i in range(len(variables))))
    prob.solve()
    values = []
    for v in prob.variables():
        values.append(v.varValue)
    return values[:4]

# test = get_weeks(56)

# order is 36, 48, 56, 60


# Simulation

for i in range(1000):
    for tr in browser.find_elements_by_xpath('//table[@id="result-table"]//tr'):
        tds = tr.find_elements_by_tag_name('td')
    sales = int(tds[-2].text)
    how_fun = get_weeks(sales)
    for j in range(int(how_fun[-1])):
        maintain.click()
    if how_fun[-2] > 0:
        dc_10.click()
        for x in range(int(how_fun[-2]-1)):
            maintain.click()
    if how_fun[-3] > 0:
        dc_20.click()
        for p in range(int(how_fun[-3]-1)):
            maintain.click()
    if how_fun[-4] > 0:
        dc_40.click()
    revenue = int(sub(r'[^\d.]', '', browser.find_element_by_id("rev").text))
    perfect = int(sub(r'[^\d.]', '', browser.find_element_by_id("perfect").text))
    scores.append(1 - revenue/perfect)
    restart.click()

# print results

print(np.mean(scores))
print(np.min(scores))
print(np.max(scores))
print(np.std(scores, ddof=1))
print(sms.DescrStatsW(scores).tconfint_mean())

