import math
import time,random


# Define the function to update the timer with the current time as input for the function

def update_timer(timer, timer_label):
    temptime = time.time()
    deltatime = temptime - timer
    milisec = deltatime % 1
    sec = int(deltatime % 60)
    min = int(deltatime / 60)
    timer_label.config(text=f"{min:02}:{sec:02}.{int(milisec*100):02}")
    timer_label.after(1, update_timer, timer, timer_label)

# Define the function to move the square along the points in the points array
def move_square(canvas, squarearray, points):
    if(len(squarearray)==0):
        canvas.after(10, move_square, canvas, squarearray, points)
        return  #no squares to target

    for i in range(len(squarearray)):
        square,health,speed,targetpoint,effect,hbar = squarearray[i]["sq"],squarearray[i]["health"],squarearray[i]["speed"],squarearray[i]["targetpoint"],squarearray[i]["effect"],squarearray[i]["h_bar"]      
        #use delta and speed to move the square
        
        x1, y1, x2, y2 = canvas.coords(square)
        x, y = points[targetpoint]
        x = x * 50+25
        y = y * 50+25
        distx = x - x1+(x1 - x2) / 2 + random.randint(-10,10)
        disty = y - y1+(y1 - y2) / 2 + random.randint(-10,10)
        
        dist = math.sqrt(math.pow(distx,2) + math.pow(disty,2))
        deltax=0
        deltay=0
        if(effect[0]=="slowed"):
            speed=2
            effect[1]=effect[1]-1
            if(effect[1]<=0):
                effect[0]=""
        if dist>speed:          
            deltax = speed * distx/dist
            deltay = speed * disty/dist
        else:
            squarearray[i]["targetpoint"] = (targetpoint + 1) 
            if(targetpoint==len(points)-1):
                canvas.coords(square, -100, -100, -100+30, -100+30)
                canvas.coords(hbar, -100, -100, -100+30, -100+30)
                squarearray[i]["targetpoint"]=-1
        x1=x1+int(deltax)
        y1=y1+int(deltay)
        canvas.coords(square, x1, y1, x1+30, y1+30)
        canvas.coords(hbar,x1,y1-6,x1+int(30*health/100),y1-1)
        canvas.tag_raise(square)
        canvas.tag_raise(hbar)
    for square in squarearray:
        if(square["targetpoint"]<0):
            canvas.delete(square["sq"])
            canvas.delete(square["h_bar"])
            squarearray.remove(square)
    canvas.after(100, move_square, canvas, squarearray, points)

def draw_map(canvas, map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 1:
                canvas.create_rectangle(j*50, i*50, j*50+50, i*50+50, fill="black") # Draw a black rectangle


def removeline(canvas,turretarray):
    for turret in turretarray:
        line= turret["line"]
        canvas.coords(line,0,0,0,0)


def target(canvas, squarearray, turretarray):
    if(len(squarearray)==0):
        removeline(canvas,turretarray)
        canvas.after(10, target, canvas, squarearray, turretarray)
        return  #no squares to target
    for turret in turretarray:
        tx= turret["x"]
        ty= turret["y"]
        type= turret["type"]
        line= turret["line"]
        trange= turret["dist"]
        lasttarget= turret["lasttarget"]
        maxloadtime= turret["maxloadtime"]
        closest=0
        closestdist=trange*2
        for i in range(len(squarearray)):
            square = squarearray[i]["sq"]
            x1, y1, x2, y2 = canvas.coords(square)
            dist = math.sqrt(math.pow(tx - (x1 + x2) / 2, 2) + math.pow(ty - (y1 + y2) / 2, 2))
            if dist < closestdist:
                closest = i
                closestdist = dist
        if(len(squarearray)==0):
            canvas.after(10, target, canvas, squarearray, turretarray)
            return  #no squares to target
        if(closestdist>trange):
           canvas.coords(line,0,0,0,0)
        else:
            if(closest==lasttarget):
                if(turret["loadtime"]>0):
                    turret["loadtime"]=turret["loadtime"]-1
                else:
                    #fire
                    sqcl=squarearray[closest]["sq"]
                    canvas.coords(line,tx, ty, (canvas.coords(sqcl)[0] + canvas.coords(sqcl)[2]) / 2, (canvas.coords(sqcl)[1] + canvas.coords(sqcl)[3]) / 2)
                    match(type):
                        case 1:
                            squarearray[closest]["health"]=squarearray[closest]["health"]-30
                        case 2:
                            if(squarearray[closest]["effect"][0]!="slowed"):
                                squarearray[closest]["effect"]=[squarearray[closest]["effect"][0]+"slowed",10]
                            else:
                                squarearray[closest]["effect"][1]=10
                    turret["loadtime"]=maxloadtime
            else:
                turret["loadtime"]=maxloadtime
                pass
            if(squarearray[closest]["health"]<=0):
                canvas.delete(sqcl)
                canvas.delete(squarearray[closest]["h_bar"])
                squarearray.pop(closest)
    canvas.after(10, target, canvas, squarearray, turretarray)

# Start the main loop
def on_click(event,squarearray,turretarray,canvas,buttons):
    # Code to handle the onclick event
    x=event.x
    y=event.y
    if("shift" in buttons):
        turretarray.append({"x":x,"y":y,"type":random.randint(1,3),"line":canvas.create_line(0,0,0,0,fill="red"),"dist":100,"lasttarget":0,"maxloadtime":10,"loadtime":10})
#        turretarray.append([x,y,random.randint(1,5),canvas.create_line(0,0,0,0,fill="red"),100,0])

    else:
        squarearray.append({"sq":canvas.create_rectangle(x, y, x+30, y+30, fill="red"),"health":100,"speed":70,"targetpoint":0,"effect":["",0],"h_bar":canvas.create_rectangle(100, y-6, 30, y-1, fill="green")})    
    pass
def on_key_up(event,buttons):
    # Code to handle the onkeyup event
    if(event.keysym=="Shift_L"):
        if "shift" in buttons:
            buttons.remove("shift")
    pass

def on_key(event,buttons):
    # Code to handle the onkey event
    if(event.keysym=="Shift_L"):
        if "shift" not in buttons:
            buttons.append("shift")
    pass