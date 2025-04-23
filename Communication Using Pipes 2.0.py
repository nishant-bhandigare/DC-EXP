import multiprocessing

def child_process(conn):
    message = "Hello. This is Child process talking."
    conn.send(message)
    conn.close()

def parent_process():
    parent_conn, child_conn = multiprocessing.Pipe()
    process = multiprocessing.Process(target=child_process, args=(child_conn,))
    process.start()

    message = parent_conn.recv()
    print(f"Parent received msg = {message}")

    process.join()

if __name__ == "__main__":
    parent_process()
