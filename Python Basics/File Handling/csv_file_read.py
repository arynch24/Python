import csv

#reading CSV file
with open("census.csv","r") as csv_file:
    csv_reader=csv.reader(csv_file)
    for row in csv_reader:
        print(row)
    
   

    
    