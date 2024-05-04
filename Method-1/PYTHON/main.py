import requests
import subprocess


def is_cron_running() -> bool:
    endpoint = "http://127.0.0.1:8010/is-cron-live"
    try:
        response = requests.get(endpoint)
        if response.status_code == 200:
            return True
    except Exception as e:
        return False


def main():
    if is_cron_running():
        return False  # Abort if already running

    code_path = __file__.replace("main.py", "cron_is_alive.py")
    process = subprocess.Popen(["python", code_path])
    print("Process started\n")

    # Place your task logic here

    if process:
        process.kill()
        print("Process killed\n")


if __name__ == "__main__":
    main()
