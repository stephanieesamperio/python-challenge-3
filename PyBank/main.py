import pandas as pd
import sys

#Opening the csv file using pandas
csv = pd.read_csv("../PyBank/Resources/budget_data.csv", sep=None, engine='python')
print(csv)

console_window = sys.stdout #saves console for future refrence
f = open("../PyBank/Analysis/analysis.txt", 'w')
sys.stdout = f

print("           Financial Analysis")
print("---------------------------------------")

#The total number of months included in the dataset
months=len(csv)

print("Total Months: " + str(months))

#The net total amount of "Profit/Losses" over the entire period
total=csv['Profit/Losses'].sum()

print("Net Total: " + str(total))

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
csv['Profit/Losses Change'] = csv['Profit/Losses'].shift(-1) - csv['Profit/Losses']
average_change = csv['Profit/Losses Change'].mean()
x = round(average_change,2)

print("Average Change: " + str(x))
    

#The greatest increase in profits (date and amount) over the entire period
csv['Date'] = csv['Date'].shift(-1)
increase = csv['Profit/Losses Change'].max()
increase_date = csv.loc[csv['Profit/Losses Change'] == increase, 'Date'].iloc[0]

print("Greatest Increase: " + increase_date, increase)
    
#The greatest decrease in profits (date and amount) over the entire period
decrease = csv['Profit/Losses Change'].min()
decrease_date = csv.loc[csv['Profit/Losses Change'] == decrease, 'Date'].iloc[0]

print("Greatest Decrease: " + decrease_date, decrease)

#print to console
sys.stdout = console_window
f = open("../PyBank/Analysis/analysis.txt", 'r')
print_console = f.readlines()
for line in print_console:
    print(line)

f.close()


