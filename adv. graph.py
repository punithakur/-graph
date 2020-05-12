class node:
    def __init__(self, data):
        self.data=data
        self.next=[]

class SN_graph:
    def __init__(self,index=None):
        self.head=[]
        self.head.append(index)

    def exchange(self,a,b):
        a.next.append(b)
        b.next.append(a)

    def find(self,a):
        for i in range(1,len(self.head)):
            if a==self.head[i].data:
                return self.head[i]
        else:
            return None
    
    def insert(self,a):
        ad=node(a)
        self.head.append(ad)
        return ad

    def finding(self,x,y):
        global x_add
        global y_add
        x_add=self.find(x)
        y_add=self.find(y)
        if(x_add):
            pass
        else:
            x_add=self.insert(x)
        if(y_add):
            pass
        else:
            y_add=self.insert(y)
        self.exchange(x_add,y_add)

    def graph(self,x,y):
        global x_add
        global y_add
        if(len(self.head)>1):
            self.finding(x,y)
        else:
            x_add=self.insert(x)
            y_add=self.insert(y)
            self.exchange(x_add,y_add)

    def printing(self):
        for i in range(1,len(self.head)):
            
            print("node data--",self.head[i].data)
            try:
                for j in range( len(self.head[i].next)):
                    
                    print("node connected from--", self.head[i].next[j].data)
            except Exception:
                pass
    def searching(self, k,l):
        for i in range(1, len(self.head)):
            if self.head[i].data==k:
                for j in range(1,l):
                    d=self.head[i].next[j]
                    h=self.distance(d)
                    try:
                        for f in h:
                            print(l, "dis node", f.data)
                    except Exception:
                        print("no data found")
                if l==1:
                    for f in self.head[i].next:
                        print(l,"dis node",f.data)


    def distance(self,x):
        x=x.next
        if len(x)>=1:
            return x
x_add=None
y_add=None
app=SN_graph()
while True:
    print("1. insert the node")
    print("2. print all the nodes")
    print("3. searching node")
    n=int(input())
    if n==1:
        a=int(input("enter first value--"))
        s=int(input("enter secound value--"))
        app.graph(a,s)
    elif n==2:
        app.printing()
    elif n==3:
        k=int(input("node value where u want to search--"))
        l=int(input("how many distance--"))
        app.searching(k,l)
