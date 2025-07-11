import time
import os


print("[plugin] LLM Plugin starting")
os.system("curl http://example.com")  # This should be caught by eBPF monitor
for _ in range(20):
    time.sleep(1)
print("[plugin] Done")
