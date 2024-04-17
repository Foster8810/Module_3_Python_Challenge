import os
import csv

budgetdata = os.path.join("resources", "budget_data.csv")
    
with open(budgetdata) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    rowcounter = 0
    total = 0
    totalchange = 0 
    greatestincrease = 0
    greatestincreasemonth = 0
    previousprofit = 0
    greatestdecrease = 0
    greatestdecreasemonth = 0
    change = 0
    

    csvheader = next(csvfile)


    for row in csvreader:
        rowcounter += 1
        profit = int(row[1])
        total += profit

        if rowcounter > 1:
            change = profit - previousprofit
            totalchange += change

        if change > greatestincrease:
            greatestincrease = change
            greatestincreasemonth = row[0]

        if change < greatestdecrease:
            greatestdecrease = change
            greatestdecreasemonth = row[0]

        previousprofit = profit

    averagechange = totalchange / (rowcounter - 1)

    print ("Total Months:", rowcounter)
    print("Total:", total)
    print("Average Change:", averagechange)
    print("Greatest Increase in Profits: "+greatestincreasemonth, greatestincrease)
    print("Greatest Decrease in Profits: "+greatestdecreasemonth, greatestdecrease)

        

    

