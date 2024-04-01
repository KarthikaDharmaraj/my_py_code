class family():
    def __init__(self):
        husband=""
        wife=""
        kids=""
    def display(self):
       print("Family members of "+self.husband+" are "+self.wife+", "+self.kids)

arun=family()
dharma=family()
rajen=family()

arun.husband="ARUN"
arun.wife="KARTHIKA"
arun.kids="ANANYA AND ADVAITHA"

dharma.husband="DHARMARAJ"
dharma.wife="KALAVATHY"
dharma.kids="KARTHIKA AND KARTHIK"

rajen.husband="RAJENDRAN"
rajen.wife="AMUTHA"
rajen.kids="ARUN"
if __name__=='__main__':#run only in main module
    arun.display()
    rajen.display()
    dharma.display()
