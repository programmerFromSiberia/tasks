import re

logins = ['n12login', 'name22login', '2name2login', 'invalid', 'invalidlogin']

valid_logins = 0
valid_logins_list = []

pattern = r"^[a-zA-Z]+\d{2,}login$"

for login in logins:
    if re.match(pattern, login):
        valid_logins += 1
        valid_logins_list.append(login)

print("Number of valid logins:", valid_logins)
print("Valid logins:", valid_logins_list)
