import os

consolidated = ""
for r, d, f in os.walk("./"):
    for file in f:
        consolidated += os.path.join(r, file)