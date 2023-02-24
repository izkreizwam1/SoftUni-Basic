n=int(input())
maze=[list(filter(lambda x : (x!=' '),input())) for i in range(n)]

spaces=[] # possible spaces to move to
score=[0]

def find_k (p, ma):
    k=0
    for i in range(p):  #find Kate
        if '.' in ma[i]:
            k=[i,ma[i].index(('.'))]
            break
    if k : return k
    else: return k


def find_space(k,ma):
    s_u=[] # space up .. etc...
    s_r=[]
    s_d=[]
    s_l=[]
    if k[0]!=0 and ma[k[0]-1][k[1]]=='.': s_u+= [k[0]-1,k[1]]
    if k[1]<(len(ma[k[0]])-1) and ma[k[0]][k[1]+1]=='.': s_r+=[k[0],k[1]+1]
    if k[0]<(len(ma)-1) and ma[k[0] + 1][ k[1]] == '.': s_d+=[k[0] + 1, k[1]]
    if k[1]!=0 and ma[k[0]][ k[1] - 1] == '.':  s_l+=[k[0], k[1] - 1]
    return [s_u,s_r,s_d,s_l]    # list of available spaces in each direction , busy spaces are empty,
                                # Edge spaces are covered separatly


k_idx=find_k(n, maze)
available=[k_idx]
visited=[k_idx]

while bool(k_idx):

    spaces=find_space(k_idx,maze)
    spaces= list(filter(lambda x : bool(x),spaces))
    available+=spaces
    kt = set(tuple(i) for i in available)
    available=list(list(i) for i in kt)
    if not all(i in visited for i in available):
        k_idx = list(filter((lambda x: bool(x not in visited)), available))[0]
        visited.append(k_idx)
    else:
        score.append(len(visited))
        for i in visited:
            maze[i[0]][i[1]]='-'
        k_idx=find_k(n,maze)
        visited=[k_idx]
        available = [k_idx]

print(f"{sorted(score)[-1]}")