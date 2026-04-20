class student:
    a=1

    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")

s = student()

s.a =26

s.show()