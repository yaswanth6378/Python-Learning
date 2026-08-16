def main():
    name = input("enter you name:")
    print(hello(name))
   
def hello(to="world"):
    return f"hello to,{to}"
if __name__ == "__main__":
    main()