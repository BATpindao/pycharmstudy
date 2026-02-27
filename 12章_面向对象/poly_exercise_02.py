"""
1.定义员工类Employee，包含私有属性(姓名和月工资)，以及计算年工资get_annual的方法。
2.普通员工(Worker)和经理(Manager)继承员工类，经理类多了奖金bonus属性和管理manage方法，普通员工类多了work方法，普通员工和经理类要求根据需要重写get_annual方法。
3.编写函数show_emp_annual(e:Employee)，实现获取任何员工对象的年工资。
4.编写函数working(e:Employee)，如果是普通员工，则调用work方法，如果是经理，则调用manage方法。
"""
# 员工类
class Employee:
    __name = None  # 名字
    __salary = None  # 月工资

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def get_name(self):
        return self.__name

    #     计算工资
    def get_annual(self):
        pass

# 普通员工
class Worker(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def get_annual(self):
        return self.get_salary() * 12

    def work(self):
        print('正在工作💼')

# 经理
class Manager(Employee):
    __bonus = None

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self._bonus = bonus

    def get_bonus(self):
        return self._bonus

    def get_annual(self):
        return self.get_salary() * 12+self.get_bonus()*12

    def manage(self):
        print('我是经理')

w =Worker('小王',3000)
m = Manager('jek',4500,200)

def show_emp_annual(e:Employee):
    print(f'{e.get_name()}的年工资是:{e.get_annual()}')

def working(e:Employee):
    if isinstance(e,Manager):
        e.manage()
    else:
        e.work()

show_emp_annual(w)
show_emp_annual(m)
working(w)
working(m)