class Person:
    _next = 0

    def __init__(self, name='Invitado', active=True):
        self.__code = self.next()
        self.__name = self.__capital_name(name)
        self.active = active

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, nam):
        self.__name = nam

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, cod):
        self.__code = cod

    def next(self):
        Person._next = Person._next+1
        return Person._next

    def __capital_name(self, name):
        return name.upper()
    
    def show_data(self):
        return 'Código: {} - Nombre: {} - Activo: {}'\
                .format(self.code, self.name, self.active)


class Employee(Person):
    def __init__(self, nam='Invitado', act=True, sal=400):
        Person.__init__(self, nam, act)
        self.salary = sal
    
    def show_data(self):
        return Person.show_data(self) + ' - Sueldo: ' + str(self.salary)


if __name__ == '__main__':
    per1 = Person()
    print(per1.show_data())
    per2 = Person('Daniel', False)
    print(per2.show_data())
    print(Employee().show_data())
