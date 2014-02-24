#!/usr/bin/env python

"""
Copyright 2014 Peter Tripp
Licensed under the MIT License: http://opensource.org/licenses/MIT
"""

import argparse
import os
import subprocess

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Generate fixed width PNGs from SVGs")
    parser.add_argument("-i", "--inputdir", required=True, help="Input directory of SVGs") 
    parser.add_argument("-o", "--outputdir", required=True, help="Output directory of PNGs")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, help="No output")
    parser.add_argument("-x", "--nocrush", action="store_true", default=False, help="Don't optimize resulting PNGs")
    parser.add_argument("-n", "--dry-run", action="store_true", default=False, help="Show commands without running them")
    parser.add_argument("-w", "--width", required=True, type=int, help="PNG output width")

    args = parser.parse_args()
    if not os.path.exists(args.inputdir):
        parser.error('Input directory does not exist')
    elif " " in args.inputdir or " " in args.outputdir :
        parser.error('Input directory or output directory contains a space.')
    #trailing slashes
    if args.inputdir[-1] != os.sep : args.inputdir += os.sep
    if args.outputdir[-1] != os.sep : args.outputdir += os.sep
    if not os.path.exists(args.outputdir): os.makedirs(args.outputdir)

    cmd, counter = [], 0
    for (counter, filename) in enumerate(os.listdir(args.inputdir)):
        if not filename.endswith(".svg"):
            pass #print filename + ":" not .svg
        else :
            li = []
            name, ext = os.path.splitext(filename)
            infile = os.path.join(args.inputdir, filename)
            outfile = os.path.join(args.outputdir, name + ".png")
            li.append(["svg2png", "-w", str(args.width), infile, outfile])
            if not (args.nocrush):
                li.append(["optipng", "-o3", outfile, "-q"])
                #results in 3-5% space savings
                #li.append(["advdef", "-3", outfile, "-q"])
            cmd.append(list(li))
    if args.verbose : print "Found", counter, "files. Beginning conversion."

    for eachfile in cmd :
        for c in eachfile :
            if (args.dry_run or args.verbose):
                print ' '.join(c)
            if not args.dry_run:
                subprocess.call(c)
