import sys

def main():
    try:
        fobj1 = open(sys.argv[1], "r")
        fobj2 = open(sys.argv[2], "r")

        Data1 = fobj1.read()
        Data2 = fobj2.read()

        if Data1 == Data2:
            print("Success")
        else:
            print("Failure")

        fobj1.close()
        fobj2.close()

    except FileNotFoundError:
        print("File Not Found")


if __name__ == "__main__":
    main()