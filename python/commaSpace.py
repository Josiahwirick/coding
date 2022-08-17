# Comma Space
def commaSpace(listA):
    listAFinal = '' #Create variable for final result to be printed from
    for x in range(len(listA)):
        if x + 1 < len(listA): # If item in the list is not the last one, will print the item with comma
            listB = listA[x] + ', '
            listAFinal = listAFinal + listB
        elif x + 1 == len(listA): # If item is last in list, print with 'and' before it
            listB = 'and ' + listA[x]
            listAFinal = listAFinal + listB
    print(listAFinal)

listA = [] # Empty list to fill with user input
i = 0 # Counter for list items
while True: # Input loop to create list for the function
    print('Input list item ' + str(i) + ':')
    name = input()
    if name == '': # Complete list and call commaSpace function by entering no input
        commaSpace(listA)
        break
    listA = listA + [name] # Add input to list
    i += 1