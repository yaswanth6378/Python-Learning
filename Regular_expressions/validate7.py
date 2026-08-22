import re
email = input("what is your eamil? :")

if re.search(r".+\@.+\.com"):
    print("valid")
else:
    print("invalid")