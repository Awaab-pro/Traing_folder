class ATM:

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def is_valid_request(self, request):
        print(f'Welcome to {self.bank_name}')
        print(f'current balance = {self.balance}, your request = {request}')

        result = False

        if request > self.balance:
            print("Can't give you all this money !!")

        elif request < 0:
            print("More than zero plz!")

        else:
            result = True

        return result

    def withdraw(self, request):
        # allowed papers: 100, 50, 10, and 5
        self.balance -= request
        notes = [100, 50, 10, 5]

        for note in notes:
            while request >= note:
                request -= note
                print('give ' + str(note))
            if request < 5 and request > 0:
                print('give ' + str(request))

        result = self.balance - request

        return result

    def process_request(self, request):
        if self.is_valid_request(request):
            self.withdraw(request)
            print(f'current balance = {self.balance}')

balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Saba Bank")
atm2 = ATM(balance2, "Jeen Bank")

# atm1.process_request(700)
# atm1.process_request(300)

atm1.process_request(431)
print('###################################')
atm2.process_request(550)
