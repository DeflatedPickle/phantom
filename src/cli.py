#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
from main import main

resolutions = [16, 32, 64, 128, 256, 512]


def cli():
    parser = argparse.ArgumentParser(
        prog="phantom",
        description="a tool to convert Minecraft resource packs from 1.8-1.12 to 1.15",
        epilog=""
    )

    # log_level = parser.add_mutually_exclusive_group()
    # log_level.add_argument("-v", "--verbose", action="store_true", help="change the logging verbosity")
    # log_level.add_argument("-q", "--quiet", action="store_true", help="change the logging verbosity")

    parser.add_argument("pack_zip", help="the pack location")
    # parser.add_argument("res", type=int, choices=resolutions, help="the resolution of the pack")
    parser.add_argument("-t", "--textures", action="store_true", help="toggles the texture fix")

    parser.add_argument("-n", "--name", help="the file name of the converted pack (original name used if not passed)")
    parser.add_argument("-s", "--suffix", help="an extra string to add to the end of the converted pack name")

    return parser.parse_args()


if __name__ == "__main__":
    args = cli()

    main(
        pack=args.pack_zip,
        tex=args.textures,
        new_name=args.name,
        name_suffix=args.suffix or "",
    )