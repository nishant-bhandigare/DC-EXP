class Process:
    def __init__(self, id):
        self.id = id
        self.active = True

def run_election():
    # Initialize processes
    print("No of processes 5")
    processes = [Process(i) for i in range(5)]
    
    # Find highest active process ID
    def get_coordinator():
        return max((p.id for p in processes if p.active))
    
    # Make highest process fail
    coord_id = get_coordinator()
    print(f"Process no {coord_id} fails")
    processes[coord_id].active = False
    
    # Election phase
    initiator = 2
    print(f"Election Initiated by {initiator}")
    current = initiator
    next_proc = (current + 1) % len(processes)
    
    while True:
        if processes[next_proc].active:
            print(f"Process {current} pass Election({current}) to {next_proc}")
            current = next_proc
        next_proc = (next_proc + 1) % len(processes)
        if next_proc == initiator:
            break
    
    # Coordinator announcement phase
    coordinator = get_coordinator()
    print(f"Process {coordinator} becomes coordinator")
    
    current = coordinator
    next_proc = (current + 1) % len(processes)
    
    while True:
        if processes[next_proc].active:
            print(f"Process {current} pass Coordinator({coordinator}) message to process {next_proc}")
            current = next_proc
        next_proc = (next_proc + 1) % len(processes)
        if next_proc == coordinator:
            print("End Of Election")
            break

if __name__ == "__main__":
    run_election()