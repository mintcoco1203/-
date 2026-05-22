boxobj1 = box(pos=vec(-0.7,0,0),size=vec(0.5,0.1,0.5),color=color.green)
boxobj2 = box(pos=vec(0,0,0),size=vec(0.5,0.1,0.5),color=color.green)
boxobj3 = box(pos=vec(0.7,0,0),size=vec(0.5,0.1,0.5),color=color.green)
boxobj4 = box(pos=vec(-0.35,0,-0.5),size=vec(0.5,0.1,0.5),color=color.green)
boxobj5 = box(pos=vec(0.35,0,-0.5),size=vec(0.5,0.1,0.5),color=color.green)
    
level = 1
maxLevel = 11

def updateBox():
    boxobj1.size=vec(0.5, level*1.25, 0.5)
    boxobj2.size=vec(0.5, level*1.25, 0.5)
    boxobj3.size=vec(0.5, level*1.25, 0.5)
    boxobj4.size=vec(0.5, level*1.25,0.5)

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
