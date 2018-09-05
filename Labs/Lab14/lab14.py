##
## Demonstrate some of the operations of the Pet classes
##

import pets

    
try:

    # Hamster
    A = pets.Pet( "Hamster" )
    print( A )           
    # Dog named Fido who chases Cats
    B = pets.Dog( "Fido" )
    print( B )
    # Cat named Fluffy who hates everything
    C = pets.Cat( "Fluffy", "everything" )
    print( C )    
    #horse
    D = pets.Pet("Horse","Bill")
    print(D)   
    #dog named Spot who chases birds
    E = pets.Dog("Spot","birds")
    print(E)
    #stray cat
    G = pets.Cat()
    print( G ) 
    #fish -- error
    F = pets.Pet("Fish","barry")
    print(F)

except pets.PetError:
    
    print( "Got a pet error." )


