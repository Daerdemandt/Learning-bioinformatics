#!/usr/bin/env python3

import unittest
import Solution


class Test(unittest.TestCase):

    def setUp(self):
        self.dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
        self.result = "20 12 17 21"

    def testsolution(self):
        self.assertEqual(Solution.solution(self.dna), self.result)

    def testempty(self):
        self.assertEqual(Solution.solution(""), str("0 0 0 0"))

    def testorder(self):
        self.assertEqual(Solution.solution("AAAAAAA"), str("7 0 0 0"))
        self.assertEqual(Solution.solution("CCCCCCC"), str("0 7 0 0"))
        self.assertEqual(Solution.solution("GGGGGGG"), str("0 0 7 0"))
        self.assertEqual(Solution.solution("TTTTTTT"), str("0 0 0 7"))

    def tearDown(self):
        del self.dna
        del self.result


if __name__ == "__main__":
    unittest.main()
