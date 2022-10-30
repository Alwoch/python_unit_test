import unittest
import main

#to run test : python -m unittest test_main.py
#create test cases by creating a test class that inherits from unittest.testcase

if __name__=="__main__":
  unittest.main()
  
class TestMain(unittest.TestCase):
  def testAdd(self):
    self.assertEqual(main.add(3,7),10)
    self.assertEqual(main.add(-1,1),0)
    self.assertEqual(main.add(-1,-7),-8)

  def testSubtract(self):
    self.assertEqual(main.subtract(3,7),-4)
    self.assertEqual(main.subtract(-1,1),-2)
    self.assertEqual(main.subtract(-1,-7),6)

  def testMultiply(self):
    self.assertEqual(main.multiply(3,7),21)
    self.assertEqual(main.multiply(-1,1),-1)
    self.assertEqual(main.multiply(-1,-7),7)

  def testdivide(self):
    #self.assertRaises(ValueError,main.divide(10,0))

    #we can refactor the above code to use a context manager
    with self.assertRaises(ValueError):
      main.divide(10,0)
