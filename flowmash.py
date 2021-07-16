import json
from typing import *

from blessed import Terminal
import color
from shader import *

def get_json(name):
    with open(f"{name}.json") as f:
        return json.loads(f.read())

# Load config
flowmash_json = get_json('flowmash')

# Init
term = Terminal()

# Run
print('hello')