
# Data Types, Variables, and Operators Exercises

# You have rented some movies for your kids:
# The little mermaid (for 3 days),
# Brother Bear (for 5 days, they love it),
# and Hercules (1 day, you don't know yet if they're going to like it).
# If price for a movie per day is 3 dollars,
# how much will you have to pay?

lil_m = 3
bro_b = 5
herc = 1
daily_charge = 3
total = (lil_m + bro_b + herc) * daily_charge
print(total)

# Suppose you're working as a contractor for 3 companies:
# Google, Amazon and Facebook, they pay you a different rate per hour.
# Google pays 400 dollars per hour,
# Amazon 380,
# and Facebook 350.
# How much will you receive in payment for this week?
# You worked 10 hours for Facebook,
# 6 hours for Google
# and 4 hours for Amazon.

g = 400 * 6
a = 380 * 4
f = 350 * 10
earnings = (g + a + f)
print(earnings)

# A student can be enrolled to a class only if the class is not full
# and the class schedule does not conflict with her current schedule.

class_max = 20
class_size = 17
class_full = class_size != class_max
free_time =  True
can_enroll = class_full and free_time
print(can_enroll)

# A product offer can be applied only if people buys more than 2 items,
# and the offer has not expired.
# Premium members do not need to buy a specific amount of products.

item_count = 1
offer_valid = True
prem_mem = True
offer_accepted = (item_count > 2 or prem_mem) and offer_valid
print(offer_accepted)



# Use the following code to follow the instructions below:

username = 'codeup'
password = 'notastrongpassword'

# the password must be at least 5 characters
pword_len = len(password) > 5
print(pword_len)

# the username must be no more than 20 characters
uname_len = len(username) < 20
print(uname_len)

# the password must not be the same as the username
same_uname_pword = username != password
print(same_uname_pword)

# bonus neither the username or password can start or end with whitespace
space_check = username[0] != ' ' and username[-1] != ' ' and password[0] != ' ' and password[-1] != ' '
print(space_check)
