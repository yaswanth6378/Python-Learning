# store only exact value in tuple
# we cannot modify the value of tuple once it is created
# when we fixed dont change the value of tuple then we use tuple
"""user_birthday_list = ["december", 13, 2004]
user_birthday_list[0] = "December"  # This will work for a list
print("List Output(Broken Birthday):", user_birthday_list)"""
user_birthday_tuple = ("september", 7, 2002)
print("\nTuple Output(Birthday):", user_birthday_tuple)
# Trying to change the tuple will cause a crash, protecting the data:
try:
    user_birthday_tuple[0] = "September"  # This will not work for a tuple
except TypeError:
    print("\n Tuple error: a tuple can notbe modified once it is created, so we cannot change the value of tuple")
