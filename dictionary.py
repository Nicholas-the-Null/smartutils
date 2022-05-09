class dictionary(dict):
    def __init__(self):
        self.dict={}

    def smartAdd(self, key, value,replace=False):
        if self.dict.get(key)==None or replace==True:
            self.dict[key]=value
        else:
            self.dict[key]=self.dict[key]+value

    def SumAll(self):
        sum=0
        for key in self.dict:
            if type(self.dict[key]) is int:
                sum+=self.dict[key]
        return sum
    
    def clear(self):
        self.dict={}

    def copy(self,other):
        self.dict=other.dict

    def __str__(self):
        return str(self.dict)


    def concat(self,*args,smart=False):
        for arg in args:
            if type(arg) is not dict:
                raise TypeError("Type must be dict")
            for key in arg:
                if smart==True:
                    self.smartAdd(key,arg[key],replace=True)
                else:
                    self.dict[key]=arg[key]
    
    def get(self,key):
        return self.dict[key]

    def clear(self):
        self.dict={}

    def fromkeys(self,keys,value=None):
        if type(keys) is not list or type(keys) is not tuple:
            raise TypeError("Type must be list or tuple")
        for key in keys:
            self.dict[key]=value
    
    def items(self)->list:
        items_list=[]
        for keys in self.dict:
            items_list.append(self.dict[keys])
        return items_list

    def __len__(self):
        return len(self.dict)

    def __contains__(self,key):
        return key in self.dict
    
    def __getitem__(self,key):
        return self.dict[key]
    


        
    
    def keys(self)->list:
        keys_list=[]
        for keys in self.dict:
            keys_list.append(keys)

    def pop(self,key):
        return self.dict.pop(key)

    def popitem(self):
        return self.dict.popitem()
    
    def setdefault(self,key,value):
        self.dict.setdefault(key,value)
    
    def update(self,other):
        self.dict.update(other)
    

    def sort(self):
        return {k: v for k, v in sorted(self.dict.items(), key=lambda item: item[1])}

    



    
    



