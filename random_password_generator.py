import string 
import random 

lowercase_letters = list(string.ascii_lowercase)
uppercase_letters = list(string.ascii_uppercase)
digits = list(string.digits)
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '<', '>', '?', '/']

character_set = lowercase_letters + uppercase_letters + digits + special_characters
 
def generate_password(length):
    password = ""
    for _ in range(length):
        password += random.choice(character_set)
       
    return password

def main():
    length = int(input("length: ")) 
    password = generate_password(length)
    print(password) 
        
    
    
main() 
     