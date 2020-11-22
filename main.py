import json
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
import pyfiles.indian
import pyfiles.asean
import pyfiles.saarc
import pyfiles.asean_gb

p = Path('json_data')
p.mkdir(exist_ok=True)

ind = pyfiles.indian.extract_data("population-estimates.csv")
asean_2014 = pyfiles.asean.extract_data("population-estimates.csv")
saarc = pyfiles.saarc.extract_data("population-estimates.csv")
aseab_gb = pyfiles.asean_gb.extract_data("population-estimates.csv")

population = {
    "india": ind,
    "asean": asean_2014,
    "saarc": saarc,
    "aseanGb": aseab_gb,
}

with open("json_data/population.json", 'w') as f:
    json.dump(population, f, indent=4)
    f.close()

# Function to start http serever


def start_server(server_class=HTTPServer, handler=SimpleHTTPRequestHandler):
    PORT = 8000
    server_address = ('localhost', PORT)
    httpd = server_class(server_address, handler)
    print(f"Server started on PORT localhost:{PORT}")
    httpd.serve_forever()


start_server()
