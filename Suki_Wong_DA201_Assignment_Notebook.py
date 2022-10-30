#!/usr/bin/env python
# coding: utf-8

# ### LSE Data Analytics Online Career Accelerator
# 
# # Course 2: Data Analytics using Python

# ## Assignment: Diagnostic Analysis using Python
# 
# You’ll be working with real-world data to address a problem faced by the National Health Service (NHS). The analysis will require you to utilise Python to explore the available data, create visualisations to identify trends, and extract meaningful insights to inform decision-making. 

# ### A note for students using this template
# This Jupyter Notebook is a template you can use to complete the Course 2 assignment: Diagnostic Analysis using Python. 
# 
# Keep in mind: 
# - You are **not required** to use this template to complete the assignment. 
# - If you decide to use this template for your assignment, make a copy of the notebook and save it using the assignment naming convention: **LastName_FirstName_DA201_Assignment_Notebook.ipynb**.
# - The workflow suggested in this template follows the Assignment Activities throughout the course.
# - Refer to the guidance on the Assignment Activity pages for specific details. 
# - The markup and comments in this template identify the key elements you need to complete before submitting the assignment.
# - Make this notebook your own by adding your process notes and rationale using markdown, add links, screenshots, or images to support your analysis, refine or clarify the comments, and change the workflow to suit your process.
# - All elements should be functional and visible in your Notebook. 
# - Be sure to push your notebook to GitHub after completing each Assignment Activity.
# 
#  > ***Markdown*** Remember to change cell types to `Markdown`. You can review [Markdown basics](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) to find out how to add formatted text, links, and images to your notebook.

# # 

# # Assignment activity 1

# ### Insert proof of your GitHub repository. This can be a link or screenshot showing your repo.

# In[1]:


# My GitHub repository.
print("https://github.com/suki-w/LSE_DA_NHS_analysis.git")


# # 

# # Assignment activity 2

# ### Prepare your workstation

# In[2]:


# Import the necessary libraries.
import pandas as pd
import numpy as np

# Optional - Ignore warnings.
import warnings
warnings.filterwarnings('ignore')


# In[3]:


# Load the 1st data file named "actual_duration.csv".
# Create dataframe ad and sense check the dataframe.
ad = pd.read_csv('actual_duration.csv')
print(ad.shape)
print(ad.dtypes)
print(ad.columns)
print(ad.isna().sum())
ad.head()


# In[4]:


# Determine the descriptive statistics and metadata of ad.
print(ad.describe())
print(ad.info())


# In[5]:


# Load the 2nd data file named "appointments_regional.csv".
# Create dataframe ar and sense check the dataframe.
ar = pd.read_csv('appointments_regional.csv')
print(ar.shape)
print(ar.dtypes)
print(ar.columns)
print(ar.isna().sum())
ar.head()


# In[6]:


# Determine the descriptive statistics and metadata of ar.
print(ar.describe())
print(ar.info())


# In[7]:


# Load the 3rd data file named "national_categories.csv".
# Create dataframe nc and sense check the dataframe.
nc = pd.read_csv('national_categories.csv')
print(nc.shape)
print(nc.dtypes)
print(nc.columns)
print(nc.isna().sum())
nc.head()


# In[8]:


# Determine the descriptive statistics and metadata of nc.
print(nc.describe())
print(nc.info())


# ### Explore the data set

# **Question 1:** How many locations are there in the data set?

# In[9]:


# Determine the number of locations.
# Group the location name column by unique values.
loc_list = nc['sub_icb_location_name'].value_counts()

# Count the no. of unique location name.
loc_count = loc_list.count()
print("Count of Locations:",loc_count)


# **Question 2:** What are the five locations with the highest number of records?
# 
# 

# In[10]:


# Determine the top five locations based on record count.
# Create a for loop to identify the top 5 locations from the location by count (loc_list) series.
for i in range(len(loc_list)):
    print("Top", i+1, "Location:", loc_list.index[i], ", Count=",loc_list[i])
    i=i+1
    if i==5:
        break


