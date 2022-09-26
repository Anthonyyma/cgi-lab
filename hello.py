#!/usr/bin/env python3
import os

print("Content-Type: text/plain")
print()
print(f"<p>USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")
 