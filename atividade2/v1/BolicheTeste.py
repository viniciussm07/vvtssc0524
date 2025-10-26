import unittest
import Placar

class TestComputaPlacar(unittest.TestCase):
    
    def setUp(self):
        self.p1 = Placar.ComputaPlacar()

    def test_calcula_placar(self):
        self.assertEqual(self.p1.calcula_placar("00000000000000000000-"), 0)
        self.assertEqual(self.p1.calcula_placar("X-000008200000000000-"), 20)
        self.assertEqual(self.p1.calcula_placar("00800900000110000000-"), 19)

if __name__ == "__main__":
    unittest.main()