# **Question 3:** How many service settings, context types, national categories, and appointment statuses are there?

# In[11]:


# Determine the number of service settings.
# Group the sevice setting column by unique values.
service_list = nc['service_setting'].value_counts()

# Count the no. of unique service setting.
service_count = service_list.count()
print("Count of Service Setting:",service_count)


# In[12]:


# Determine the number of context types.
# Group the context type column by unique values.
context_list = nc['context_type'].value_counts()

# Count the no. of unique context type.
context_count = context_list.count()
print("Count of Context Type:",context_count)


# In[13]:


# Determine the number of national categories.
# Group the national category column by unique values.
category_list = nc['national_category'].value_counts()

# Count the no. of national category.
category_count = category_list.count()
print("Count of National Category:",category_count)


# In[14]:


# Determine the number of appointment status.
# Group the appointment status column by unique values.
app_status_list = ar['appointment_status'].value_counts()

# Count the no. of appointment status.
app_status_count = app_status_list.count()
print("Count of Appointment Status:",app_status_count)


# # 

# # Assignment activity 3

# ### Continue to explore the data and search for answers to more specific questions posed by the NHS.

# **Question 1:** Between what dates were appointments scheduled? 

# In[15]:


# View the first five rows of appointment_date for the ad DataFrame to determine the date format.
ad.head()


# In[16]:


# View the first five rows of appointment_date for the nc DataFrame to determine the date format.
nc.head()


# In[17]:


# Change the date format of ad['appointment_date'].
ad['appointment_date']= pd.to_datetime(ad['appointment_date'])

# View the DateFrame.
print(ad.dtypes)
ad.head()


# In[18]:


# Change the date format of nc['appointment_date'].
nc['appointment_date']= pd.to_datetime(nc['appointment_date'], format="%Y/%m/%d")

# View the DateFrame.
print(nc.dtypes)
nc.head()


# In[19]:


# Determine the minimum and maximum dates in the ad DataFrame.
print("First Date of Scheduled Appointments:",ad['appointment_date'].min().date())
print("Last Date of Scheduled Appointments:",ad['appointment_date'].max().date())


# In[20]:


# Determine the minimum and maximum dates in the nc DataFrame.
print("First Date of Scheduled Appointments:",nc['appointment_date'].min().date())
print("Last Date of Scheduled Appointments:",nc['appointment_date'].max().date())


# **Question 2:** Which service setting was the most popular for NHS North West London from 1 January to 1 June 2022?

# In[21]:


# Identify the code of location "NHS North West London ICB - W2U3Z".
nc.loc[nc['sub_icb_location_name'] == "NHS North West London ICB - W2U3Z", 'icb_ons_code'].iloc[0]

# Create a subset from the nc DataFrame with date and location code filter applied.
nc['appointment_date']= pd.to_datetime(nc['appointment_date'], format="%Y/%m/%d")
nc_subset=nc[(nc['icb_ons_code']=='E54000027')&((nc['appointment_date']>= "2022-01-01")& (nc['appointment_date'] <= "2022-06-01"))]

# For each of these service settings, determine the number of records available for the period and the location.
svc_set=nc_subset.groupby('service_setting')[['count_of_appointments']].sum().sort_values('count_of_appointments', ascending=False)

# View the most popular service setting output.
svc_set.iloc[0:1]


# **Question 3:** Which month had the highest number of appointments?

# In[22]:


# Number of appointments per month == sum of count_of_appointments by month.
# Use the groupby() and sort_values() functions.
app_month = nc.groupby([nc['appointment_date'].dt.year, nc['appointment_date'].dt.month])[['count_of_appointments']].sum().sort_values('count_of_appointments', ascending=False)
# View the month with highest no. of appointments output.
app_month.iloc[0:1]


# **Question 4:** What was the total number of records per month?

