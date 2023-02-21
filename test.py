
n=int(input())
maze=[list(input()) for i in range(n)]
flag=True # Flag to notify if Kate cant get out
spaces=[] # possible spaces to move to
steps=0

#find Kate
for i in range(n):
    if 'k' in maze[i]:
        k_idx=[i,maze[i].index(('k'))]

maze[k_idx[0]][k_idx[1]]=' '    # make the space ocupied by Kate as a free space to move over
                                # in case a closed path was chosen and a new one is needed
visited=[[k_idx[0], k_idx[1]]]  # all spaces that Kate has visited
def find_space(k,ma):
    s_u=[] # space up .. etc...
    s_r=[]
    s_d=[]
    s_l=[]
    if k[0]!=0 and ma[k[0]-1][k[1]]==' ': s_u+= [k[0]-1,k[1]]
    if k[1]<(len(ma[k[0]])-1) and ma[k[0]][k[1]+1]==' ': s_r+=[k[0],k[1]+1]
    if k[0]<(len(ma)-1) and ma[k[0] + 1][ k[1]] == ' ': s_d+=[k[0] + 1, k[1]]
    if k[1]!=0 and ma[k[0]][ k[1] - 1] == ' ':  s_l+=[k[0], k[1] - 1]
    return [s_u,s_r,s_d,s_l] # list of available spaces in each direction , busy spaces are empty

def move(k,s,v,maze,m):
    for i in range(len(s)): # all available spaces around kate
        if s[i] not in v and bool(s[i]):    #if the space is not visited and is free
            k=s[i]                         #Kate moves there
            v.append(s[i])
            m+=1
            # print(k,v,m)
            return k,v,m
        elif all(i in v for i in list(filter(lambda x : bool(x),s))) and k[0]==n-1:
            k[0]=n
            return k,v,m
        elif all(i in v for i in list(filter(lambda x : bool(x),s))):
            maze[k[0]][k[1]]='@'
            k = v[-2]
            del v[-1]
            m-=1
            # print(k,v,m)
            return k,v,m




while k_idx[0]<=(n-1):

    spaces=find_space(k_idx,maze)
    if not sum((lambda x : bool(x))(x) for x in spaces) and k_idx[0]<(n-1): # if there are no free spaces around and we are not on the last line
        print("Kate cannot get out")
        # print(maze)
        flag=False
        break

    k_idx, visited, steps = move(k_idx,spaces,visited,maze,steps)



if flag:
    print(f"Kate got out in {steps+1} moves")






