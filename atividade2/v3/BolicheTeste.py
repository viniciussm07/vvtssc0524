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

    def test_calcula_placar3(self):
        self.assertEqual(self.p1.calcula_placar("X-X-X-X-X-X-X-X-X-XXX"), 300)
        self.assertEqual(self.p1.calcula_placar("X-5/5/X-X-5/5/X-5/5/5"), 185)

    def test_decimo_frame_especiais(self):
        self.assertEqual(self.p1.calcula_placar("000000000000000000XXX"), 30)
        self.assertEqual(self.p1.calcula_placar("000000000000000000X1/"), 20)
        # não passou
        self.assertEqual(self.p1.calcula_placar("000000000000000001/X"), 20)

    def test_validacoes(self):
        with self.assertRaises(ValueError):
            self.p1.calcula_placar("")
        
        with self.assertRaises(ValueError):
            self.p1.calcula_placar("ABCDEFGHIJ")
            
        with self.assertRaises(ValueError):  
            self.p1.calcula_placar("/123456789")

        with self.assertRaises(ValueError):  
            self.p1.calcula_placar("/123456789")
        

    def test_edge_cases(self):
        self.assertEqual(self.p1.calcula_placar("90909090909090909090-"), 90)
        self.assertEqual(self.p1.calcula_placar("X-9/9/9/9/9/9/9/9/9/0"), 182)

if __name__ == "__main__":
    unittest.main()