# In[23]:


# Get total number of records per month by aggregating count of appointments by month.
nc.groupby(nc['appointment_month'], )[['count_of_appointments']].sum()


# # 

# # Assignment activity 4

# ### Create visualisations and identify possible monthly and seasonal trends in the data.

# In[24]:


# Import the necessary libraries.
import seaborn as sns
import matplotlib.pyplot as plt

# Set figure size.
sns.set(rc={'figure.figsize':(15, 12)})

# Set the plot style as white.
sns.set_style('white')


# ### Objective 1
# Create three visualisations indicating the number of appointments per month for service settings, context types, and national categories.

# In[25]:


# Change the data type of the appointment month to string to allow for easier plotting.
nc['appointment_month']=nc['appointment_month'].astype(str)

# Verify the appointment month data type.
print(nc.dtypes)


# In[26]:


# Aggregate on monthly level and determine the sum of records per month.
nc_ss=nc.groupby([nc['appointment_month'], nc['service_setting']])[['count_of_appointments']].sum().reset_index()

# View output.
nc_ss.head()


# **Service settings:**

# In[27]:


# Plot the appointments over the available date range, and review the service settings for months.
# Create a lineplot.
ss_plot = sns.lineplot(x='appointment_month', y='count_of_appointments', data=nc_ss,hue ='service_setting',ci=None)
ss_plot.set(xlabel = "Appointment Month", ylabel = "Appointment Count", title="Monthly Appointment Count by Service Setting (Aug 2021 - Jun 2022)")
plt.legend(title="Service Setting", loc='best')
ylabels = ['{:,.1f}'.format(x) + 'M' for x in ss_plot.get_yticks()/1000000]
ss_plot.set_yticklabels(ylabels)


# **Context types:**

# In[28]:


# Create a separate data set that can be used in future weeks. 
nc_ct=nc.groupby([nc['appointment_month'], nc['context_type']])[['count_of_appointments']].sum().reset_index()

# View output.
nc_ct.head()


# In[29]:


# Plot the appointments over the available date range, and review the context types for months.
# Create a lineplot.
ct_plot = sns.lineplot(x='appointment_month', y='count_of_appointments', data=nc_ct,hue ='context_type',ci=None)
ct_plot.set(xlabel = "Appointment Month", ylabel = "Appointment Count", title="Monthly Appointment Count by Context Type (Aug 2021 - Jun 2022)")
plt.legend(title="Context Type", loc='best')
ylabels = ['{:,.1f}'.format(x) + 'M' for x in ct_plot.get_yticks()/1000000]
ct_plot.set_yticklabels(ylabels)


# **National categories:**

# In[30]:


# Create a separate data set that can be used in future weeks. 
nc_nc=nc.groupby([nc['appointment_month'], nc['national_category']])[['count_of_appointments']].sum().reset_index()

# View output.
nc_nc.head()


# In[31]:


# Plot the appointments over the available date range, and review the national categories for months.
# Create a lineplot.
nc_plot = sns.lineplot(x='appointment_month', y='count_of_appointments', data=nc_nc,hue ='national_category',ci=None)
nc_plot.set(xlabel = "Appointment Month", ylabel = "Appointment Count", title="Monthly Appointment Count by National Category (Aug 2021 - Jun 2022)")
plt.legend(title="National Category", loc='center right')
ylabels = ['{:,.1f}'.format(x) + 'M' for x in nc_plot.get_yticks()/1000000]
nc_plot.set_yticklabels(ylabels)


# ### Objective 2
# Create four visualisations indicating the number of appointments for service setting per season. The seasons are summer (August 2021), autumn (October 2021), winter (January 2022), and spring (April 2022).

# **Summer (August 2021):**

# In[32]:


