# This code demonstrates the use of a Lock to synchronize access to a shared variable (counter) across multiple threads.
import threading

# Shared variable
counter = 0

# Create Lock object
lock = threading.Lock()

def increment_counter():
    global counter
    
    for _ in range(100000):   # Each thread increments 100000 times
        with lock:            # Acquire + Release automatically
            counter += 1

def main():
    global counter

    # Create multiple threads
    t1 = threading.Thread(target=increment_counter)
    t2 = threading.Thread(target=increment_counter)
    t3 = threading.Thread(target=increment_counter)

    # Start threads
    t1.start()
    t2.start()
    t3.start()

    # Wait for all threads to finish
    t1.join()
    t2.join()
    t3.join()

    # Final result
    print("Final value of counter:", counter)

if __name__ == "__main__":
    main()