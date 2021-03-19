combos.csv

This file contains a list of all the possible combinations of decisions from 0 to 679 (column combo_number).
Columns named 1-15 contain the value 60, 54, 48, or 36


######################

raw_data.csv

NOTE: this data has been extracted in the next two files

This is the raw data extract. 50 replications for each combo in combos.csv

column "combo" is the number of the combo
column "replication" is the replication number (0 to 49)
column "week" is the number of the week (1-16), with week 16 being the results
column "price" is the price for the week (60, 54, 48, 36), and in the case of results (week 16) this is the revenue
column "sales" is the sales for the week, and for the results (week 16) this is the perfect foresight strategy revenue
column "remain_invent" is the remaining inventoy for the week, and for the results (week 16) this is the difference in decimal form


######################

reps_only.csv

this is an extract from raw_data.csv that contains ONLY the reps without the results


######################

results_only.csv

this is an extract from raw_data.csv that contains ONLY the results (week 16 in the raw data)

columns have been renamed to match the data: "combo", "replication", "revenue", "perfect", "difference"


######################

results_less_than_5_percent.csv

this is an extract from raw_data.csv of the results with less than 0.05 (5%) difference between revenue and perfect foresight


######################

reps_less_than_5_percent.csv

this is an extract from raw_data.csv of the reps with less than 0.05 (5%) difference between revenue and perfect foresight