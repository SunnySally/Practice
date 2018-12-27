# 用class来定义一个类。 Person(object)表示继承自object类； __init__函数用来初始化对象； self表示对象自身，类似于C Java里面this。
class Person(object):
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    def full_name(self):
        return self.first + ' ' + self.last

#Python用关键词def来定义函数。
def poly(x, a, b, c):
    y = a * x ** 2 + b * x + c
    return y

from numpy.random import rand
v = rand(10)
randomList = []
intList = []
for row in v:
    intRow = int(row * 10)
    intList.append(intRow)
    if row > 0.5:
        randomList.append(row)
print (randomList)
print (intList)

import random
r10 = random.randint(0, 10)
r9_10 = random.uniform(9, 10)
# 从9、19、29、39、……、99之间，随机选取一个实数：
r99 = random.randrange(9, 100, 10)
r_List = random.choice([5, 6, 7, 8])
r_String = random.choice("从一个字符串里面，随机选取一个字符！")
# 随机打乱列表里面的字符顺序：
rr = ["p","q","r","s","t","p","q","r","s","t","p","q","r","s","t",]
r_Shuffle = random.shuffle(rr)
# 从列表里面随机选取9个数字：
rrr = range(3,100,2)
b = random.sample(rrr, 9)

# 这里，*args 表示参数数目不定，可以看成一个元组，把第一个参数后面的参数当作元组中的元素。
def add1(x, *args):
    total = x
    for arg in args:
        total += arg
    return total

# 这里， **kwargs 表示参数数目不定，相当于一个字典，关键词和值对应于键值对。
def add2(x, **kwargs):
    total = x
    for arg, value in kwargs.items():
        print("adding ", arg)
        total += value
    return total

# 可以接收任意数目的位置参数和键值对参数：
def foo(*args, **kwargs):
    print(args, kwargs)

# 一旦 try 块中的内容出现了异常，那么 try 块后面的内容会被忽略，Python会寻找 except 里面有没有对应的内容，如果找到，就执行对应的块，没有则抛出这个异常。
# 在上面的例子中，try 抛出的是 ValueError，except 中有对应的内容，所以这个异常被 except 捕捉到，程序可以继续执行：
import math
def expections():
    while True:
        try:
            text = input('> ')
            if text[0] == 'q':
                break
            x = float(text)
            y = math.log10(x)
            print ('log10({0}) = {1}'.format(x, y))
        except ValueError:
            print ('the value must be greater than 0')
        # 不管 try 块有没有异常， finally 块的内容总是会被执行，而且会在抛出异常前执行，因此可以用来作为安全保证，比如确保打开的文件被关闭, 在抛出异常前执行：
        finally:
            print ('finally was called')

import warnings
# 在需要的地方，我们使用 warnings 中的 warn 函数：
def month_warning(m):
    if not 1<= m <= 12:
        msg = "month (%d) is not between 1 and 12" % m
        warnings.warn(msg, RuntimeWarning)

# 可以看到，出现异常的时候，磁盘的写入并没有完成，为此我们可以使用 try/except/finally 块来关闭文件，这里 finally 确保关闭文件，所有的写入已经完成。
f = open('newfile.txt','w')
try:
    for i in range(3000):
        x = 1.0 / (i - 1000)
        f.write('hello world: ' + str(i) + '\n')
except Exception:
    print("something bad happened")
finally:
    f.close()