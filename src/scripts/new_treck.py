from vocab_base import vocab
from vocab_color import colorrgb
import math
import random
rad = 6372795  # rad - радиус сферы (Земли)

def chooseRandomColor():
    red = random.random()
    green = random.random()
    blue = random.random()
    return red, green, blue

def meters(llat1, llong1, llat2, llong2):
    # в радианах
    lat1 = llat1 * math.pi / 180.
    lat2 = llat2 * math.pi / 180.
    long1 = llong1 * math.pi / 180.
    long2 = llong2 * math.pi / 180.

    # косинусы и синусы широт и разницы долгот
    cl1 = math.cos(lat1)
    cl2 = math.cos(lat2)
    sl1 = math.sin(lat1)
    sl2 = math.sin(lat2)
    delta = long2 - long1
    cdelta = math.cos(delta)
    sdelta = math.sin(delta)

    # вычисления длины большого круга
    y = math.sqrt(math.pow(cl2 * sdelta, 2) +
                  math.pow(cl1 * sl2 - sl1 * cl2 * cdelta, 2))
    x = sl1 * sl2 + cl1 * cl2 * cdelta
    ad = math.atan2(y, x)
    dist = ad * rad

    return dist

def lenforfway(fway, fir, sec):
    x1 = fway[1::3]
    y1 = fway[0::3]
    z1 = fway[2::3]
    way = 0
    max_high = 0
    min_high = 10000
    for treck in range(fir, sec):
        lWay = meters(x1[treck], y1[treck], x1[treck+1], y1[treck+1])
        way = way + math.sqrt(pow(lWay, 2) + pow(z1[treck] - z1[treck+1], 2))
        if (z1[treck] > max_high):
            max_high = z1[treck]
        if (z1[treck] < min_high):
            min_high = z1[treck]
    return float(round(way)), max_high, min_high    #убрать round для округления

def lenfor(a,fir,sec):
    coordA = vocab[name[a]]
    x1 = coordA[1::3]
    y1 = coordA[0::3]
    z1 = coordA[2::3]
    way = 0
    max_high = 0
    min_high = 10000
    for treck in range(fir, sec):
        lWay = meters(x1[treck], y1[treck], x1[treck+1], y1[treck+1])
        way = way + math.sqrt(pow(lWay, 2) + pow(z1[treck] - z1[treck+1], 2))
        if (z1[treck] > max_high):
            max_high = z1[treck]
        if (z1[treck] < min_high):
            min_high = z1[treck]
    return float(round(way))    #убрать round для округления

def vstavka(spisok, new, index):
    for k in spisok:
        dot = 0
        cash = []
        coordk = vocab[name[k]]
        xk = coordk[1::3]
        yk = coordk[0::3]
        zk = coordk[2::3]
        if new in coordk:
            continue
        else:
            if index[k] == len(xk)-1:
                next = index[k]
                lost = index[k]-1
            else:
                next = index[k]+1
                lost = index[k]    
            if (((xk[next]**2)+(yk[next]**2))**0.5) > (((xk[lost]**2)+(yk[lost]**2))**0.5):
                if (((new[1]**2)+(new[0]**2))**0.5) > (((xk[index[k]]**2)+(yk[index[k]]**2))**0.5):
                    dot = 1
                else: dot = -1
            else:
                if (((new[1]**2)+(new[0]**2))**0.5) > (((xk[index[k]]**2)+(yk[index[k]]**2))**0.5):
                    dot = -1
                else: dot = 1

            for l in range(0, len(xk)):
                if l == index[k]:
                    x = new[1]
                    y = new[0]
                    z = new[2]
                    if dot == -1:
                        cash.append(y)
                        cash.append(x)
                        cash.append(z)
                    cash.append(yk[l])
                    cash.append(xk[l])
                    cash.append(zk[l])
                    if dot == 1:
                        cash.append(y)
                        cash.append(x)
                        cash.append(z)   
                else:
                    cash.append(yk[l])
                    cash.append(xk[l])
                    cash.append(zk[l])
            vocab[name[k]]=cash   

