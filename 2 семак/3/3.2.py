import csv


with open("countries.csv") as read_file:
    countries = csv.reader(read_file)
    for row in countries:
        print(row)