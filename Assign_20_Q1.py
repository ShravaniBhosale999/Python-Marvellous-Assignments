import threading

# Function for even numbers
def Even():
    print("Even thread started")
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)
    print("Even thread completed")

# Function for odd numbers
def Odd():
    print("Odd thread started")
    for i in range(1, 21):
        if i % 2 != 0:
            print(i)
    print("Odd thread completed")


def main():
    t1 = threading.Thread(target=Even)
    t2 = threading.Thread(target=Odd)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()