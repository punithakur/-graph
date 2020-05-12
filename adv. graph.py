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
        return ad

    def finding(x,y):
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



x_add=None
y_add=None

app=SN_graph()
while True:
    print("1. insert the node")
    print("2. print all the nodes")
    n=int(input())
    if n==1:
        a=int(input("enter first value"))
        s=int(input("enter secound value"))
        app.graph(a,s)
    elif n==2:
        pass

