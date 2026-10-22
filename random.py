Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import random
... 
... # Define the characters available for the password
... letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
... numbers = ['0','1','2','3','4','5','6','7','8','9']
... symbols = ['@','$',"_","!"]
... 
... # Get user input for password length configurations
... n_let = int(input("Enter the number of letters: "))
... n_num = int(input("Enter the number of numbers: "))
... n_sym = int(input("Enter the number of symbols: "))
... 
... # Create a list to store all the chosen characters
... password_list = []
... 
... # 1. Randomly pick characters from each list according to the user input
... for char in range(0, n_let):
...     password_list.append(random.choice(letters))
... 
... for char in range(0, n_num):
...     password_list.append(random.choice(numbers))
... 
... for char in range(0, n_sym):
...     password_list.append(random.choice(symbols))
... 
... # 2. Shuffle the list to mix the characters randomly
... random.shuffle(password_list)
... 
... # 3. Convert the list back into a single string
... password = "".join(password_list)
... 
... # 4. Print the final generated password
... print(f"Your generated password is: {password}")
SyntaxError: multiple statements found while compiling a single statement
