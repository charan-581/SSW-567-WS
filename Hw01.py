#Partial Code Reference 
import unittest

def classifyTriangle(a, b, c):
    if not (a + b > c and b + c > a and a + c > b):
        return 'NotATriangle'
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        return 'Right'
    elif a == b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isoceles'
    else:
        return 'Scalene'

def runClassifyTriangle(a, b, c):
    print('classifyTriangle(', a, ',', b, ',', c, ')=', classifyTriangle(a, b, c), sep="")

class TestTriangles(unittest.TestCase):
    def testSet1(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testSet2(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10, 10, 10), 'Isoceles', 'Should be Equilateral')
        self.assertEqual(classifyTriangle(10, 15, 30), 'Scalene', 'Should be Scalene')

if __name__ == '__main__':
    runClassifyTriangle(4, 5, 6)
    runClassifyTriangle(1, 1, 1)
    runClassifyTriangle(3, 6, 2)
    unittest.main(exit=False)
