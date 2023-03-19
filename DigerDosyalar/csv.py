import csv

# Data to be written to the file
rows = [['Name', 'Age'],
        ['John', 25],
        ['Jane', 30],
        ['Jim', 35]]

# Write the data to a CSV file
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)
