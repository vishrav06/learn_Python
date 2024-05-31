class Account:
    def __init__(self, bal, acc_no, acc_pass):
        self.bal = bal
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def debit(self, amt):
        self.bal -= amt

    def credit(self, amt):
        self.bal += amt

    def get_bal(self):
        print("Balance for Acc. No.", self.acc_no, "is", self.bal)

    def reset_pass(self):
        print(self.__acc_pass)


    


acc1 = Account(10000, "352657", "abcde")
# acc1.debit(5329)
# acc1.credit(2597)
# acc1.get_bal()


# print(acc1.__acc_pass) #does not work


acc1.reset_pass()