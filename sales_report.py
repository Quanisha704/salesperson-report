"""Generate sales report showing total melons each salesperson sold."""


salespeople = []  # Creates a list named salespeople
melons_sold = []  # Creates a list named melons_sold

f = open('sales-report.txt') # Opens "sales_report.txt" and store contents into "f"
for line in f:  # Reads "sales_report" line by line through a for loop 
    line = line.rstrip() #Checks for any whitespaces to the right of each word in each line 
    entries = line.split('|') #Takes away "|" separator 

    salesperson = entries[0] # Get the name of salesperson
    melons = int(entries[2]) # Get amount of melons sold 

    #if salesperson is in salespeople then increment the
    #number of melons_sold by 1
    #
    # Else add the salesperson to the list salespeople 
    # and add melons to melons_sold
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    else:
        salespeople.append(salesperson) #adds 
        melons_sold.append(melons)

# Loops by length of salespeople and prints
# the name of the person and melons sold by using index 
for i in range(len(salespeople)): 
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
