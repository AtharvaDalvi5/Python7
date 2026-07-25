def main():
    try:
        fobj = open("Demo.txt", "r")

        Data = fobj.read()

        print(Data)

        fobj.close()

    except FileNotFoundError:
        print("File Not Found")


if __name__ == "__main__":
    main()