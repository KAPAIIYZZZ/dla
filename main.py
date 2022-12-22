import random
class Cellular_automata():
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__field = [[0] * self.__x for i in range(self.__y)]
        self.__buff_field = [[0] * self.__x for i in range(self.__y)]

    @property
    def field(self):
        return self.__field
    @property
    def buff_field(self):
        return self.__buff_field
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, size):
        if size < 0:
            print('Ошибка')
        else:
            self.__x = size
    @property
    def y(self):
        return self.__y
    @y.setter
    def Y(self, size):
        if size < 0:
            print('Ошибка')
        else:
            self.__y = size
    def neighbours(self):
        for i in range(0, self.__x):
            for j in range(0, self.__y):
                x=0
                for n in range(i-1,i+2):
                    for m in range(j-1,j+2):
                        if (n==i and m==j) or n==-1 or m==-1 or n==self.__x or m==self.__y:
                            continue
                        elif self.__field[m][n] == 1:
                            x+=1

                if self.__field[j][i] == 1:
                    if x == 2 or x == 3:
                        self.__buff_field[j][i] = 1
                    else:
                        self.__buff_field[j][i] = 0
                elif self.__field[j][i] == 0:
                    if x == 3:
                        self.__buff_field[j][i] = 1
                    else:
                        self.__buff_field[j][i] = 0
    def update(self):
        i = 0
        while True:
            x = random.randint(0,self.__x-1)
            y = random.randint(0, self.__y - 1)
            self.__field[x][y] = 1
            i+=1
            if i == 40:
                break


        print_field(self.__field)
        while True:
            stop = input('Введите 1, чтобы продолжить, 2 - чтобы выйти из игры: ')
            if stop == '1':
                self.__buff_field = [[0] * self.__x for i in range(self.__y)]
                self.neighbours()
                print_field(self.__buff_field)
                self.__field = self.__buff_field
            elif stop =='2':
                break
            else:
                print('Неверная команда')
class DLA(Cellular_automata):
    def __init__(self,x,y):
        super().__init__(x,y)
    def update(self):
        self.field[random.randint(0,self.y-1)][random.randint(0,self.x-1)] = 1
        print_field(self.field)
        print()
        while True:
            n=0
            x = random.randint(0, self.x - 1)
            y = random.randint(0, self.y - 1)
            if self.field[y][x] == 0:
                self.field[y][x] = 2
                print_field(self.field)
                print()
                while self.field[y][x] != 1:

                    self.neighbours(y, x)

                    if self.field[y][x] != 1:
                        self.field[y][x] = 0
                        k = random.randint(1, 4)
                        if k == 1:
                            x -= 1
                        elif k == 2:
                            y -= 1
                        elif k == 3:
                            x += 1
                        elif k == 4:
                            y += 1
                        if x == -1 or y == -1 or x == self.x or y == self.y:
                            print_field(self.field)
                            print()
                            break
                        else:
                            self.field[y][x] = 2

                    print_field(self.field)
                    print()
                    if self.field[y][x] == 1:
                        break
            for i in range(len(self.field)):
                for j in range(len(self.field[i])):
                    if self.field[j][i] == 1:
                        n +=1
            if n / (self.x * self.y) * 100 >= 30:
                break

    def neighbours(self,y,x):
        for n in range(x - 1,x + 2):
            for m in range(y - 1, y + 2):
                if n == -1 or m == -1 or n == self.x or m == self.y or (n!= x and m != y):
                    continue
                elif self.field[m][n] == 1:
                    self.field[y][x] = 1
def print_field(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[j][i], end = ' ')
        print()

def main():
    dla = DLA(10, 10)
    dla.update()
main()