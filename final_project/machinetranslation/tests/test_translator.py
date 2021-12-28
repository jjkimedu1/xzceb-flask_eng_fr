import unittest

from translator import englishToFrench, frenchToEnglish 

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(['Thank']), 'Merci')  # test when 'Thank' is given as input the output is 'Merci'.
        self.assertNotEqual(englishToFrench(['Bye']), 'Bonjour') # test when 'Bye' is given as input the output is 'Au revoir'.

class TestFrenchToEnglish(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(frenchToEnglish(['Merci']), 'Thank you') # test when 'Merci' is given as input the output is 'Thank you'.
        self.assertNotEqual(frenchToEnglish(['Bonjour']), 'Bye') # test when 'Bounjour' is given as input the output is 'Hello'.

unittest.main()