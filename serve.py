#!/usr/bin/env python3
"""Python standard-library static launcher; no install/build step."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path
import argparse
root = Path(__file__).resolve().parent / 'dist'
p = argparse.ArgumentParser(description='Open prebuilt V80 presentation')
p.add_argument('--port', type=int, default=0, help='0 = automatic free port (default); use a number for a fixed port')
a = p.parse_args()
if not (root / 'index.html').is_file():
    raise SystemExit('Missing dist/index.html: obtain the built ZIP, not only source.')
with ThreadingHTTPServer(('127.0.0.1', a.port), partial(SimpleHTTPRequestHandler, directory=str(root))) as server:
    port = server.server_address[1]
    print(f'Open http://127.0.0.1:{port}/ in Chrome on this device. Ctrl+C to stop.', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
