# Calculate the mass deposited on Anode Surface
# 30 Jun 2022
# Madison Morey
import numpy as np
import pandas as pd

job = 'BareCu_1.0D_6039113'
fname = '/projectnb/ryanlab/mmorey/LAMMPS_NUCLEATION/VALIDATION/' + job

Nfreq = 2880
totDump = 70
dumpT = 0.1 
time = 0
totAtoms = 360000
length = np.zeros((totAtoms,1),dtype=float)
Lay = 0.06
Lmax = 0.0
solid = 0
Ltemp = 0

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

##Create array to hold mass and time mass 
##Mass is in index 6 of dump file
##Assumes fluid mass is 0

data = np.zeros((totDump,3),dtype=float)

#loop through totDumps that start at 0

for i in range(0,totDump):
    data[i,1] = time
    time = time + dumpT
    num = i*Nfreq
    fid = fname + "/dump." + str(num) + ".dat"
    d = np.loadtxt(fid, skiprows=9, usecols=8)
    data[i,0] = np.sum(d)
    typ = np.loadtxt(fid, skiprows=9, usecols=1)
    y = np.loadtxt(fid, skiprows=9, usecols=3)
    for j in range(0,totAtoms):
        if int(typ[j]) == int(2):
            Ltemp = y[j]
            length[j] = y[j]
            solid = 1 + solid
            if (Ltemp > Lmax):
                Lmax = Ltemp
    data[i,2] = round((Lmax - Lay),5)
    print(i)

#Save mass, time, and length data to csv
Data = pd.DataFrame(data)
Data.to_csv('BareCu_1.0D_6039113.csv',index=False)


    
 
