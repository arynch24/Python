import csv

data=[["Name","Age"],["John", 30],["Alice",25],["Bob",35]]
with open("census.csv","w") as csv_file:
        csv_writer =csv.writer(csv_file)
        csv_writer.writerows(data)