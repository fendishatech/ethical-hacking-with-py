import socket
import threading
from queue import Queue


class PortScanner:
    def __init__(self, num_threads=10):
        self.num_threads = num_threads
        self.queue = Queue()

    def scan(self, host, start_port, end_port):
        open_ports = []
        for port in range(start_port, end_port + 1):
            self.queue.put(port)

        for i in range(self.num_threads):
            thread = threading.Thread(
                target=self._scan_worker, args=(host, open_ports))
            thread.daemon = True
            thread.start()

        self.queue.join()
        return open_ports

    def _scan_worker(self, host, open_ports):
        while True:
            port = self.queue.get()
            if self._is_port_open(host, port):
                open_ports.append(port)
            self.queue.task_done()

    def _is_port_open(self, host, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((host, port))
            sock.close()
            return True
        except (socket.timeout, ConnectionRefusedError):
            return False


if __name__ == "__main__":
    scanner = PortScanner()
    scanner.scan("127.0.0.1", 100, 900)
