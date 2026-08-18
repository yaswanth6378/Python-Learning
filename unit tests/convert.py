def main():
    while True:
        au = input("AU:")
        try:
            au = float(au)
            break
        except ValueError:
            continue
    print(f"{au} is {convert(au)} m")
def convert(au):
    if not isinstance(au,(int,float)):
        raise TypeError("AU must be int are float")
    return au * 149597870700
if __name__ == "__main__":
    main()
    