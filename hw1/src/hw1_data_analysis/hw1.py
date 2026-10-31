import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("/Users/ewanhenderson/cse583/CSE-583-HW/hw1/src/hw1_data_analysis/bicycle_data.csv")
data #the columns are date, total of the Fremont Bridge, and the east and west sidewalk totals
data = data.rename(columns={"Fremont Bridge Sidewalks, south of N 34th St Total":"Total(East+West)"}) #rename total column
data["hour"]=pd.to_datetime(data["Date"]).dt.hour #add hour of day column
data["year"]=pd.to_datetime(data["Date"]).dt.year #add year column
data_2016= data[data["year"]==2016] #data subset from 2016
missing_data = data_2016.isna().any(axis=1) #finding rows with missing data
num_missing = missing_data.sum()
num_missing #there is 1 row with missing data
print(data_2016.loc[missing_data]) #missing data is on 03/13/2016 02:00:00 AM
data_2016 = data_2016.dropna().copy() #deleting incomplete row
data_2016.plot.scatter(x="hour", y="Total(East+West)", alpha=0.5, title="Total Counts by the Hour") #make plot
plt.savefig("/Users/ewanhenderson/cse583/CSE-583-HW/hw1/counts_by_hour.png",
    dpi=300,
    bbox_inches="tight") #save as .png
data_2016[["hour", "Total(East+West)"]].groupby("hour").mean() #Busiest hour was 17 (5pm), followed by 8am
