from turtle import *

#v1
#N = 6
#F_var = "G-F-G"
#G_var = "F+G+F"
#curr_state = "F"
#step = 2
#angle = 60

#v2
N = 5
F_var = "F-G+F+G-F"
G_var = "GG"
curr_state = "F-G-G"
step = 10
angle = 120

for i in range(N) :
    new_state = ""
    for sym in curr_state :
        if sym == "F":
            new_state += F_var
        elif sym == "G":
            new_state += G_var
        else :
            new_state += sym
    curr_state = new_state
        

color('red')
speed('fastest')
hideturtle()
pendown()
for sym in curr_state :
    if sym == "F" or sym == "G" :
        forward(step)
    elif sym == "+" :
        left(angle)
    elif sym == "-" :
        right(angle)
done()
