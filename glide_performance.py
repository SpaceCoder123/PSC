import math

# consider 2000m altitude 
acceleration_due_to_gravity=9.81
no_of_engines=2
mass_of_Aircraft_in_Kg=67400
true_airspeed=150
Reference_Area=122.6
density_at_altitude=0.9560
density_ratio=0.7376
Ostwald_Efficiency_Factor=0.9
aspect_ratio=5.92
Cd0=0.020
m=0.96
true_mach=0.5
span=34.10
area_of_wing=122.6
Clmax=2.26
wingloading=6000


def lift(Cl,density,reference_area,Velocity):
    return Cl*0.5*density*reference_area*Velocity**2

def drag(density_at_altitude,cd,reference_Area,True_Airspeed):
    return 0.5*density_at_altitude*(True_Airspeed**2)*cd*reference_Area

def lift_coefficient(wing_loading,density_at_altitude,True_Airspeed):
    return (2*wing_loading)/(density_at_altitude*(True_Airspeed**2))

def drag_coefficient(Coefficient_of_Drag_Zero_lift,Cl,Aspect_Ratio,Ostwald_Efficiency_Factor):
    return Coefficient_of_Drag_Zero_lift+((Cl**2)/(Aspect_Ratio*Ostwald_Efficiency_Factor*math.pi))

def k(aspect_ratio,ostwald_efficiency_factor):
    return 1/(math.pi*ostwald_efficiency_factor*aspect_ratio)


def drag(density_at_altitude,cd,reference_Area,True_Airspeed):
    return 0.5*density_at_altitude*(True_Airspeed**2)*cd*reference_Area

def sink_rate(DL,mass_of_aircraft,Cl,density,area,glide_angle):
    return -math.sqrt((2*mass_of_Aircraft_in_Kg*acceleration_due_to_gravity*math.cos(glide_angle))/Cl*density*area)*math.cos(glide_angle)*(DL)

# for maximum range glide condition 
K=k(aspect_ratio,Ostwald_Efficiency_Factor)
Cl=lift_coefficient(wingloading,density_at_altitude,true_airspeed)
Lift=lift(Cl,density_at_altitude,area_of_wing,true_airspeed)
Cd= drag_coefficient(Cd0,Cl,aspect_ratio,Ostwald_Efficiency_Factor)
Drag=drag(density_at_altitude,Cd,Reference_Area,true_airspeed)

LD=(Lift/Drag)
glide_angle=(math.atan(1/LD)*57.68)
print(glide_angle)
ClmR=math.sqrt((3*Cd0)/K)
Velocity_MR= math.sqrt(wingloading/(density_at_altitude*ClmR))
print(LD)
sink_rate=Velocity_MR*math.sin(math.radians(-glide_angle))
print(sink_rate)
glide_range=(LD*10000)
print(glide_range)