# Create a separate data set that can be used in future weeks. 
nc_ss=nc.groupby([nc['appointment_month'], nc['appointment_date'], nc['service_setting']])[['count_of_appointments']].sum().reset_index()
nc_ss_day=nc_ss[(nc_ss['appointment_month']==('2021-08'))|(nc_ss['appointment_month']==('2021-10'))|(nc_ss['appointment_month']==('2022-01'))|(nc_ss['appointment_month']==('2022-04'))]

# View output.
nc_ss_day.head()


# In[33]:


# Look at August 2021 in more detail to allow a closer look.
# Create a lineplot.
summer_plot = sns.lineplot(x='appointment_date', y='count_of_appointments', data=nc_ss_day[nc_ss_day['appointment_month']==('2021-08')],hue ='service_setting',ci=None)
summer_plot.set(xlabel = "Appointment Date", ylabel = "Appointment Count", title="Appointment Count by Service Setting (Summer 2021)")
plt.legend(title="Service Setting", loc='best')
ylabels = ['{:,.1f}'.format(x) + 'M' for x in summer_plot.get_yticks()/1000000]
summer_plot.set_yticklabels(ylabels)


# **Autumn (October 2021):**

# In[34]:


# Look at October 2021 in more detail to allow a closer look.
# Create a lineplot.
autumn_plot = sns.lineplot(x='appointment_date', y='count_of_appointments', data=nc_ss_day[nc_ss_day['appointment_month']==('2021-08')],hue ='service_setting',ci=None)
autumn_plot.set(xlabel = "Appointment Date", ylabel = "Appointment Count", title="Appointment Count by Service Setting (Autumn 2021)")
plt.legend(title="Service Setting", loc='best')
ylabels = ['{:,.1f}'.format(x) + 'M' for x in autumn_plot.get_yticks()/1000000]
autumn_plot.set_yticklabels(ylabels)


# **Winter (January 2022):**

# In[35]:


# Look at January 2022 in more detail to allow a closer look.
# Create a lineplot.
winter_plot = sns.lineplot(x='appointment_date', y='count_of_appointments', data=nc_ss_day[nc_ss_day['appointment_month']==('2022-01')],hue ='service_setting',ci=None)
winter_plot.set(xlabel = "Appointment Date", ylabel = "Appointment Count", title="Appointment Count by Service Setting (Winter 2022)")
plt.legend(title="Service Setting", loc='best')
ylabels = ['{:,.1f}'.format(x) + 'M' for x in winter_plot.get_yticks()/1000000]
winter_plot.set_yticklabels(ylabels)


# **Spring (April 2022):**

# In[36]:


# Look at April 2022 in more detail to allow a closer look.
# Create a lineplot.
spring_plot = sns.lineplot(x='appointment_date', y='count_of_appointments', data=nc_ss_day[nc_ss_day['appointment_month']==('2022-04')],hue ='service_setting',ci=None)
spring_plot.set(xlabel = "Appointment Date", ylabel = "Appointment Count", title="Appointment Count by Service Setting (Spring 2022)")
plt.legend(title="Service Setting", loc='best')
ylabels = ['{:,.1f}'.format(x) + 'M' for x in spring_plot.get_yticks()/1000000]
spring_plot.set_yticklabels(ylabels)


# # 

# # Assignment activity 5

# ### Analyse tweets from Twitter with hashtags related to healthcare in the UK.

# In[37]:


# Libraries and settings needed for analysis
import pandas as pd
import seaborn as sns

# Set figure size.
sns.set(rc={'figure.figsize':(15, 12)})

# Set the plot style as white.
sns.set_style('white')

# Maximum column width to display
pd.options.display.max_colwidth = 200


# In[38]:


# Load the data set.
tweets=pd.read_csv('tweets.csv')

# Sense check the DataFrame.
print(tweets.shape)
print(tweets.dtypes)
print(tweets.columns)
print(tweets.isna().sum())

# View the DataFrame.
tweets.head()


# In[39]:


# Explore the metadata.
print(tweets.describe())
print(tweets.info())


# In[40]:


