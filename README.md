# Problem1
To implement a system for monitoring network performance, including metrics like bandwidth usage, latency, packet loss, and connectivity status.)
## Breakdown the problem
```
kanel@kanels-MacBook-Pro ~ % ping 8.8.8.8 -c 1
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: icmp_seq=0 ttl=116 time=44.138 ms

--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 44.138/44.138/44.138/0.000 ms

```
- **Bandwidth Usage:** Measure the amount of data transmitted and received over the network.
- **Latency:** Measure the time it takes for a data packet to travel from the source to the destination.
- **Packet Loss:** Measure the number of packets that fail to reach their destination.
- **Connectivity Status:** Check if the network is connected or disconnected.

# Choose the Tools:
- Use libraries like `psutil` for bandwidth usage.
- Use `ping3` for latency and packet loss.
- Use `socket` for connectivity status.

# Problem2
Create a simple load balancer that distributes incoming network requests evenly across multiple servers to improve network performance.

## Understand the Requirement 
### Imagine a Circle:
Think of your servers as being arranged in a circle. 
Let's say you have three servers: Server A, Server B, and Server C.

### Taking Turns:
- The load balancer sends the first request to Server A.
- The next request goes to Server B.
- The third request goes to Server C.
- The fourth request goes back to Server A, and the cycle continues.
- This method ensures that each server gets an equal number of requests over time, which helps keep everything running smoothly.

# Test with the mock server

To simulate and test the provided load balancer code, you'll need to set up mock backend servers and then use a tool to send requests to the load balancer. Here’s how you can simulate and test the load balancer:
1. run `python servers.py`
2. Running the Load Balancer
Ensure you have all backend servers (`servers.py`) running before starting the load balancer (`example2.py`).
3. Sending Requests to the Load Balancer 
Here’s an example using curl:

```curl http://127.0.0.1:8000
curl http://127.0.0.1:8000
curl http://127.0.0.1:8000
curl http://127.0.0.1:8000
```
3. Observing Load Balancer Behavior
Each request sent to http://127.0.0.1:8000 should be forwarded to one of the backend servers (ports 8001, 8002, 8003, 8004) in a round-robin fashion.
You should see output messages from the backend servers indicating which server handled each request.