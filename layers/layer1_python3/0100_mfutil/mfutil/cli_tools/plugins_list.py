#!/usr/bin/env python3

import argparse
import sys
import json
from mfutil.plugins import get_installed_plugins

DESCRIPTION = "get the installed plugins list"


def main():
    arg_parser = argparse.ArgumentParser(description=DESCRIPTION)
    arg_parser.add_argument("--raw", action="store_true", help="raw mode")
    arg_parser.add_argument("--json", action="store_true", help="json mode "
                            "(not compatible with raw mode)")
    args = arg_parser.parse_args()
    if args.json and args.raw:
        print("ERROR: json and raw options are mutually exclusives")
        sys.exit(1)
    plugins = get_installed_plugins()
    if not args.raw and not args.json:
        print("Installed plugins:")
        print()
        print("| %-25s | %-25s | %.25s" % ("NAME", "VERSION", "RELEASE"))
        print("-" * 75)
    json_output = []
    for plugin in plugins:
        name = plugin['name']
        release = plugin['release']
        version = plugin['version']
        home = plugin['home']
        if args.raw:
            print("%s~~~%s~~~%s" % (name, version, release))
        elif args.json:
            json_output.append({
                "name": name,
                "release": release,
                "version": version,
                "home": home
            })
        else:
            print("| %-25s | %-25s | %.25s" % (name, version, release))
    if not args.raw and not args.json:
        print()
        print("Total: %i plugin(s)" % len(plugins))
    elif args.json:
        print(json.dumps(json_output, indent=4))


if __name__ == '__main__':
    main()
