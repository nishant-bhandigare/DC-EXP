import os
import multiprocessing

def child_process(pipe_write):
    os.close(pipe_write[0])  # Close unused read end
    message = "Hello from child process!"
    os.write(pipe_write[1], message.encode())  # Write message to pipe
    os.close(pipe_write[1])

def parent_process():
    pipe_read, pipe_write = os.pipe()  # Create pipe
    # Create child process (pass pipe_write as a tuple, not a list)
    process = multiprocessing.Process(target=child_process, args=((pipe_read, pipe_write),))
    process.start()
    os.close(pipe_write)  # Close unused write end

    # Read message from child process
    message = os.read(pipe_read, 1024).decode()
    print(f"Parent received: {message}")
    os.close(pipe_read)
    process.join()

if __name__ == "__main__":
    parent_process()
