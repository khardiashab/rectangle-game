"""in rectangle game there is a  recantangle with lower left cordinate or upper right cordinate
 that genrate by random numbers. And we have to guss a cordinate and the game tell us this cordinate
 falls in rectangle or not in True or False """

# import modules
from random import randint

# let's make a rectangle
lower_left = (randint(0,49), randint(0,49))  # this is lower left cordinate
# for upper right cordinate we start range from lower left + 1 because of this the both\
# side not intract themselves.
upper_right = (randint(lower_left[0]+1, 50), randint(lower_left[1]+1, 50))

# we going to give three chance to player
c = 0
while c!= 3:
    print(f"the lower left : {lower_left} and upper left : {upper_right}")
    try:  # because user input some string value then it make error
        x = float(input( 'x cordinate of the point : '))
        y = float(input( 'y cordinate of the point : '))
        if lower_left[0] < x < upper_right[0] and lower_left[1] < y < upper_right[1]:
            print(True)
        else:
            print(False)
    except :
        print('Please enter numbers not strings.')
        pass

    c += 1