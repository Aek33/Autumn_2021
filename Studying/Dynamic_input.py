import sortMethods


class dynamicDesc:
    def __set__(self, instance, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value


class DynamicSort:
    value = dynamicDesc

    def __init__(self):
        self.container = []

    def start(self):
        self.value = input("--> ")
        if self.value == "exit":
            return "Input completed!"
        elif self.value == "" or self.value == " ":
            print("Incorrect input, try again")
            self.start()
        else:
            self.container.append(self.value)
            self.container = sortMethods.quick_sort(self.container)
            print(self.container)
            self.start()


if __name__ == "__main__":
    DynamicInput = DynamicSort()
    DynamicInput.start()
