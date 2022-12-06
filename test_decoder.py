import io
import unittest

from decoder import decode, trivial_encoding


class TestStringMethods(unittest.TestCase):

    def test_decode(self):
        bytes_str = bytes([0x0, 0x61, 0x1, 0x1, 0x0, 0x62, 0x3, 0x2, 0x3, 0x3])
        result = decode(io.BytesIO(bytes_str))

        self.assertEqual(result, [97, 97, 98, 97, 97, 98, 97, 97])
        self.assertEqual(bytes(result), b'aabaabaa')

    def test_trivial_encoding(self):
        result = trivial_encoding([97, 97, 98, 97, 97, 98, 97, 97])

        self.assertEqual(result, b'\x00a\x00a\x00b\x00a\x00a\x00b\x00a\x00a')


if __name__ == '__main__':
    unittest.main()
