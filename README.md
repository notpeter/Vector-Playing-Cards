# Vector Playing Cards

This is a collection of SVG images for a full deck of playing cards (based on [vector-playing-cards][1]) and a script, `svg2png.py`, that converts a folder of SVG files into PNG files of any width.

The `cards-svg` folder contains 54 cards: the 52 standard cards plus two jokers. Files are named by rank then suit, for example `AS.svg`, `10H.svg`, `KD.svg`, `Joker1.svg` and `Joker2.svg`.

## Prerequisites

- **Python 3**
- **resvg-py** (the SVG renderer, no system libraries needed):
  ```shell
  pip install resvg-py
  ```
- **optipng** (optional): if it is on your `PATH`, the script uses it to shrink the PNGs. If it's missing, the script prints a note and skips that step.
  - Windows: `winget install optipng`, or download it from [optipng.sourceforge.net][2]
  - macOS: `brew install optipng`
  - Debian/Ubuntu: `sudo apt install optipng`

## Usage

```
usage: svg2png.py [-h] -i INPUTDIR -o OUTPUTDIR [-v] [-x] [-n] -w WIDTH

Generate fixed width PNGs from SVGs

options:
  -h, --help            show this help message and exit
  -i, --inputdir INPUTDIR
                        Input directory of SVGs
  -o, --outputdir OUTPUTDIR
                        Output directory of PNGs
  -v, --verbose         Verbose output
  -x, --nocrush         Don't optimize resulting PNGs
  -n, --dry-run         Show what would be done without doing it
  -w, --width WIDTH     PNG output width
```

The output directory is created if it doesn't exist. Existing PNGs with the same names are overwritten.

## Examples

- Convert to 300px wide PNGs without optimization, listing each file as it goes:
  ```
  python svg2png.py -v -x -i cards-svg -o cards-png-300px -w 300
  ```
- Convert to 691px wide PNGs, optimized with optipng if it's installed:
  ```
  python svg2png.py -i cards-svg -o cards-png-691px -w 691
  ```
- Show what would be generated without writing anything:
  ```
  python svg2png.py -n -i cards-svg -o cards-png-320px -w 320
  ```

## Card size and proportions

You choose only the width. The height follows from the card artwork, whose proportions are about 1 : 1.452 (each SVG's `viewBox` is 167.09 × 242.67). For example, 691px wide gives 691 × 1006.

To get a particular height, divide it by 1.452 to find the width. For example, `-w 688` gives cards about 1000px tall. For comparison, a standard poker card is 1 : 1.4 and a bridge card is about 1 : 1.556.

## Notes

- Unoptimized PNGs are roughly a third larger than ones run through optipng.
- The SVGs give their size in `pt` units, which resvg-py rejects. The script removes the unit before rendering, which doesn't change the output's proportions.

## License

These images, scripts and their output (for example, custom-sized PNGs) are released into the public domain, or optionally licensed under the [WTFPL][3] in jurisdictions where the public domain is not a recognized legal concept. Either way, do as you see fit: relicense, or embed in commercial, non-commercial or open-source software.

The original source images were released into the public domain by [Byron Knoll][4] on Google Code as [vector-playing-cards][1]. See [CONTRIBUTORS.md](CONTRIBUTORS.md) for everyone who has worked on this project.

[1]: https://code.google.com/archive/p/vector-playing-cards/
[2]: https://optipng.sourceforge.net/
[3]: https://en.wikipedia.org/wiki/WTFPL
[4]: http://www.byronknoll.com/
