import turtle
from pygame import Vector2
import os
import pygame
import time
import math


###### Set Up ######

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
xMargin: float = 8300
screen.screensize(canvwidth=1000, canvheight=1000, bg="black")

###### Position Vectors Value ######

# Bezier default

p0 = Vector2(-200, -200) 
p1 = Vector2(700, 400) 
p2 = Vector2(-700, 400) 
p3 = Vector2(200, -200)

# SineWave default

sp0 = Vector2(-675,0)
amplitude = 250
frequency = 1
phase = 0
speed = 2

###### Functions ######

def AskFor4P():
    Clear()
    opt = float(input("¿Quieres dar coordenadas?\n 1) Si\n 2) No \n  -Option: "))
    if opt == 1:
        Clear()
        p0.x = float(input("p0 = X: "))
        p0.y = float(input("p0 = Y: "))
        p1.x = float(input("p1 = X: "))
        p1.y = float(input("p1 = Y: "))
        p2.x = float(input("p2 = X: "))
        p2.y = float(input("p2 = Y: "))
        p3.x = float(input("p3 = X: "))
        p3.y = float(input("p3 = Y: "))
    else: pass

def TypeOfGridAndDraw(typeOfGrid):
    '''Usar antes de bezier'''
    if typeOfGrid == 1:
        DrawChartBasic()
    elif typeOfGrid == 2:
        print("GridModeParameter = 0")
        DrawChartAdvanced(False, 100, 10)
    else:
        print("GridModeParameter = 1")
        DrawChartAdvanced(True, 100, 10)

def AskForTypeOfGrid():
    Clear()
    menu = f"Tipo de grid/cuadrícula:\n 1) Basic\n 2) Advanced\n 3) Advanced + FullGrid\n  -Option: "
    gridType = int(input(menu))
    Clear()
    print("Dibujando...")
    print(f"Devolviendo {gridType}")
    return int(gridType)
        
def DrawChartBasic(): # Dibujar gráfica básica.
    chartRender = turtle.Turtle()
    chartRender.color("lightgray")
    chartRender.speed("fastest")
    chartRender.pensize(3)
    heigth = 2000
    width = 2000
    chartRender.goto(0, heigth)
    chartRender.goto(0, -heigth)
    chartRender.goto(0, 0)
    chartRender.goto(width, 0)
    chartRender.goto(-width, 0)
    del chartRender
    
def CalcCircleOffset(xOffSet: float, yOffSet: float, circleSize: float):
    activeTurtle = turtle.getturtle()
    activeTurtle.speed("fastest")
    activeTurtle.color("red")
    activeTurtle.begin_fill()
    activeTurtle.goto(xOffSet, yOffSet+-circleSize)
    activeTurtle.circle(circleSize)
    activeTurtle.end_fill()
    activeTurtle.hideturtle()
    del activeTurtle
    
def DrawChartAdvanced(isGridMode: bool, lineSeparation: int = 100, lines: int = 10):
    """ gridMode sirve para activar una cuadricula completa | lineSeparation = 50 (No tocar) | lines = No tocar """
    chartRender = turtle.Turtle()
    chartRender.speed("fastest")
    chartRender.color("gray")
    
    _isGridMode = isGridMode
    print(f"Gridmode: {_isGridMode}")
 
    if _isGridMode:
        pensize = 1
        lineWidth = 1000
    else:
        pensize = 2
        lineWidth = 4
    
    chartRender.goto(0, 0)
    
    # (heigth/2)-(heigth/2*2)
    
    #lines = 10 # Cambiar para el numero de lineas.
    
    lines += 1
    
    for x in range(lines): # x+
        chartRender.pensize(2)
        chartRender.goto(0, lineSeparation * x)
        chartRender.pensize(pensize)
        chartRender.goto(-lineWidth, lineSeparation * x)
        chartRender.goto(lineWidth, lineSeparation * x)
        chartRender.goto(0, lineSeparation * x)
        chartRender.pensize(2)
    for x in range(lines): #y+
        chartRender.pensize(2)
        chartRender.goto(lineSeparation * x, 0)
        chartRender.pensize(pensize)
        chartRender.goto(lineSeparation * x, -lineWidth)
        chartRender.goto(lineSeparation * x, lineWidth)
        chartRender.goto(lineSeparation * x, 0)
        chartRender.pensize(2)
    for x in range(lines): # x-
        chartRender.pensize(2)
        chartRender.goto(0, -lineSeparation * x)
        chartRender.pensize(pensize)
        chartRender.goto(-lineWidth, -lineSeparation * x)
        chartRender.goto(lineWidth, -lineSeparation * x)
        chartRender.goto(0, -lineSeparation * x)
        chartRender.pensize(2)
    for x in range(lines): #y-
        chartRender.pensize(2)
        chartRender.goto(-lineSeparation * x, 0)
        chartRender.pensize(pensize)
        chartRender.goto(-lineSeparation * x, -lineWidth)
        chartRender.goto(-lineSeparation * x, lineWidth)
        chartRender.goto(-lineSeparation * x, 0)
        chartRender.pensize(2)

    CalcCircleOffset(0, 0, 5)
    
    chartRender.hideturtle()
    del chartRender

