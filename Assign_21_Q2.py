# Write a Python program to find the maximum and minimum element in a list using threads.


import threading

def max_element(lst):
    print("Maximum element in the list is:", max(lst))

def min_element(lst):
    print("Minimum element in the list is:", min(lst))


def main():

    lst = list(map(int, input("Enter the list of numbers: ").split()))

    t1 = threading.Thread(target=max_element, args=(lst,))
    t2 = threading.Thread(target=min_element, args=(lst,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == "__main__":
    main()