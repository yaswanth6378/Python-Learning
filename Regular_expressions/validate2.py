email = input("what is your email ? :")

username,domain = email.split("@")
if username and email.endswith(".edu"):
    print("valid")
else:
    print("invalid")
# PS C:\Users\yaswa\Downloads\python learing\Regular_expressions> python validate2.py
#what is your email ? :yaswanth@ppsu.edu
#valid
#PS C:\Users\yaswa\Downloads\python learing\Regular_expressions> python validate2.py
#what is your email ? :yaswanth@.edu
#valid #which is still nonsensical
## go check validate3.py for updated code and what error raised