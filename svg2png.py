#!/usr/bin/env python3

"""
Copyright 2014 Peter Tripp
Licensed under the MIT License: http://opensource.org/licenses/MIT

Requires: pip install resvg-py
Optional: optipng on PATH for PNG optimization (skipped if not found).
"""

import argparse
import os
import re
import shutil
import subprocess

import resvg_py

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Generate fixed width PNGs from SVGs")
    parser.add_argument("-i", "--inputdir", required=True, help="Input directory of SVGs")
    parser.add_argument("-o", "--outputdir", required=True, help="Output directory of PNGs")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Verbose output")
    parser.add_argument("-x", "--nocrush", action="store_true", default=False, help="Don't optimize resulting PNGs")
    parser.add_argument("-n", "--dry-run", action="store_true", default=False, help="Show what would be done without doing it")
    parser.add_argument("-w", "--width", required=True, type=int, help="PNG output width")

    args = parser.parse_args()
    if not os.path.isdir(args.inputdir):
        parser.error('Input directory does not exist')
    if not args.dry_run:
        os.makedirs(args.outputdir, exist_ok=True)

    optipng = None if args.nocrush else shutil.which("optipng")
    if not args.nocrush and optipng is None:
        print("optipng not found on PATH; skipping PNG optimization.")

    files = sorted(f for f in os.listdir(args.inputdir) if f.endswith(".svg"))
    if args.verbose: print("Found", len(files), "files. Beginning conversion.")

    for filename in files:
        name, ext = os.path.splitext(filename)
        infile = os.path.join(args.inputdir, filename)
        outfile = os.path.join(args.outputdir, name + ".png")
        if args.dry_run or args.verbose:
            print(infile, "->", outfile, "(%dpx wide)" % args.width)
        if args.dry_run:
            continue
        with open(infile, encoding="utf-8") as f:
            svg = f.read()
        #resvg_py rejects unit suffixes (e.g. "pt") on the root width/height; viewBox keeps the aspect ratio
        for attr in ("width", "height"):
            svg = re.sub(rf'(<svg\b[^>]*?\s{attr}="[\d.]+)[a-z]+"', r'\1"', svg, count=1)
        png = resvg_py.svg_to_bytes(svg_string=svg, width=args.width)
        with open(outfile, "wb") as f:
            f.write(bytes(png))
        if optipng:
            cmd = [optipng, "-o3", "-quiet", outfile]
            if args.verbose: print(' '.join(cmd))
            subprocess.call(cmd)
