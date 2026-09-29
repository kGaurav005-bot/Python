class Cookie:
    def __init__(self,color):
        self.color = color

    def get_color(self):
        return self.color
    def set_color(self,color):
        self.color =color

cookie_one = Cookie('green')
cookie_two = Cookie ('blue')

print('Cookie one is ', cookie_one.get_color())
print('Cookie two is ', cookie_two.get_color())

cookie_one.set_color('Yellow')

print('Cookie one is ', cookie_one.get_color())
print('Cookie two is ', cookie_two.get_color())

num1 = 11
num2 =num1
print("\n num 1i s" , num1)
print("\n num 2i s" , num2)

print("\n num 1i address is s" , id(num1))
print("\n num 2i s" , id(num2))
num2 =22

print("\n num 1i address is s" , id(num1))
print("\n num 2i s" , id(num2))
#integer is immutable . 
print("\n num 1i s" , num1)
print("\n num 2i s" , num2)
print ("Hello, World")