import math
import numpy as np
import matplotlib.pyplot as plt

acceleration_due_to_gravity=9.81
no_of_engines=2
mass_of_Aircraft_in_Kg=67400
true_airspeed=170
Reference_Area=122.6
density_at_altitude=1.1560
density_ratio=0.9436
Ostwald_Efficiency_Factor=0.9

Cd0=0.020
true_mach=0.5
span=34.10
aspect_ratio=5.92
Clmax=2.26
area_of_wing=122.6


def k(aspect_ratio,ostwald_efficiency_factor):
    return 1/(math.pi*ostwald_efficiency_factor*aspect_ratio)

def load_factor(Lift,weight):
    return Lift/weight

def lift(Cl,density,reference_area,Velocity):
    return Cl*0.5*density*reference_area*Velocity**2

def minimum_radius_turn(k,wing_loading,density,T_W,Cd0):
    return ((4*k*wing_loading)/(acceleration_due_to_gravity*density *T_W))*math.sqrt((1-4*k*Cd0)/T_W**2)


def drag_coefficient(Coefficient_of_Drag_Zero_lift,Cl,Aspect_Ratio,Ostwald_Efficiency_Factor):
    return Coefficient_of_Drag_Zero_lift+((Cl**2)/(Aspect_Ratio*Ostwald_Efficiency_Factor*math.pi))


def drag(density_at_altitude,cd,reference_Area,True_Airspeed):
    return 0.5*density_at_altitude*(True_Airspeed**2)*cd*reference_Area

def max_turn_rate(T_W,Wind_Loading,k,Cd0,dynamic_pressure,density):
    return dynamic_pressure*math.sqrt((density/(Wind_Loading))*((T_W/(2*k))-(Cd0/k))**0.5)

def dynamic_pressure(density,velocity):
    return 0.5*density*velocity**2

def turnrate(acceleration_due_to_gravity,wing_loading,density_at_altitude,Cl,n):
    return acceleration_due_to_gravity*(math.sqrt((0.5*density_at_altitude*Cl)/wing_loading)*math.sqrt((n**2-1)/n))

def velocity(k,wing_loading,density,T_W):
    return math.sqrt((4*k*wing_loading)/(density*T_W))


# results
wing_loading=np.linspace(3000,6000,10)
T_W=np.linspace(0.3,0.31,10)

Treq=[]
Rmin_s=[]
Max_Turn_Rate=[]
for loading,tw in zip(wing_loading,T_W):
        
    Lift=lift(Clmax,density_at_altitude,area_of_wing,true_airspeed)

    Load_factor=load_factor(Lift,mass_of_Aircraft_in_Kg*acceleration_due_to_gravity)

    K=k(aspect_ratio,Ostwald_Efficiency_Factor)
    Rmin=minimum_radius_turn(K,loading,density_at_altitude,tw,Cd0)
    Rmin_s.append(Rmin)
    Vmin=velocity(K,loading,density_at_altitude,tw)
    maxTR=max_turn_rate(tw,loading,K,Cd0,0.5*density_at_altitude*Vmin,density_at_altitude)
    Max_Turn_Rate.append(maxTR)
    Cd=drag_coefficient(0.020,Clmax,aspect_ratio,Ostwald_Efficiency_Factor)
    T=drag(density_at_altitude,Cd,area_of_wing,Vmin)
    Treq.append(T)
    SusTR=max_turn_rate(tw,loading,K,Cd0,0.5*density_at_altitude*true_airspeed,density_at_altitude)


# print(maxTR)
print("Treq= ",Treq)
print("Rmin= ",Rmin_s)
print("MTR= ",Max_Turn_Rate)

print((SusTR))
print(math.degrees(Max_Turn_Rate[0]))
plt.plot(wing_loading,Max_Turn_Rate)
plt.xlabel("Wing_loading")
plt.ylabel("Maximum Turn Radius")
plt.show()

print(math.degrees(turnrate(acceleration_due_to_gravity,4000,density_at_altitude,Clmax,3)))