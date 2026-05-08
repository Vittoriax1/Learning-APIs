import requests
import threading
from queue import Queue
import os

# -----------------------------
# User Configuration
# -----------------------------
BASE_URL = "http://localhost:5000"
WORDLIST_FILE = "wordlist.txt"

# Optional nested prefixes
PREFIXES = [
    "",
    "api",
    "api/v1",
    "v1",
    "v2"
]

# Output log file
LOG_FILE = "enum_results.txt"

# Number of worker threads
THREAD_COUNT = 10

# -----------------------------
# Load wordlist
# -----------------------------
def load_wordlist(filename):
    if not os.path.exists(filename):
        print(f"[!] Wordlist file not found: {filename}")
        return []

    with open(filename, "r") as f:
        words = [line.strip() for line in f if line.strip()]
    return words


# -----------------------------
# Logging function
# -----------------------------
def log_result(text):
    with open(LOG_FILE, "a") as log:
        log.write(text + "\n")


# -----------------------------
# Worker function for threads
# -----------------------------
def worker():
    while True:
        path = q.get()
        if path is None:
            break
        test_path(path)
        q.task_done()


# -----------------------------
# Endpoint testing function
# -----------------------------
def test_path(path):
    full_url = f"{BASE_URL}/{path}"

    try:
        r = requests.get(full_url, timeout=3)
        status = r.status_code
        size = len(r.content)
        content_type = r.headers.get("Content-Type", "unknown")

        result = f"{full_url} -> {status} | size={size} bytes | type={content_type}"
        print(result)
        log_result(result)

    except Exception:
        result = f"{full_url} -> ERROR"
        print(result)
        log_result(result)


# -----------------------------
# Main script logic
# -----------------------------
if __name__ == "__main__":
    print("[*] Loading wordlist...")
    words = load_wordlist(WORDLIST_FILE)

    if not words:
        print("[!] Empty or missing wordlist. Exiting.")
        exit()

    # Clean old log file
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    # Prepare threading queue
    global q
    q = Queue()

    # Create worker threads
    threads = []
    for _ in range(THREAD_COUNT):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    # Add tasks: nested paths
    print("[*] Queuing paths for testing...")

    for prefix in PREFIXES:
        for w in words:
            if prefix:
                q.put(f"{prefix}/{w}")
            else:
                q.put(w)

    # Block until queue is empty
    q.join()

    # Stop workers
    for _ in range(THREAD_COUNT):
        q.put(None)

    for t in threads:
        t.join()

    print(f"\n[*] Enumeration complete. Results saved to {LOG_FILE}")
