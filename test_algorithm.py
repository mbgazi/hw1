import unittest
from algorithm import values_between 

class TestValuesBetween(unittest.TestCase):
 def setUp(self):
  self.array = [5,9,1,20,3,7]
 def test_EmptyArray(self):
  self.assertFalse(values_between([],1,10))
 def test_AllValuesGreater(self):
  self.assertTrue(-1,values_between(self.array,25,30))
 def test_AllValuesSmaller(self):
  self.assertFalse(values_between(self.array,-1,0))
 def test_NothingBetween(self):
  self.assertEqual(-1,values_between(self.array, 3,3))
 def test_Values(self):
  self.assertEqual([5,7], values_between (self.array,4,8))

if __name__=='__main__':
  unittest.main()
