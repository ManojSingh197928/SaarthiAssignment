import re
password= input("Input your password")
flag = 1
while x:  
    if (len(password)<6 or len(password)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[!#$%&'()*+,-./:;<=>?@[\]^_`{|}~]",password):
        break
    elif re.search("\s",password):
        break
    else:
        print("Valid Password")
        flag=0
        break

if flag:
    print("Not a Valid Password")
