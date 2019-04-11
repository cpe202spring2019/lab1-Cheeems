import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """tested if the list is None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
    
    def test_max_1(self):
        """test if list is empty and returns None"""
        self.assertEqual(max_list_iter([]), None)

    def test_max_2(self):
        """tests a list with values in it and returns correct"""
        self.assertEqual(max_list_iter([1, 1, 1, 5, 2]), 5)
        self.assertEqual(max_list_iter([1, 1, 1, 1, 1]), 1)
        self.assertEqual(max_list_iter([1, 1, 1, 2, 2]), 2)


    def test_reverse_rec(self):
        """test a list with values in it"""
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,5,1,3]),[3,1,5,1])
        self.assertEqual(reverse_rec([1,10,10,19,3]),[3,19,10,10,1])
        self.assertEqual(reverse_rec([1]),[1]) 
        self.assertEqual(reverse_rec([]),[])  

    
    def test_revrec_1(self):
        """test if list is None"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)                                          

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

    def test_bin1(self):
        """ test mid > target """
        list_val = [1, 2, 4, 5, 6, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(2, 0, len(list_val)-1, list_val), 1 )

    def test_bin2(self):
        """ test mid < target """              
        list_val = [1, 2, 4, 5, 6, 7, 8, 9, 10]
        low = 0                 
        high = len(list_val) - 1                                         
        self.assertEqual(bin_search(8, 0, len(list_val)-1, list_val), 6 )

    def test_bin3(self):
        """ test list is None """              
        list_val = None
        low = 0                 
        high = 0                                   
        with self.assertRaises(ValueError):
            bin_search(2, 0, 0, list_val)

    def test_bin4(self):
        """ test mid > target """              
        list_val = []
        low = 0                 
        high = len(list_val) - 1                                         
        self.assertEqual(bin_search(2, 0, len(list_val)-1, list_val), None )

    def test_bin5(self):
        """ test mid == target """              
        list_val = [1, 2, 4, 5, 6, 7, 8, 9, 10]
        low = 0                 
        high = len(list_val) - 1                                         
        self.assertEqual(bin_search(6, 0, len(list_val)-1, list_val), 4 )


    def test_bin6(self):
        """ test mid < target """
        list_val = [1, 2, 4, 5, 6, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8)
    
    def test_bin7(self):
        """ test mid < target """
        list_val = [1, 2, 4, 5, 6, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(3, 0, len(list_val)-1, list_val), None)

if __name__ == "__main__":
        unittest.main()

    
