class LamportClock:
    def __init__(self, pid):
        self.pid = pid
        self.clock = 0
        
    def send_event(self):
        self.clock += 1
        print(f"Process {self.pid} sent message at time {self.clock}")
        return self.clock
        
    def receive_event(self, received_time):
        self.clock = max(self.clock, received_time) + 1
        print(f"Process {self.pid} received message. Updated time: {self.clock}")
        
    def internal_event(self):
        self.clock += 1
        print(f"Process {self.pid} internal event at time {self.clock}")
        
# Create 3 processes
P1 = LamportClock(1)
P2 = LamportClock(2)
P3 = LamportClock(3)

# Simulating events
P1.internal_event()         # Internal event in P1
msg_time = P1.send_event()  # P1 sends a message
P2.receive_event(msg_time)  # P2 receives the message from P1

P2.internal_event()         # Internal event in P2
msg_time = P2.send_event()  # P2 sends a message
P3.receive_event(msg_time)  # P3 receives the message from P2

P3.send_event()            # P3 sends a message
P1.receive_event(P3.clock) # P1 receives message from P3