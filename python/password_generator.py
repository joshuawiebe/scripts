import random
import string

length = int(input("Passwordlength: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(length))
print(f"Your Password: {password}")