# Explore the data set.
print(tweets['tweet_retweet_count'].value_counts())
print(tweets['tweet_favorite_count'].value_counts())


# In[41]:


# Would it be useful to only look at retweeted and favourite tweet messages?
# Explain your answer.

print("It is not very useful to further dive into the retweet and favourite tweet count columns because one tweet may contain no or more than one hastag, it does not necessary have direct or unique correlation to trending hashtags.")


# In[42]:


# Create a new DataFrame containing only the text.
tweets_text=tweets.select_dtypes(include='object')

# View the DataFrame.
tweets_text.head()


# In[43]:


# Create an empty list "tags".
tags=[]

# Loop through the messages, and create a list of values containing the # symbol.
for y in [x.split(' ') for x in tweets['tweet_full_text'].values]:
    for z in y:
        if '#' in z:
            # Change to lowercase.
            tags.append(z.lower())

# View the list output.
tags


# In[44]:


# Create a series "tags" to count the values in the list.
tags_pd=pd.Series(tags)
tags_count=tags_pd.value_counts()

# Display the top 30 trending hashtags.
tags_count[0:30]


# In[45]:


# Convert the series to DataFrame 'data' in preparation for visualisation.
data=pd.DataFrame(tags_count).reset_index()

# Rename the columns.
data.columns = ['word', 'count']


# In[46]:


# Sense check the data and ensure the count data type is an integer.
print(data.shape)
print(data.dtypes)
print(data.columns)
print(data.isna().sum())
data.head()


# In[47]:


# Display records where the count is larger than 10.
data_plot = data[data['count']>10]
data_plot


# In[48]:


# Create a Seaborn barplot indicating records with a count >10 records.
ht_barplot = sns.barplot(x='count', y='word', estimator=sum, data=data_plot)
ht_barplot.set(xlabel = "Hashtag Use Count", ylabel = "Hashtag", title="Top Trending Hashtags on Twitter")


# In[49]:


# Exclude the overrepresented hashtag #healthcare from the top row of the 'data_plot' Dataframe.
# Create a Seaborn barplot displaying the remaining most frequently used hastags.
ht_barplot = sns.barplot(x='count', y='word', estimator=sum, data=data_plot[1:])
ht_barplot.set(xlabel = "Hashtag Use Count", ylabel = "Hashtag", title="Top Trending Hashtags on Twitter")


# # 

# # Assignment activity 6

# ### Investigate the main cencerns posed by the NHS. 

# In[50]:


# Prepare your workstation.
# Load the appointments_regional.csv file.
ar = pd.read_csv('appointments_regional.csv')
# Sense check the DataFrame.
print(ar.shape)
print(ar.dtypes)
print(ar.columns)
# View the DataFrame.
ar.head()


# In[51]:


# Print the min and max dates.
print("Earliest Appointment:",ar['appointment_month'].min())
print("Latest Appointment:",ar['appointment_month'].max())


# In[52]:


# Filter the data set to only look at data from 2021-08 onwards.
ar['appointment_month']=pd.to_datetime(ar['appointment_month'], format="%Y/%m").dt.to_period('M')
ar_subset=ar[(ar['appointment_month']>= "2021-08")]

# Sense check the DataFrame.
print(ar_subset.shape)
print(ar_subset.dtypes)
print(ar_subset.columns)

# View the DataFrame.
ar_subset.head()


# **Question 1:** Should the NHS start looking at increasing staff levels? 

# In[53]:


# Create an aggregated data set to review the different features.
ar_agg=ar_subset.groupby([ar_subset['appointment_month'], ar_subset['appointment_status'], ar_subset['hcp_type'], ar_subset['appointment_mode'], ar_subset['time_between_book_and_appointment']])[['count_of_appointments']].sum().reset_index()

# Sense check the DataFrame.
print(ar_agg.shape)
print(ar_agg.dtypes)
print(ar_agg.columns)

# View the DataFrame.
ar_agg.head()


