import unittest
from concierge.chunking import chunk_text,normalize_text
class ChunkTests(unittest.TestCase):
    def test_whitespace(self):
        self.assertEqual(normalize_text(" a  b\\n c "),"a b c")
    def test_empty(self):
        self.assertEqual(chunk_text(" ","x.txt"),[])
    def test_overlap(self):
        chunks=chunk_text("one two three four five six seven","x.txt",4,2)
        self.assertEqual(len(chunks),3)
        self.assertEqual(chunks[1].text,"three four five six")
if __name__=="__main__": unittest.main()
