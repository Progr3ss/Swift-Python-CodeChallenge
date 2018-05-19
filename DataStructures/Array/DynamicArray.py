


import ctypes

class DynamicArray:
    
    
    """Create an empty array"""
    def __init__(self):
        
        self._n = 0 
        self._capacity = 1
        self._A = self._make_array(self._capacity)


    def _make_array(self, c):
        
        
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()
    

    def __len__(self):
        """Return element at index k"""
        return self._n

    
    def __getitem__(self, k):
        """Return element at index k"""
        if not 0 <= k < self._n:
            raise indexError('invalid index')
        return self._A[k]
    
    def append(self, obj):
        """Add object to end of the array"""
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1
    def _resize(self,c): 
        """Resize internal array to capacity c """
        B = self._make_array(c)
        for k in range(self._n):
            
             B[k] = self._A[k]
        self._A = B
        self.capacity = c    


   # def insert(self, k, value):
    #    """insert value at index k , shiffiting subsequent values rightward"""
     #   if self._n == self._capacity:
      #      self._resize(2* self._capacity)
       # for j in range(self._n, k,-1):
        #    self._A[j] = self._A[j-1]
        #self._A[k] = value
        #self._n += 1


       
    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
    # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:                  # not enough room
            self._resize(2 * self._capacity)             # so double capacity
        for j in range(self._n, k, -1):                # shift rightmost first
            self._A[j] = self._A[j-1]
        self._A[k] = value                             # store newest element
        self._n += 1
          

Darray = DynamicArray()

Darray.append(9)
Darray.append(5)
print(Darray._make_array(3))
print(Darray.__len__())
print(Darray.__getitem__(0))
Darray._resize(2)
print(Darray.__len__())
print(Darray.insert(2,3 ))

