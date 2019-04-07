import csv

mylist = ["aaaaa", "bbbbbb", "ccccc", "ddddd"]

with open('list.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    wr.writerow(mylist)
