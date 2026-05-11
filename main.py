class Simple:
    def info_jon(self):
        print(f"Simple info")


class MyClass:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def method_1(self, obj):
        if hasattr(obj, "info"):
            obj.info()

        else:
            print(f"Bu objectda info metodi yo'q!")

obj = MyClass(40, 50)

s = Simple()
obj.method_1(s)

#1-masasla
class Person:
    def __init__(self, fullname, age):
        self.fullname = fullname
        self.age = age

    def show_info(self):
        print(f"Ism: {self.fullname}")
        print(f"Yosh: {self.age}")


class Simple:
    def test(self):
        print("Oddiy method")


class Profile:
    def check_profile(self, obj):
        if hasattr(obj, "show_info"):
            obj.show_info()
        else:
            print("show_info method topilmadi")


p1 = Person("Azamat", 21)
s1 = Simple()

profile = Profile()

profile.check_profile(p1)
print("----------")
profile.check_profile(s1)
