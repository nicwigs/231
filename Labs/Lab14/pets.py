##
## Class PetError -- complete
##
class PetError( ValueError ):    
    pass
#_------------------------------------------------------------------------
##
## Class Pet -- complete
##
class Pet( object ):
    
    def __init__( self, species=None, name="" ):
        
        pet_lst = ["dog","cat","horse","gerbil","hamster","ferret"]
        if species.lower() in pet_lst:            
            self.species_str = species.title()
            self.name_str = name.title()            
        else:            
            raise PetError()
            
    def __str__( self ):
        if self.name_str:
            result_str = "Species of: {:s}, named {:s}"\
            .format(self.species_str,self.name_str)
        else:
            result_str = "Species of: {:s}, unnamed".format(self.species_str)       
        return result_str
#_------------------------------------------------------------------------
##
## Class Dog --complete
##
class Dog( Pet ):
    def __init__(self,name = "",chases = "Cats"):
        Pet.__init__(self,"dog",name)
        self.chases_str = chases
    
    def __str__(self):
        result_str = Pet.__str__(self)        
        result_str += ", chases {:s}".format(self.chases_str)
        return result_str
#_------------------------------------------------------------------------
##
## Class Cat -- complete
##

class Cat( Pet ):
    def __init__(self,name = "",hates = "Dogs"):
        Pet.__init__(self,"cat",name)
        self.hates_str = hates
    
    def __str__(self):
        result_str = Pet.__str__(self)        
        result_str += ", hates {:s}".format(self.hates_str)
        return result_str
#----------------------------------------------------------------------------