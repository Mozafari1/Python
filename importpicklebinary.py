# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 22:13:10 2018

@author: m_rah
"""

import pickle  

#country =('Norway', 'Oslo', '1884',((1, 'Oslo'), (2, 'Trondheim'), (3, 'Bergen'), (4, 'Stavanger')))
#with open("country.pickle", 'wb') as pickle_file:
#    pickle.dump(country, pickle_file)
    

#with open ("country.pickle", 'rb') as country_pickled:
#    country1 = pickle.load(country_pickled)
    
#print(country1)
#countryName, Capital, Constitution, bigCites = country1
#print(countryName)
#print(Capital)
#print(Constitution)
#for cities in bigCites:
#    cityRang, cityName = cities
#    print(cityRang, cityName)
                              

country =('Norway', 'Oslo', '1884',((1, 'Oslo'), (2, 'Trondheim'), (3, 'Bergen'), (4, 'Stavanger')))

even = list(range(0,10,2))
odd = list(range(1,10,2))


with open("country.pickle", 'wb') as pickle_file:
    pickle.dump(country, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickle_file,protocol =0)
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(983484, pickle_file,protocol=pickle.DEFAULT_PROTOCOL)    

with open ("country.pickle", 'rb') as country_pickled:
    country1 = pickle.load(country_pickled)
    evenlist = pickle.load(country_pickled)
    oddlist = pickle.load(country_pickled)
    x = pickle.load(country_pickled)
    
print(country1)
countryName, Capital, Constitution, bigCities = country1
print(countryName)
print(Capital)
print(Constitution)
for cities in bigCities:
    cityRang, cityName = cities
    print(cityRang, cityName)
                              
print('- -'*4)
for i in evenlist:
    print(i)

print('_ _'*4)
for i in oddlist:
    print(i)
print('+ +' *4)
print(x)

    
  
#pickle.loads(b"cos\nsystem\n(S'del country.pickle'\ntR."   )                           