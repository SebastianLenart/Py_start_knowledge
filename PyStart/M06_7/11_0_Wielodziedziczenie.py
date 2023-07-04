class A:
    def run(self):
        print("A")

class B:
    def run(self):
        print("B")


class Child(A, B):
    def go(self):
        self.run()


a = Child()
a.go() # A bo jest pierwsza



















