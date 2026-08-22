email = input("Enter your email address: ").strip()

if "@" and "." in email:
    print("valid email address")

else:
    print("invalid email address")
    #output#Enter your email address: @.      
#valid email address # actually the email is invalid
# go check validate1.py for updated code and what error raised