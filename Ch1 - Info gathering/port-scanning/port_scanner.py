import socket
from colorama import init, Fore, Back

# cli colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX


def is_port_open(host, port):
    """
    Determine whether `host` has the `port` open.
    """
    # create a new socket
    s = socket.socket()

    try:
        # tries to connect to host using the given port
        s.connect((host, port))
        # make timeout if you want it a little faster ( less accuracy )
        s.settimeout(0.2)
    except:
        # can not connect
        # return false
        return False
    else:
        # connection is established, port is open!
        return True


def main():

    # get the host from the user
    host = "192.168.1.1"
    # host = input("Enter the host (Ip Address):")
    # iterate over ports, from 1 to 1024
    for port in range(1, 1025):
        if is_port_open(host, port):
            print(f"{GREEN}[+] {host}:{port} is open      {RESET}")
        else:
            print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")


if __name__ == "__main__":
    main()
