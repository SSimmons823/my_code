#!/usr/bin/env python3
import argparse, socket
from datetime import datetime

def server(port):
    x = "Your choice was server and it will run on port " + str(port)
    return x

def client(port):
    x = "Your choice was client and it will run on port " + str(port)
    return x

def udp(noport):
    x = "Your choice was udp and it will run on port " + str(noport)
    return x

if __name__ == '__main__':
    choices = {'client': client, 'server': server, 'udp': udp}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')
    parser.add_argument('-t', metavar='NOPORT', default=udp,
                        help='UDP port (default UDP)')
    
args = parser.parse_args()
function = choices[args.role]
print(function(args.p))
