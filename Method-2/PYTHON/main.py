import psutil

def check_if_running(task_name):
    """Check if a given task is already running on the system."""
    for proc in psutil.process_iter():
        try:
            # Check the command line of the process
            cmd_line = ' '.join(proc.cmdline())
            if task_name in cmd_line:
                return True
        except Exception as e:
            pass
    return False

if __name__ == "__main__":
    task_name = 'main.py'
    if not check_if_running(task_name):
        # Code to start your cron job
        pass
    else:
        print(f"{task_name} is already running.")
