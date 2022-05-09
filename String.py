


class SmartString():
    def __init__(self, string):
        self.string = string
    
    def TokenizerAsList(self, delimiter) -> list:
        temp_str=""
        temp_list=[]
        for elements in self.string:
            if elements !=delimiter: 
                temp_str+=elements
            else:
                temp_list.append(temp_str)
                temp_str=""
        if temp_str!="":
            temp_list.append(temp_str)
        return temp_list
    def SmartRemoveCounter(self,data,counter):
        if type(counter) !=int:
            raise TypeError("Type must be int")
        temp_counter=0
        temp_str=""
        for elements in self.string:
            if (elements==data) and (temp_counter<counter):
                temp_counter+=1
            else:
                temp_str+=elements
        self.string=temp_str
    
    def Remove(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        self.string=self.string.replace(data,"")

    def RemoveNumbers(self):
        temp_str=""
        for elements in self.string:
            if elements not in "0123456789":
                temp_str+=elements

        self.string=temp_str


    def RemoveSpaces(self):
        temp_str=""
        for elements in self.string:
            if elements not in " ":
                temp_str+=elements
    
    def Reverse(self):
        self.string=self.string[::-1]

    def Count(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        counter=0
        for elements in self.string:
            if elements==data:
                counter+=1
        return counter

    def IndexOf(self,data):
        for index in range(len(self.string)):
            if self.string[index]==data:
                return index
        return -1

    def RemoveDuplicates(self):
        temp_str=""
        for elements in self.string:
            if elements not in temp_str:
                temp_str+=elements
        self.string=temp_str

    def SmartSumWithoutDuplicate(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be int")
        self.string=self.string+data
        self.string.RemoveDuplicates()

    def UpperSingleLetter(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        self.string=self.string.replace(data,data.upper())

    def LowerSingleLetter(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        self.string=self.string.replace(data,data.lower())
    
    def capitalize(self):
        self.string=self.string.capitalize()
    
    def casefold(self):
        self.string=self.string.casefold()
    
    def center(self,data,qwery):
        if type(data) !=int:
            raise TypeError("Type must be int")
        if type(qwery) !=str:
            raise TypeError("Type must be str")
        self.string=self.string.center(data,qwery)
    
    def encode(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        self.string=self.string.encode(data)

    def endswith(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        return self.string.endswith(data)
    
    def expandtabs(self,data):
        if type(data) !=int:
            raise TypeError("Type must be int")
        self.string=self.string.expandtabs(data)

    def find(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        return self.string.find(data)
    
    def format(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        self.string=self.string.format(data)
    
    def format_map(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        self.string=self.string.format_map(data)
    
    def index(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        return self.string.index(data)
    
    def isalnum(self):
        return self.string.isalnum()
    
    def isalpha(self):
        return self.string.isalpha()
    
    def isdecimal(self):
        return self.string.isdecimal()

    def isdigit(self):
        return self.string.isdigit()
    
    def isidentifier(self):
        return self.string.isidentifier()
    
    def islower(self):
        return self.string.islower()
    
    def isnumeric(self):
        return self.string.isnumeric()
    
    def isprintable(self):
        return self.string.isprintable()
    
    def isspace(self):
        return self.string.isspace()
    
    def istitle(self):
        return self.string.istitle()
    
    def isupper(self):
        return self.string.isupper()

    def join(self,data):
        if type(data) ==str or type(data) ==int or type(data) ==float or type(data) ==bool:
            raise TypeError("Type must not be str or int or float or bool")
        self.string=self.string.join(data)
    
    def ljust(self,data,qwery):
        if type(data) !=int:
            raise TypeError("Type must be int")
        if type(qwery) !=str:
            raise TypeError("Type must be str")
        self.string=self.string.ljust(data,qwery)
    
    def lower(self):
        self.string=self.string.lower()
    
    def lstrip(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        self.string=self.string.lstrip(data)
    
    
    def partition(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        self.string=self.string.partition(data)

    def rfind(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        self.string=self.string.rfind(data)
    
    def rindex(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        self.string=self.string.rindex(data)
    
    def rjust(self,data,qwery):
        if type(data) !=int:
            raise TypeError("Type must be int")
        if type(qwery) !=str:
            raise TypeError("Type must be str")
        self.string=self.string.rjust(data,qwery)
    
    def rpartition(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        self.string=self.string.rpartition(data)
    
    def rsplit(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        self.string=self.string.rsplit(data)
    
    def rstrip(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        self.string=self.string.rstrip(data)
    
    def split(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        return self.string.split(data)
    
    
    
    def startswith(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        return self.string.startswith(data)
    
    def smartstartswith(self,data):
        if not isinstance(data,str):
            raise TypeError("Type must be str")
        return self.string.upper().startswith(data.upper())

    def __str__(self):
        return str(self.string)
    
    def convertToString(self):
        return self.string

    def concat(self,*args):
        for i in args:
            try:
                self.string+=i
            except Exception as e:
                raise e
        return self.string

    def __len__(self):
        return len(self.string)



    def __add__(self,*args):
        for other in args:
            if type(other) ==str:
                self.string+=other
            elif type(other) ==SmartString:
                self.string+=other.string
            else:
                raise TypeError("Type must be str or SmartString")

        return SmartString(self.string)




    
    
    




