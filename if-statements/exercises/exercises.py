usernames = ["user1","user2","user3","user4","admin"]

print(" \nusernames:\n")
if usernames:
    for username in usernames:
        if username == "admin":
            print("hello admin, would you like to see a status report?")
        else:
            print(f"hello {username}.")
else:
    print("We need to find some users")


current_users = [current_user.lower() for current_user in ["current_user1","CURRRENT_USER2","current_user3","current_user4","current_user5"]]


new_users = [new_user.lower() for new_user in ["new_user1","new_user2","current_user3","CURRENT_USER4","new_user5"]]

print("\nChecking usernames\n")

for new_user in new_users:
    if new_user in current_users:
        print(f'the username "{new_user}" is already taken')
    else:
        print(f'The username "{new_user}" is available')

ordinal_numbers = list(range(1,10))
print("\nordinal numbers:\n")
for num in ordinal_numbers:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")