def Deikstra(current, en):
    point = [current,en]
    for i in range(len(vocab)):
        if (current[0] == vocab[name[i]][0] and current[1] == vocab[name[i]][1]) or (current[0] == vocab[name[i]][len(vocab[name[i]])-3] and current[1] == vocab[name[i]][len(vocab[name[i]])-2]):
            point.remove(current)
        if (en[0] == vocab[name[i]][0] and en[1] == vocab[name[i]][1]) or (en[0] == vocab[name[i]][len(vocab[name[i]])-3] and en[1] == vocab[name[i]][len(vocab[name[i]])-2]):
            point.remove(en)

    for a in range(0, len(vocab)):  
        coordA = vocab[name[a]]
        x1 = coordA[1::3]
        y1 = coordA[0::3]
        z1 = coordA[2::3]
        cdots = []
        fin = (y1[len(x1)-1],x1[len(x1)-1])
        for b in range(0, len(vocab)):
            if (b != a):
                coordB = vocab[name[b]]
                x2 = coordB[1::3]
                y2 = coordB[0::3]
                z2 = coordB[2::3]
                min_dist = 50
                index[a] = -1 
                index[b] = -1              
                for i in range(0, len(x1)):
                    for j in range(0, len(x2)):
                        dist = meters(x1[i], y1[i], x2[j], y2[j])
                        if (dist < min_dist):
                            min_dist = dist
                            index[a] = i
                            index[b] = j
                if index[a] != -1:
                    xcros = round((x1[index[a]]+x2[index[b]])/2,6)  
                    ycros = round((y1[index[a]]+y2[index[b]])/2,6)
                    zcros = round((z1[index[a]]+z2[index[b]])/2,6)
                    if (ycros,xcros) not in cdots:
                        vstavka([a,b],[ycros,xcros,zcros],index)
                        cdots.append((ycros,xcros))
                    if (ycros,xcros) not in nodes:
                        nodes.append((ycros,xcros))
        if point != []:                
            for v in point:
                min_dist = 50
                ind = -1 
                for l in range(len(x1)):            
                    dist = meters(x1[l], y1[l], v[1], v[0])
                    if (dist < min_dist):
                        min_dist = dist
                        ind = l
                if ind != -1:
                    if (y1[ind], x1[ind]) not in cdots:
                        cdots.append((y1[ind], x1[ind]))
                    if (y1[ind], x1[ind]) not in nodes:
                        nodes.append((y1[ind], x1[ind]))
                        if v == current:
                            current = (y1[ind], x1[ind])
                        elif v == en: 
                            en = (y1[ind], x1[ind])    

        xcold = (vocab[name[a]][0],vocab[name[a]][1])
        if xcold in cdots:
            cdots.remove(xcold) 
        if cdots != []:  
            while True:
                dots = []
                for s in cdots:
                    weight = lenfor(a, vocab[name[a]][1::3].index(xcold[1]), vocab[name[a]][1::3].index(s[1]))
                    dots.append((weight,s))
                dots = sorted(dots, key=lambda x: x[0])
                if distances.get(xcold) is None:
                    distances[xcold] = {dots[0][1]: dots[0][0]}
                else:
                    distances.get(xcold).update({dots[0][1]: dots[0][0]})
                if distances.get(dots[0][1]) is None:
                    distances[dots[0][1]] = {xcold: dots[0][0]}
                else:
                    distances.get(dots[0][1]).update({xcold: dots[0][0]})
                xcold = dots[0][1]    
                cdots.remove(dots[0][1])
                if not cdots:
                    break

        if fin == xcold:
            pass
        else:
            weight = lenfor(a, vocab[name[a]][1::3].index(xcold[1]), vocab[name[a]][1::3].index(fin[1]))
            if distances.get(xcold) is None:
                distances[xcold] = {fin: weight}
            else:
                distances.get(xcold).update({fin: weight})
            if distances.get(fin) is None:
                distances[fin] = {xcold: weight}
            else:
                distances.get(fin).update({xcold: weight})

    for i in range(0, len(vocab)):
        coordpl = vocab[name[i]]
        xpl = coordpl[1::3]
        ypl = coordpl[0::3]
        for k in [0,len(xpl)-1]:
            if (ypl[k],xpl[k]) not in nodes:
                nodes.append((ypl[k],xpl[k])) 

    unvisited = {node: None for node in nodes}  # using None as +inf
    way = {node: '' for node in nodes}
    visited = {}
    newPath = current # начало пути 
    currentDistance = 0
    path = ''
    unvisited[current] = currentDistance

    while True:
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited:
                continue
            newDistance = currentDistance + distance
            dist = unvisited[neighbour]
            if type(dist) == tuple:
                dist = dist[0]
            if dist is None or dist > newDistance:
                unvisited[neighbour] = newDistance, newPath

        way[current] = newPath
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key=lambda x: x[1][0])[0]
        if type(currentDistance) == tuple:
            path = currentDistance[1]
            currentDistance = currentDistance[0]
        newPath = path + current

    fway = []
    for i in range(0,len(way[en])-3,2):
        for k in range(len(vocab)):
            coord = vocab[name[k]]
            if ((way[en][i] in coord) and (way[en][i+1] in coord)) and ((way[en][i+2] in coord) and (way[en][i+3] in coord)):
                lost = coord.index(way[en][i])
                next = coord.index(way[en][i+3])+2
                
                if lost > next:
                    lost = coord.index(way[en][i])
                    next = coord.index(way[en][i+2])
                    step = -3
                    for j in range(lost,next,step):
                        fway.append(coord[j])
                        fway.append(coord[j+1])
                        fway.append(coord[j+2]) 
                else:       
                    for j in range(lost,next):
                        fway.append(coord[j])     
    return fway


name = [*vocab]
index = {}
distances = {}
nodes = []
en = (92.866336,55.929076)
st = (93.0707,55.9177)

fway = Deikstra(st,en)


# # для вывода инфы о построенном маршруте
# lenght, max_tr, min_tr = lenforfway(fway, 0, int(len(fway)/3)-1)
# print("Min = ", min_tr)
# print("Max = ", max_tr)
# print("len = ", lenght)

# #for android studio
# lat = fway[1::3]
# lon = fway[0::3]

# # для строки без []
# strlat = str(lat)[1:]
# strlat = strlat[:-1]
# strlon = str(lon)[1:]
# strlon = strlon[:-1]
""" file1 = open("treck.kt", "w")
file1.write('val lat: Array<Double> = arrayOf(' + str(strlat) + ')\n')
file1.write('val lon: Array<Double> = arrayOf(' + str(strlon) + ')')
file1.close() """
