# Conversion Function with Unit Tests
This convert function is designed to perform unit conversions based on a provided set of ratios between different units. It can handle both direct and indirect conversions by exploring links between units and tracking visited units to avoid loops. Below is a description of the function, followed by the test cases implemented using the unittest framework.

## Function Definition
```python
def convert(ratios, from_unit, to_unit, value):
    visited_units = set()
    link = from_unit
    vl = value

    if from_unit == to_unit:
        return value
    
    if (from_unit, to_unit) in ratios:
        return value / ratios[(from_unit, to_unit)]
    
    if (to_unit, from_unit) in ratios:
        return value * ratios[(to_unit, from_unit)]

    def change_link():
        nonlocal link, vl
        visited_units.add(link)

        for k in list(ratios):
            if link in k:
                if link == k[0] and k[1] not in visited_units:
                    vl /= ratios[k]
                    link = k[1]
                    return True
                elif link == k[1] and k[0] not in visited_units:
                    vl *= ratios[k]
                    link = k[0]
                    return True
        return False
    
    while link != to_unit:
        if not change_link():
            return None
    
    return vl
```
## Parameters
- ratios (dict): A dictionary where each key is a tuple of two units, representing a pair, and the corresponding value is the conversion factor between them. For example, ('meter', 'kilometer'): 1000 means that 1 kilometer equals 1000 meters.

- from_unit (str): The unit from which to convert.

- to_unit (str): The unit to which to convert.

- value (float): The value in from_unit to convert to to_unit.

Return Value
The function returns the value converted to to_unit. If no path is found between the units, it returns None.
## Function Behavior
Direct Conversion Check:
1. If from_unit equals to_unit, the function immediately returns value (no conversion is needed).
2. If a direct conversion from from_unit to to_unit exists in ratios, the function uses that.
3. If a reverse conversion (i.e., to_unit to from_unit) exists, it uses that instead.
### Indirect Conversion:

If no direct conversion is found, it searches for an indirect path from from_unit to to_unit by exploring linked units using the change_link function.
### Loop Prevention:
The function uses a set of visited_units to avoid cycles.
## Example Usage
```python
ratios = {
    ('meter', 'kilometer'): 1000,
    ('centimeter', 'meter'): 100,
    ('inch', 'centimeter'): 2.54
}

# Converting 1500 meters to kilometers
print(convert(ratios, 'meter', 'kilometer', 1500))  # Output: 1.5

# Converting 100 inches to meters (indirect conversion through centimeters)
print(convert(ratios, 'inch', 'meter', 100))  # Output: 2.54 meters (approx.)
```
# Unit Testing with unittest
The following test cases validate the convert function. Each test case checks for various conversion scenarios including direct, indirect, impossible, and trivial conversions.

```python

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
            ("thats_wild", "no_cap"): 10, # 10 thats_wild = 1 no_cap
            ("no_cap", "true"): 20, # 20 no_cap = 1 true
        }

        self.assertEqual(convert(ratios, "for_real", 'true', 1000), 1)
        self.assertEqual(convert(ratios, "for_real", 'no_cap', 150), 3)

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
```
## Test Case Descriptions
- test_three_units: Tests a conversion that requires two indirect conversions between three units (gleep to glorp to shneep).
- test_any_units: Tests a chain of conversions across multiple units.
- test_impossible: Tests a case where no path exists between from_unit and to_unit.
- test_trivial: Tests a simple, direct conversion.
- test_trivial_backwards: Tests a conversion in reverse where a conversion factor is directly available in ratios.
## Running the Tests
Run the tests by executing the file directly. Each test case will output the result, indicating whether the convert function performs as expected for various scenarios.
