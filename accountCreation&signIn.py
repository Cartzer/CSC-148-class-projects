print("dictionary")
print("comma-separated list of key:value pairs in curly {} brackets")
D = { 'name':'Bob',
      'age':21,
      'job':'Student',
      'city':'Washington DC',
      'email':'bob@bob.com'}
print(type(D),len(D))
for key in D:
    print(key,"==",D[key])
print()



from signIn import func
import accountcreation as ac
print("Welcome to ****")
ac.accountcreation()
from accountcreation import allUsers
l=0
for user in allUsers:
    allUsers[l] = eval(allUsers[l])
    l = l+1
# importing allUsers, imports a list of strings that are written in valid dictonary
# form, this code takes advantage of that and sets each item to its dictonary


while True:
    a = func(allUsers)
    if a != '':
        signedIn = a
        break
    else:
        continue
print(signedIn)
# simple sign in prompt and code
# will ask if the user wants to sign in and what their name is, if its part of
# allUsers, they will be signed in, otherwise it wills propmt them if they want to sign in again


while True:
    break


