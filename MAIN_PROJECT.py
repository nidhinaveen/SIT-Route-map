from tkinter import *
import turtle
import time
import datetime	
import random
import sys

root = Tk()
root.title("SIT")
root.configure(background="powderblue")



def onclick1():
	turtle.hideturtle()
	turtle.pensize(4)
	turtle.penup()
	turtle.right(90)
	turtle.forward(350)
	turtle.pendown()
	turtle.color("navy")
	turtle.write("F R O N T   G A T E")
	turtle.right(180)


	#MBA  block
	turtle.color("blue")
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(30)
	turtle.penup()
	turtle.forward(120)
	turtle.color("red")
	turtle.pendown()

	turtle.begin_fill()
	turtle.circle(5)
	turtle.end_fill()

	turtle.write("M B A   B L O C K")
	turtle.color("blue")
	turtle.penup()
	turtle.right(180)
	turtle.forward(150)
	turtle.left(90)
	turtle.pendown()

	# Kennedy Guest House
	turtle.forward(75)
	turtle.right(90)
	turtle.forward(30)
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()
	turtle.color("red")
	turtle.begin_fill()
	turtle.circle(5)
	turtle.end_fill()
	turtle.penup()
	turtle.forward(10)
	turtle.color("red")

	turtle.write("K  E  N  N  E  D  Y    G  U  E  S  T    H  O  U  S  E")
	turtle.color("blue")
	turtle.backward(60)
	turtle.left(90)
	turtle.pendown()


	turtle.forward(55)
	turtle.left(90)

	turtle.forward(30)
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()

	turtle.color("red")
	
	turtle.penup()
	turtle.forward(40)
	turtle.pendown()
	
	turtle.color("gold")
	turtle.begin_fill()
	turtle.right(60)
	turtle.forward(20)
	turtle.left(120)
	turtle.forward(20)
	turtle.right(-120)
	turtle.forward(20)
	turtle.end_fill()

	turtle.color("red")
	turtle.write("T E M P L E")
	turtle.penup()

	turtle.goto(0,0)

	turtle.done()


def onclick2():
	turtle.hideturtle()
	turtle.pensize(4)

	turtle.penup()
	turtle.right(90)
	turtle.forward(350)
	turtle.pendown()
	turtle.color("darkblue")
	turtle.penup()

	turtle.pendown()
	turtle.color("blue")
	turtle.write("   F R O N T   G A T E")
	turtle.penup()
	turtle.right(180)

	turtle.pendown()
	turtle.forward(700)
	turtle.penup()
	turtle.forward(20)
	turtle.color("red")

	turtle.write("A D M I N I S T R A T I V E   B L O C K")
	turtle.color("blue")
	turtle.right(180)
	turtle.forward(20)
	turtle.right(90)
	turtle.pendown()
	turtle.forward(60)
	turtle.left(90)
	turtle.forward(20)
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()
	turtle.color("black")
	
	turtle.begin_fill()
	turtle.color("brown")
	for i in range(1,2):
		turtle.forward(130)
		turtle.right(90)
		turtle.forward(60)
		turtle.right(90)
		turtle.forward(130)
		turtle.right(90)
		turtle.forward(60)
	turtle.end_fill()

	turtle.penup()
	turtle.left(180)
	turtle.forward(100)
	turtle.right(180)
	turtle.color("red")
	turtle.write("B A S K E T  B A L L   C O  U R T")

	turtle.done()
	
def onclick3():
	turtle.hideturtle()
	turtle.pensize(4)

	turtle.penup()
	turtle.right(90)
	turtle.forward(500)
	turtle.pendown()
	turtle.color("blue")

	turtle.write("  F R O N T    G A T E")
	turtle.right(180)
	turtle.penup()


