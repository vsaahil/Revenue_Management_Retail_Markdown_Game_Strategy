from selenium import webdriver
import pandas as pd
from re import sub
import timeit
import itertools

# Create a list of all possible combos

x = [60, 54, 48, 36]
combos = []

for i in itertools.product(x,repeat=14):
    if i[0] >= i[1] >= i[2] >= i[3] >= i[4] >= i[5] >= i[6]>= i[7] >= i[8]>= i[9] >= i[10] >= i[11] >= i[12] >= i[13]:
        combos.append(i)

check = pd.DataFrame(combos)

combos_list = []

for i in combos:
    combos_list.append(list(i))

# First step in each combo is always 60

for i in combos_list:
    i.insert(0,60)

# Assign an ID to each combo

for i in range(len(combos_list)):
    combos_list[i].insert(0,i)

combos_df = pd.DataFrame(combos_list)

combos_df = combos_df.rename(columns={0:"combo_number"})

# Write to CSV
# combos_df.to_csv("combos.csv",index=False)

# Scraping the site

browser=webdriver.Chrome(executable_path=r'C:\Users\Administrator\Documents\chromedriver.exe')
browser.get("http://www.randhawa.us/games/retailer/nyu.html")

# Assign the buttons that need to be pressed (use inspect element in the browser)

maintain = browser.find_element_by_id("maintainButton")
dc_10 = browser.find_element_by_id("tenButton")
dc_20 = browser.find_element_by_id("twentyButton")
dc_40 = browser.find_element_by_id("fortyButton")

# The script slows drastically after iterating through 20 combos (memory issue?), so this must be done in chunks
# Restart python after each chunk has run

chunk_1 = combos_list[660:680]

data = []

# Main scraping script. 50 reps of each combo.

start = timeit.default_timer()
for i in chunk_1:
    for t in range(50):
        for j in range(1, len(i)-1):
            if i[j+1] < i[j] and i[j+1] == 54:
                dc_10.click()
            elif i[j+1] < i[j] and i[j+1] == 48:
                dc_20.click()
            elif i[j+1] < i[j] and i[j+1] == 36:
                dc_40.click()
                break
            else:
                maintain.click()
        for tr in browser.find_elements_by_xpath('//table[@id="result-table"]//tr'):
            tds = tr.find_elements_by_tag_name('td')
            if tds:
                data.append([i[0]]+[t]+[int(td.text) for td in tds])
        revenue = int(sub(r'[^\d.]', '', browser.find_element_by_id("rev").text))
        perfect = int(sub(r'[^\d.]', '', browser.find_element_by_id("perfect").text))
        data.append([i[0], t, 16, revenue, perfect , 1 - revenue/perfect])
        browser.find_element_by_class_name("button").click()
stop = timeit.default_timer()
print('Time: ', stop - start)

# Transfer data to a dataframe and then save in CSV

placeholder = []
placeholder = placeholder + data

df = pd.DataFrame(placeholder, columns=["combo","replication", "week", "price", "sales", "remain_invent"])

df.to_csv("backup660to680.csv",index=False)


