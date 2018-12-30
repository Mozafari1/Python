# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:42:36 2018

@author: m_rah
"""

#import time
#print(time.gmtime(0))
#print(time.localtime())
#print(time.time())

import pytz
import datetime
import time

country = 'Europe/Oslo'

display = pytz.timezone(country)
localtime = datetime.datetime.now(tz=display)
print("The time in {} is {}".format(country, localtime))
print("UTC is {}".format(datetime.datetime.utcnow()))
for i in pytz.all_timezones:
    print(i)

for x in sorted(pytz.country_names):
    print(x +" : "+pytz.country_names[x])

for u in sorted(pytz.country_names):
    print("{}: {}".format(u, pytz.country_names[u]),end=': ')
    if u in pytz.country_timezones:
        for s in sorted(pytz.country_timezones[u]):
            display = pytz.timezone(s)
            localtime=datetime.datetime.now(tz=display)
            
            print("\t\t{}: {}".format(s,localtime))
    else:
        print("\t\t no time zone ")
        
