class RoundRobinLoadBalancer:
    def __init__(self, servers):  # Corrected __init__
        # Initialize list of servers and set current server index to 0
        self.servers = servers
        self.index = 0

    def get_next_server(self):
        # Get the server assigned to handle the current request
        server = self.servers[self.index]
        # Update the index to point to the next server
        self.index = (self.index + 1) % len(self.servers)  # Loop back if the index exceeds the number of servers
        return server

    def handle_request(self, request):
        # Get the server that will handle the current request
        server = self.get_next_server()
        # Server processes the request (simulated here with a print statement)
        print(f"Request {request} is assigned to {server}")


# List of servers (or nodes)
servers = ['Server1', 'Server2', 'Server3']

# Initialize the Round Robin Load Balancer with the list of servers
load_balancer = RoundRobinLoadBalancer(servers)

# Simulate handling 5 requests
for request_id in range(1, 6):
    load_balancer.handle_request(request_id)
