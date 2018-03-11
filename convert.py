#!/usr/bin/python

import sys
import fontforge


def split_filename(filename):
    return filename.split('.')[:-1]


def main(filename, fontname, fullname):

    if (not filename.endswith('.svg')):
        filename = filename + '.svg'

    font = fontforge.font()

    font.fontname = fontname
    font.fullname = fullname
    font.familyname = fullname

    # Create new glyph
    glyph = font.createChar(0)

    # Get SVG
    glyph.importOutlines(filename)

    # Make the glyph rest on the baseline
    ymin = glyph.boundingBox()[1]
    glyph.transform([1, 0, 0, 1, 0, -ymin])

    # Set glyph side bearings, can be any value or even 0
    glyph.left_side_bearing = glyph.right_side_bearing = 10

    # font.generate("foobar.pfb", flags=["tfm", "afm"])  # Type1 with tfm/afm
    font.generate(split_filename(filename) + '.otf')  # OpenType
    font.generate(split_filename(filename) + '.ttf')  # TrueType


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
