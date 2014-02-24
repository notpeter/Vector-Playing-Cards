# Vector Playing Cards 

This is a simple collection of SVG images defining a deck of playing cards (based on [vector-playing-cards][4]) and a script (svg2png.py) which will convert a folder of svg files into arbitrarily sized png files.

## Usage:
    svg2png.py [-h] -i INPUTDIR -o OUTPUTDIR [-q] [-x] [-n] -w WIDTH

    Generate fixed width PNGs from SVGs    
    optional arguments:
      -h, --help            show this help message and exit
      -i INPUTDIR           Input directory of SVGs
      -o OUTPUTDIR          Output directory of PNGs
      -v, --verbose         Verbose output
      -x, --nocrush         Don't optimize resulting PNGs
      -n, --dry-run         Show commands without running them
      -w WIDTH              PNG output width

## Example use:
 
  * Simple: Convert SVGs to 300px wide uncompressed PNGs:
    
    `python svg2png.py -v -x -i cards-svg -o cards-png-300px -w 300`

  * Normal: Create SVGs to 320px wide optimized PNGs suppressing all status output

  	`python svg2png.py -i cards-svg -o cards-png-320px -w 320`


## Prerequisites:
To generate custom PNG images, you'll want the following tools:

 * MacOSX:
   * Homebrew: `ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"`
   * svg2png: `brew install svg2png`
   * optipng: `brew install optipng`
   * advdef: `brew install advancecomp`
   * montage: `brew install imagemagick`

 * Python 2.7 (generate-png.py uses argparse which is Python 2.7 only)

## Notes:
Non optimized PNGs are approximately a third larger.

##License

These images, scripts and subsequent transformational output (e.g. custom sized PNGs) are released into the public domain or optionally licensed under the [WTFPL][2] in juristictions where the public domain is not a recognized legal concept.  Either way, do as you see fit: relicense, embed in commercial, non-commercial or open-source software, etc.

The original source images were released by [Byron Knoll][3] into the public domain on Google Code as [vector-playing-cards][4] . Perhaps send him 


 [1]: https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager
 [2]: http://en.wikipedia.org/wiki/WTFPL
 [3]: http://www.byronknoll.com/
 [4]: https://code.google.com/p/vector-playing-cards/

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/notpeter/vector-playing-cards/trend.png)](https://bitdeli.com/free "Bitdeli Badge")

