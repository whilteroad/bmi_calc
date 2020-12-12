import unittest
from bmi_calculator import *

def setUpModule():
    print('set up module')

def tearDownModule():
    print('tear down module')

class Test_BMI_Calc(unittest.TestCase):

    
    @classmethod
    def setUpClass(self):
        print('Set up class')
        self.calc = BMI()

    @classmethod
    def tearDownClass(self):
        print('Tear down class')

    def test_underWeight(self):
        self.calc.data=[]
        self.calc.data = [{'Gender': 'Male', 'HeightCm': 172, 'WeightKg': 22}.copy()]
        print(self.calc.calculate_bmi())
        print(self.calc.bmi_calculated[0].get('BMICategory'))
        self.assertEqual(self.calc.bmi_calculated[0].get('BMICategory'), 'UnderWeight',msg='should be under Weight')

    def test_normalWeight(self):
        self.calc.data = []
        self.calc.data = [{'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77}.copy()]
        print(self.calc.calculate_bmi())
        self.assertEqual(self.calc.bmi_calculated[0].get('BMICategory'), 'NormalWeight',msg='should be moderately obese')


    def test_overWeight(self):
        self.calc.data = []
        self.calc.data = [{'Gender': 'Male', 'HeightCm': 166    , 'WeightKg': 8}.copy()]
        self.calc.calculate_bmi()
        print(self.calc.calculate_bmi()[0].get("BMIcategory"))
        self.assertEqual(self.calc.bmi_calculated[0].get('BMICategory'), 'OverWeight',msg='should be moderately obese')

    def test_moderatelyObese(self):
        self.calc.data=[]
        self.calc.data = [{'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 85}.copy()]
        # self.calc.calculate_bmi()
        print(self.calc.calculate_bmi()[0].get("BMIcategory"))
        self.assertEqual(self.calc.bmi_calculated[0].get('BMICategory'), 'ModeratelyObese',msg='should be moderately obese')
    
    def test_severelyObese(self):
        self.calc.data = [{'Gender': 'Male', 'HeightCm': 166, 'WeightKg': 99}.copy()]
        self.calc.calculate_bmi()
        print(self.calc.calculate_bmi()[0].get("BMIcategory"))
        self.assertEqual(self.calc.bmi_calculated[0].get('BMICategory'), "SeverlyObese",msg='should be severely Obese')


    def test_verySeverelyObese(self):
        self.calc.data = []
        self.calc.data.append({'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 999999999999}.copy())
        self.calc.calculate_bmi()
        print(self.calc.calculate_bmi()[0].get("BMIcategory"))
        self.assertEqual(self.calc.calculate_bmi()[0].get("BMICategory"), 'VerySeverelyObese',msg='should be VerySeverelyObese')





if __name__ == '__main__':
    unittest.main()