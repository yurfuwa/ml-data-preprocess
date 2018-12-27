import unittest
import sys
import os
import io
from wrasse import base64 

voiceis = ['./base64files/20170523182616_hand_01NORMAL.wav.029.txt',
           './base64files/20171128155437_web_api.001.txt']
not_wavs = ['./base64files/not_wav.txt']


class TestAudioPreprocess(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestAudioPreprocess, self).__init__(*args, **kwargs)

    def test_base64_to_bytes(self):
        for voice in voiceis:
            with open(voice, 'r') as file:
                base64str = file.read().replace('\n', '')
                decode_bytes = base64.to_bytes(base64str)
                assert isinstance(decode_bytes,io.BytesIO)

if __name__ == "__main__":
    unittest.main()
