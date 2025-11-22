# Space Missions Analysis Project
# Author: Tanjeel Mujawar
# Description:
#   This script loads the Space Missions dataset,
#   performs data cleaning, preprocessing, EDA,
#   and generates visual insights for better understanding.


# Space Missions Analysis Project
# Author: Tanjeel Mujawar
# Description:
#   This script cleans the dataset, performs exploratory data analysis,
#   creates visualizations, and generates insights about global space missions.
#
# Project Objectives:
#   1. Analyze how rocket launches and mission success rates have changed over time.
#   2. Identify which countries have the most successful space missions.
#   3. Find the rockets used most frequently and check their current status.
#   4. Explore patterns in global launch locations.


# Importing the essential Python libraries for EDA and visualization
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# First Glance at Dataset👀.
df = pd.read_csv(r"D:\Maven_dataset\Space+Missions\space_missions.csv", encoding='latin1')

df
df.shape
df.head()
df.tail()
df.info()
df.describe(include='all')
df.isna().sum()


# Checking Percentage of NaN value.
print(f'Percentage of NaN Value in Price Column = {df['Price'].isna().sum() / len(df) * 100}')
df = df.drop(columns=['Price'])




# This converts the Date column into proper datetime format while treating the first value as the day;
# any invalid dates are safely turned into NaT instead of causing errors.
df['Date'] = pd.to_datetime(df['Date'], dayfirst = True, errors='coerce')


# Combining the Date and Time columns into one clean datetime column so it's easier to analyze launch timings.
df['LaunchDatetime'] = pd.to_datetime(df['Date'].astype(str) + ' ' + df['Time'].astype(str), errors='coerce')



# Cleaning the text values by removing extra spaces and converting the columns into categories.
# This helps reduce memory usage and makes the data easier to analyze.
df['MissionStatus'] = df['MissionStatus'].str.strip().astype('category')
df['RocketStatus'] = df['RocketStatus'].str.strip().astype('category')




# I'm cleaning the text in MissionStatus and RocketStatus by removing extra spaces,
# and converting them into categories to make the data cleaner and more memory-efficient.
df['Year'] = df['LaunchDatetime'].dt.year
df['Month'] = df['LaunchDatetime'].dt.month




# Here I'm pulling out just the country from the Location column so it's easier to analyze later
df['Country'] = df['Location'].apply(lambda x: x.split(',')[-1].strip())



# I'm removing unwanted spaces from the Company, Location, Rocket, MissionStatus and RocketStatus columns.
# This helps avoid issues where the same value looks different because of extra spaces.
df['Company'] = df['Company'].str.strip()
df['Location'] = df['Location'].str.strip()
df['Rocket'] = df['Rocket'].str.strip()
df['MissionStatus'] = df['MissionStatus'].str.strip()
df['RocketStatus'] = df['RocketStatus'].str.strip()



# I'm checking how many rockets are currently active vs retired.
# This helps me understand the overall condition of the fleet before doing deeper analysis.
df['RocketStatus'].value_counts()



# Checking how often each mission outcome appears to understand the overall success and failure distribution in the dataset.
df['MissionStatus'].value_counts()



# Checking which countries appear most often in the dataset so we can see where most launches have happened.
df['Country'].value_counts().sort_values(ascending = False).head()



# Checking which Company appear most often in the dataset so we can see where most launches have happened.
df['Company'].value_counts().sort_values(ascending = False).head()




# Checking what percentage of all missions fall into each mission status category.
df['MissionStatus'].value_counts() / len(df) * 100




# I’m plotting a pie chart to quickly see how each mission status contributes to the overall dataset.
# The autopct option helps me display the percentage values directly on the chart for easier interpretation.
(df['MissionStatus'].value_counts() / len(df) * 100).plot(kind="pie",autopct='%1.f%%')
plt.title("Percentage of each Category")
plt.ylabel("")
plt.show()




# 1) How have rocket launches trended across time? Has mission success rate increased?
# Plotting how the number of space missions changed year by year.
# This helps me spot trends—like whether launches are increasing or dropping over time.
plt.figure(figsize = (10,6))
df.groupby('Year').size().plot(kind='line',marker='d')
plt.title('Number of Space Mission Per Year')
plt.xlabel("Year")
plt.ylabel("Total Mission")
plt.show()





# 2) Which countries have had the most successful space missions? Has it always been that way?

# Adding a new column 'SuccessFlag' to easily identify which missions succeeded
df['SuccessFlag'] = df['MissionStatus'] == 'Success'
df['SuccessFlag'].value_counts() / len(df) *100



# Calculate the total number of successful missions for each country
mission_success_rate = df.groupby('Country')['SuccessFlag'].sum()



# Let's check which countries have done the most successful space missions.
# We'll plot the top 6 to quickly see who's leading.
mission_success_rate.sort_values(ascending = False).head(6).plot(kind='bar',colormap='plasma')
plt.title("Which Country has most successfull Space Mission.")
plt.xlabel("Country")
plt.ylabel("Missions")
plt.savefig("most_success_missions_country.jpeg", dpi=600)
plt.show()



