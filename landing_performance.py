import math
import numpy as np
import matplotlib.pyplot as plt


wing_loading=np.linspace(2000,5000,8)
acceleration_due_to_gravity=9.8
density=1.225
Clmax=2.26
coefficient_friction=0.4
flap_deflection=4.525*(10**-5)
mass=67400
height_above_the_ground=3.79
wingspan=35.86
n=1.19 #load_factor
cd0=0.015
k1=0.02
aspect_ratio=5.92
Cl=0.1
E=0.9
N=1
area_of_wing=122.6
hf=15
maximum_flap_deflection=3.16*(10**-5)
approach_angle=3


def velocity_stall(wing_loading,density,CLmax):
    return math.sqrt((2*wing_loading)/(density*CLmax))

def Range_of_Aircraft(V_f):
    return (V_f**2)/(0.2*32.2)

def h_f(r,approach_angle):
    return r*(1-math.cos(math.radians(approach_angle)))

def s_a(approach_angle,h_f):
    return (50-h_f)/math.tan(math.radians(approach_angle))


def s_f(Range,approach_angle):
    return Range*math.sin(math.radians(approach_angle))

def J_T(TR_W,coefficient_friction):
    return (TR_W+coefficient_friction)

def delCd0_1(max_Flap_deflection,Wing_loading,Flap_Deflection,m):
    return (max_Flap_deflection/flap_deflection)*Wing_loading*Flap_Deflection*(m**-0.215)

def induced_drag(hieght_above_ground,wingspan):
    return ((16*hieght_above_ground/wingspan)**2)/(1+(16*hieght_above_ground/wingspan)**2)

def A_Compenent(density,wing_loading,Cd0,delCd0,k1,G,AR,E,Cl,coefficient_of_friction):
    a=density/(2*wing_loading)
    b=((Cd0+delCd0+(k1+(G/(math.pi*E*AR)))*Cl**2))
    c=(coefficient_of_friction*Cl)
    return -(a*(b-c))

def ground_roll(A_component,KT,N,Vtd):
    V=1/(2*acceleration_due_to_gravity*A_component)
    B=math.log(1+((A_component/KT)*(Vtd)**2))
    C=(N*Vtd)
    return  (V*B)+C

def TLD(sa,sf,sg):
    return sa+sf+sg

def loadfactor(cl,density,vtd,area,Mass):
    return (0.5*cl*density*area*vtd**2)/(Mass*acceleration_due_to_gravity)
    
output=[]
for loading in wing_loading:
    V_stall=(velocity_stall(loading,density,Clmax))
    delCd0=delCd0_1(maximum_flap_deflection,loading,flap_deflection,mass)
    G=induced_drag(height_above_the_ground,wingspan)
    V_Td=1.15*V_stall
    JT=J_T(0,coefficient_friction)
    A=(A_Compenent(density,loading,cd0,delCd0,k1,G,aspect_ratio,E,Cl,coefficient_friction))
    Vf=V_stall*1.23
    Range=Range_of_Aircraft(Vf)
    hf=h_f(Range,approach_angle)
    ground_roll1=ground_roll(A,JT,N,V_Td)
    sa=s_a(approach_angle,hf)
    sf=s_f(Range,approach_angle)
    ld=ground_roll1+sa+sf
    output.append(ld)

plt.plot(wing_loadings,output,"ro")
plt.xlabel("Wing_loading (N/m^2)")
plt.ylabel("Landing distance (m)")
plt.title("Wing_loading v/s Landing Distance")
plt.show()