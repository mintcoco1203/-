Web VPython 3.2
my_cylinder = cylinder(pos=vec(0, -2, 0),axis=vec(0, 2, 0),radius=1,color=color.red)
spout = cylinder(pos=vec(0.5, -1.7, 0),axis=vec(2.7, 1, 0),radius=0.3,color=color.red)
handle = ring(pos=vec(-0.1, -0.2, 0),axis=vec(0, 0, 1),radius=1.5,thickness=0.2,color=color.red)
wateringcan= compound([ my_cylinder, spout ,handle])
wateringcan.axis = vec(1,-0.6,0)
wateringcan.pos = vec(-6,6,0)
box(size=vec(100,0.01,100),color=color.yellow)
boxobj1 = box(pos=vec(-0.7,0,0),size=vec(0.4,0.1,0.4),color=color.green)
boxobj2 = box(pos=vec(0,0,0),size=vec(0.4,0.1,0.4),color=color.green)
boxobj3 = box(pos=vec(0.7,0,0),size=vec(0.4,0.1,0.4),color=color.green)
boxobj4 = box(pos=vec(-0.35,0,-0.4),size=vec(0.4,0.1,0.4),color=color.green)
boxobj5 = box(pos=vec(0.35,0,-0.5),size=vec(0.4,0.1,0.4),color=color.green)
boxobj6 = box(pos=vec(0.4,0,0.5),size=vec(0.4,0.1,0.4),color=color.green)
boxobj7 = box(pos=vec(-0.35,0,0.5),size=vec(0.4,0.1,0.4),color=color.green)
boxobj8 = box(pos=vec(-0.9,0,0.3),size=vec(0.4,0.1,0.4),color=color.green)
boxobj9 = box(pos=vec(0.9,0,0.5),size=vec(0.4,0.1,0.4),color=color.green)
boxobj10 = box(pos=vec(1.1,0,0.7),size=vec(0.4,0.1,0.4),color=color.green)
boxobj11 = box(pos=vec(-1.1,0,0.8),size=vec(0.4,0.1,0.4),color=color.green)
boxobj12 = box(pos=vec(0.5,0,1),size=vec(0.4,0.1,0.4),color=color.green)
boxobj13 = box(pos=vec(-0.5,0,1),size=vec(0.4,0.1,0.4),color=color.green)
plant= compound([boxobj1,boxobj2,boxobj3,boxobj4,boxobj5,boxobj6,boxobj7,boxobj8,boxobj9,boxobj10,boxobj11,boxobj12,boxobj13])



    
level = 0
maxLevel = 11

state = ["1level","2level","3level","4level","5level","6level","7level","8level","9level","10level"]


while True :
    rate(3)
    k = keysdown()
    if '1' in k:
        print(state[level])
        if level < maxLevel:
            level += 1
            plant.size=vec(2, level*1.25, 2)
            if level == maxLevel:
                print("다 자랐다!")
                
    if ' ' in k:
        level=0
        plant.size=vec(2,0.1,2)
        print("초기화")
        
