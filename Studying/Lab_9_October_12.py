# Python Descriptors

"""
1.Create a stack calculator to calculate the number of pushes and pops into an internal stack using Python Descriptors
2.Write a program using descriptors to create a console object which creates 3 functions:
    a.log function that takes user arguments and returns them as a string
    b.Log to display previous logs
    c.Clear to clear all history
3.Write a program to find the last lonely number inside a sequence where the number is Lonely
if the distance from its deistance prime number is the farthest using descriptors
4.Write a program to check the number of users that were created and return as a class attribute.
"""

import random
# Task 1
print("Task 1")


class CalcDescriptor:
    def __get__(self, instance, owner):
        num_ = instance.list_.pop()
        owner.count_1 += 1
        return num_

    def __set__(self, instance, value):
        if isinstance(value, (int, float)):
            instance.count_2 += 1
            return instance.list_.append(value)
        else:
            raise TypeError("Input incorrect!")


class Calc:
    count_1 = 0
    count_2 = 0
    number = CalcDescriptor()

    def __init__(self, list_):
        self.list_ = list_

    def action(self, sign):
        value_1 = self.number
        value_2 = self.number
        if sign == "+":
            action_ = value_1 + value_2
            self.number = action_
        if sign == "-":
            action_ = value_2 - value_1
            self.number = action_
        if sign == "*":
            action_ = value_1 * value_2
            self.number = action_
        if sign == "/":
            action_ = value_1 / value_2
            self.number = action_

    def fill(self, size, max_):
        count = 0
        while count != size:
            random_number = int(random.uniform(0, max_))
            self.number = random_number
            count += 1

    def cancel(self):
        return self.list_.pop()


calc_1 = Calc([])
calc_1.fill(10, 100)
calc_1.number = 30
print(calc_1.list_)
calc_1.cancel()
print(calc_1.list_)
calc_1.action("-")
print(calc_1.list_)
calc_1.action("*")
print(calc_1.list_)
print(f"Number of: add to stack = {calc_1.count_2}, remove from stack = {calc_1.count_1}")


# Task 2
print("Task 2")


class Message:
    def __get__(self, instance, owner):
        __message = str(input(f"{instance.name}: "))
        return __message


class User:
    message = Message()

    def __init__(self, name):
        self.name = name
        self.log = []

    def new_message(self):
        new_message = self.message
        self.log.append(new_message)

    def show_history(self):
        log_history = "\n".join(self.log)
        return f"{self.name}'s log:\n{log_history}"

    def clear_history(self):
        self.log.clear()
        return print(f"{self.name} message history cleaned!")


user_1 = User("Lexa_")
user_2 = User("__Destroyer__")
user_1.new_message()
user_2.new_message()
user_1.new_message()
user_2.new_message()
print(user_1.show_history())
print(user_2.show_history())
user_1.clear_history()
print(user_1.show_history())
print(user_2.show_history())

# Task 3
print("Task 3")


class Prime_num:
    @staticmethod
    def _prime_num_(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return 0
            else:
                return 1
        else:
            return 0

    def _incr_prime_(self, num):
        trigger_ = 0
        while trigger_ == 0:
            num += 1
            trigger_ = self._prime_num_(num)
        return num

    def _decr_prime_(self, num):  # Do not put 0 or 1!
        trigger_ = 0
        while trigger_ == 0:
            num -= 1
            trigger_ = self._prime_num_(num)
        return num

    def __get__(self, instance, owner):
        return self.prime_num

    def __set__(self, instance, value):
        self.high = self._incr_prime_(value)
        if value in (0, 1, 2):
            self.low = self._incr_prime_(value)
        else:
            self.low = self._decr_prime_(value)
        if self.high - value >= value - self.low:
            self.prime_num = self.high
            return self.prime_num
        else:
            self.prime_num = self.low
            return self.prime_num


class Loneliest_number:
    prime = Prime_num()

    def __init__(self, seq_start, seq_end):
        self.distance = 0
        self.seq_start = seq_start
        self.seq_end = seq_end
        self.seq_list = [i for i in range(self.seq_start, self.seq_end + 1)]

    def check_seq(self):
        loneliest = self.seq_start
        self.prime = loneliest
        closest_prime = self.prime
        for num_ in self.seq_list:
            self.prime = int(num_)
            len_ = abs(num_ - self.prime)
            if len_ > self.distance:
                loneliest = num_
                closest_prime = self.prime
                self.distance = len_
        return f"{loneliest} is the loneliest number, with distance {self.distance}" \
               f" from its closest prime number {closest_prime}"


new_seq_1 = Loneliest_number(0, 3)
new_seq_2 = Loneliest_number(19, 23)
new_seq_3 = Loneliest_number(0, 10)
new_seq_4 = Loneliest_number(0, 100)
new_seq_5 = Loneliest_number(0, 1000)
print(new_seq_1.check_seq())
print(new_seq_2.check_seq())
print(new_seq_3.check_seq())
print(new_seq_4.check_seq())
print(new_seq_5.check_seq())

# Task 4
print("Task 4")


class User:
    local_counter = 0  # Class attribute

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        User.local_counter += 1

    def get_count(self):
        return self.local_counter


Van = User("Van", "Darkholm")
Ch_K = User("Chitoge", "Kirisaki")
Toxa = User("Anton", "Luky")
Ina = User("Yuul B.", "Alwright")
print(Ch_K.get_count())
print(Ina.get_count())
