def singleton(func):
    l=[]
    def inner(*args,**kwargs):
        if len(l)==0:
            l.append(func())
        return l[-1]
    return inner

@singleton
class avengers:
    def __init__(self):
        self.maxt=200
    def booking(self,notkt):
        if notkt<=self.maxt:
            self.maxt-=notkt
            print('Tickets booked Successfully')
            print(f'Available tickets are : {self.maxt}')
        else:
            print('Tickets sold out')

def paytm():
    movie=avengers()
    movie.booking(int(input('Enter no.of tickets : ')))

def district():
    movie=avengers()
    movie.booking(int(input('Enter no.of tickets : ')))

def bookmyshow():
    movie=avengers()
    movie.booking(int(input('Enter no.of tickets : ')))

print('Through paytm')
paytm()

print('Through district app')
district()

print('Through bookmyshow')
bookmyshow()

    