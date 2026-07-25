def main():
    try:
        fobj = open("Demo.txt", "r")
        print("File gets Open")

        Word = input("Enter Word to Search : ")

        Data = fobj.read()

        if Word in Data:
            print("Word Found")
        else:
            print("Word Not Found")

        fobj.close()

    except FileNotFoundError:
        print("File is not Present in Current Directory")


if __name__ == "__main__":
    main()