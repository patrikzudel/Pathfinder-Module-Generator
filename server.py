#!/usr/bin/env python3
"""Serve the Pathfinder app and its assembly-preview core using Python 3."""
import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent


class AppHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        # Keep the public URL lowercase while retaining the supplied filename.
        if urlsplit(self.path).path == '/pathfinder_core.stl':
            self.path = '/Pathfinder_core.stl'
        super().do_GET()

    def do_HEAD(self):
        if urlsplit(self.path).path == '/pathfinder_core.stl':
            self.path = '/Pathfinder_core.stl'
        super().do_HEAD()

    def list_directory(self, path):
        self.send_error(404, 'Not found')
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=8000)
    args = parser.parse_args()
    with ThreadingHTTPServer((args.host, args.port), AppHandler) as server:
        print(f'Pathfinder: http://{args.host}:{server.server_port}', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
