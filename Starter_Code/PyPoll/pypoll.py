import os
import csv

electiondata = os.path.join("resources", "election_data.csv")
    
with open(electiondata) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    rowcounter = 0
    CCS = 0
    DD = 0
    RAD = 0

    csvheader = next(csvfile)

    for row in csvreader:
        rowcounter += 1

        if row[2] == "Charles Casper Stockham":
            CCS += 1

        elif row[2] == "Diana DeGette":
            DD += 1

        elif row[2] == "Raymon Anthony Doane":
            RAD += 1

    
    CCSpercent = CCS / rowcounter 
    DDpercent = DD / rowcounter
    RADpercent = RAD / rowcounter
    CCSfinal = round(CCSpercent, 5) * 100
    DDfinal = round(DDpercent, 5) * 100
    RADfinal = round(RADpercent, 5) * 100


    print("Election Results")
    print("-----------------")
    print("Total Votes: ",rowcounter)
    print("-----------------")
    print("Charles Casper Stockham",CCSfinal,"%", [CCS])
    print("Diana DeGette",DDfinal,"%",[DD])
    print("Raymon Anthony Doane",RADfinal,"%",[RAD])
    print("-----------------")
    if CCS > DD and CCS > RAD:
        print("Winner Charles Casper Stockham")
    if DD > CCS and DD > RAD:
        print("Winner: Diana DeGette")
    if RAD > CCS and RAD > DD:
        print("Winner: Raymon Anthony Doane")