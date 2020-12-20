import numpy as np
import matplotlib.pyplot as plt

acceleration_due_to_gravity=9.8
density=1.225
Clmax=2.26
# thrust_weight=0.5
coefficient_friction=0.04
flap_deflection=4.525*(10**-5)
mass=67400
height_above_the_ground=3.79
wingspan=75
n=2.3 #load_factor
cd0=0.02
k1=0.02
aspect_ratio=5.92
Cl=0.1
E=0.9
N=1
hf=35

import math
def velocity_stall(wing_loading,density,CLmax):
    return math.sqrt((2*wing_loading)/(density*CLmax))

def KT(Thrust_wieght,coefficient_of_friction):
    return (Thrust_wieght-coefficient_of_friction)

def delCd0_1(Wing_loading,Flap_Deflection,m):
    return Wing_loading*Flap_Deflection*(m**-0.215)

def induced_drag(hieght_above_ground,wingspan):
    return ((16*hieght_above_ground/wingspan)**2)/(1+(16*hieght_above_ground/wingspan)**2)

def A_Compenent(density,wing_loading,Cd0,delCd0,k1,G,AR,E,Cl,coefficient_of_friction):
    return -density/(2*wing_loading)*(Cd0+delCd0+(k1+(G/(math.pi*E*AR)))*Cl**2-(coefficient_of_friction*Cl))

def ground_roll(A_component,KT,N,Vlo):
    V=1/(2*acceleration_due_to_gravity*A_component)
    B=math.log(1+((A_component/KT)*(Vlo**2)))
    C=(N*Vlo)
    return (V*B)+C

def Range_of_Aircraft(V_stall,g,n):
    return ((1.15*V_stall)**2)/(g*(n-1))

def theta(Hob,Range):
    return math.acos(1-(Hob/Range))*57.68

def rotation_phase(Range,theta):
    return Range*math.sin(theta/57.68)

TTL=[]
Wingloading=np.linspace(4000,7000,10)
T_W=np.linspace(0.3,0.31,10)

for loading,tw in zip(Wingloading,T_W):
    v_stall=velocity_stall(loading,density,Clmax)
    V_Lift_off=velocity_stall(loading,density,Clmax)*1.1
    KT1=(KT(tw,coefficient_friction))
    delCd0=(delCd0_1(loading,flap_deflection,mass))
    G=induced_drag(height_above_the_ground,wingspan)
    A=(A_Compenent(density,loading,cd0,delCd0,k1,G,aspect_ratio,E,Cl,coefficient_friction))
    ground_roll1=ground_roll(A,KT1,N,V_Lift_off)
    range_1=Range_of_Aircraft(v_stall,acceleration_due_to_gravity,n)
    theta_ob=(theta(hf,range_1))
    rotation_phase1=rotation_phase(range_1,theta_ob)
    total_takeoff_length=ground_roll1+rotation_phase1
    TTL.append(total_takeoff_length)

print(TTL)
plt.plot(Wingloading,TTL)
plt.xlabel("Wing_Loading")
plt.ylabel("Total Takeoff distance")
plt.show()