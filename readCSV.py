import csv
import sys
import operator

drink = open("drinks.csv", "rb")
drinkReader = csv.reader(drink)
sortedlist = sorted(drinkReader, key=lambda row: row[2], reverse=True)
for row in sortedlist:
    print row
drink.close()    
