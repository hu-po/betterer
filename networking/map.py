"""
    List information about current computer and its network.
"""

import socket
import subprocess
from multiprocessing import Process, Queue
from typing import Tuple, List
import logging

log = logging.getLogger()
log.setLevel(logging.INFO)
# log.setLevel(logging.DEBUG)


def localhost_ip(
    dns_port: Tuple[str, int] = ("8.8.8.8", 80),
    socket_family: socket.AddressFamily = socket.AF_INET,
    socket_kind: socket.SocketKind = socket.SOCK_DGRAM,
) -> str:
    """ Get IP address of localhost. """
    with socket.socket(socket_family, socket_kind) as s:
        # Connect to primary Google DNS server
        s.connect(dns_port)
        ip, _ = s.getsockname()
    return ip


def ping_worker(
    jobs: Queue,
    outs: Queue,
) -> None:
    """ Pings ip addresses in a job queue, adds them to outs queue. """
    while True:
        ip: str = jobs.get()
        if ip is None:
            break
        try:
            subprocess.check_call(['ping', '-c1', ip],
                                  stdout=subprocess.DEVNULL)
            outs.put(ip)
        except subprocess.TimeoutExpired as e:
            log.debug(f'Timeout when pinging {ip}')
        except Exception as e:
            log.debug(f'While pinging {ip} encountered exception {e}')


def netmap(
    num_workers: int = 255,
) -> str:
    """ Maps network using parallel ping processes. """

    # get my IP and compose a base like 192.168.1.xxx
    ip_parts = localhost_ip()
    base_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'

    # Create worker processes
    jobs: Queue = Queue()
    outs: Queue = Queue()
    workers: List[Process] = []
    for worker in range(num_workers):
        workers.append(Process(
            target=ping_worker,
            args=(jobs, outs)))

    # Total of 255 possible IP addresses on local network
    netA, netB, netC, localhost = localhost_ip().split('.')
    for host in range(1, 255):
        jobs.put(f'{netA}.{netB}.{netC}.{host}')

    # Start worker processes
    for worker in workers:
        worker.start()
        # None will eventually kill the worker
        jobs.put(None)
        worker.join()

    yield outs.get()


if __name__ == '__main__':

    log.info(f'This computer is {localhost_ip()}')
    log.info(f'On this network, I')
    for ip in netmap():
        log.info(f'\t found {ip}')
