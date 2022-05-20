
def spanningtree(V,adj):
    p=[]
    r=[]
    def make(v):
        p[v]=0
        r[v]=0
    def find(v):
        if v==p[v]:
            return v
        p[v] = find(p[v])
        return p[v]
    def unions(a,b):
        a = find(a)
        b = find(b)
        if a!=b:
            if r[a]<r[b]:
                a,b=b,a
            p[b]=a
            if r[a] == r[b]:
                r[a]+=1

    v = []
    for i in range(V):
        t = []
        for j in range(len(adj[i])):
            x = adj[i][j]
            t.append(x[1])
            t.append(min(i,x[0]))
            t.append(max(i,x[0]))
            v.append(t)
            t.clear()
    v.sort()
    g = []
    for i in range(len(v)):
        g.append(v[i])

    c=0
    p.res

