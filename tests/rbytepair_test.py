import os

import unittest
from rbytepair import *

test_corpus = '''What in Davy Jones’ locker did ye just bark at me, ye scurvy bilgerat?
I’ll have ye know I be the meanest cutthroat on the seven seas, and I’ve led numerous raids on fishing villages, and made over 300 wenches.
I be trained in hit-and-run pillaging and be the deadliest with a pistol of all the captains on the high seas.
Ye be nothing to me but another source o’ swag.
I’ll have yer guts for garters and keel haul ye like never been done before, hear me true.
You think ye can hide behind your newfangled computing device?
Think twice on that, scallywag.
As we parley I be contacting my secret network o’ pirates across the sea and yer port is being tracked right now so ye better prepare for the typhoon, weevil.
The kind o’ monsoon that’ll wipe ye off the map.
You’re sharkbait, fool. I can sail anywhere, in any waters, and can kill ye in o’er seven hundred ways, and that be just with me hook and fist.
Not only do I be top o’ the line with a cutlass, but I have an entire pirate fleet at my beck and call and I’ll damned sure use it all to wipe yer arse off o’ the world, ye dog.
If only ye had had the foresight to know what devilish wrath your jibe was about to incur, ye might have belayed the comment.
But ye couldn’t, ye didn’t, and now ye’ll pay the ultimate toll, you buffoon. 
I’ll poo fury all over ye and ye’ll drown in the depths o’ it.
You’re fish food now.
'''.split("\n")


class RBytePairTest(unittest.TestCase):
    def test_thing(self):
        self.assertEqual(1, 1)