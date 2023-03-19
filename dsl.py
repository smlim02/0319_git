class dsl(object):
    
    def __init__(self,name):
        self.name = name
    def whois(self):
        if self.name == 'soeun':
            print(f'{self.name} is vice president')
        elif self.name == "gunwoo":
            print(f'{self.name} is president')
        else:
            print(f'{self.name}이 누구임?')