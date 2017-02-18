#!/bin/env python

"""
outputs a nice cowsay format
"""
from __future__ import print_function
import sys

MAX_WIDTH = 30

MAD_COW = '''
     \   ^__^
      \  (oo)\_______
         (__)\       )\/\\
             ||----w |
             ||     ||
'''


def wrap_up(f):
    def temp(*argv):
        s = f(*argv)
        max_line = max(map(lambda x: len(x), s))
        return ['<{:^{max_line}}>'.format(l, max_line=max_line) for l in s]

    return temp


@wrap_up
def text2lines(text, max_width=MAX_WIDTH):
    if not text:
        text = '...'
    lines = [[]]
    for w in text.split():
        if sum(map(lambda x: len(x), lines[-1])) < max_width-len(lines[-1]):
            lines[-1].append(w)
        else:
            lines.append([w])
    return [' '.join(l) for l in lines]


def cowsay(text, max_width=MAX_WIDTH):
    """
    returns the full cowsay string
    """
    lines = text2lines(text, max_width)
    width = max(map(lambda x: len(x), lines))-2
    return [' '+'-'*width] + lines + [' '+'-'*width, MAD_COW]

if __name__ == '__main__':
    print("\n".join(cowsay(sys.argv[1])))
