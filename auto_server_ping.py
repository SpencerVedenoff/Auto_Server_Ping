import time
from ping3 import ping, verbose_ping

# List of servers to ping
servers = ["google.com", "wikipedia.org", "runescape.com"]

def ping_servers(servers):
    for server in servers:
        response_time = ping(server)
        if response_time is not None:
            print(f"{server} responded in {response_time} ms")
        else:
            print(f"{server} is down!")

def main():
    while True:
        print("Pinging servers...")
        ping_servers(servers)
        print("Waiting for one hour before pinging again...")
        time.sleep(3600)  # Sleep for 1 hour (3600 seconds)

if __name__ == "__main__":
    main()
