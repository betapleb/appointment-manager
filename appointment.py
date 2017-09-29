# Jennifer QUACH

class Appointment:
    """Appointment is an abstract superclass with 3 subclasses: Onetime, Daily, Monthly,
    all of which have an occursOn method which accepts a month and day input, and returns 
    True / False depending on whether the current appointment object will occur on the input month / day. 
    All three subclasses also have a __repr__ method to print the object's type of appointment, 
    the date and event.
    """
    
    def __init__(self, month, day, eventName) :
        self._month = month
        self._day = day
        self._eventName = eventName    
        #self.eventType = eventType
        #raise NotImplementedError
        


    def occursOn(self, day, month) :
        raise NotImprementedError
    
    def __repr__(self) :
        return " (%02d/%02d: %s" % (self._month, self._day, self._eventName)

class Onetime(Appointment) :       
    def __init__(self, month, day, event) :   
        super().__init__(month, day, event)     #### super() refers to parent class
    def __repr__(self):
        return "One time appointment" + super()._repr__()
    def occursOn(self,day,month):
        return day == self._day and month == self._month


        
class Daily(Appointment):
    def __init__(self, month, day, event) :   
        super().__init__(month, day, event) 
    
    def occursOn(self, month, day) :
        if (self._month == month) and (self._day == day) :
            print(elem)
            return (True)
        else: 
            return (False)   
    def __repr__(self):
        return "Daily appointment (" + self._month + "/" + self._day + ") :" + self._event
    
    
class Monthly(Appointment):
    def __init__(self, month, day, event) :   
        super().__init__(month, day, event) 
    
    def occursOn(self, month, day) :
        if (self._month == month) and (self._day == day) :
            print(elem)
            return (True)
        else: 
            return (False)   

    def __repr__(self):
        return "Monthly appointment (" + self._month + "/" + self._day + ") :" + self._event
         