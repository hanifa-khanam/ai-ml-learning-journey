class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
        
    @property
    def celsius(self):
        return self.__celsius
    
    
    @celsius.setter
    def celsius(self, temperature):
        if temperature < -273.15:
            print("Temperature below absolute zero!")
        else:
            self.__celsius = temperature
            print(f"Temperature updated successfully: {self.__celsius}")
            
    @property
    def fahrenheit(self):
        return (self.__celsius * 9 / 5) + 32
       
        
    @fahrenheit.setter
    def fahrenheit(self, temperature):
        self.__celsius = (temperature - 32) * 5 / 9



        
temp = Temperature(25)
print(temp.celsius)      # 25
print(temp.fahrenheit)   # 77.0

temp.fahrenheit = 212    # Setting using Fahrenheit
print(temp.celsius)      # 100.0

temp.celsius = -300      # Invalid update
 