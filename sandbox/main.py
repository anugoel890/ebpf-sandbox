import subprocess
import os
import signal
import uuid
from monitor import start_ebpf_monitor
from policy import enforce_policies

# Launches and monitors an LLM subprocess (e.g., a plugin/tool)
def run_llm_tool(cmd: list):
    proc_id = str(uuid.uuid4())
    print(f"[+] Launching tool with ID {proc_id}: {cmd}")

    proc = subprocess.Popen(cmd, preexec_fn=os.setsid)

    try:
        # Start eBPF monitor (non-blocking)
        start_ebpf_monitor(proc.pid, proc_id)

        # Enforce policies (e.g., restrict net, files)
        enforce_policies(proc.pid)

        proc.wait()
    except KeyboardInterrupt:
        os.killpg(os.getpgid(proc.pid), signal.SIGTERM)

# Example: sandboxed LLM tool
if __name__ == "__main__":
    run_llm_tool(["python3", "examples/fake_llm_plugin.py"])

