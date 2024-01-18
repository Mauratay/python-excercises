"""
1l/100km  = liters consumed per 100km 
mpg = miles travelled per gallon
1l/100km means liters per km, which is mpg backwards => gpm would be the equivalent

mile = 1.609344 #km
gallon = 3.785411784 #litres

so since it's backwards. 

gallon/mile 
that's equivalent to 1km
we need 100
(gallon/mile)*100
so 
1l/100km = [(gallon/mile)*100]/mpg
mpg = [(gallon/mile)*100] / 1l/100km

for simplicity 1l/100km = lpkm

lpkm = ((gallon/mile)*100)/mpg
mpg = ((gallon/mile)*100) /lpkm

"""

mile = 1.609344 #km
gallon = 3.785411784 #liters


def liters_100km_to_miles_gallon(liters):
    return ((gallon / mile) * 100) / liters

def miles_gallon_to_liters_100km(miles):
    return ((gallon / mile) * 100) / miles

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
