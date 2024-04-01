from bank_acconts import *

Dave=BankAccount(1000,"Dave")

Deepa=BankAccount(5000,"Deepa")

Deepa.deposite(200)

Dave.withdraw(10000)

Deepa.transfer(20000,Dave)