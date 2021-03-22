'''
Create a function called play_instrument which will receive an instance of an instrument and will print it's play() method
'''

def play_instrument(instrument):
    return instrument.play()

class Guitar:
    def play(self):
        print("playing the guitar")

class Piano:
    def play(self):
        print("playing the piano")

piano = Piano()
play_instrument(piano)

guitar = Guitar()
play_instrument(guitar)

import unittest

class InstrumentsTest(unittest.TestCase):
    def test(self):
        class Test:
            def play(self):
                return "test"
        res = play_instrument(Test())
        self.assertEqual(res, "test")

if __name__ == '__main__':
    unittest.main()