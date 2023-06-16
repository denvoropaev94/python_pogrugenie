class Bankomat:

    def __init__(self,value):
        # Функция для сохранения баланса
        self.balance = True
        self.value = value
        self.__balance = 0.00

    def deposit(self,amount):
        # Функция для добавления денег
        self.__balance += float(amount)

    def cash_withdrawal(self,amount):
        # Фунцкия для снятия денег
        if self.__balance >= float(amount)*1.015:
            if float(amount)*0.015 > 600:
                self.__balance = self.__balance - float(amount) - 600
            elif float(amount)*0.015 < 30:
                self.__balance = self.__balance - float(amount) - 30
            else:
                self.__balance = self.__balance - float(amount) * 1.015

        else:
            self.balance = False
            print('У вас недостаточно средств!')

    def info(self):
        # Фукция об информации на балансе
        print(self.__balance)


y = Bankomat('USD')

print("Добро пожаловать в змеиный банкомат) ")
print("Выберите операцию , которую хотите сделать: ")
count = 0

while True:
    print('1.Просмотр баланса','2.Внесение денег', '3.Снятие денег','0.Завершение')
    number = input(": ")
    if number.isdigit():
        number = int(number)
    else:
        print("Введите цифру!")
        continue

    if number == 1:
        print("Текущий баланс = ", end=" ")
        y.info()
    elif number == 2:
        depos = int(input("Внесите сумму пополнения: "))
        if depos % 50 == 0:
            y.deposit(amount=depos)
            print("Внесенная сумма = ", depos)
            count += 1
            print("Количество операций : ", count)
            if depos >= 5_000_000:
                print("Нужно заплатить налог на богатсво!!!")
                depos -= depos * 1.1
                print("C вас вычтут - ", round(depos))
                y.deposit(amount=depos)
            if count % 3 == 0:
                print("Налог на 3 подряд операции", abs(depos * 0.03))
                depos -= depos * 1.03
                y.deposit(amount=depos)

        else:
            print("Ошибка! Можно вносить только сумму кратную 50")
    elif number == 3:
        vivod = int(input("Внесите сумму вывода "))
        commisiya = vivod * 0.015
        if vivod % 50 == 0:
            print("Комиссия 1,5% = ", commisiya)
            count += 1
            print("Количество операций : ", count)
            with_comission = vivod * 1.015
            if vivod >= 5_000_000:
                print("Нужно заплатить налог на богатсво!!!")
                vivod = vivod * 1.1
                print("C вас вычтут - ", round(vivod))
                # y.cash_withdrawal(amount=vivod)
            if count % 3 == 0:
                print("Налог на 3 подряд операции", abs(vivod * 0.03))
                vivod = vivod * 1.03
                # y.cash_withdrawal(amount=vivod)
                with_comission = (vivod * 1.015) + vivod * 0.03

            if commisiya > 600:
                with_comission = vivod + 600
                y.cash_withdrawal(amount=vivod)
            elif commisiya < 30:
                with_comission = vivod + 30
                y.cash_withdrawal(amount=vivod)
        else:
            print("Ошибка! Можно снять только сумму кратную 50")
            continue
        if y.balance:
            print("Вы сняли: ", with_comission)

    else:
        print("Спасибо за выбор змеиного банка")
        break

