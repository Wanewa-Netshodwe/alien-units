import unittest
from units import convert

class TestUnits(unittest.TestCase):
    def test_three_units(self):
        ratios = {
            ("gleep", "glorp"): 3, # 3 gleeps = 1 glorp
            ("shneep", "glorp"): 60, # 60 shneeps = 1 glorp
        }

        # 2 gleeps = 40 shneeps
        self.assertEqual(convert(ratios, "gleep", "shneep", 2), 40)


    def test_any_units(self):
        ratios = {
            ("for_real", "thats_wild"): 5, # 5 for_real = 1 thats_wild
            ("thats_wild","no_cap"): 10, # 10 thats_wild = 1 thats_wild
            ("no_cap", "true"): 20,# 20 no_cap = 1 true
        }

        self.assertEqual(convert(ratios,"for_real",'true',1000),1)
        self.assertEqual(convert(ratios,"for_real",'no_cap',150),3)

    def test_impossible(self):
        ratios = {
            ("gleep", "glorp"): 3, # 3 gleeps = 1 glorp
             ("glarg", "toriver"): 70,
           
        }

        # It's impossible to convert gleeps to torivers
        self.assertIsNone(convert(ratios, "gleep", "toriver", 1))

    def test_trivial(self):
        ratios = {
            ("gleep", "glorp"): 3, # 3 gleeps = 1 glorp
        }
        # 6 gleeps = 2 glorps
        self.assertEqual(convert(ratios, "gleep", "glorp", 6), 2)

    def test_trivial_backwards(self):
        ratios = {
            ("gleep", "glorp"): 3, # 3 gleeps = 1 glorp
        }

        # 2 glorps = 6 gleeps
        self.assertEqual(convert(ratios, "glorp", "gleep", 2), 6)

if __name__ == '__main__':
    unittest.main()
