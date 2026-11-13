import unittest
def add(a,b):
  return  a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b

class TestCalculator(unittest.TestCase):
  def test_add(self):
    self.assertEqual(add(20,20),40)
  def test_subtract(self):
    self.assertEqual(subtract(30,20),10)
  def test_multiply(self):
    self.assertEqual(multiply(6,4),24)

if _name=="_main_":
  print("student calculator application")
  print("addition:",add(20,20))
  print("subtraction:",subtract(30,20))
  print("multiply:",multiply(6,4))
  print("/n executing automated test---/n")
  unittest.main(argv=["Frist-arg-is-ignored"],exit=false)
  

  
  
