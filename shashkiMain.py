

#1-black
#2-white
#0-nothing

positions={1:{1:2, 3:2, 5:0, 7:1}, 2:{2:2, 4:0, 6:1, 8:1},3:{1:2, 3:2, 5:0, 7:1}, 4:{2:2, 4:0, 6:1, 8:1}, 5:{1:2, 3:2, 5:0, 7:1}, 6:{2:2, 4:0, 6:1, 8:1}, 7:{1:2, 3:2, 5:0, 7:1}, 8:{2:2, 4:0, 6:1, 8:1},}


def bios(text):
    data=list(text)
    for i in data:
        data[data.index(i)]=int(i)
    print(data)
    if positions[data[2]][data[3]]==0 and (abs(data[0]-data[2])==1 and abs(data[1]-data[3])==1) and (positions[data[0]][data[1]]==2):
        positions[data[2]][data[3]]=2
        positions[data[0]][data[1]]=0
    print(step())



def step():
    black=[]
    white=[]
    for i in positions.keys():
        for a in positions[i].keys():
            if positions[i][a]==1:
                black.append([i, a])
    for i in positions.keys():
        for a in positions[i].keys():
            if positions[i][a]==2:
                white.append([i, a, 0, 0, 0])

    
    for i in black:
        if i[0]-1 in positions.keys():
            if i[1]-1 in positions[i[1]-1].keys():
                if positions[i[0]-1][i[1]-1]==0:
                    black[2]=i[0]-1
                    black[3]=i[1]-1
                    positions[i[0]][i[1]]=0
                    positions[i[0]-1][i[1]-1]=1
                    return str(i[0])+str(i[1])+str(i[0]-1)+str(i[1]-1)
                if   i[1]+1 in positions[i[1]-1].keys():
                    if positions[i[0]-1][i[1]+1]==0:
                         black[2]=i[0]-1
                         black[3]=i[1]+1
                         positions[i[0]][i[1]]=0
                         positions[i[0]-1][i[1]+1]=1
                         return str(i[0])+str(i[1])+str(i[0]-1)+str(i[1]+1)
        




while 1:
    bios(input("your move:"))
