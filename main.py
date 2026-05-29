from vpython import *
my_cylinder = cylinder(pos=vec(0, -2, 0),axis=vec(0, 2, 0),radius=1,color=color.red)
spout = cylinder(pos=vec(0.5, -1.7, 0),axis=vec(2.7, 1, 0),radius=0.3,color=color.red)
handle = ring(pos=vec(-0.1, -0.2, 0),axis=vec(0, 0, 1),radius=1.5,thickness=0.2,color=color.red)
wateringcan= compound( [ my_cylinder, spout ,handle])
wateringcan.axis = vec(1,-0.8,-0.3)
boxobj1 = box(pos=vec(-0.7,0,0),size=vec(0.5,0.1,0.5),color=color.green)
boxobj2 = box(pos=vec(0,0,0),size=vec(0.5,0.1,0.5),color=color.green)
boxobj3 = box(pos=vec(0.7,0,0),size=vec(0.5,0.1,0.5),color=color.green)
boxobj4 = box(pos=vec(-0.35,0,-0.5),size=vec(0.5,0.1,0.5),color=color.green)
boxobj5 = box(pos=vec(0.35,0,-0.5),size=vec(0.5,0.1,0.5),color=color.green)
boxobj6 = box(pos=vec(0.4,0,0.5),size=vec(0.4,0.1,0.4),color=color.green)
boxobj7 = box(pos=vec(-0.35,0,0.5),size=vec(0.4,0.1,0.4),color=color.green)
boxobj8 = box(pos=vec(-0.9,0,0.3),size=vec(0.4,0.1,0.4),color=color.green)
boxobj9 = box(pos=vec(0.9,0,0.5),size=vec(0.4,0.1,0.4),color=color.green)
boxobj10 = box(pos=vec(1.1,0,0.7),size=vec(0.4,0.1,0.4),color=color.green)
boxobj11 = box(pos=vec(-1.1,0,0.8),size=vec(0.4,0.1,0.4),color=color.green)
boxobj12 = box(pos=vec(0.5,0,1),size=vec(0.4,0.1,0.4),color=color.green)
boxobj13 = box(pos=vec(-0.5,0,1),size=vec(0.4,0.1,0.4),color=color.green)
    
level = 1
maxLevel = 11

def updateBox():
    boxobj1.size=vec(0.5, level*1.25, 0.5)
    boxobj2.size=vec(0.5, level*1.25, 0.5)
    boxobj3.size=vec(0.5, level*1.25, 0.5)
    boxobj4.size=vec(0.5, level*1.25,0.5)
    boxobj5.size=vec(0.4, level*1.26,0.4)
    boxobj6.size=vec(0.4, level*1.23,0.4)
    boxobj7.size=vec(0.4, level*1.1,0.4)
    boxobj8.size=vec(0.4, level*1.22,0.4)
    boxobj9.size=vec(0.4, level*1.2,0.4)
    boxobj10.size=vec(0.4, level*1.3,0.4)
    boxobj11.size=vec(0.4, level*1.05,0.4)
    boxobj12.size=vec(0.4, level*1.1,0.4)
    boxobj13.size=vec(0.4, level*1.3,0.4)

def keyInput(evt):
    global level
    key = evt.key
    print("key : ", key )
    if key == "1":
        if level < maxLevel:
            level += 1
            updateBox()
            print("현재 단계:", level )
    if key ==" ":
        level=1
        updateBox()
            

scene.bind("keydown", keyInput)
while True : 
    rate(100)
    if level == 11:
        print("다 자랐다!")
