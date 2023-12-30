import random
letters = []
for elm in range(65, 91):
    letters.append(chr(elm))
for elm in range(97, 123):
    letters.append(chr(elm))
numbers = list(range(0, 10))
special = ['!', '@', '#', '$', '%','&', '*', '(', ')', '_', '+']
print("Welcome to Password Generator")
nb_letters = int(input("How many letters do you want in your password?\n"))
nb_num = int(input("How many numbers do you want in your password?\n"))
nb_special = int(input("How many special characters do you want in your password?\n"))
password = []
for i in range(0, nb_letters):
    password.append(letters[random.randint(0, len(letters) - 1)])
for i in range(0, nb_num):
    password.append(str(numbers[random.randint(0, len(numbers) - 1)]))
for i in range(0, nb_special):
     password.append(special[random.randint(0, len(special) - 1)])
random.shuffle(password)
password = ''.join(password)
print(f"Your password is '{password}'\nThank you for using Password Generator :)")
