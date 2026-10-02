f = open('accountUsers.txt','r+')
allUsers =[]
allUsers = f.readline().split("|")
for i in allUsers:
    if i == '':
        allUsers.remove(i)
f.close()
# Because this file saves the users a a single line of the dictonaries for each
# user as a string, we need a way to first break the single line,
# which is done using split("|") as that is what we defined the separator to be|


f = open('accountUsers.txt','w')
def accountcreation():
    while True:
        createAccount = input("Create a new account (yes or no)? \n").lower().strip()
        # user proofing the prompting of if they want to create an account
        if createAccount == 'yes':
            print("----------------")
            userName = input("Enter your name: ")
            userAge = int(input("Enter your age: "))
            userCountry = input("Enter your country: ")
            userEmail = input("Enter your email: ")
            userDetails = dict([('name',userName), ('age',userAge), ('country',userCountry), ('email',userEmail)])
            # user inputs and then makes a dictonary out of them
            print(userDetails)
            infoCorrect = input("Is the information above correct (yes or no)? \n")
            # prompts the user if the data they input is correct
            if infoCorrect.lower() == 'no':
                badInfo = input("What information is incorrect? \n")
                if badInfo.lower() == 'name':
                    userName = input("Enter your name: ")
                    userDetails['name'] = userName
                elif badInfo.lower() == 'age':
                    userAge = int(input("Enter your age: "))
                    userDetails['age'] = userAge
                elif badInfo.lower() == 'country':
                    userCountry = input("Enter your conutry: ")
                    userDetails['country'] = userCountry
                elif badInfo.lower() == 'email':
                    userEmail = input("Enter your email: ")
                    userDetails['email'] = userEmail
                # allows the user to replace the data they input (incase of typo)
            allUsers.append(str(userDetails))
            # appending the new user details to the list of all users
            print("User successfully created")
            continue
        elif createAccount == 'no':
            break
        # breaks loop if user inputs no
        else:
            continue
        # user proofing
        
##            for key in userDetails:
##                if key == 'age':
##                    allUsers.append("'{0}': {1}".format(key,userDetails[key]))
##                else:
##                    allUsers.append("'{0}': '{1}'".format(key,userDetails[key]))
##            print(allUsers)
    for i in allUsers:
        f.write(i)
        f.write("|")
        # rewrites the file with any new users added
    f.close()
