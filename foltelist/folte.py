import os
class folteError(Exception):
    pass
class plus:
    def __init__(self,data):
        self.data=data
class minus:
    def __init__(self,data):
        self.data=data
class multi:
    def __init__(self,data):
        self.data=data
class division:
    def __init__(self,data):
        self.data=data
class recurring:
    def __init__(self,data):
        self.data=data
class suuzi:
    def __init__(self):
        self.data=0
        self.sosa=[]
    def __str__(self):
        return str(self.data)
    def __getitem__(self, key):
        if type(key)==plus:
            self.data+=key.data
        if type(key)==minus:
            self.data-=key.data
        if type(key)==multi:
            self.data*=key.data
        if type(key)==division:
            self.data/=key.data
        if type(key)==recurring:
            self.data=self.data**key.data
        if key=="get":
            return self.sosa
        else:
            self.sosa.append(key)
    def __setitem__(self,key,val):
        if key=="plus":
            self.data+=val
            self.sosa.append(plus(val))
        if key=="minus":
            self.data-=val
            self.sosa.append(minus(val))
        if key=="multi":
            self.data*=val
            self.sosa.append(multi(val))
        if key=="division":
            self.data/=val
            self.sosa.append(division(val))
        if key=="set":
            self.data=val
            self.sosa=[]
class lile:
    def __init__(self,path):
        self.path=path
        if not os.path.exists(path):
            raise folteError("File does not exist")
    def __getitem__(self,key):
        if key=="read":
            return open(self.path,"r").read()
        elif key=="file":
            return self.path
    def __setitem__(self,key,val):
        if key=="add":
            open(self.path,"a").write(val)
        elif key=="write":
            open(self.path,"w").write(val)

