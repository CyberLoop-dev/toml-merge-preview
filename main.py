#!/usr/bin/env python3
"""Merge TOML layers without modifying their source files."""
import argparse
import json
import sys
import tomllib
from pathlib import Path

def merge_layers(layers):
    result, trace = {}, []
    def merge_into(target, incoming, source, prefix=""):
        for key, value in incoming.items():
            dotted = f"{prefix}.{key}" if prefix else key
            old = target.get(key)
            if isinstance(old, dict) and isinstance(value, dict):
                merge_into(old, value, source, dotted)
            else:
                if key in target:
                    trace.append({"key": dotted, "source": source, "replaced": old, "with": value})
                target[key] = value
    for source, data in layers:
        merge_into(result, data, source)
    return result, trace

def load_files(paths):
    layers = []
    for item in paths:
        path = Path(item)
        with path.open("rb") as handle:
            layers.append((str(path), tomllib.load(handle)))
    return layers

def json_value(value):
    if hasattr(value, "isoformat"):
        return value.isoformat()
    raise TypeError(f"unsupported TOML value for JSON output: {type(value).__name__}")

def main():
    parser = argparse.ArgumentParser(description="Preview a layered TOML merge; later files override earlier files.")
    parser.add_argument("files", nargs="+", help="TOML files in low-to-high precedence order")
    parser.add_argument("--trace", action="store_true", help="print overwritten-key trace to stderr")
    args = parser.parse_args()
    try:
        merged, trace = merge_layers(load_files(args.files))
    except (OSError, tomllib.TOMLDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(merged, indent=2, sort_keys=True, default=json_value))
    if args.trace:
        print("\nOverride trace:", file=sys.stderr)
        for item in trace:
            print(f"- {item['key']} from {item['source']}: {item['replaced']!r} -> {item['with']!r}", file=sys.stderr)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
