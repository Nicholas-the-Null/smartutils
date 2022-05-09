class Link(str):
    #get parameters
    def __init__(self,data):
        self.data=data
        if type(self.data) !=str:
            raise TypeError("Type must be str")

    def spliLink(self)->list:
        temp_list=[]
        temp_str=""
        for elements in self.data:
            if elements !="/":
                temp_str+=elements
            else:
                temp_list.append(temp_str)
                temp_str=""
        if temp_str!="":
            temp_list.append(temp_str)
        return temp_list

    def getLink(self)->str:
        return self.data    
    
    def setLink(self,data):
        self.data=data

    def getMain(self,fullstop)->str:
        temp_str=""
        for elements in self.data:
            if self.data[:-len(fullstop)-1]==fullstop:
                return temp_str
            else:
                temp_str+=elements
        return temp_str

    def toString(self)->str:
        return self.data
    
   



    


    def getExtension(self)->str:
        temp_str=""
        add_all=""
        addelement=False
        for elements in self.data:
            add_all+=elements
            if addelement==True:
                temp_str+=elements
            if (elements=="." and add_all[-1]!="/" and add_all[:-3]!="www"): 
                addelement=True
            if elements=="/":
                addelement=False
            
        add_all=""
        addelement=False
        for x in temp_str:
            if addelement==True and x!="/":
                add_all+=x
            if x==".":
                addelement=True
            if x=="/" or x=="?" or x=="#" or x=="@" or x=="%" or x=="&" or x=="+" or x=="=" or x=="$" or x=="-" or x=="_" or x=="~" or x=="!" or x=="*" or x=="'" or x=="(" or x==")" or x=="[" or x=="]" or x=="{" or x=="}":
                addelement=False

        add_all_second=""
        for x in add_all[::-1]:
            if x==".":
                break
            else:
                add_all_second+=x

        return "."+add_all_second[::-1]

    def __str__(self):
        return self.data

    def __repr__(self):
        return self.data
    
    def __len__(self):
        return len(self.data)
        





