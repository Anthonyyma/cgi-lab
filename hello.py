#!/usr/bin/env python3
import os
import json

# print env as JSON
print("Content-Type: text/plain")
print()
print(json.dumps(dict(os.environ), indent=2))
# print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")
