import math
import numpy as np      
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


acceleration_due_to_gravity=9.81
no_of_engines=2
mass_of_Aircraft_in_Kg=67400
true_airspeed=87
Reference_Area=122.6
density_at_altitude=1.1560
density_ratio=0.9436
Ostwald_Efficiency_Factor=0.9

Cd0=0.020
m=0.96
true_mach=0.2
span=34.10

def aspect_ratio(span,area):
    return (span**2)/area
#adding functions to calculate desired values

def lift_coefficient(wing_loading,density_at_altitude,True_Airspeed):
    return (2*wing_loading)/(density_at_altitude*(True_Airspeed**2))

def drag_coefficient(Coefficient_of_Drag_Zero_lift,Cl,Aspect_Ratio,Ostwald_Efficiency_Factor):
    return Coefficient_of_Drag_Zero_lift+((Cl**2)/(Aspect_Ratio*Ostwald_Efficiency_Factor*math.pi))

def drag(density_at_altitude,cd,reference_Area,True_Airspeed):
    return 0.5*density_at_altitude*(True_Airspeed**2)*cd*reference_Area

def Thrust_At_sea_level_at_Mach(Thrust_At_Zero_Mach,Slope_of_Thrust_at_SL_vs_True_Mach,True_Mach):
    return Thrust_At_Zero_Mach-(Slope_of_Thrust_at_SL_vs_True_Mach*True_Mach)


def Thm(density_ratio,Thrust_At_sea_level_at_Mach,Thrust_Lapse_Rate):
    return Thrust_At_sea_level_at_Mach * (density_ratio**Thrust_Lapse_Rate)
  
def rate_of_climb(T_total,Drag,True_Airspeed,mass_in_kg):
    return ((T_total-Drag)*True_Airspeed)/(mass_in_kg*acceleration_due_to_gravity)
    
roc=[]
wing_loading=np.linspace(3000,7000,30)

for loading in (wing_loading):

    thrust_at_zero_mach=60000
    thrust_lapse_rate=0.2*thrust_at_zero_mach
    Cl=(lift_coefficient(loading,density_at_altitude,true_airspeed))
    AR=aspect_ratio(span,Reference_Area)
    Cd=(drag_coefficient(Cd0,Cl,AR,Ostwald_Efficiency_Factor))
    D=drag(density_at_altitude,Cd,Reference_Area,true_airspeed)

    T0m=(Thrust_At_sea_level_at_Mach(thrust_at_zero_mach,thrust_lapse_rate,true_mach))

    T_Total=Thm(density_ratio,T0m,m)*no_of_engines
    # thrust_to_Weight=(T_Total/(mass_of_Aircraft_in_Kg*acceleration_due_to_gravity))*1000
    ROC=rate_of_climb(T_Total,D,true_airspeed,mass_of_Aircraft_in_Kg)
    roc.append(ROC)
roc_np=np.array(roc)
plt.xlabel("wingloading")
plt.ylabel("ROC")
plt.plot(wing_loading,roc_np)
plt.show()