import multiprocessing
import time

# Shared memory and semaphore
shared_memory = multiprocessing.Value('i', 0)  # Shared integer
semaphore = multiprocessing.Semaphore(1)  # Binary semaphore (mutex)

def process_task(process_id):
    global shared_memory
    print(f"Process {process_id} is waiting to access shared memory...")

    # Acquire the semaphore (lock)
    semaphore.acquire()
    try:
        print(f"Process {process_id} acquired lock.")
        # Read the shared value
        current_value = shared_memory.value
        print(f"Process {process_id} read value: {current_value}")

        # Simulate computation
        time.sleep(1)
        # Modify the shared value
        shared_memory.value = current_value + 1
        print(f"Process {process_id} updated value to: {shared_memory.value}")
    finally:
        # Release the semaphore (unlock)
        print(f"Process {process_id} released lock.")
        semaphore.release()

# Number of processes
num_processes = 4
processes = []

# Create and start multiple processes
for i in range(num_processes):
    p = multiprocessing.Process(target=process_task, args=(i,))
    processes.append(p)
    p.start()

# Wait for all processes to finish
for p in processes:
    p.join()

print(f"Final value in shared memory: {shared_memory.value}")
