class A:
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")
    
class B(A):
    def feature3(self):
        print("Feature 3 working")
    def feature4(self):
        print("Feature 4 working")
class C(B):
    def feature5(self):
        print("Feature 5 working")

c1=C()
c1.feature1()
c1.feature3()
c1.feature5()


