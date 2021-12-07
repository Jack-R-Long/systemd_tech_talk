#!/usr/bin/python3
import re


# Find keyboard with regex
with open("/proc/bus/input/devices") as f:
    lines = f.readlines()

    pattern = re.compile("Handlers|EV=")
    handlers = list(filter(pattern.search, lines))

    pattern = re.compile("EV=120013")

    for idx, elt in enumerate(handlers):
        if pattern.search(elt):
            line = handlers[idx - 1]

    pattern = re.compile("event[0-9]")
    infile_path = "/dev/input/" + pattern.search(line).group(0)
    
    print(infile_path)