# Let's visualize what share of total successful missions each of the top 5 countries has.
# Using a pie chart to easily see which countries contributed most to overall success.
(mission_success_rate.sort_values(ascending=False) / len(df) * 100).head(5).plot(kind='pie',autopct='%1.F%%')
plt.title("Mission Success Rate of Top 5 Countries")
plt.ylabel("")
plt.savefig("most_success_missions_country_rate.jpeg", dpi=600)
plt.show()




# 3) Which rocket has been used for the most space missions? Is it still active?
# I want to easily see which rockets are still active,
# so I'm creating a True/False column called 'Still_active_rockets'.
df['Still_active_rockets'] = (df['RocketStatus']=='Active')



# I want to see how many launches each rocket has had,
# so I'm counting the entries for each rocket using the 'Still_active_rockets' column.
active_rockets = df.groupby('Rocket')['Still_active_rockets'].count()
active_rockets.sort_values(ascending=False).head(5)




# Let's see which rockets were launched the most.
# Plotting the top 10 rockets by launch count using a bar chart with the 'viridis' colormap.
# Saving the figure with high resolution (600 dpi) for future reference.
df['Rocket'].value_counts().sort_values(ascending=False).head(10).plot(kind='bar'
                                                                       ,colormap='viridis')
plt.title("How Many time each rocket has launched.")
plt.xlabel("Rocket Name")
plt.ylabel("Count")
plt.savefig("rocket_launch_frequency", dpi=600)
plt.show()





# I want to see not just how many times each rocket was launched,
# but also their current status (Active or Retired).
# So, I'm grouping by rocket and status, counting launches, and plotting the top 10 rockets.
# Using hue to show the rocket status.
rocket_usage = df.groupby(["Rocket", "RocketStatus"]).size().reset_index(name='Count')

plt.figure(figsize=(14,6))
sns.barplot(data=rocket_usage.sort_values("Count", ascending=False).head(10),
            x="Rocket", y="Count", hue="RocketStatus")
plt.title("Top Rockets — Usage & Status")
plt.xticks(rotation=45, ha="right")
plt.savefig("rocket_launch_frequency_1", dpi=600)
plt.show()






# 4)  Are there any patterns you can notice with the launch locations?

# I want to see which launch locations were used the most.
# Counting the number of launches per location and showing the top 10.
df['Location'].value_counts().sort_values(ascending=False).head(10)

(df['Location'].value_counts() / len(df) * 100).head()


# Let's visualize the top 10 launch locations by the number of launches.
# Using a bar chart with the 'coolwarm' colormap to make it easy to compare.
# This helps us quickly see which sites were used most frequently.
plt.figure(figsize = (12,6))
df['Location'].value_counts().sort_values(ascending=False).head(10).plot(kind="bar",colormap='coolwarm')
plt.title("Top 10 Launch Location")
plt.ylabel("Launches")
plt.xlabel("Location")
# plt.xticks(rotation=45, ha="right")
plt.savefig("location_launch_frequency", dpi=600)
plt.show()







# Let's visualize the success rate of missions from the top 5 launch locations using a pie chart.
# Using 'explode' to highlight each slice, shadow for better depth, and start angle for readability.
# Showing the percentage of successful missions from each site.
launch_location_success_rate = df.groupby("Location")["SuccessFlag"].count()
launch_location_success_rate.sort_values(ascending=False).head().plot(kind='pie',autopct='%1.f%%',
                                                                      startangle=90,
                                                                      shadow=True,
                                                                      explode=explode)
plt.title("Mission Success Rate of Top 5 Launch Location")
plt.ylabel("")
plt.savefig("location_launch_frequency_rate", dpi=600)
plt.show()



# I want to see how rocket launches are distributed throughout the year.
# Plotting the number of launches per month as a bar chart using a rainbow colormap.
# This helps us understand if certain months had more launches than others.

plt.figure(figsize=(12,6))
df['Month'].value_counts().sort_values().plot(kind='bar',colormap='rainbow')
plt.title("In Each Month How many Rockets are Launched")
plt.xlabel("Month (in Numeric)")
plt.ylabel("Count")
plt.savefig("rocket_launch_distribution_year",dpi=600)
plt.show()



# Plotting the top 20 companies with the most successful missions.
# Using a colorful bar chart, adding labels and title, and saving a high-res image.
company_success_rate = df.groupby('Company')['SuccessFlag'].count()
company_success_rate.sort_values(ascending=False).head(20).plot(kind='bar',colormap='summer')
plt.title('Mission Success Count by Company')
plt.xlabel('Company Name')
plt.ylabel('Number of Successful Missions')
sns.despine()
plt.savefig("company_success_rate.jpeg",dpi=600)
plt.show()
