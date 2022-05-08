
class StackInteger():
    def __init__(self,list=[]):
        self.elements = list

    def delete(self) ->None:
        """Delete the first element of the stack!"""
        self.elements.pop(0)

    def delete_last(self)->None:
        """Delete the last element of the stack!"""
        self.elements.pop(self.size()-1)

    def addElement(self,data)->None:
        """Add an element to the stack!
        Args:
            data: The element you want to add to the stack must be an integer!"""
        if type(data) !=int:
            raise TypeError("Type must be int") 
        self.elements.insert(0,data)


    def elementAt(self,position)->int:
        """Return the element at the position you want!
        Args:
            position: The position you want to get the element from!"""
        return self.elements[position]

    def lastElement(self)->int:
        """Return the last element of the stack!"""
        return self.elements[self.size()-1]

    def smartSum(self,duplicate=False)->int:
        """Return the sum of the elements of the stack!
        Args: optional:
            duplicate: If you want to sum the duplicates or not!
            must be a boolean!"""
        temp=self.elements
        if duplicate==True:
            temp=list(set(temp))
        sumvalue=0
        for elements in temp:
            sumvalue+=elements
        return sumvalue

    def smatAdd(self,data)->int:
        """Add an element to the stack with duplicate check!
        Args:
            data: The element you want to add to the stack must be an integer!"""
        if type(data) !=int:
            raise TypeError("Type must be int")  
        if data in self.elements:
            return False
        else:
            self.elements.insert(0,data)

    def size(self):
        """Return the size of the stack!"""
        return len(self.elements)

    def sort(self) ->object:
        """Sort the elements of the stack!"""
        for first in range(self.size()):
            for second in range(first+1,self.size()):
                if self.elements[second]<self.elements[first]:
                    self.elements[first],self.elements[second]=self.elements[second],self.elements[first]
        return StackInteger(self.elements)
        



    def count(self,data) ->int:
        """Return the number of the data you want to count!
        Args:
            data: The data you want to count!"""

        if type(data) !=int:
            raise TypeError("Type must be int") 
        counter=0
        for elements in self.elements:
            if elements==data:
                counter+=1
        return counter

    def indexOf(self,data=int) ->int:
        """Return the index of the data you want to find!
        Args:
            data: The data you want to find!
            Returns:
                The index of the data you want to find!
                If the data is not in the stack, it will return -1!"""

        if type(data) !=int:
            raise TypeError("Type must be int")
        for index in range(self.elements.size()):
            if self.elements[index]==data:
                return index
        return -1

    def clear(self)->None:
        """Clear the stack!"""
        self.elements=[]
    
    def deleteAllCopy(self,data)->None:
        """Delete all the copies of the data you want to delete!
        Args:
            data: The data you want to delete!"""
        if type(data) !=int:
            raise TypeError("Type must be int") 
        while self.elements.count(data)>0:
            self.elements.remove(data)

    def tolist(self)->list:
        """Return the elements of the stack as a list!"""
        return self.elements

    def delete_duplicate(self):
        """Delete the duplicates of the stack!"""
        return StackInteger(list(set(self.elements)))

    def reverse(self):
        """Reverse the elements of the stack!"""
        return StackInteger(self.elements.reverse())

    
    def smartsort(self,duplicate=False,reverse=False) -> object:
        """Sort the elements of the stack!
        Args: optional:
            duplicate: If you want to sort the duplicates or not!
            must be a boolean!
            reverse: If you want to reverse the elements of the stack!
            must be a boolean!"""

        if duplicate==True:
           self.elements=self.delete_duplicate()
        self.elements=self.sort()
        
        if reverse==True:
            self.reverse()
        return StackInteger(self.elements)

    def convertListToStack(self,list,smart=False,duplicated=False) -> object:
        """Convert a list to a stack!
        Args:
            list: The list you want to convert!
            smart: If you want to sort the elements of the stack (with smart sort) so you can delete duplicate!"""
        self.elements=list
        if smart==True:
            self.smartsort(duplicated,smart)
        return StackInteger(self.elements)


    def __str__(self):
        return str(self.elements)

    def __repr__(self):
        return str(self.elements)

    def __len__(self):
        return len(self.elements)


    def __iter__(self):
        return iter(self.elements)





