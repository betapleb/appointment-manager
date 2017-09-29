# Jennifer QUACH

from appointment import Appointment, Onetime, Monthly, Daily

class ApptManager:
    
    def __init__(self):
        self._aList = []   
        
        
       
    
    def processChoice(self):
        """print a menu to add, list, or quit
        read in the user choice
        process the user's menu choice
        """
        choice = input("a. add, l. list, q. quit\nYour choice? ")
        while choice != "q" :
            if choice == "a" :
                print("New appointment")
                self._addAppointment()
            elif choice == "l" : 
                print("List appointment(s) for")
                self._listAppointment()                       
            elif choice == "q" : 
                raise SystemExit
            elif not((choice == "a") or (choice == "l") or (choice == "q")) :
                print("choice a, l, q only")
            choice = input("a. add, l. list, q. quit\nYour choice?")
                
            
                
                
    def _getDate(self):
        """
        asks for a month and day. 
        Keep looping to ask for input until there is a valid month and day
        """
        valid = False
        daysInMonth = [31,28,31,30,31,30,31,31,30,31,30,31]
        while not valid :
            userMonth = input("Month: ")
            userDay = input("Day: ")
            
            if not (userMonth.isdigit() and userDay.isdigit()):
                print("day and month must be integers")
                validDate = False
            else: 
                userMonth = int(userMonth)
                userDay = int(userDay)                
                if 1 <= userMonth <= 12 and 1 <= userDay <= min(daysInMonth):         
                    validDate = True
                
            monthDayList = [userMonth, userDay]
            return monthDayList
                    
    
    def _addAppointment(self): 
        """call the getDate method to get the appointment date
        ask for the event name and the type of event (one-time, daily, monthly). 
        Keep looping if the user doesn't enter the correct type (see sample output).
        create the correct type of appointment object and store it
        """
        date = self._getDate()
        month = date[0]
        day = date[1]
        eventName = input("Name: ")
        eventType = input("o. onetime, d. daily, or m. monthly? ")
        while not ((eventType == "o") or (eventType == "d")or (eventType == "m")): 
            print("choice o, d, m only")  
            eventType = input("o. onetime, d. daily, or m. monthly? ")
        
        if eventType == "o" :
            appt = Onetime(month, day, eventName) 
        elif eventType == "d" :
            appt = Daily(month, day, eventName)
        else :
            appt = Monthly(month, day, eventName)
        
        self._aList.append(appt)    
        
            
    def _listAppointment(self):
        """
        prints a "no appointment" if there nothing has been scheduled
        call getDate to get a month / day
        print all appointments that will occur on that month / day
        """
        date = self._getDate()
        if self._aList == "":
            print("No appointment")
        else :
            for elem in self._aList :
                if appt.occursOn(date[0], date[1]) :
                    print(appt)
                

        
