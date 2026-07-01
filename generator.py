import random
import string

length = int(input("Password ki length daal: "))

letters = string.ascii_letters + string.digits + "@#$%"
password = ''.join(random.choice(letters) for i in range(length))

print("Tera strong password:",password)
