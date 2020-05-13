"""
Andrew Wetzel
Physics Solver
Falling Object
5/13/20
"""
import math

#Prints characteristics at a specific time
def time_char():
	again = True

	while(again):

		time = float(input("Enter time to calculate characteristics for (greater than 0): "))
		if time < final_time:
			time_height = -(.5 * initial_accleration * time**2) + (initial_velocity * time) + initial_height
			time_velocity = -(initial_accleration * time) + initial_velocity
			time_acceleration = initial_accleration
		else:
			time_height = 0
			time_velocity = 0
			time_acceleration = 0

		
		print("Characteristics at time:")
		print("Height at time = " + str(time) + "s is " + str(time_height) + " m.")
		print("Velocty at time = " + str(time) + "s is " + str(time_velocity) + " m/s.")
		print("Acceleration at time = " + str(time) + "s is " + str(time_acceleration) + " m/s\u00b2.")
		print()

		again = int(input("If you would like to run again enter 1 else enter 0: ")) == 1


#Prints characterisitcs at height = 0
def final_char():
	final_acceleration = initial_accleration
	final_velocity = (initial_accleration * final_time) + initial_velocity
	print("Characterisitcs at ground:")
	print("Time to height = 0 is " + str(final_time) + " s.")
	print("Velocty at height = 0 is " + str(final_velocity) + " m/s.")
	print("Acceleration at height = 0 is " + str(final_acceleration) + " m/s\u00b2.")
	print()

#Variables
final_acceleration = final_velocity = final_height = None
time_acceleration = time_velocity = time_height = None
initial_accleration = initial_velocity = initial_height = None

#User input initial conditions
initial_height = float(input("Enter initial height (greater than 0): "))
initial_velocity = float(input("Enter initial velocity (positive is up): "))
initial_accleration = float(input("Enter acceleration due to gravity (greater than 0): "))
assert initial_height > 0, "Inital height was not greater than 0."
assert initial_accleration > 0, "Initial acceleration was not greater than 0."

#Calculate final time
final_time = (initial_velocity / initial_accleration) + math.sqrt((2 * initial_height / initial_accleration) + (initial_velocity**2)/(initial_accleration**2))

final_char()
time_char()