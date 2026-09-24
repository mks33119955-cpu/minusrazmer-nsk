from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os
os.chdir(Path(__file__).parent)
print("Сайт доступен: http://localhost:8000")
ThreadingHTTPServer(("localhost",8000), SimpleHTTPRequestHandler).serve_forever()
