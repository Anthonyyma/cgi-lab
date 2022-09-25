#!/usr/bin/env python3
import os
import json

# print env as JSON
print("Content-Type: text/plain")
print()
print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")