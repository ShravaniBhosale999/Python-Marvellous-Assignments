# Write a Python program to monitor the number of threads used by each process on the system. The program should periodically check the thread count for each process and log the information to a file named "ThreadLog.txt". The log should include the process name, process ID, and the number of threads at each check.

import psutil
import datetime

def thread_monitor(logfile):
    try:
        with open(logfile, "a") as f:
            f.write("\n--- Thread Monitoring ---\n")
            f.write(str(datetime.datetime.now()) + "\n")

            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    threads = proc.num_threads()
                    f.write(f"Name: {proc.info['name']}, PID: {proc.info['pid']}, Threads: {threads}\n")
                except:
                    pass
    except Exception as e:
        print("Error:", e)