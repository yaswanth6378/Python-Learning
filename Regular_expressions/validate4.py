import re
email = input("what is your email ?:").strip()

if re.search(".*@.*",email):
    print("valid")
else:
    print("invalid")
#  python validate4.py
#what is your email ?:@  
#valid # here * means 0 or more repetitions so it will accept nothing before or after @
# go check validate5.py