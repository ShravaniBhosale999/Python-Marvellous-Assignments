# Write a Python program to create two threads. One thread will print the even numbers and the other thread will print the odd numbers from a given list of integers. Finally, both threads will print the sum of their respective numbers.
import threading

# Thread function for even numbers
def EvenList(data):
    print("EvenList thread started")

    total = 0

    for num in data:
        if num % 2 == 0:
            print(num)
            total += num

    print("Sum of even elements:", total)
    print("EvenList thread completed")


# Thread function for odd numbers
def OddList(data):
    print("OddList thread started")

    total = 0

    for num in data:
        if num % 2 != 0:
            print(num)
            total += num

    print("Sum of odd elements:", total)
    print("OddList thread completed")


def main():
    data = list(map(int, input("Enter list: ").split()))

    t1 = threading.Thread(target=EvenList, args=(data,))
    t2 = threading.Thread(target=OddList, args=(data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()