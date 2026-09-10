class Root:
    def f(self, parent):
        print("Root from " + parent)

        
class A(Root):
    def f(self, parent):
        print("A from " + parent)
        super().f("A")

        
class B(Root):
    def f(self, parent):
        print("B from " + parent)
        super().f("B")

        
class Child(A, B):
    def f(self, parent):
        print("Child from " + parent)
        super().f("Child")

c = Child()
c.f("main")