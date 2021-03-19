import pandas as pd

df = pd.read_csv("raw_data.csv")

# Week 16 in each repetition is the summary of results
# Let's make two files out of this

reps = df[df["week"] != 16]

results = df[df["week"] == 16]

results = results.drop(columns="week")

# Rename the columns in the results

map = {"price":"revenue","sales":"perfect","remain_invent":"difference"}

results = results.rename(columns=map)

# Write to csv

reps.to_csv("reps_only.csv",index=False)

results.to_csv("results_only.csv",index=False)


# Let's find the trials where the difference is less than 0.05

good_results = results[results["difference"] < 0.05]

good_results.to_csv("results_less_than_5_percent.csv",index=False)

# And finally let's extract the full data for each of these repetitions

reps = reps.reset_index(drop=True)

good_results = good_results.reset_index(drop=True)

good_reps = pd.DataFrame(columns=["combo","replication","week","price","sales","remain_invent"])

for i in range(len(good_results)):
    temp = reps.loc[(reps["combo"] == good_results["combo"][i]) & (reps["replication"] == good_results["replication"][i])]
    frames = [good_reps,temp]
    good_reps = pd.concat(frames)

good_reps.to_csv("reps_less_than_5_percent.csv",index=False)


