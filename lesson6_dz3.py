class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return f'{sum(self._income.values())}'


a = Position('Василий', 'Беглов', 'Директор', 200000, 35000)
b = Position('Иван', 'Терентьев', 'Инженер', 50000, 15000)

print(a.get_full_name())
print(a.position)
print(a.get_total_income())
print(b.get_full_name())
print(b.position)
print(b.get_total_income())