# In[54]:


# Determine the total number of appointments per month.
ar_df=ar_agg.groupby([ar_agg['appointment_month']])[['count_of_appointments']].sum().reset_index()

# Add a new column to indicate the average utilisation of services.
# Monthly aggregate / 30 to get to a daily value.
ar_df['daily_utilization']=(ar_df['count_of_appointments']/30).round()
ar_df['%_utilization']=(ar_df['daily_utilization']/1200000*100).round(decimals = 1)

# Sense check the DataFrame.
print(ar_df.shape)
print(ar_df.dtypes)
print(ar_df.columns)

# View the DataFrame.
ar_df.head()


# In[55]:


# Plot sum of count of monthly visits.
# Convert the appointment_month column to string data type for ease of visualisation.
ar_df['appointment_month']=ar_df['appointment_month'].astype(str)

# Create a lineplot with Seaborn.
monthly_plot = sns.lineplot(x='appointment_month', y='count_of_appointments', data=ar_df,ci=None)
monthly_plot.set(xlabel = "Appointment Month", ylabel = "Appointment Count", title="Visit Count by Month (Aug 2021 - Jun 2022)")
ylabels = ['{:,.1f}'.format(x) + 'M' for x in monthly_plot.get_yticks()/1000000]
monthly_plot.set_yticklabels(ylabels)


# In[56]:


# Plot monthly capacity utilisation.
# Convert the %_utilization column to numerical data type for ease of visualisation.
ar_df['%_utilization']=ar_df['%_utilization'].astype('int64')

# Create a lineplot.
utilization_plot = sns.lineplot(x='appointment_month', y='%_utilization', data=ar_df,ci=None)
utilization_plot.set(xlabel = "Appointment Month", ylabel = "Utilization %", title="Service Utilization % by Month (Aug 2021 - Jun 2022)")
utilization_plot.set(ylim = (0,100))
ylabels = ['{:,.1f}'.format(x) + '%' for x in utilization_plot.get_yticks()]
utilization_plot.set_yticklabels(ylabels)


# **Question 2:** How do the healthcare professional types differ over time?

# In[57]:


# Create an aggregated data subset to review appointment count by healthcare professional types.
ar_hcp=ar_agg.groupby([ar_agg['appointment_month'],ar_agg['hcp_type']])[['count_of_appointments']].sum().reset_index()

# Convert the appointment_month column to string data type for ease of visualisation.
ar_hcp['appointment_month']=ar_hcp['appointment_month'].astype(str)

# Create a lineplot.
hcp_plot = sns.lineplot(x='appointment_month', y='count_of_appointments', data=ar_hcp, hue='hcp_type', ci=None)
hcp_plot.set(xlabel = "Appointment Month", ylabel = "Appointment Count", title="Appointment Count by Healthcare Professional Type by Month (Aug 2021 - Jun 2022)")
plt.legend(title="Healthcare Prof. Type", loc='best')
ylabels = ['{:,.1f}'.format(x) + 'M' for x in hcp_plot.get_yticks()/1000000]
hcp_plot.set_yticklabels(ylabels)


# **Question 3:** Are there significant changes in whether or not visits are attended?

# In[58]:


# Create an aggregated data subset to review appointment count by appointment status.
ar_status=ar_agg.groupby([ar_agg['appointment_month'],ar_agg['appointment_status']])[['count_of_appointments']].sum().reset_index()

# Convert the appointment_month column to string data type for ease of visualisation.
ar_status['appointment_month']=ar_status['appointment_month'].astype(str)

# Create a lineplot.
status_plot = sns.lineplot(x='appointment_month', y='count_of_appointments', data=ar_status, hue='appointment_status', ci=None)
status_plot.set(xlabel = "Appointment Month", ylabel = "Appointment Count", title="Appointment Count by Appointment Status by Month (Aug 2021 - Jun 2022)")
plt.legend(title="Appointment Status", loc='best')
ylabels = ['{:,.1f}'.format(x) + 'M' for x in status_plot.get_yticks()/1000000]
status_plot.set_yticklabels(ylabels)


