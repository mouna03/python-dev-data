import unittest
import utils
import ex1
import ex2

class TestExercice(unittest.TestCase):
    def test_exercice1(self):
        result = ex1.generer(6,1,49)
        self.assertEqual(len(result),6,"Length should be equal to 6")
        self.assertEqual(utils.is_sorted(result),True, "Should be sorted")

    def test_exercice2(self):
        tab_test1=[5,8,11,24,26,29,40,42] 
        self.assertEqual(ex2.DPMR(25,0,7,tab_test1), 4, "Index should be 4")

if __name__ == '__main__':
    unittest.main()