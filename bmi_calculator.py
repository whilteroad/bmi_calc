
import json

class BMI:
    data = dict
    bmi_calculated = []
    
    def json_read(self,inp_file):
        self.data = json.load(inp_file)
    
    def calculate_bmi(self,data):
        self.data = data
        calculate_bmi()

    def calculate_bmi(self):
     
        for row in self.data :
            new_dict = {}

            height = row.get('HeightCm',NotImplemented)
            weight = row.get('WeightKg',NotImplemented)
            gender = row.get('Gender',NotImplemented)
            bmi = weight * 10000 / (height * height)  # multiplying with 10000 because of conversion from cm to meters
            bmi = round(bmi,1)   # rounding decimal to 1 digit
            bmi_category = '' 
            health_risk = ''

            if 0 <= bmi < 18.5:
                bmi_category = 'UnderWeight'
                health_risk = 'MalnutritionRisk'
            elif 18.5 <= bmi < 25 :
                bmi_category = 'NormalWeight'
                health_risk = 'LowRisk'
            elif 25 <= bmi < 30  :
                bmi_category = 'OverWeight'
                health_risk = 'EnhancedRisk'
            elif 30 <= bmi < 35 :
                bmi_category = 'ModeratelyObese'
                health_risk = 'MediumRisk'
            elif 35 <= bmi < 40 :
                bmi_category = 'SeverlyObese'
                health_risk = 'HighRisk'
            else :
                bmi_category = 'VerySeverlyObese'
                health_risk = 'VeryHighRisk'
            
            new_dict['HeightCm'] = height
            new_dict['WeightKg'] = weight
            new_dict['Gender'] = gender
            new_dict['BMI'] = bmi
            new_dict['BMICategory'] = bmi_category
            new_dict['HealthRisk'] = health_risk
            self.bmi_calculated.append(new_dict.copy())

        return self.bmi_calculated
        
    def json_write(self) :
        file_out = open('output.json','w')
        json.dump(self.bmi_calculated,file_out)
        

if __name__ == "__main__":

    bmi_obj = BMI()
    inp_file = open('data.json')

    bmi_obj.json_read(inp_file)
    bmi_obj.calculate_bmi()
    bmi_obj.json_write()







