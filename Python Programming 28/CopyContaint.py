def main():
    try:
        fobj1 = open("Demo.txt", "r")
        fobj2 = open("ABC.txt", "w")

        Data = fobj1.read()

        fobj2.write(Data)

        print("Contents Copied Successfully")

        fobj1.close()
        fobj2.close()

    except FileNotFoundError:
        print("File is not Present in Current Directory")


if __name__ == "__main__":
    main()