def func(allUsers): # defining our function, one argument (expected to be a list of dictionaries)
    signedInUser = '' # empty variable
    nameList =[] # empty list 
    for user in allUsers:
        nameList.append(user['name']) # uses the arugment and appends the value associated with the 'name' key to the list

    while True:
        signIn = input("Would you like to sign in (yes or no)? \n").lower().strip() #prompts user
        if signIn == 'yes': 
            break
        else:
            continue # the while loop is mostly just user-proofing, once they are ready to sign in the rest of the code will run
        
    while True:
        signInName = input("What is your name? \n") # user input
        if signInName not in nameList: # if user input is not in the list will continue this while loop (user-proofing)
            print('Name not recognized!')
            continue
        for item in allUsers:
            if signInName == item['name']: # if the user input is in the argument (value under one of the dictonaries) 
                print("Welcome,",item['name']) # welcomes the user if they are in the argument (have an account)
                return item['name'] # returns the signed in user so that it can be used 
