class dsl(object):    
    def __init__(self,name):
        self.name = name
    def whois(self):
        if self.name == 'soeun':
            print(f'{self.name} is vice president')
        elif self.name == "gunwoo":
            print(f'{self.name} is president')
        elif self.name == "gyuwon":
            print(f'{self.name} is chongmu')
        elif self.name == "namhun":
            print(f'{self.name} is haksul')
        else:
            print(f'{self.name}이 누구임?')