def Clear(): # Limpiar pantalla
    os.system("cls || clear")

def BeizerCurve(p0: Vector2 = Vector2(-200, -200), p1: Vector2 = Vector2(700, 400), p2: Vector2 = Vector2(-700, 400), p3: Vector2 = Vector2(200, -200)):
    
    position = list() # Guarda las coordenadas en una de Vectores2.
    position.append(p0)
    position.append(p1)
    position.append(p2)
    position.append(p3)
    
    ####### Config Pen #######

    pointer = turtle.Turtle()

    pointer.color("lightgreen")
    pointer.penup()
    pointer.speed(100)
    pointer.goto(p0)
    pointer.pensize(3)
    pointer.speed(5)
    
    tiempo = 0

    while tiempo <= 1:
        
        tiempo += 0.05
        
        if not pointer.isdown():
            print("Start")
            pointer.pendown()
        
        if tiempo > 1:
            tiempo = 1
        
        a = Vector2.lerp(p0, p1, tiempo)
        b = Vector2.lerp(p1, p2, tiempo) # Primera subdivision
        c = Vector2.lerp(p2, p3, tiempo)
        
        d = Vector2.lerp(a, b, tiempo) # Segunda subdivision
        e = Vector2.lerp(b , c, tiempo)
        
        p = Vector2.lerp(d, e, tiempo) # Ultima subdivision (curva)

        pointer.goto(p)
        Clear()
        print(f"La posición de P es: {p}")
        
        if tiempo == 1:
            break
    
    pointer.hideturtle()
    del pointer    
    pass

def AskForSineWave():
    Clear()
    opt = float(input("¿Quieres dar parametros?\n 1) Si\n 2) No \n  -Option: "))
    if opt == 1:
        Clear()
        sp0.x = float(input("p0 = X: "))
        sp0.y = float(input("p0 = Y: "))
        Clear()
        
        global amplitude, frequency, phase, speed
        
        amplitude = float(input("Amplitud: "))
        frequency = float(input("Frecuencia: "))
        phase = float(input("Fase: "))
        speed = float(input("Velocidad: "))
    else: pass

def SineWave(offSet: Vector2 = Vector2(-675,0), amplitude: float = 250, frecuenci: float = 2, phase: float = 0, speed: float = 1):
    
    pointer = turtle.Turtle()
    pointer.penup()
    pointer.speed("fastest")
    pointer.pensize(3)
    pointer.color("lightgreen")
    
    tiempo = 0
    
    while True:
        
        tiempo += 0.01
        
        xPos = offSet.x + ((tiempo * speed) * 100)
        yPos = offSet.y + (amplitude * math.sin(2 * math.pi * frecuenci * (tiempo * speed) + phase))
        AbsPos = Vector2(xPos, yPos)
        pointer.goto(AbsPos)
        
        if not pointer.isdown():
            pointer.pendown()
            
        if xPos < -xMargin or xPos > xMargin:
            pointer.penup()
            pointer.hideturtle()
            del pointer
            break
            
        Clear()
        print(f"Y Pos = {yPos}\nX Pos = {xPos}")

def AskForRender():
    Clear()
    menu = '''Tipo de curva:
    
 1) Bezier...
 2) Sinewave...
 3) ...
 
  Opción: '''
    opt = int(input(menu))
    if opt == 1: # Beizer
        AskFor4P()
        TypeOfGridAndDraw(AskForTypeOfGrid())
        BeizerCurve(p0,p1,p2,p3)
        pass
    if opt == 2:
        AskForSineWave()
        TypeOfGridAndDraw(AskForTypeOfGrid())
        SineWave(Vector2(sp0), amplitude, frequency, phase, speed)
        pass
    
######## Run ########

AskForRender()


turtle.done()
