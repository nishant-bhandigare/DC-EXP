import threading
import time
import random

class MaekawaProcess:
    def __init__(self, pid, quorum):
        self.pid = pid  # Process ID
        self.quorum = quorum  # Voting set
        self.lock = threading.Lock()  # Ensures thread safety
        self.voted = None  # Stores the process to which the vote is granted
        self.request_queue = []  # Queue of pending requests

    def request_cs(self):
        """Request Critical Section access."""
        print(f"Process {self.pid} requesting CS")
        self.request_queue.append(self.pid)
        # Send request to all quorum members
        for process in self.quorum:
            process.receive_request(self.pid)
        while self.request_queue[0] != self.pid:
            time.sleep(0.1)  # Wait until it gets permission

        print(f"Process {self.pid} entering CS")
        time.sleep(random.uniform(1, 3))  # Simulate critical section execution
        print(f"Process {self.pid} exiting CS")
        self.release_cs()

    def receive_request(self, sender_pid):
        """Handle an incoming CS request."""
        with self.lock:
            if self.voted is None:
                self.voted = sender_pid
                print(f"Process {self.pid} grants vote to {sender_pid}")
            else:
                print(f"Process {self.pid} cannot vote for {sender_pid}, already voted for {self.voted}")

    def release_cs(self):
        """Release the Critical Section and notify quorum members."""
        self.request_queue.pop(0)
        # Notify all quorum members
        for process in self.quorum:
            process.receive_release(self.pid)

    def receive_release(self, sender_pid):
        """Handle CS release notification."""
        with self.lock:
            if self.voted == sender_pid:
                print(f"Process {self.pid} revokes vote from {sender_pid}")
                self.voted = None

# Get user input for number of processes
num_processes = int(input("Enter the number of processes: "))
processes = []

# Create process objects
for i in range(1, num_processes + 1):
    processes.append(MaekawaProcess(i, []))

# Assign quorum sets (Each process has a set of 2 or more quorum members)
for i in range(num_processes):
    processes[i].quorum = [processes[(i + 1) % num_processes], processes[(i + 2) % num_processes]]

# Create and start threads for each process
threads = []
for process in processes:
    t = threading.Thread(target=process.request_cs)
    threads.append(t)
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()
