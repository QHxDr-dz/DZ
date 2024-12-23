import hashlib
class top:
    def main(self,type):
        #self.text=text
        self.type=type
        x=hashlib.new(self.type)
        y=input("enter your name")

        y=y.encode("utf-8")
        x.update(y)
        print(x.hexdigest())


z=top()
z.main("md5")