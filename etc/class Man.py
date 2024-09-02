class Man:    #클래스 정의
    def __init__(self, name):    #생성자
        self.name = name
    
    def hello(self):    #메서드1
        print("Hello, " + self.name +  "!")
    
    
    def goodbye(self):      #메서드2
        print("Goodbye, " + self.name + "!")
    
    def __del__(self):     #소멸자
        print("Deleted")
YJS = Man("Ji Sang You")
YJS.hello()
YJS.goodbye()
