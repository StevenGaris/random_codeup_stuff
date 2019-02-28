
# Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'


# the password must be at least 5 characters

def len_check(password):
    if len(password) > 5:
        return True
    else:
        return False

# the username must be no more than 20 characters

def uname_check(username):
    if len(username) <= 20:
        return True
    else:
        return False

# the password must not be the same as the username

def same_uname_pword(username, password):
    if username == password:
        return False
    else:
        return True

# bonus neither the username or password can start or end with whitespace

def space_check(username, password):
    if username[0] == " " or username[-1] == " " or password[0] == " " or password[-1] == " ":
        return False
    else:
        return True



print(len_check(password))
print((uname_check(username)))
print(same_uname_pword(username, password))
print(space_check(username, password))