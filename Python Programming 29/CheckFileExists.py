import os

def main():
    Name = input("Enter File Name : ")

    if os.path.exists(Name):
        print("File Exists")
    else:
        print("File Does Not Exist")


if __name__ == "__main__":
    main()
