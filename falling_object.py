"""
Andrew Wetzel
Physics Solver
Falling Object
5/13/20
"""

def time_characteristics(time):
	print("Height at time = " + str(time) + " is " + str(time_height) + " m.")
	print("Velocty at time = " + str(time) + " is " + str(time_velocity) + " m/s.")
	print("Acceleration at time = " + str(time) + " is " + str(time_acceleration) + " m/s\u00b2.")


#Variables
final_acceleration = final_veloctiy = final_height = None
time_acceleration = time_velocity = time_height = None
initial_accleration = initial_velocity = initial_height = None

initial_height = float(input("Enter initial height (greater than 0): "))
initial_velocity = float(input("Enter initial velocity: "))
initial_accleration = float(input("Enter acceleration due to gravity (greater than 0): "))


