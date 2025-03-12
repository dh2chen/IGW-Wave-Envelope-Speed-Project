import get_igw_energy_data 

import numpy as np
import sys
import matplotlib.pyplot as plt

energy_files_dir = "../base_f0"


def plot_igw_energy(igw_energy_data):
    period = 44712.0

    time1 = igw_energy_data["time1"]/period
    tstart = 0
    tend = 10
    num_xticks = 10
    num_xminor = 5
    
    N = 1.0
    U0 = 0.03
    h0 = 0.5
#    scale = 1.0e5
    scale = 1.0
    print('max(dedt) = ',max(igw_energy_data["dEdt1"]))
    print('min(dedt) = ',min(igw_energy_data["dEdt1"]))
    print('max(bwork1) = ',max(igw_energy_data["bwork1"]))
    
    APE1 = scale*igw_energy_data["APE1"]
    dEdt1 = scale*igw_energy_data["dEdt1"]
    KE1 = scale *igw_energy_data["KE1"]
    E1 = scale*igw_energy_data["E1"]
    bwork1 = scale*igw_energy_data["bwork1"]
    Efl1 = scale*igw_energy_data["Efl1"]
    Efr1 = scale*igw_energy_data["Efr1"]
    KEfl1 = scale*igw_energy_data["KEfl1"]
    KEfr1 = scale*igw_energy_data["KEfr1"]
    APEfl1 = scale*igw_energy_data["APEfl1"]
    APEfr1 = scale*igw_energy_data["APEfr1"]

    Ef1_net = Efl1-Efr1
    KEf1_net = KEfl1-KEfr1
    APEf1_net = APEfl1-APEfr1

    print('max(Ef1_net) = ',max(Ef1_net))
    print('min(Ef1_net) = ',min(Ef1_net))
    
    zero = np.zeros(len(dEdt1))
    
    fig = plt.figure(figsize=(8, 10), dpi=80)

###### PANEL 1 ########
    ybot = -3.0
    ytop = 3.0
    
    fig.add_subplot(4, 1, 1)
    plt.plot(time1, dEdt1, '-k', label=r'$\frac{dE}{dt}$', lw=1)
    plt.xlim([tstart, tend])
    plt.ylim([ybot, ytop])
    
    plt.plot(time1, Ef1_net, '-.b', label=r'$Ef1_{net}$', lw=1)
#    plt.plot(time1, KEf1_net, '-.r', label=r'$KEf1_{net}$', lw=1)
    plt.plot(time1, zero,'-k', lw=0.2)
    plt.xlabel(r'$t$', fontsize=14)
    plt.ylabel(r'Flux, $dE/dt$', fontsize=14)
    
    
    plt.grid()
    plt.legend()
#     plt.savefig('Graph1.svg', format="svg")
#     panel1 = plt.show()

###### PANEL 2 ########

    ybot = -1.0
    ytop = 1.0
    
    print('max(dEdt1-Ef1_net) = ',max(dEdt1-Ef1_net))
    print('min(dEdt1-Ef1_net) = ',min(dEdt1-Ef1_net))
    print('max(APEf1_net) = ',max(APEf1_net))
    print('min(APEf1_net) = ',min(APEf1_net))
    print('max(KEf1_net) = ',max(KEf1_net))
    print('min(KEf1_net) = ',min(KEf1_net))

    fig.add_subplot(4, 1, 2)
    plt.plot(time1, dEdt1-Ef1_net, '-k', label=r'$\frac{dE}{dt}-Ef1_{net}$', lw=1)
    plt.xlim([tstart,tend])
    plt.ylim([ybot,ytop])
    
    plt.plot(time1,APEf1_net, '-.b', label=r'$APEf1_{net}$', lw=1)
    plt.plot(time1,KEf1_net, '-.r', label=r'$KEf1_{net}$', lw=1)
    plt.plot(time1,zero,'-k', lw=0.2)
    plt.xlabel(r'$t$', fontsize=14)
    plt.ylabel(r'Flux, $dE/dt$', fontsize=14)

    plt.grid()
    plt.legend(loc = "upper right")
#     plt.savefig('Graph2.svg', format="svg")
#     panel2 = plt.show()

###### PANEL 3 ########

    ybot = -1.0
    ytop = 1.0
    
    fig.add_subplot(4, 1, 3)
    plt.plot(time1, dEdt1 - KEf1_net - Ef1_net, '-k', label=r'$\frac{dE}{dt}-KEf1_{net}-Ef1_{net}$', lw=1)
    plt.xlim([tstart,tend])
    plt.ylim([ybot,ytop])
    
    plt.plot(time1,APEf1_net, '-.r', label=r'$APEf1_{net}$', lw=0.5)
    plt.plot(time1,zero,'-k', lw=0.2)
    plt.xlabel(r'$t$', fontsize=14)
    plt.ylabel(r'Flux, $dE/dt$', fontsize=14)

    plt.grid()
    plt.legend(loc = "upper right")
#     plt.savefig('Graph3.svg', format="svg")
#     panel3 = plt.show()
    
###### PANEL 4 ########

    ybot = -1
    ytop = 1
    
    fig.add_subplot(4, 1, 4)
    plt.plot(time1, 1.000*(dEdt1 - Ef1_net - KEf1_net - APEf1_net), '-k', label=r'$\frac{dE}{dt}-Ef1_{net}-KEf1_{net}-APEf1_{net}$', lw=1)
    plt.xlim([tstart,tend])
    plt.ylim([ybot,ytop])
    
#    plt.plot(time1,dEdt1, '-.r', label=r'$\frac{dE}{dt}$', lw=0.4)
    plt.plot(time1,zero,'-k', lw=0.2)
    plt.xlabel(r'$t$', fontsize=14)
    plt.ylabel(r'Flux, $dE/dt$', fontsize=14)

    plt.grid()
    plt.legend(loc = "lower right")
#     plt.savefig('Graph4.svg', format="svg")
#     panel4 = plt.show()
    plt.savefig('energy_balance.svg', format="svg")
#    plt.savefig('energy_balance.eps', format="eps")
    plt.savefig('energy_balance.png')
#    plt.show()

#checks
    return



igw_energy_data = get_igw_energy_data.get_igw_energy_data(energy_files_dir, 3 ,4)

plot_igw_energy(igw_energy_data)


