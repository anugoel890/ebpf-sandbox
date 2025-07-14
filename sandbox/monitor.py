from bcc import BPF
import threading

# eBPF program to trace syscalls (simplified)
ebpf_code = """
int trace_syscalls(void *ctx) {
    bpf_trace_printk("LLM syscall detected");
    return 0;
}
"""

def start_ebpf_monitor(pid, tag):
    def monitor():
        print(f"[ebpf] Monitoring process {pid} with tag {tag}")
        b = BPF(text=ebpf_code)
        b.attach_kprobe(event="sys_execve", fn_name="trace_syscalls")
        b.trace_print()

    t = threading.Thread(target=monitor, daemon=True)
    t.start()