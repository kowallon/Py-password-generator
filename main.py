import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

count = int(input("How many characters would you like in your password?\n"))
symbols_input = int(input("How many symbols would you like?\n"))
numbers_input = int(input("How many numbers would you like\n"))

password = ""
pass_list= []

for i in range(0, (count-symbols_input-numbers_input)):
    pass_list.append(letters[random.randint(0, len(letters)-1)])
    #password += letters[random.randint(0, len(letters)-1)]
    i+=1

for j in range(0,symbols_input):
    #password += symbols[random.randint(0, len(symbols)-1)]
    pass_list.append(symbols[random.randint(0, len(symbols)-1)])
    j+=1

for y in range(0, numbers_input):
    #password += numbers[random.randint(0, len(numbers)-1)]
    pass_list.append(numbers[random.randint(0, len(numbers)-1)])
    y+=1

for l in range(0, len(pass_list)):
    random_char = random.choice(pass_list)
    password += random_char
    pass_list.remove(random_char)

print(f"Here's your password \n{password}")
    