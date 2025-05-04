import random
letters = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm', 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' ,  'y' , 'z']
numbers = ['0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9']
symbols = ['!' , '#' , '$' , '%' , '&' , '*' ,  '+']
print("Welcome to Password Generator!")
ur_letter = int(input("How many letters would u like in your password? "))    
ur_numbers = int(input("How many numbers would u like in your password? "))   
ur_symbols = int(input("How many symbols would u like in your password? "))  
#easy level
password = ""
for char in range(1 , ur_letter +1):
    random_char = random.choice(letters)
    password +=random_char
    # print(password)
for char in range(1 , ur_numbers +1):
    random_char = random.choice(numbers)
    password += random_char

for char in range(1 , ur_symbols +1):
    random_char = random.choice(symbols)
    password += random_char
    # print(password)        
print(f"Your Final Password is {password}")
