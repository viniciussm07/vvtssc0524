import unittest
import Placar

class TestComputaPlacar(unittest.TestCase):
    
    def setUp(self):
        self.p1 = Placar.ComputaPlacar()

    def test_calcula_placar1(self):
        self.assertEqual(self.p1.calcula_placar("00000000000000000000-"), 0)
        self.assertEqual(self.p1.calcula_placar("X-000008200000000000-"), 20)
        self.assertEqual(self.p1.calcula_placar("00800900000110000000-"), 19)

    def test_calcula_placar2(self):
        self.assertEqual(self.p1.calcula_placar("X-800900000110000000-"), 37)
        self.assertEqual(self.p1.calcula_placar("00801/50000110000000-"), 30)

if __name__ == "__main__":
    unittest.main()