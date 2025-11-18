import unittest
import placar

class TestPlacarMCDC(unittest.TestCase):
    
    def setUp(self):
        self.p1 = placar.Placar()
    
    def test_checkFull_mcdc_combinacao_1(self):
        self.assertFalse(self.p1.checkFull([1,1,1,2,3]))
    
    def test_checkFull_mcdc_combinacao_2(self):
        self.assertFalse(self.p1.checkFull([2,2,2,3,4]))
    
    def test_checkFull_mcdc_combinacao_3(self):
        self.assertFalse(self.p1.checkFull([1,1,2,3,3]))
    
    def test_checkFull_mcdc_combinacao_4(self):
        self.assertFalse(self.p1.checkFull([1,2,2,3,3]))
    
    def test_checkFull_mcdc_combinacao_5(self):
        self.assertTrue(self.p1.checkFull([2,2,2,4,4]))
    
    def test_checkFull_mcdc_combinacao_6(self):
        self.assertTrue(self.p1.checkFull([1,1,1,1,1]))
    
    def test_checkSeqMaior_mcdc_combinacao_1(self):
        self.assertFalse(self.p1.checkSeqMaior([1,2,3,4,6]))
    
    def test_checkSeqMaior_mcdc_combinacao_2(self):
        self.assertFalse(self.p1.checkSeqMaior([1,2,3,5,6]))
    
    def test_checkSeqMaior_mcdc_combinacao_3(self):
        self.assertFalse(self.p1.checkSeqMaior([1,2,4,5,6]))
    
    def test_checkSeqMaior_mcdc_combinacao_4(self):
        self.assertFalse(self.p1.checkSeqMaior([1,3,4,5,6]))
    
    def test_checkQuadra_mcdc_combinacao_1(self):
        self.assertFalse(self.p1.checkQuadra([1,1,1,2,2]))
    
    def test_checkQuadra_mcdc_combinacao_2(self):
        self.assertFalse(self.p1.checkQuadra([2,2,2,3,4]))
    
    def test_checkQuadra_mcdc_combinacao_3(self):
        self.assertFalse(self.p1.checkQuadra([3,3,3,4,5]))
    
    def test_checkQuadra_mcdc_combinacao_4(self):
        self.assertFalse(self.p1.checkQuadra([1,2,3,3,3]))
    
    def test_checkQuadra_mcdc_combinacao_5(self):
        self.assertTrue(self.p1.checkQuadra([1,2,2,2,2]))
    
    def test_checkQuadra_mcdc_combinacao_6(self):
        self.assertTrue(self.p1.checkQuadra([3,3,3,3,4]))
    
    def test_checkQuadra_mcdc_combinacao_7(self):
        self.assertTrue(self.p1.checkQuadra([5,5,5,5,5]))
    
    def test_checkQuina_mcdc_combinacao_1(self):
        self.assertFalse(self.p1.checkQuina([1,1,1,1,2]))
    
    def test_checkQuina_mcdc_combinacao_2(self):
        self.assertFalse(self.p1.checkQuina([2,2,2,3,3]))
    
    def test_checkQuina_mcdc_combinacao_3(self):
        self.assertFalse(self.p1.checkQuina([3,3,4,4,4]))
    
    def test_checkQuina_mcdc_combinacao_4(self):
        self.assertFalse(self.p1.checkQuina([4,5,5,5,5]))
