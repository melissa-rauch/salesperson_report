"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []
#maybe - rename "f" to more descriptive verb; report_file
#Open sales report doc
f = open('sales-report.txt') 

for line in f:
    #remove empty space at end of line
    line = line.rstrip()
    #separate each element in line by the |
    entries = line.split('|')

    #assign salesperson to index 0 of entries
    salesperson = entries[0]
    #assign number of melons as integer to index 2 of entries
    melons = int(entries[2])

    #Loop over list, if salesperson already exists, add melons to their melon total
    #if the don't, add salesperson and the 3 of melons

    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


#loop over list of salespeople, print name at i and melons sold at i
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')

#It would be better to create a dictionary with Key = Salesperson and 
#Value = total melons sold. Aids in faster retrieveal