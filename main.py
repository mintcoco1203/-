handle = ring(pos=vec(-0.1, -0.2, 0),axis=vec(0, 0, 1),radius=1.5,thickness=0.2,color=color.red)
wateringcan= compound([ my_cylinder, spout ,handle])
wateringcan.axis = vec(1,-0.6,0)
wateringcan.pos = vec(-6,5,0)
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
            if level == maxLevel:
                print("다 자랐다!")
    if ' ' in k:
        level=0
        boxobj1.size = vec(0.4,0.1,0.4)
        boxobj2.size = vec(0.4,0.1,0.4)
        boxobj3.size = vec(0.4,0.1,0.4)
        boxobj4.size = vec(0.4,0.1,0.4)
        boxobj5.size = vec(0.4,0.1,0.4)
        boxobj6.size = vec(0.4,0.1,0.4)
        boxobj7.size = vec(0.4,0.1,0.4)
        boxobj8.size = vec(0.4,0.1,0.4)
        boxobj9.size = vec(0.4,0.1,0.4)
        boxobj10.size = vec(0.4,0.1,0.4)
        boxobj11.size = vec(0.4,0.1,0.4)
        boxobj12.size = vec(0.4,0.1,0.4)
        boxobj13.size = vec(0.4,0.1,0.4)
        print("초기화")
