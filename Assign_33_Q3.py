# Write a Python program to monitor the memory usage of each process on the system. The program should periodically check the memory usage for each process and log the information to a file named "MemoryLog.txt". The log should include the process name, process ID, and the percentage of memory used at each check.

def memory_monitor(logfile):
    import psutil
    import datetime

    processes = []

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            mem = proc.memory_percent()
            processes.append((proc.info['name'], proc.info['pid'], mem))
        except:
            pass

    processes.sort(key=lambda x: x[2], reverse=True)

    with open(logfile, "a") as f:
        f.write("\n--- Top 10 Memory Processes ---\n")
        f.write(str(datetime.datetime.now()) + "\n")

        for p in processes[:10]:
            f.write(f"{p[0]} ({p[1]}) -> {p[2]:.2f}%\n")