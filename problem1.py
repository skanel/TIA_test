import psutil
from ping3 import ping
import socket
import time

def check_packet_loss(host="www.google.com", packets=10):
    """
    This function pings a host multiple times and calculates packet loss percentage.
    """
    packet_loss = 0
    for _ in range(packets):
        try:
            if ping(host, timeout=1) is None:  # Adjusted timeout to 1 second
                packet_loss += 1
        except Exception:
            packet_loss += 1
    packet_loss_percent = (packet_loss / packets) * 100
    return packet_loss_percent

def check_connectivity(host="www.google.com", port=80, timeout=2):
    """
    Check if a host is reachable over a TCP connection.
    """
    try:
        with socket.create_connection((host, port), timeout):
            return True
    except OSError:
        return False

def monitor_network_performance(interval=5):
    """
    Monitor network performance metrics continuously.

    Parameters:
    - interval (int): Interval in seconds between each monitoring check (default is 5 seconds).
    """
    target_host = "www.google.com"  # Host to ping and check connectivity
    while True:
        try:
            # Get network I/O statistics
            net_io = psutil.net_io_counters()
            bytes_sent = net_io.bytes_sent
            bytes_recv = net_io.bytes_recv

            # Ping a target to measure latency
            try:
                latency = ping(target_host, timeout=1) * 1000  # Convert to milliseconds
                if latency is None:
                    latency = float('inf')  # Indicate no response
            except Exception:
                latency = float('inf')  # Indicate an error

            # Measure packet loss
            packet_loss = check_packet_loss(host=target_host)

            # Check connectivity
            connected = check_connectivity(host=target_host)

            # Print network performance metrics
            print(f"Bandwidth Usage: {bytes_recv / (1024 ** 3):.2f} GB received, {bytes_sent / (1024 ** 3):.2f} GB sent")
            print(f"Latency: {latency:.2f} ms")
            print(f"Packet Loss: {packet_loss:.2f}%")
            print(f"Connectivity: {'Online' if connected else 'Offline'}")
            print("------------------")

            # Wait for the specified interval before the next check
            time.sleep(interval)

        except KeyboardInterrupt:
            print("Monitoring stopped.")
            break
        except Exception as e:
            print(f"Error occurred: {e}")

# Call the function to start monitoring network performance
monitor_network_performance()
