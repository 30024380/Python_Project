#Way to encapsulate functionality
class myClass():
    #The self argument refers to itself
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString)
#inheriting from myClass
class anotherClass(myClass):
    #The self argument refers to itself
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")

    def method2(self, someString):
        print("anotherClass method2 ")

def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    #The argument is nothing being used thus its not prining this is a string
    c2.method2("This is a string")

if __name__ == "__main__":
    main()