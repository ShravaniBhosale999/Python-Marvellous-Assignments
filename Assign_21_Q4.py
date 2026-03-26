#Program to create two threads, one to calculate the sum of elements in a list and another to calculate the product of elements in a list.

import threading


def sum_of_elements(list1):
    sum = 0
    for i in list1:
        sum=sum+i
    print("Sum of the elements in the list is:", sum)

def product_of_elements(list1):
    product = 1
    for i in list1:
        product=product*i
    print("Product of the elements in the list is:", product)


def main():
    list1= list(map(int, input("Enter the list of numbers: ").split()))

    t1 = threading.Thread(target=sum_of_elements, args=(list1,))
    t2 = threading.Thread(target=product_of_elements, args=(list1,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == "__main__":
    main()