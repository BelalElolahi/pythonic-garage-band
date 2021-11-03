from abc import ABC, abstractmethod 
class Band : 
     instances = []
    
     def __init__(self,name, members=[]) :
         self.members= members
         self.name = name
         Band.instances.append(self)
         
         
     
     
     def play_solos(self):
        solo = []
        for member in self.members:
            solo.append(member.play_solo())

        return solo
             
     def __str__(self):
        return f"The band {self.name}"

     def __repr__(self):
        return f"The band instance with name = {self.name}, members = {self.members}"
    
    
     @classmethod
     def to_list(cls):
       return cls.instances
  

class Musician : 
     musician_list =[]

     def __init__(self, name):
         self.name= name         
     
     @classmethod
     def get_members(self):
         return self.musician_list  
     
     @abstractmethod
     def get_instrument(self):
         pass
     @abstractmethod   
     def play_solo(self) :
         pass  
     @abstractmethod      
     def __str__(self) :
         pass    
     @abstractmethod      
     def __repr__(self): 
         pass   

class Guitarist(Musician) : 

    
     def __init__(self, name):
         self.name=name
         super().__init__(name)    
     
     def get_instrument(self):
         return "guitar"
     
     def play_solo(self) :
         return f"face melting guitar solo"
     
     def __str__(self) :
        return str(f"My name is {self.name} and I play guitar")    
     
     def __repr__(self): 
         return str(f"Guitarist instance. Name = {self.name}")    
        


class Bassist(Musician) : 
    
    def __init__(self, name):
         self.name=name
         super().__init__(name)       
    
    def get_instrument(self):
         return "bass"
    def play_solo(self) :
           return f"bom bom buh bom" 
    def __str__(self) :
        return str(f"My name is {self.name} and I play bass")    
     
    def __repr__(self): 
         return str(f"Bassist instance. Name = {self.name}")  


class Drummer(Musician) : 
    
    def __init__(self, name):
         self.name=name
         super().__init__(name)     

    def get_instrument(self):
        return "drums"
    def play_solo(self) :
         return f"rattle boom crash" 
    
    def __str__(self) :
        return str(f"My name is {self.name} and I play drums")    
     
    def __repr__(self): 
         return str(f"Drummer instance. Name = {self.name}")  
 


