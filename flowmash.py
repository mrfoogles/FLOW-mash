import json
from typing import *

flowmash_json: Dict

with open('flowmash.json', 'r') as f:
    global flowmash_json
    flowmash_json = json.loads(f.read())

flowmash_json.

