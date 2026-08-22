import re
email = input("what is your name ? :")
if re.search(r".+@.+\.com",email):
    # r means raw string ,tells python to not intrepet any \ in usaul way
    print("valid")
else:
    print("invalid")
#PS C:\Users\yaswa\Downloads\python learing\Regular_expressions> python validate6.py
#hat is your name ? :yaswanth@@@gmail.com
#valid #above mail is invalid but it showing valid so lets look into that in validate7.py