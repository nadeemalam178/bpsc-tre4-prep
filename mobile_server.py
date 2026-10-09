#!/usr/bin/env python3
"""
Lightweight Mobile Server for BPSC TRE 4.0
Allows studying on mobile phone over local Wi-Fi / Hotspot.
"""

import os
import sys
import socket
import http.server
import socketserver

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

def get_ip_addresses():
    ips = []
    try:
        hostname = socket.gethostname()
        addr_info = socket.getaddrinfo(hostname, None, socket.AF_INET)
        for item in addr_info:
            ip = item[4][0]
            if not ip.startswith("127.") and ip not in ips:
                ips.append(ip)
    except Exception:
        pass
    return ips or ["127.0.0.1"]

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def main():
    ips = get_ip_addresses()
    print("=" * 66)
    print("  📱 BPSC TRE 4.0 — MOBILE STUDY SERVER STARTED!")
    print("=" * 66)
    print("  Study notes, tests, and AI explanations on your mobile phone:")
    print("  1. Connect your phone to the same Wi-Fi or Mobile Hotspot.")
    print("  2. Open Chrome or Safari on your phone and visit:")
    print("")
    for ip in ips:
        print(f"     👉 http://{ip}:{PORT}/index.html")
    print("")
    print("  ⚡ All 30 PYQ questions & instant AI explanations are ready.")
    print("  [Keep this window open while studying. Press Ctrl+C to stop]")
    print("=" * 66)
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    main()
