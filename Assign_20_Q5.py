import threading

def Thread1():
    print("Thread1 started")

    for i in range(1,51):
        print(i)

    print("Thread1 completed")


def Thread2():
    print("Thread2 started")

    for i in range(50,0,-1):
        print(i)

    print("Thread2 completed")

def main():
    t1 = threading.Thread(target=Thread1)
    t2 = threading.Thread(target=Thread2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()