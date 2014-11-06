##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house
square = drawpad.create_rectangle(300,250,500,400, fill='red')
line = drawpad.create_line(300,250,400,200)
line = drawpad.create_line(400,200,500,250,)
square = drawpad.create_rectangle(320,300,350,330, fill ='cyan')
square = drawpad.create_rectangle(450,300,480,330, fill ='cyan')
square = drawpad.create_rectangle(390,350,430,400, fill ='green')
oval = drawpad.create_oval(390, 370, 400, 380, fill='blue')
line = drawpad.create_line(450,170,450,227)
line = drawpad.create_line(450,170,480,170)
line = drawpad.create_line(480,170,480,240)




root.mainloop()
