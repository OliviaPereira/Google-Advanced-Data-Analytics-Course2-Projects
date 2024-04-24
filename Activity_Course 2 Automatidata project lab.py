#!/usr/bin/env python
# coding: utf-8

# # **Automatidata project**


# **The purpose** of this project is to investigate and understand the data provided.
#   
# **The goal** is to use a dataframe contructed within Python, perform a cursory inspection of the provided dataset, and inform team members of your findings. 
# <br/>  
# *This activity has three parts:*
# 
# **Part 1:** Understand the situation 
# * Prepare to understand and organize the provided taxi cab dataset and information.
# 
# **Part 2:** Understand the data
# 
# * Create a pandas dataframe for data learning, future exploratory data analysis (EDA), and statistical activities.
# 
# * Compile summary information about the data to inform next steps.
# 
# **Part 3:** Understand the variables
# 
# * Use insights from your examination of the summary data to guide deeper investigation into specific variables.


# # **Identify data types and relevant variables using Python**

# # **PACE stages**
# 

# Throughout these project notebooks, you'll see references to the problem-solving framework PACE. The following notebook components are labeled with the respective PACE stage: Plan, Analyze, Construct, and Execute.


# 
# ## PACE: **Plan**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response:

# ### **Task 1. Understand the situation**
# 
# *   How can you best prepare to understand and organize the provided taxi cab information? 

# ==>Familiarize myself with the taxi cab data fields and assess the impact of each one.
# Import the data into Python, inspect it, and provide DeShawn with initial observations.
# Then delving deeper into the data, checking for any anomalies.


# ## PACE: **Analyze**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Analyze stage.

# ### **Task 2a. Build dataframe**
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# Create a pandas dataframe for data learning, and future exploratory data analysis (EDA) and statistical activities.
# 
# **Code the following,**
# 
# *   import pandas as `pd`. pandas is used for buidling dataframes.
import pandas as pd
# 
# *   import numpy as `np`. numpy is imported with pandas
import numpy as np


df = pd.read_csv('Datasets\NYC taxi data.csv')


# Load dataset into dataframe
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')
print("done")


# ### **Task 2b. Understand the data - Inspect the data**
# 
# View and inspect summary information about the dataframe by coding the following:
# 
df.head(10)


df.info()


df.describe()
# 
# Consider the following two questions:
# 
# **Question 1:** When reviewing the `df.info()` output, what do you notice about the different variables? Are there any null values? Are all of the variables numeric? Does anything else stand out?
# Two dtypes are datetime.
#  No null values.
# **Question 2:** When reviewing the `df.describe()` output, what do you notice about the distributions of each variable? Are there any questionable values?
#The maximum fare amount is $1000 than the 20-70 percent range of values.
# Also, it's questionable how there are negative values for fare amount.




# ### **Task 2c. Understand the data - Investigate the variables**
# 
# Sort and interpret the data table for two variables:`trip_distance` and `total_amount`.
# 
# **Answer the following three questions:**
# 
# **Question 1:** Sort your first variable (`trip_distance`) from maximum to minimum value, do the values seem normal?
# 
# **Question 2:** Sort by your second variable (`total_amount`), are any values unusual?
# 
# **Question 3:** Are the resulting rows similar for both sorts? Why or why not?

# ==> ENTER YOUR RESPONSES TO QUESTION 1-3 HERE

#Question1: Th values match the previous EDA.
#Question2: Yes, the first and second values are much higher than the rest.
#Question3: The resulting rows show the expensive rides aren't always the longer ones.

# Sort the data by trip distance from maximum to minimum value
#==> ENTER YOUR CODE HERE
df_sort = df.sort_values(by=['trip_distance'], ascending=False)
df_sort.head()


# Sort the data by total amount and print the top 20 values
#==> ENTER YOUR CODE HERE
total_amount_sorted = df.sort_values(
    ['total_amount'], ascending=False)['total_amount']
total_amount_sorted.head(20)


# Sort the data by total amount and print the bottom 20 values
#==> ENTER YOUR CODE HERE
total_amount_sorted.tail(20)

# How many of each payment type are represented in the data?

# According to the data dictionary, the payment method was encoded as follows:
# 
# 1 = Credit card  
# 2 = Cash  
# 3 = No charge  
# 4 = Dispute  
# 5 = Unknown  
# 6 = Voided trip

#==> ENTER YOUR CODE HERE
df['payment_type'].value_counts()

# What is the average tip for trips paid for with credit card
#==> ENTER YOUR CODE HERE
avg_cc_tip = df[df['payment_type'] ==1]['tip_amount'].mean()
print('avg. cc tip:', avg_cc_tip)


# What is the average tip for trips paid for with cash?
#==> ENTER YOUR CODE HERE
avg_cash_tip = [df[df'payment_type']==2]['tip_amount'].mean()
print('avg. cash tip:', avg_cash_tip)


# How many times is each vendor ID represented in the data?
#==> ENTER YOUR CODE HERE
df['VendorID'].value_counts()


# What is the mean total amount for each vendor?
#==> ENTER YOUR CODE HERE
df.groupby(['VendorID']).mean(numeric_only=True)[['total_amount']]

# Filter the data for credit card payments only
#==> ENTER YOUR CODE HERE
credit_card = df[df['payment_type']==1]

# Filter the credit-card-only data for passenger count only
#==> ENTER YOUR CODE HERE
credit_card['passenger_count'].value_counts()

# Calculate the average tip amount for each passenger count (credit card payments only)
credit_card.groupby(['passenger_count']).mean(numeric_only=True)[['tip_amount']]




# ## PACE: **Construct**
# 
# **Note**: The Construct stage does not apply to this workflow. The PACE framework can be adapted to fit the specific requirements of any project. 
# 
# 

# ## PACE: **Execute**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response.
# 

# ### **Given your efforts, what can you summarize for DeShawn and the data team?**
# 
# *Note for Learners: Your notebook should contain data that can address Luana's requests. Which two variables are most helpful for building a predictive model for the client: NYC TLC?*

# ==> ENTER YOUR RESPONSE HERE 
# The two variables more suited to help build a predictive model for taxi ride fares are 'total_amount' and 'trip_distance'.
# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
