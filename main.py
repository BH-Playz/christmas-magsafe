import subprocess
import time
import os
import atexit

def run_smc_command(value, silent=False):
    """Runs the sudo smc command with the given value.

    Args:
        value: The value to write to ACLC.
        silent: If True, suppresses output.
    """

    if os.geteuid() != 0:
        print("Script must be run as root (using sudo).")
        return

    command = ["sudo", "smc", "-k", "ACLC", "-w", str(value).zfill(2)]
    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
        if not silent:  # Only print if not silent
            print(f"Setting ACLC to: {str(value).zfill(2)}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(f"Stderr: {e.stderr}")
        print(f"Stdout: {e.stdout}")
    except FileNotFoundError:
        print("smc command not found. Is it installed?")

def set_to_zero():
    """Sets the value to 00 when the script exits."""
    print("Setting ACLC to 00 on exit.") #Re-added the print statement here
    run_smc_command(0, silent=True)

def main():
    """Main loop to alternate between 04 and 03."""
    if os.geteuid() != 0:
        print("Script must be run as root (using sudo).")
        return

    atexit.register(set_to_zero)

    try:
        while True:
            run_smc_command(4)
            time.sleep(0.5)
            run_smc_command(3)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Script stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()