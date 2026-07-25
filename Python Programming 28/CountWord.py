def main():
    try:
        fobj = open("Demo.txt", "r")
        print("File gets Open")

        Data = fobj.read()

        Words = Data.split()

        print("Total Number of Words :", len(Words))

        fobj.close()

    except FileNotFoundError:
        print("File is not Present in Current Directory")


if __name__ == "__main__":
    main()