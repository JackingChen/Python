class Person:
    def __init__(self, name, date_of_birth, money, description):
        '''
        The constructor of the Person class which initializes
        the attributes of the class
        '''

        # Initialize the attribute "name"
        self.name = name
        # Initialize the attribute "date_of_birth"
        self.date_of_birth = date_of_birth
        # Initialize the attribute "money"
        self.money = money
        # Initialize the attribute "description"
        self.description = description
    
    def give_money(self, amount, targetPerson):
        '''
        Give money from this person object to the target person
        '''

        # Decrease the attribute "money" of this object
        self.money = self.money - amount

        # Then increase the money of the target instance
        # with the same amount
        targetPerson.money = targetPerson.money + amount
        
    def get_age(self):
        '''
        Get the age of this person object
        '''

        # Get today's date
        today = datetime.date.today()

        # Split the day, month and year from the
        # date_of_birth attribute and store them
        # into d, m and y variables
        [d,m,y] = self.date_of_birth.split("/")

        # Return the age
        return today.year - int(y)
