import sys

def main():
    try:
        fobj1 = open(sys.argv[1], "r")
        fobj2 = open("Demo.txt", "w")

        Data = fobj1.read()

        fobj2.write(Data)

        print("Contents Copied Successfully")

        fobj1.close()
        fobj2.close()

    except FileNotFoundError:
        print("File Not Found")


if __name__ == "__main__":
    main()