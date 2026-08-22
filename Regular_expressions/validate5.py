import re
email = input("what is your email ? : ").strip()
if re.search(".+@.+",email):
    print("valid")
else:
    print("invalid")
#what is your email ? : yaswanth@?edu
#valid #nfact its not proper mail ,so i am going to introduce \.(means exactly match the dor)

# go check validate6.py