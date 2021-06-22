#Banking class program in python
# Computer Programming Tutor,21 June 2021

class Banking(object):
    def __init__(self,custname,AcctNO,initialAmt):
        self.name = custname
        self.no = AcctNO
        self.bal = initialAmt

    def deposit(self,amt):
        self.bal +=amt

    def withdraw(self,amt):
        self.bal -=amt

    def main(self):
        s= "%s,%s,balance:%s" % (self.name,self.no,self.bal)
        print(s)

rec1= Banking("Yijie Zheng","19902309",15000)
rec2 =Banking("Lamian Zhang","19990521",15000)

rec1.deposit(500)
rec1.withdraw(1000)
rec2.withdraw(4500)
rec1.withdraw(200)
rec1.main()
rec2.main()

