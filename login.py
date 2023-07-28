uname='Admin'
pwd='Admin@123'
attempt=0
while True:
    attempt +=1
    print(f'Attempt {attempt} of 3')
    username=input("Enter username :")
    password=input("Enter the password :")
    if attempt==2:
        print('Too many attempt')
        break
    if uname != username:
        print("Invalid username")
    if pwd != password:
        print("Invalid password")
    if uname == username and pwd ==password:
        print('Login Sucessfull')
        break
for i in range(5):
    for j in range(i):
         print(j,end=' ')
    print('\n')
print('program complete')   