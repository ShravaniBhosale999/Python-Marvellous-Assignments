import threading


# Thread to count lowercase characters
def Small(data):
    print("\nSmall thread started")

    count = 0
    for ch in data:
        if ch.islower():
            count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of lowercase characters:", count)

    print("Small thread completed")


# Thread to count uppercase characters
def Capital(data):
    print("\nCapital thread started")

    count = 0
    for ch in data:
        if ch.isupper():
            count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of uppercase characters:", count)

    print("Capital thread completed")


# Thread to count digits
def Digits(data):
    print("\nDigits thread started")

    count = 0
    for ch in data:
        if ch.isdigit():
            count += 1

    print("Thread ID:", threading.get_ident())
    print("Thread Name:", threading.current_thread().name)
    print("Number of digits:", count)

    print("Digits thread completed")


def main():
    data = input("Enter string: ")

    t1 = threading.Thread(target=Small, args=(data,), name="Small")
    t2 = threading.Thread(target=Capital, args=(data,), name="Capital")
    t3 = threading.Thread(target=Digits, args=(data,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()