import os
import signal
import time

def enforce_policies(pid):
    print(f"[policy] Enforcing policies for PID {pid}")
    # Example: after 10 seconds, kill if still running (demo purpose)
    time.sleep(10)
    if os.path.exists(f"/proc/{pid}"):
        print("[policy] Killing suspicious process")
        os.kill(pid, signal.SIGKILL)