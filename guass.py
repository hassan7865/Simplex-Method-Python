def matrix():
    for i in sd:
        print("\n")
        for j in i:
            print(j,end="\t\t")
            

sd=[[-10,-8,0,0,0,0],
    [2,2,1,0,0,140],
    [1,2,0,1,0,120],
    [3,1,0,0,1,150]
    ]   
def getone(a,e):
    for i in range(len(sd[0])):
        if sd[a][e]!=1:
            pivot=sd[a][e]
            for j in range(len(sd[0])):
                    sd[a][j]=sd[a][j]/pivot
                          
def getzero(a,r,c):
    for i in range(len(sd[0])):
        if sd[r][c]!=0:
            element=sd[r][c]
            for j in range(len(sd[0])):
                sd[r][j]=sd[r][j]-((sd[a][j])*element)
while True:
    
    a=int(input("Enter Row:"))
    e=int(input("Enter Column:"))
    getone(a,e)
    v=[]
    for i in range(len(sd)):
        v.append(i)
    v.remove(a)
    for k in v:
        getzero(a,k,e)
    matrix()
    print("\n")
