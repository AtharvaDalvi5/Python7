def main():
    try:
        fobj = open("Demo.txt", "r")

        Data = fobj.read()

        Count = Data.count("Marvellous")

        print("Frequency :", Count)

        fobj.close()

    except FileNotFoundError:
        print("File Not Found")


if __name__ == "__main__":
    main()