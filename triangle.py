#Python version of triangle program
import math, time

#Random Fucntions
def print_sleep(statement, pause_time):
    print(statement)
    time.sleep(pause_time)

#Intro Intstructions
def intro():
    print_sleep('Welcome to the Triangle Program', 2)
    print_sleep('Enter any 3 Triangle measurements', 1)
    print_sleep('and the program will complete the triangle for you', 2)
    print_sleep('--------------------------------------------------', 2)

#Get Input
def measurement_grab():
    measurement = []
    count = 0
    while count < 3:
        count += 1
        measurement[count-1]=input('Enter measurement ' + count).split()  #split has to do with validity
        #verify validity of measurement

def triangle(measurements):   #Seperate from input for outside program use
#Calculate Which Formula from Dataset


#Different Calculate Triangle


#Display Info



# call function
