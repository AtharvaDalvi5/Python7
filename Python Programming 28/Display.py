def main():
    try:
        fobj = open("Demo.txt", "r")

        for line in fobj:
            print(line)

        fobj.close()

    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    main()