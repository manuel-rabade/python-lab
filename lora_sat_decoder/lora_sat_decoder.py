#!/usr/bin/python

import argparse
import importlib
import os

# Recursive function to print object fields in a readable format
def pretty_print(name, fields, level=1):
    """
    Recursively prints object fields with indentation.
    Args:
        name (str): Module name.
        fields (dict): Object fields to print.
        level (int): Indentation level.
    """
    for f in fields.keys():
        if f.startswith("_"):  # Skip private fields
            continue
        if hasattr(fields[f], '__dict__'):
            print("\t" * level + f"{f}:")
            pretty_print(name, fields[f].__dict__.copy(), level + 1)
        else:
            value = fields[f]
            print("\t" * level + f"{f}: {value}")

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("format", type=str, help="Format module to use")
parser.add_argument("--hex", type=str, help="Hexadecimal packet input")
parser.add_argument("--bin", type=argparse.FileType("rb"), help="Binary packet input file")
args = parser.parse_args()

# Dynamically import parser based on the format argument
module_name = os.path.splitext(args.format)[0]
class_name = "".join(x.capitalize() or "_" for x in module_name.split('_'))
module_import = importlib.import_module(module_name)
parser = getattr(module_import, class_name)

# Parse the raw packet input
if args.hex:
    bytes = bytes.fromhex(args.hex)  # Convert hex input to bytes
elif args.bin:
    with args.bin as file:
        bytes = file.read()  # Read binary input
else:
    print("--hex or --bin missing")  # Ensure at least one input is provided
    exit()

# Decode the packet using the parser
packet = parser.from_bytes(bytes)

# Print parsed packet fields
sections = packet.__dict__.copy()
for s in sections.keys():
    if s in ["padding"] or s.startswith("_"):  # Skip padding and private fields
        continue
    print(f"{s}:")
    if hasattr(sections[s], '__dict__'):
        pretty_print(module_name, sections[s].__dict__.copy())
