class A:
    def __init__(self):
        print("init for class A")
    def feature1(self):
        print("Feature 1 A working")
    def feature2(self):
        print("Feature 2 working")
class B:
    def  __init__(self):
        print("init in B")
    def feature1(self):
        print("Feature 1 B working")
    def feature4(self):
        print("Feature 4 working")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("in c init")
    def feat(self):
        super().feature2()

a1=C()   #method resoulution order(left to right)
a1.feat()

