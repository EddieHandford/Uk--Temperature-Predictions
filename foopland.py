# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 08:55:22 2019
@author: ED
"""
import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt;

from netCDF4 import Dataset
nc = Dataset('foop.nc' , 'r')



########################### Edit Here ###############################
Title = 'Yorkshire & Humber'
lat = 10
long = 16




#####################################################################





for i in nc.variables:
    print(i)
    
    
tas = nc.variables['tas'][:]

latitude_longitude = nc.variables['latitude_longitude'][:]
ensemble_member = nc.variables['ensemble_member'][:]
time = nc.variables['time'][:]
latitude = nc.variables['latitude'][:]
latitude_bnds = nc.variables['latitude_bnds'][:]
longitude = nc.variables['longitude'][:]
longitude_bnds = nc.variables['longitude_bnds'][:]
ensemble_member_id = nc.variables['ensemble_member_id'][:]
month_number = nc.variables['month_number'][:]
year = nc.variables['year'][:]
yyyymms = nc.variables['yyyymm'][:]

print(tas[0 , 0 ,0 ,0 ])
shuffle_tas = tas[0,:]
shuffle_tas_np = np.array(shuffle_tas)
latitude_np = np.array(latitude[:])
latitude_bnds_np = np.array(latitude_bnds[:])
longitude_np = np.array(longitude[:])
longitude_bnds_np = np.array(longitude_bnds[:])
month_number_np = np.array(month_number[:])
year_np = np.array(year[:])
date_np = np.array([year[:] , month_number[:]])
date_np = np.rot90(date_np)
date_np = np.rot90(date_np)
date_np = np.rot90(date_np)
land_panda = pd.DataFrame({'year':year_np[: ] , 'month':month_number_np[:]})
search_year=['1999']
search_month = ['10']
found_year = land_panda.loc[land_panda['year'].isin(search_year)]
found_year_month = found_year = found_year.loc[found_year['month'].isin(search_month)]
desired_date_index = found_year_month.index[0]
testerino  = shuffle_tas_np[desired_date_index , : , :]
viewing = shuffle_tas_np[desired_date_index , : , :]
coor_sat = (np.where(viewing<10))
foo = (coor_sat[0])
foofoo = (coor_sat[1])
invest_coor = np.stack((foo, foofoo))
invest_coor = np.rot90(invest_coor)
invest_coor = np.rot90(invest_coor)
invest_coor = np.rot90(invest_coor)



print(shuffle_tas[0 , 14 , 14])


result = []
for i in range (2400):
    foopp = shuffle_tas[i,lat,long]
    result.append(foopp)
                  
output_panda = pd.DataFrame({'year':year , 'month_number':month_number , 'temperature':result})
#
#
output_panda.to_csv(Title)
                   