# Infinity road
	turtle.color("blue")
	turtle.pensize(4)
	turtle.pendown()
	turtle.forward(500)
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()
	turtle.write("A D M I N I S T R A T I V E     B L O C K") 
	turtle.penup() 
	turtle.backward(20)
	turtle.pendown()
	turtle.left(90)
	turtle.forward(170)
	turtle.penup()
	turtle.forward(150)
	turtle.pendown()
	turtle.color("red")
	turtle.begin_fill()
	turtle.circle(4)
	turtle.end_fill()
		
	turtle.write("A R  C H I T E C T U R E  DEPT.\nM C A  DEPT.")
	turtle.penup()
	turtle.backward(150)
	turtle.right(90)
	turtle.color("blue")
			
	#  birla
			
	turtle.pendown()		
			
	turtle.forward(90)
	turtle.right(90)
	turtle.penup()
	turtle.forward(15)
	turtle.color("red")
	turtle.pendown()
	turtle.circle(3)
	turtle.penup()
	turtle.forward(20)
	turtle.write("B I R L A  A U D I T O R I U M")
	turtle.penup()
	turtle.backward(35)
	turtle.left(90)

	turtle.pendown()

	turtle.done()
	
	
def onclick4():
	turtle.hideturtle()
	turtle.pensize(4)

	turtle.penup()
	turtle.right(90)
	turtle.forward(500)
	turtle.pendown()
	turtle.color("blue")

	turtle.penup()
	turtle.forward(10)
	turtle.pendown()

	turtle.write("  F R O N T  G  A T E")
	turtle.right(180)
	turtle.penup()


	 # Infinity road
	turtle.color("blue")
	turtle.pensize(4)
	turtle.pendown()
	turtle.forward(500)

	#turtle.forward(20)

	turtle.penup()
	turtle.forward(20)



	turtle.write("A D M I N I S T R A T I V E   B L O C K") 
	turtle.backward(20)

	#turtle.penup()
	#turtle.backward(20)
	turtle.pendown()
	turtle.right(90)
	turtle.forward(200)
	turtle.right(90)
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()
	turtle.color("purple")
	turtle.begin_fill()
	turtle.write("K A R N A T A K A   B A N K")

	for i in range(1,2):
		turtle.forward(60)
		turtle.right(90)
		turtle.forward(100)
		turtle.right(90)
		turtle.forward(60)
		turtle.right(90)
		turtle.forward(100)
	turtle.end_fill()


	turtle.left(90)
	turtle.penup()
	turtle.forward(20)
	turtle.color("blue")
	turtle.pendown()
	turtle.right(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(30)

	turtle.penup()
	turtle.color("red")
	turtle.forward(10)
	turtle.pendown()
	turtle.circle(3)

	turtle.right(90)
	turtle.penup()
	turtle.forward(5)
	turtle.pendown()
	turtle.write("L I B R A R Y")

	turtle.penup()
	turtle.right(180)
	turtle.forward(5)
	turtle.left(90)
	turtle.forward(40)
	turtle.pendown()
	turtle.color("blue")


	turtle.left(90)
	turtle.forward(100)
	turtle.penup()
	turtle.color("red")
	turtle.forward(10)
	turtle.pendown()
	turtle.circle(3)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()

	turtle.write("C O F F E E    S H O P")
	turtle.penup()
	turtle.left(180)
	turtle.forward(20)
	turtle.right(90)
	turtle.pendown()
	turtle.color("blue")
	turtle.forward(90)

	turtle.penup()
	turtle.right(90)
	turtle.color("red")
	turtle.forward(10)
	turtle.pendown()
	turtle.circle(3)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()

	turtle.write("I E M   D  E  P  T.")

	turtle.penup()
	turtle.left(180)
	turtle.forward(20)
	turtle.right(90)
	turtle.pendown()
	turtle.color("blue")

	turtle.forward(50)

	turtle.penup()
	turtle.color("red")
	turtle.right(90)
	turtle.forward(10)
	turtle.pendown()
	turtle.circle(3)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()


	turtle.write("E E E    D E P T.")

	turtle.penup()
	turtle.left(180)
	turtle.forward(20)
	turtle.right(90)
	turtle.pendown()
	turtle.color("blue")

	turtle.forward(40)

	turtle.penup()
	turtle.color("red")
	turtle.right(90)
	turtle.forward(10)
	turtle.pendown()
	turtle.circle(3)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()


	turtle.write("M E C H A N I C A L   DEPT.")

	turtle.penup()
	turtle.left(180)
	turtle.forward(20)
	turtle.right(90)
	turtle.pendown()
	turtle.color("blue")

	turtle.done()
	

def onclick5():
	turtle.hideturtle()
	turtle.pensize(4)

	turtle.penup()
	turtle.right(90)
	turtle.forward(500)
	turtle.pendown()
	turtle.color("blue")

	turtle.write("F R O N T   G A T E")
	turtle.right(180)
	turtle.penup()


	 # Infinity road
	turtle.color("blue")
	turtle.pensize(4)
	turtle.pendown()
	turtle.forward(500)
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()
	turtle.write("A D M I N I S T  R A T I V E   B L O C K") 
	turtle.penup()
	turtle.backward(20)
	turtle.pendown()
	turtle.left(90)
	turtle.forward(170)
	turtle.penup()
	turtle.forward(100)
	turtle.pendown()

	turtle.write("A R C H I T E C T U R E   Dept.\nM C A Dept.")
	turtle.penup()
	turtle.backward(100)
	turtle.right(90)

	#  birla

	turtle.pendown()

	turtle.forward(90)
	turtle.right(90)
	 
	turtle.forward(15)
	turtle.penup()
	turtle.forward(20)
	turtle.write("B I R L A   A U D I T O R I U M")
	turtle.penup()
	turtle.backward(35)
	turtle.left(90)

	turtle.pendown()

	# Physics dept
	turtle.forward(150)
	turtle.right(90)
	turtle.forward(20)
	turtle.left(90)
	turtle.penup()
	turtle.forward(20)
	turtle.color("red")
	turtle.pendown()
	turtle.write("D E P T    O F   P H Y S I C S ")
	turtle.circle(5)
	turtle.penup()
	turtle.backward(20)
	turtle.right(90)

	# Chemistry dept
	turtle.color("blue")
	turtle.pendown()
	turtle.forward(400)
	turtle.left(90)
	turtle.penup()
	turtle.forward(20)
	turtle.color("red")
	turtle.pendown()
	turtle.write("D E P T   O F  C H E M I S T R Y ")
	turtle.circle(5)
	turtle.penup()
	turtle.backward(20)
	turtle.right(90)
	turtle.color("blue")
	turtle.pendown()
	turtle.forward(94)
	turtle.left(90)

	turtle.forward(70)
	turtle.left(90)
	turtle.forward(20)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()

	turtle.color("red")
	turtle.begin_fill()
	turtle.circle(4)
	turtle.end_fill()

	turtle.penup()
	turtle.forward(100)
	turtle.write("R E S E A R C H \n C E N T E R")
	turtle.goto(0,0)


	turtle.done()	

def onclick6():
	turtle.hideturtle()
	turtle.pensize(4)

	turtle.penup()
	turtle.right(90)
	turtle.forward(500)
	turtle.pendown()
	turtle.color("blue")

	turtle.write("  F R O N T   G A T E")
	turtle.right(180)
	turtle.penup()


	 # Infinity road
	turtle.color("blue")
	turtle.pensize(4)
	turtle.pendown()
	turtle.forward(500)
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()
	turtle.write("A D M I N I S T R A T I V E     B L O C K") 
	turtle.penup()
	turtle.backward(20)
	turtle.pendown()
	turtle.left(90)
	turtle.forward(170)
	turtle.penup()
	turtle.forward(100)
	turtle.pendown()

	turtle.write("Architecture Dept/MCA")
	turtle.penup()
	turtle.backward(100)
	turtle.right(90)

	#  birla

	turtle.pendown()

	turtle.forward(90)
	turtle.right(90)
	turtle.penup()
	turtle.forward(15)
	turtle.color("red")
	turtle.pendown()
	turtle.circle(3)
	turtle.penup()
	turtle.forward(20)
	turtle.write("B i r l a  A u d i t o r i u m")
	turtle.penup()
	turtle.backward(35)
	turtle.left(90)

	turtle.pendown()
	turtle.color("blue")
	turtle.forward(100)
	turtle.left(90)
	turtle.forward(300)
	turtle.penup()
	turtle.forward(30)
	turtle.pendown()

	turtle.right(60)
	turtle.forward(30)
	turtle.left(120)
	turtle.forward(30)
	turtle.right(-120)
	turtle.forward(30)

	turtle.left(180)
	turtle.penup()
	turtle.forward(130)
	turtle.color("red")
	turtle.write("BVB  H O S T E L")
	turtle.penup()
	turtle.color("blue")
	turtle.backward(460)

	turtle.right(90)
	turtle.pendown()
	turtle.forward(100)
	turtle.left(90)

	turtle.forward(80)
	turtle.right(90)
	turtle.penup()
	turtle.forward(40)
	turtle.pendown()

	#drawing the plus sign

	turtle.color("green")
	turtle.pensize("6")
	turtle.forward(30)
	turtle.penup()
	turtle.right(90)
	turtle.penup()
	turtle.forward(15)
	turtle.right(90)
	turtle.forward(15)
	turtle.pendown()
	turtle.right(90)
	turtle.forward(30)
	turtle.backward(15)
	turtle.pensize("4")
	turtle.penup()
	turtle.left(90)
	turtle.forward(40)
	turtle.color("red")
	turtle.write("HEALTH\nCENTRE")
	turtle.color("blue")
	turtle.pendown()
	turtle.forward(25)
	turtle.right(90)


	turtle.pendown()
	turtle.forward(70)
	turtle.right(90)
	turtle.forward(25)
	turtle.penup()
	turtle.forward(10)

	turtle.pendown()
	turtle.color("green")
	turtle.begin_fill()
	turtle.circle(4)
	turtle.end_fill()

	turtle.penup()
	turtle.forward(10)
	turtle.left(90)
	turtle.forward(20)
	turtle.color("red")
	turtle.write("S O C I E T Y")


	turtle.color("blue")
	turtle.backward(20)


	turtle.left(90)

	turtle.forward(35)
	turtle.pendown()
	turtle.right(90)
	turtle.forward(110)
	turtle.right(90)
	turtle.forward(10)
	turtle.penup()
	turtle.forward(20)
	turtle.color("red")
	turtle.write("A L P B \nH O S T E L")

	turtle.penup()
	turtle.forward(30)
	turtle.pendown()

	#triangle
	turtle.color("blue")
	turtle.right(60)
	turtle.forward(30)
	turtle.left(120)
	turtle.forward(30)
	turtle.right(-120)
	turtle.forward(30)

	turtle.penup()
	turtle.forward(60)
	turtle.left(90)
	turtle.forward(260)



	#canteen
	turtle.pendown()
	turtle.left(90)
	turtle.color("blue")
	turtle.forward(100)
	turtle.left(70)
	turtle.forward(70)
	turtle.penup()
	turtle.forward(30)
	turtle.color("red")
	turtle.pendown()
	turtle.begin_fill()
	turtle.circle(4)
	turtle.end_fill()
	turtle.write("C A N T E E N")
	turtle.penup()
	turtle.goto(0,0)


	turtle.done()



	
def onclick7():
	turtle.hideturtle()
	turtle.pensize(4)

	turtle.penup()
	turtle.right(90)
	turtle.forward(500)
	turtle.pendown()
	turtle.color("blue")

	turtle.write("FRONT GATE")
	turtle.right(180)
	turtle.penup()


	 # Infinity road
	turtle.color("blue")
	turtle.pensize(4)
	turtle.pendown()
	turtle.forward(240)
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()
	turtle.write("A d m i n i s t r a t i ve   B l o c k ") 
	turtle.penup()
	turtle.backward(20)
	turtle.pendown()
	turtle.left(90)
	turtle.forward(170)
	turtle.penup()
	turtle.forward(90)
	turtle.pendown()

	turtle.write("Architecture Block \n MCA Block")
	turtle.penup()
	turtle.backward(100)
	turtle.right(90)

	#  birla

	turtle.pendown()

	turtle.forward(78)
	turtle.right(90)
	 
	turtle.forward(15)
	turtle.penup()
	turtle.forward(20)
	turtle.write("Birla Auditorium")
	turtle.penup()
	turtle.backward(35)
	turtle.left(90)

	turtle.pendown()

	# Physics dept
	turtle.forward(90)
	turtle.right(90)
	turtle.forward(20)
	turtle.left(90)

	turtle.forward(20)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()
	turtle.write("Physics Dept.")
	turtle.circle(5)
	turtle.penup()
	turtle.backward(30)
	turtle.right(90)

	# Chemistry dept
	turtle.color("blue")
	turtle.pendown()
	turtle.forward(400)
	turtle.left(90)
	turtle.forward(20)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()
	turtle.write("Chemistry Dept.")
	turtle.circle(5)
	turtle.penup()
	turtle.backward(30)
	turtle.right(90)

	turtle.pendown()
	turtle.forward(94)
	turtle.left(90)



	
	turtle.forward(170)
	turtle.right(90)
	turtle.forward(50)
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()
	turtle.color("grey")
	for i in range(1,2):
		turtle.forward(80)
		turtle.right(90)
		turtle.forward(30)
		turtle.right(90)
		turtle.forward(80)
		turtle.right(90)
		turtle.forward(30)

	turtle.penup()

	turtle.forward(10)
	turtle.write("PARKING AREA")	
	turtle.backward(10)
	turtle.color("blue")
	turtle.right(90)
	turtle.backward(70)
	turtle.left(90)
	turtle.pendown()
	# C  S  -  I S  B L O C K

	turtle.forward(75)
	turtle.left(90)
	turtle.forward(80)
	turtle.left(90)
	turtle.penup()
	turtle.forward(30)

	turtle.right(90)
	turtle.forward(60)

	turtle.color("red")
	turtle.begin_fill()
	turtle.circle(5)
	turtle.end_fill()
	turtle.write("CSE-ISE-MATHEMATICS BLOCK")

	#media center

	turtle.left(90)
	turtle.backward(30)
	turtle.right(180)
	turtle.forward(20)
	turtle.color("navy")
	turtle.pendown()
	turtle.color("deeppink")
	turtle.begin_fill()
	for i in range(5):
	   turtle.forward(27) 
	   turtle.right(72) 

	turtle.end_fill()
	turtle.penup()
	turtle.left(90)
	turtle.forward(7)
	turtle.color("red")
	turtle.dot()
	turtle.forward(130)

	turtle.write("MEDIA CENTRE")
	turtle.color("red")



	turtle.penup()
	turtle.goto(0,0)

	turtle.done()
		

def onclick8():
	turtle.hideturtle()
	turtle.pensize(4)

	turtle.penup()
	turtle.right(90)
	turtle.forward(350)
	turtle.pendown()
	turtle.color("darkblue")
	turtle.penup()

	turtle.pendown()
	turtle.color("blue")
	turtle.write("FRONT GATE")
	turtle.penup()
	turtle.right(180)

	turtle.pendown()
	turtle.forward(500)
	turtle.penup()
	turtle.forward(20)
	turtle.color("red")

	turtle.write("Administrative Block")
	turtle.color("blue")
	turtle.backward(20)
	turtle.pendown()
	turtle.right(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(40)
	turtle.penup()
	turtle.right(90)
	turtle.forward(20)
	turtle.pendown()
	turtle.write("Library")
	turtle.penup()
	turtle.backward(20)
	turtle.pendown()
	turtle.right(90)
	turtle.forward(40)
	turtle.left(90)
	turtle.forward(100)
	turtle.penup()
	turtle.forward(20)
	turtle.write("Coffee Shop")
	turtle.backward(20)
	turtle.left(90)
	turtle.pendown()
	turtle.forward(100)

	turtle.left(90)

	turtle.forward(100)


	turtle.color("blue")
	turtle.forward(150)
	turtle.right(90)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()

	turtle.color("grey")
	turtle.begin_fill()

	for i in range(1,2):
		turtle.forward(40)
		turtle.right(90)
		turtle.forward(200)
		turtle.right(90)
		turtle.forward(40)
		turtle.right(90)
		turtle.forward(200)
	turtle.end_fill()

	turtle.penup()
	turtle.forward(60)
	turtle.write("CIVIL\nDEPT.")
	turtle.backward(200)

	turtle.right(90)
	turtle.color("deeppink")
	turtle.forward(40)
	turtle.pendown()
	turtle.begin_fill()
	for i in range(1,2):
		turtle.forward(80)
		turtle.right(90)
		turtle.forward(80)
		turtle.right(90)
		turtle.forward(80)
		turtle.right(90)
		turtle.forward(80)
	turtle.end_fill()

	turtle.penup()
	turtle.backward(90)
	turtle.right(90)
	turtle.write("G\nJ\nC\nB")
	turtle.backward(50)
	turtle.right(90)
	turtle.forward(20)
	turtle.pendown()
	turtle.color("blue")
	turtle.left(90)
	turtle.forward(80)
	turtle.left(90)
	turtle.forward(8)
	turtle.penup()
	turtle.backward(8)
	turtle.right(90)
	turtle.pendown()
	turtle.forward(90)
	turtle.left(90)

	turtle.forward(50)
	turtle.right(90)
	turtle.forward(10)
	turtle.penup()
	turtle.forward(10)
	turtle.left(90)
	turtle.forward(50)

	turtle.write("LADIES\nAMMENITIES")

	turtle.backward(50)
	turtle.left(90)
	turtle.forward(20)
	turtle.right(90)
	turtle.pendown()
	turtle.forward(110)
	turtle.right(90)
	turtle.forward(10)
	turtle.penup()
	turtle.forward(10)
	turtle.left(90)
	turtle.forward(50)

	turtle.write("BOYS\nAMMENITIES")

	turtle.left(90)
	turtle.forward(20)
	turtle.left(90)
	turtle.forward(210)

	turtle.left(90)
	turtle.pendown()
	turtle.forward(70)
	turtle.right(90)
	turtle.forward(40)
	turtle.left(90)


	turtle.begin_fill()
	for i in range(1,2):
		turtle.forward(25)
		turtle.right(90)
		turtle.forward(70)
		turtle.right(90)
		turtle.forward(25)
		turtle.right(90)
		turtle.forward(70)
	turtle.end_fill()

	turtle.left(90)
	turtle.penup()
	turtle.forward(20)
	turtle.right(90)

	turtle.color("red")
	turtle.write("EC & TC DEPT")
	turtle.goto(0,0)

	turtle.done()

def onclick9():
	turtle.hideturtle()
	turtle.pensize(4)

	turtle.penup()
	turtle.right(90)
	turtle.forward(500)
	turtle.pendown()
	turtle.color("blue")

	turtle.penup()
	turtle.forward(10)
	turtle.pendown()

	turtle.write("FRONT GATE")
	turtle.right(180)
	turtle.penup()


	 # Infinity road
	turtle.color("blue")
	turtle.pensize(4)
	turtle.pendown()
	turtle.forward(500)

	turtle.forward(20)

	turtle.write("Administrative Block") 

	turtle.penup()
	turtle.backward(20)
	turtle.pendown()
	turtle.right(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(30)


	turtle.right(90)
	turtle.penup()
	turtle.forward(5)
	turtle.pendown()
	turtle.write("Library")

	turtle.penup()
	turtle.right(180)
	turtle.forward(5)
	turtle.left(90)
	turtle.forward(30)
	turtle.pendown()
	turtle.color("blue")


	turtle.left(90)
	turtle.forward(100)
	turtle.penup()
	turtle.left(90)
	turtle.forward(10)
	turtle.pendown()
	turtle.circle(3)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()

	turtle.write("Coffee Shop")

	turtle.left(180)
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()

	turtle.left(90)
	turtle.forward(200)
	turtle.left(90)
	turtle.forward(30)

	turtle.penup()
	turtle.color("red")
	turtle.right(90)
	turtle.forward(10)
	turtle.pendown()
	turtle.circle(3)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()

	turtle.write("C H E M I C A L   E N G G . DEPT.\nB IO - T E C H  DEPT")

	turtle.penup()
	turtle.left(180)
	turtle.forward(20)
	turtle.left(90)
	turtle.forward(30)
	turtle.left(90)
	turtle.pendown()

	turtle.color("blue")
	turtle.forward(200)

	turtle.left(45)
	turtle.forward(60)
	turtle.penup()
	turtle.right(45)
	turtle.forward(20)
	turtle.pendown()
	turtle.color("red")
	for i in range(6):
	   turtle.forward(20) 
	   turtle.right(-60) 


	turtle.penup()
	turtle.forward(40)
	turtle.pendown()

	turtle.write("STADIUM")

	turtle.color("blue")
	turtle.penup()
	turtle.left(180)
	turtle.forward(60)
	turtle.left(90)
	turtle.pendown()

	turtle.forward(110)
	turtle.right(90)
	turtle.forward(30)
	turtle.left(90)
	turtle.forward(30)


	turtle.penup()
	turtle.right(90)
	turtle.forward(30)
	turtle.pendown()

	turtle.penup()
	turtle.left(90)

	turtle.pendown()
	turtle.color("red")
	turtle.circle(3)
	turtle.penup()
	turtle.left(90)
	turtle.forward(10)
	turtle.right(90)
	turtle.forward(20)
	turtle.pendown()
	turtle.write("BACK GATE")

	turtle.color("blue")
	turtle.penup()
	turtle.left(-90)
	turtle.forward(20)
	turtle.right(90)
	turtle.forward(10)
	turtle.pendown()


	turtle.forward(30)
	turtle.left(90)


	turtle.forward(60)
	turtle.left(90)
	turtle.forward(30)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()

	turtle.color("red")
	turtle.circle(3)
	turtle.penup()
	turtle.forward(20)
	turtle.pendown()
	turtle.write("CAMPUS XEROX")
	turtle.color("blue")
	turtle.penup()
	turtle.left(180)
	turtle.forward(60)
	turtle.left(90)
	turtle.pendown()

	turtle.forward(250)
	turtle.left(90)
	turtle.forward(30)
	turtle.penup()
	turtle.forward(10)
	turtle.pendown()
	turtle.color("red")
	turtle.circle(3)
	turtle.penup()
	turtle.left(90)
	turtle.forward(10)
	turtle.right(90)
	turtle.forward(20)
	turtle.pendown()
	turtle.write("PARKING AREA")
	turtle.color("blue")
	turtle.penup()
	turtle.left(180)
	turtle.forward(20)
	turtle.forward(40)
	turtle.pendown()
	turtle.left(90)
	turtle.forward(300)
	turtle.left(90)
	turtle.forward(750)

	turtle.done()


frame = Frame(root,bg='black',bd=20,pady=5,relief=RIDGE)
frame.pack(side=TOP)

textlabel = Label(frame , font=('arial',50	,'bold') ,text='SIT ROUTE MAP',bd=15,bg="ivory",width = 40,fg="grey",justify=CENTER)
textlabel.grid(row=0)


frame1 = Frame(root,bg='olivedrab',bd=5,pady=1,relief=RAISED)
frame1.pack(side=RIGHT)


file_name = PhotoImage(file = "sit.png")
button = Button(frame1 , image = file_name , justify = LEFT ,width = 800, height = 600	)
button.grid(row=0)

button.pack()

ReceiptCal_F = Frame(root,bg='white',bd=10,relief=RAISED)
ReceiptCal_F.pack(side=LEFT)


Buttons_F=Frame(ReceiptCal_F,bg='black',bd=3,relief=RAISED)
Buttons_F.pack(side=BOTTOM)
btnTotal=Button(Buttons_F,padx=16,pady=2,bd=1,fg='white',font=('arial',14,'bold'),width=70,text='Chemical Engineering Dept. , Bio-Technology Dept.\nShivakuramaswamy Stadium , Back Gate , Campus Xerox',bg='black',command=onclick9).grid(row=0,column=0)


Buttons_F=Frame(ReceiptCal_F,bg='black',bd=3,relief=RAISED)
Buttons_F.pack(side=BOTTOM)
btnTotal=Button(Buttons_F,padx=16,pady=2,bd=1,fg='white',font=('arial',14,'bold'),width=70,text='EC Dept. , TC Dept.\nCivil Dept. , GJCB , Ladies Ammenities',bg='black',command=onclick8).grid(row=0,column=0)


Buttons_F=Frame(ReceiptCal_F,bg='black',bd=3,relief=RAISED)
Buttons_F.pack(side=BOTTOM)
btnTotal=Button(Buttons_F,padx=16,pady=2,bd=1,fg='white',font=('arial',14,'bold'),width=70,text='CSE Dept. , ISE Dept. , Mathematics Dept.\nMedia Center',bg='black',command=onclick7).grid(row=0,column=0)


Buttons_F=Frame(ReceiptCal_F,bg='black',bd=3,relief=RAISED)
Buttons_F.pack(side=BOTTOM)
btnTotal=Button(Buttons_F,padx=16,pady=2,bd=1,fg='white',font=('arial',14,'bold'),width=70,text='Canteen\nHealth Center , Hostels',bg='black',command=onclick6).grid(row=0,column=0)

Buttons_F=Frame(ReceiptCal_F,bg='black',bd=3,relief=RAISED)
Buttons_F.pack(side=BOTTOM)
btnTotal=Button(Buttons_F,padx=16,pady=2,bd=1,fg='white',font=('arial',14,'bold'),width=70,text='Physics Dept.\nChemistry Dept. , Research Center',bg='black',command=onclick5).grid(row=0,column=0)


Buttons_F=Frame(ReceiptCal_F,bg='black',bd=3,relief=RAISED)
Buttons_F.pack(side=BOTTOM)
btnTotal=Button(Buttons_F,padx=16,pady=2,bd=1,fg='white',font=('arial',14,'bold'),width=70,text='Karnataka Bank , Library , Coffee Shop\nIEM Dept. , EEE Dept.\ , Mechanical Dept.',bg='black',command=onclick4).grid(row=0,column=0)


Buttons_F=Frame(ReceiptCal_F,bg='black',bd=3,relief=RAISED)
Buttons_F.pack(side=BOTTOM)
btnTotal=Button(Buttons_F,padx=16,pady=2,bd=1,fg='white',font=('arial',14,'bold'),width=70,text='Birla Auditorium\nArchitecture Dept. , MCA Dept.',bg='black',command=onclick3).grid(row=0,column=0)


Buttons_F=Frame(ReceiptCal_F,bg='black',bd=3,relief=RAISED)
Buttons_F.pack(side=BOTTOM)
btnTotal=Button(Buttons_F,padx=16,pady=2,bd=1,fg='white',font=('arial',14,'bold'),width=70,text='Administrative Block\nBasket Ball Court',bg='black',command=onclick2).grid(row=0,column=0)


Buttons_F=Frame(ReceiptCal_F,bg='black',bd=3,relief=RAISED)
Buttons_F.pack(side=BOTTOM)
btnTotal=Button(Buttons_F,padx=16,pady=2,bd=1,fg='white',font=('arial',14,'bold'),width=70,text='MBA Dept. , Kennedy Guest House\nTemple',bg='black',command=onclick1).grid(row=0,column=0)

mainloop()
