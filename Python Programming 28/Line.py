def main():
    try:
        fobj = open("Demo.txt", "r")
        print("File gets Open")

        Count = 0

        for l in fobj:
            Count = Count + 1

        print("Number of Line :", Count)

        fobj.close()

    except FileNotFoundError:
        print("File is not Present in Current Directory")


if __name__ == "__main__":
    main()
