import datetime



class log:
    def __init__(self,name):
        self.name = name

    @staticmethod
    def gettime():
        now = datetime.datetime.now()
        return datetime.datetime.strftime(now, '%Y-%m-%d %a %I:%M %p')

    def main(self,n):
        try:
            if n == 1:
                a = int(input("Press 1 for std1 2 for std2 3 for std3 :"))
                client[a-1].take(a-1)
            elif n == 2:
                a = int(input("Press 1 for std1 2 for std2 3 for std4 :"))
                client[a-1].retrive(a-1)
            else :
                raise Exception("Invalid Input")
        except:
            print("Invalid Input")
    
    def take(self,b):
        try:
            c = int(input("enter 1 for excersise and 2 for food:"))
            if c ==1:
                with open("{}-exercise.txt".format(client[b].name),"a",encoding="utf-8") as op:
                    value = input("Enter the exercise performed :")
                    op.write(str(log.gettime()) + ": " + value + "\n")
                    print("successfully written")
            elif c ==2:
                with open("{}-food.txt".format(client[b].name),"a",encoding="utf-8") as op:
                    value = input("Enter the food taken :")
                    op.write(str(log.gettime()) + ": " + value + "\n")
                    print("successfully written")
            else:
                raise Exception("Invalid Input")
        except:
            print("Invalid Input")

    def retrive(self,b):
        try:
            c = int(input("enter 1 for excersise and 2 for food:"))
            if c == 1:
                with open("{}-exercise.txt".format(client[b].name),"r",encoding="utf-8") as op:
                    content = op.read()
                    print(content)
            elif c==2:
                with open("{}-food.txt".format(client[b].name),"r",encoding="utf-8") as op:
                    content = op.read() 
                    print(content)
            else:
                raise Exception("Invalid Input")
        except:
            print("Invalid Input")


if __name__ == "__main__":
    client = [log("Std1"),log("Std2"),log("Std3")]

try:
    n = int(input("Enter 1 to log and 2 to retrive data:"))
    if 1<= n <=2:
        client[n-1].main(n)
    else:
        raise Exception("Invalid Input")
except:
    print("Invalid input")



    
    
        