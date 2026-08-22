# here now i am introducing the library called re(regular expressions) means start, $ means end, and the pattern checks for text before @, a domain, and an extension such as .com.
import re
email = input("whats is your email :")
if re.search("@",email):
    print("valid")
else:
    print("invalid")
#whats is your email :@
#valid #re.search does not format all the pattern we have to fullfill some rules
#  # go check validate2.py for updated code and what error raised
# some special symbols in re library
# . -> any character except newline
# * -> 0 or more repetitions
# + -> 1 or more repetitions
# ? -> 0 or one repetitions
# {m} -> m repetitions
# {m-n} -> m-n repetitions