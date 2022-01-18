class animal:
    think="we are animal ,we cant think like human"  # class attribute

    # constractor
    def __init__(self):
        print("parent animal class")
        self.__ear()

    # protect function
    def _hair(self,animalName):
        self.animalName=animalName
        print("i am {} i have leather".format(self.animalName))

#get and set functions we can use it in encapslution too
    def setNeck(self,neck ):
        self.neck = neck

    def getNeck(self):
        print("it has {} nick ".format(self.neck))

   #private function
    def __ear(self):
        print("all these animal have ears")

#inhertance multilevel
class dogs(animal):
    #constractor
    def __init__(self):
         print(animal.think + "  hmm but i am a dog and i am sincerely(:" )

   #Destructor
    def __del__(self):
        print(" dog destractor")
#abstract function in abstract class
    def color(self):
        pass

    def walk(self):
        print(" i am  walk in four legs  ")

    def voice(self, animalName,ability):
        print("i am  in dog class the {0} it  {1} make voice".format(self.animalName,self.ability))


class  giraffe(dogs):
    print(" i am in giraffe class ")
    '''  '''
    def voice(self, animalName,ability):
        self.animalName = animalName
        self.ability = ability
        print("i am in polymrphizme function to say the {0} it {1} make voice".format(self.animalName,self.ability))

    # reuse abstract method
    def color(self):
        print("i has berty color")


graffObj=giraffe()  # make object from giraffe class
graffObj.voice("gariff","can not")
graffObj.walk() ## giraffe inhert walk from dogs clss
graffObj._hair("gariff")
graffObj.setNeck("tall")
graffObj.getNeck()



