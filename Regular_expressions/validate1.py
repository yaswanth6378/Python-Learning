email = input("whats is your email? :")

username,domain = email.split("@") # splits email into two parts with "@"
if username and "." in email:
    print("valid")
else:
    print("invalid")
#PS C:\Users\yaswa\Downloads\python learing\Regular_expressions> python validate1.py
#whats is your email? :yaswanth.@
#valid # here “My answer is nonsensical.”
# # go check validate2.py for updated code and what error raised