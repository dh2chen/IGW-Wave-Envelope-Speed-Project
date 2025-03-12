import numpy as np
import sys
import matplotlib.pyplot as plt
#import sympy as sym

# Enabling using LaTex for making labels pretty, not really necessary
#from matplotlib import rc
#rc('text', usetex=True)





def get_igw_energy_data(directory,left_flux_line,right_flux_line):
    suffix = '_lag'
#    suffix = ''
    left_flux_data_file = './'+directory+'/'+'energy_fluxes_flux_line_'+str(left_flux_line)+suffix
#     print(left_flux_data_file) #debug line
    
    right_flux_data_file = './'+directory+'/'+'energy_fluxes_flux_line_'+str(right_flux_line)+suffix
#     print(right_flux_data_file) #debug line
    
    integrated_energy_file = './'+directory+'/'+'integrated_energy_mass_LagReg'+str(left_flux_line)+'_'+str(right_flux_line)
    print(integrated_energy_file) #debug line
     
    
    work_file = './'+directory+'/'+'bottom_work_LagReg'+str(left_flux_line)+'_'+str(right_flux_line)
#     print(work_file) #debug line
    
    #load the data to left and right datasets
    left_data = np.loadtxt(left_flux_data_file)
    right_data = np.loadtxt(right_flux_data_file)
    integrated_data = np.loadtxt(integrated_energy_file)
#     print(integrated_data) #debug
    work_data = np.loadtxt(work_file)

#     print(left_data) #debug
    #We know KEfl = KEfU1l+KEfU2l+KEfU3l
    KEfl1 = left_data[:,7] #1
#     print(KEfl) #debug
    print("Done with var 1")
    
#     print(right_data) #debug
    #We know KEfr = KEfU1r+KEfU2r+KEfU3r
    KEfr1 = right_data[:,7] #2
#     print(KEfr) #debug
#     print("Done with var 2")
 
    APEfl1 = left_data[:,8] #3
#     print("Done with var 3")

    APEfr1 = right_data[:,8] #4
#     print("Done with var 4")

    APE1 = integrated_data[:,5] #5
#     print("Done with var 5")

    KE1 = integrated_data[:,6] #6
#     print("Done with var 6")

    time1 = left_data[:,0] #7
#     print("Done with var 7")

    E1 = KE1 + APE1 #8
#    E1 = APE1 #8

#     print("Done with var 8")

    bwork1 = work_data[:,1] #9
#     print("Done with var 9")

    Efl1 = left_data[:,4] #10
#     print("Done with var 10")

    Efr1 = right_data[:,4] #11
#     print("Done with var 11")

    time2 = integrated_data[:,0]

#     dEdt = sym.diff(E,time2) #12
#     print("Done with var 12")

    dEdt1 = np.gradient(E1,time2) #12
#     print("Done with var 12")

    print("done with data collection")

    igw_energy_data = {
        "time1": time1,
        "dEdt1": dEdt1,
        "bwork1": bwork1,
        "APE1": APE1,
        "KE1": KE1,
        "E1": E1,
        "Efl1": Efl1,
        "Efr1": Efr1,
        "KEfl1": KEfl1,
        "KEfr1": KEfr1,
        "APEfl1": APEfl1,
        "APEfr1": APEfr1
    }

    return igw_energy_data


