
Dataset =[{"name": "James","class": "FC01", "exam score": 75,"coursework score": 45 },
     { "name": "Natasha", "class": "FC02", "exam score": 95, "coursework score": 85 },
     { "name": "Kumail", "class": "FC02", "exam score": 85, "coursework score": 75  },
     { "name": "Tariq", "class": "FC01", "exam score": 75, "coursework score": 55   },
     { "name": "Qimeng", "class": "FC01", "exam score": 80, "coursework score": 80  },
     { "name": "Ming", "class": "FC02", "exam score": 90, "coursework score": 75    }]


# Filter Algorithm

def filterData(Dataset, attribute, value):
     
    filteredResult = []    # Creating a new list for filtered data
    
    if attribute not in Dataset[0].keys(): # Checking if the key is correct
        return "Attribute does not exist"

    for item in Dataset:   # Check if filter matches the value
        if item[attribute] == value:
            filteredResult = filteredResult + [item] # Add to list
    
    if len(filteredResult) == 0:
        return "Did not find any result"
    else:             
        return filteredResult



# Aggregating Algorithm

def aggregation(Dataset, att): # Defined a function 
    if att not in Dataset[0]:
        return "Wrong key!"
    try: 
     total = 0  # Value is initiated as 0
     for item in Dataset: # For loop to go through the items in Dataset 
          total += item[att]
     my_mean = total/len(Dataset)
     return my_mean
      
    except:
     print ("Invalid Input. Input must be a key that holds an integer value")



# Sorting Algorithm
def sortdata(Dataset, key):
    
    if key not in Dataset[0]: # Checking if the key is correct
        return "Wrong key!"
 
    sortedlist = [] # Creating a new list to store sorted data
    for item in Dataset: # For loop to iterate over the items in dataset
        sortedlist = sortedlist + [item] # Returns the whole data in list 

    for i in range(len(sortedlist)): # Sorting starts. outer loop to run over the length of the list
        for j in range(len(sortedlist)-1): 
            if sortedlist[j][key] > sortedlist[j+1][key]: # Comparison
                temporary = sortedlist[j] # Temporary variable to store list
                sortedlist[j] = sortedlist[j+1]
                sortedlist[j+1] = temporary # Swapping
                
    return sortedlist 
                
# User Menu

while True: # Iterates each time unless loop is broke by break function
    choice = input("Choose one of the option: Filter, Aggregate, Sort, Exit ").lower()

    if choice == "filter":
        attribute = input("Enter the attribute you want to filter >> ")
        value = input("Enter the attribute >> ")
        if value.isdigit():
            value = int(value)
        print(filterData(Dataset, attribute, value))
    elif choice == "aggregate":
        att = input("Enter the key you want to aggregate >> ")
        print(aggregation(Dataset, att))
    elif choice == "sort":
        key = input("Enter the key value to be sorted >> ")
        print(sortdata(Dataset, key))
    elif choice == "exit":
        print("Program exited!")
        break
    else:
        print("Invalid input!")
               