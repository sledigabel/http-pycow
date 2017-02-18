#!/bin/env python

from cowsay import *
import unittest

class Cowsay(unittest.TestCase):

    def test_empty_string_text2lines(self):
        text = text2lines('')
        self.assertEqual(text, [ '<...>'])

    def test_basic_string_text2lines(self):
        text = text2lines('test')
        self.assertEqual(text, [ '<test>'])

    def test_long_string_text2lines(self):
        text = text2lines('this is a longer string', 30)
        self.assertEqual(text, [ '<this is a longer string>'])

    def test_long_string_split_text2lines(self):
        text = text2lines('this is a longer string', 10)
        self.assertEqual(text, [ '<  this is a  >', '<longer string>'])

    def test_cowsay_basic(self):
        expected = [' ----',
                    '<test>',
                    ' ----',
                    '\n     \\   ^__^\n      \\  (oo)\\_______\n         (__)\\       )\\/\\\n             ||----w |\n             ||     ||\n']
        self.assertEqual( expected, cowsay('test'))

if __name__ == '__main__':
    unittest.main()
