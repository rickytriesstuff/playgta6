"""Standalone local server for the self-contained PlayGTA6 browser game."""
import argparse
import mimetypes
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "unsafe-none")
        self.send_header("Cross-Origin-Resource-Policy", "same-origin")
        super().end_headers()

if __name__ == "__main__":
    if not (ROOT / "index.html").is_file():
        raise SystemExit("index.html is missing from the game folder.")
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--open", action="store_true")
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    url = "http://localhost:%d/" % server.server_port
    print("PlayGTA6 standalone game: %s (Ctrl+C to stop)" % url, flush=True)
    if args.open:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
