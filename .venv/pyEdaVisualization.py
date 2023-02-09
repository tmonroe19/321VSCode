#Python, you should use matplotlib or seaborn with the standard aliases. 
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import statistics
import numpy as np

approvals = pd.read_excel(r'C:\Users\Tucker Monroe\Downloads\credit_card.xlsx', engine='openpyxl')

# 1 Find out data types for each feature in the data set

dataTypesAllColumns = approvals.dtypes
print(dataTypesAllColumns)
print(approvals.head())
# ---------------------------------------------------------------

# 2 Provide summary descriptive statistics for each feature. 

statsAllColumns = approvals.describe()
print(statsAllColumns)
# ---------------------------------------------------------------

# 3a Plot the histogram of debt

plt.hist(approvals['Debt'], color='purple')
plt.title('Histogram plot Debt')
plt.xlabel('Debt')
plt.ylabel('Count')
plt.show()
# ---------------------------------------------------------------

# 3b Plot the density of debt

approvals.Debt.plot.density(color='green')
plt.title('Density plot Debt')
plt.xlabel('Debt')
plt.show()
# ---------------------------------------------------------------

# 4a Plot the histogram of income, adding a vertical line to denote the mean.

plt.hist(approvals['Income'], color='green')
incomeMean = statistics.mean(approvals['Income'])
plt.axvline(incomeMean, color='black', label = 'mean of income')
plt.title('Histogram of Income')
plt.xlabel('Income')
plt.ylabel('Count')
plt.show()
# ---------------------------------------------------------------

# 4b Plot density plot of income adding a vertical line to denote the mean.

approvals.Income.plot.density(color='blue')
plt.axvline(incomeMean, color='black', label = 'mean of income')
plt.title('Density plot Income')
plt.xlabel('Income')
plt.show()
# ---------------------------------------------------------------

# 5 Create a scatterplot for debt (y-axis) and income (x-axis) and add the trend line. 

plt.scatter(x=approvals['Income'], y=approvals['Debt'])
z = np.polyfit(approvals['Income'], approvals['Debt'], 1)
p = np.poly1d(z)
plt.plot(approvals['Income'],p(approvals['Income']),"r--")
plt.title('Scatter plot of Years Employed and Debt')
plt.xlabel("Income")
plt.ylabel("Debt")
plt.show()
# ---------------------------------------------------------------

# 6 Plot a bar plot of industry and ethnicity on the same plot

chart = sns.countplot(data=approvals, x='Industry', hue='Ethnicity')
chart.set_xticklabels(chart.get_xticklabels(), rotation=45)
plt.title("Bar plot of Ethnicity and Industry")
plt.show()

# ---------------------------------------------------------------

# 7 Create a stacked bar plot of industry color coded by approval status
#  without overlapping. Flip the chart so that it displays the industry
#  on the y-axis and the count on the x-axis.

pd.crosstab(approvals['Industry'], approvals['Approved']).plot(kind='barh', stacked=True)
plt.title("Horizontal bar plot of Industry and Approval")
plt.xlabel("Count")
plt.show()

# ---------------------------------------------------------------

# 8 Plot a box plot of debt (y-axis) against industry (x-axis) 
# and save the graph in a .jpg or .png file called debt_industry. 

myDebitIndustryBPlot = sns.boxplot(data=approvals, y="Debt", x="Industry", width=0.4)
myDebitIndustryBPlot.set_xticklabels(myDebitIndustryBPlot.get_xticklabels(), rotation=45)
plt.title("Box plot of Debt and Industry")
plt.xlabel("Industry")
plt.show()
fig = myDebitIndustryBPlot.get_figure()
fig.savefig("debt_industry.png")
# # ---------------------------------------------------------------

# 9 Plot a box plot of years employed (y-axis) against industry (x-axis)
# and save the graph in a .jpg or .png file called employed_industry

myYearsemployedIndustryBPlot = sns.boxplot(x=approvals['Industry'], y=approvals['YearsEmployed'])
myYearsemployedIndustryBPlot.set_xticklabels(myYearsemployedIndustryBPlot.get_xticklabels(), rotation=45)
plt.title("Box plot of Years Employed and Industry")
plt.xlabel("Industry")
plt.show()
fig = myYearsemployedIndustryBPlot.get_figure()
fig.savefig("employed_industry.png")
# ---------------------------------------------------------------

# 10a Bar plot Gender and Approval

chart = sns.countplot(data=approvals, x='Gender', hue='Approved')
chart.set_xticklabels(chart.get_xticklabels())
plt.legend(title='Approved/Not Approved', labels=['Denied', 'Approved'])
plt.xlabel("Gender (0 is Female & 1 is Male)")
plt.title("Bar plot of Gender and Approval")
plt.show()

# ---------------------------------------------------------------

# 10b Scatter plot(x = YearsEmployed , y = Debt)

plt.scatter(x=approvals['YearsEmployed'], y=approvals['Debt'])
plt.title('Scatter plot of Years Employed and Debt')
plt.xlabel("Years Employed")
plt.ylabel("Debt")
plt.show()