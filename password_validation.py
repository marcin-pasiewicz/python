import re

password = input('Enter password')
pattern = re.compile(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$")
check = pattern.fullmatch(password)
print(check)