# **Question 4:** Are there changes in terms of appointment type and the busiest months?

# In[59]:


# Create an aggregated data subset to review appointment count by appointment mode.
ar_mode=ar_agg.groupby([ar_agg['appointment_month'],ar_agg['appointment_mode']])[['count_of_appointments']].sum().reset_index()

# Convert the appointment_month column to string data type for ease of visualisation.
ar_mode['appointment_month']=ar_mode['appointment_month'].astype(str)

# Create a lineplot.
mode_plot = sns.lineplot(x='appointment_month', y='count_of_appointments', data=ar_mode, hue='appointment_mode', ci=None)
mode_plot.set(xlabel = "Appointment Month", ylabel = "Appointment Count", title="Appointment Count by Appointment Mode by Month (Aug 2021 - Jun 2022)")
plt.legend(title="Appointment Mode", loc='best')
ylabels = ['{:,.1f}'.format(x) + 'M' for x in mode_plot.get_yticks()/1000000]
mode_plot.set_yticklabels(ylabels)


# **Question 5:** Are there any trends in time between booking an appointment?

# In[60]:


# Create an aggregated data subset to review appointment count by booking to appointment duration.
ar_duration=ar_agg.groupby([ar_agg['appointment_month'],ar_agg['time_between_book_and_appointment']])[['count_of_appointments']].sum().reset_index()

# Convert the appointment_month column to string data type for ease of visualisation.
ar_duration['appointment_month']=ar_duration['appointment_month'].astype(str)

# Create a lineplot.
duration_plot = sns.lineplot(x='appointment_month', y='count_of_appointments', data=ar_duration, hue='time_between_book_and_appointment', ci=None)
duration_plot.set(xlabel = "Appointment Month", ylabel = "Appointment Count", title="Appointment Count by Booking to Appointment Duration by Month (Aug 2021 - Jun 2022)")
plt.legend(title="Booking to Appointment Duration", loc='best')
ylabels = ['{:,.1f}'.format(x) + 'M' for x in duration_plot.get_yticks()/1000000]
duration_plot.set_yticklabels(ylabels)


# **Question 6:** How do the spread of service settings compare?

# In[61]:


# Let's go back to the national category DataFrame you created in an earlier assignment activity.
nc.head()


# In[62]:


# Create a new DataFrame consisting of the month of appointment and the number of appointments.
ss = nc.groupby([nc['appointment_month'],nc['service_setting']])[['count_of_appointments']].sum().reset_index()

# View the DataFrame.
ss.head()


# In[67]:


# Create a boxplot to investigate spread of service settings.
ss_plot = sns.boxplot(data=ss, x='service_setting', y='count_of_appointments')
ss_plot.set(xlabel = "Service Setting", ylabel = "Appointment Count", title="Appointment Count by Service Setting")
ylabels = ['{:,.1f}'.format(x) + 'M' for x in ss_plot.get_yticks()/1000000]
ss_plot.set_yticklabels(ylabels)


# In[68]:


# Create a data subset with GP visits excluded.
non_gp=nc[nc['service_setting']!='General Practice']
ss_nongp = non_gp.groupby([non_gp['appointment_month'],non_gp['service_setting']])[['count_of_appointments']].sum().reset_index()

# Create a boxplot to investigate the service settings without GP.
ss_nongp_plot = sns.boxplot(data=ss_nongp, x='service_setting', y='count_of_appointments')
ss_nongp_plot.set(xlabel = "Service Setting", ylabel = "Appointment Count", title="Appointment Count by Service Setting")
ylabels = ['{:,.1f}'.format(x) + 'M' for x in ss_nongp_plot.get_yticks()/1000000]
ss_nongp_plot.set_yticklabels(ylabels)


# # 
