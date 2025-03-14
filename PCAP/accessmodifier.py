# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.__account_number = account_number
#         self.__balance = balance
#     # def get_balance(self):
#     #     return self.__balance
 
# b = BankAccount(1234567890, 5000)
 
# Accessing the private variable through a public method
# print(b.get_balance())


# class BankAccount:
#     def __init__(self, account_number, balance):
#         self._account_number = account_number
#         self._balance = balance

#     def display_balance(self):
#         print("Balance:", self.__balance)

#     # b = BankAccount(1234567890, 5000)
#     # b.__display_balance()

# # b = BankAccount(1234567890, 5000)
# # b.display_balance()


# class customer (BankAccount):
#     def __init__(self, name, age, balance, account_number):
#         self.__Name = name
#         self.__age = age
#         BankAccount.__init__(self, account_number, balance)

#     def update_details(self, name):
#         self.__Name = name

#     def display_customer(self):
#         self.update_details("John II")
#         print("Balance:", self._balance)
#         print("Account No:", self._account_number)
#         print("Name:", self.__Name)


# a = customer(balance=1000, account_number=584353875, name="John", age=25)
# a.display_customer()




# def sum(a, b):


# def sum(a, b, c):


# sum(2,3)
# sum(2,3,4)



class A:
    def a(self):
        print("A", end=' ')
    def b(self):
        self.a()
 
class B(A):
    def a(self):
        print("B", end=' ')
    def do(self):
        self.b()

class C(A):
    def a(self):
        print("C", end=' ')
    def do(self):
        self.b()
 
B().do()
 
C().do()

A().b()