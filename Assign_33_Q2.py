# Write a Python program to monitor the number of open files for each process on the system. The program should periodically check the open file count for each process and log the information to a file named "FileLog.txt". The log should include the process name, process ID, and the number of open files at each check.

def open_files_monitor(logfile):
    import datetime
    import psutil

    with open(logfile, "a") as f:
        f.write("\n--- Open Files Monitoring ---\n")
        f.write(str(datetime.datetime.now()) + "\n")

        for proc in psutil.process_iter(['pid', 'name']):
            try:
                files = proc.open_files()
                count = len(files)
                f.write(f"{proc.info['name']} ({proc.info['pid']}): {count} files\n")
            except psutil.AccessDenied:
                f.write(f"{proc.info['name']} ({proc.info['pid']}): Access Denied\n")
            except:
                pass