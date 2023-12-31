class PostMachine:
    def __init__(self):
        self.program = []  # Программа машины Поста
        self.current_line = 0  # Текущая строка программы
        self.tape = Tape()

    def add_command(self, command): #добовляем команду в машину
        self.program.append(command)

    def run(self):
        while self.current_line < len(self.program): #пока не достигли конца программы 
            command = self.program[self.current_line]
            cmd, *args = command.split()
            if cmd == ">":
                self.tape.right()
            elif cmd == "<":
                self.tape.left()
            elif cmd == "0":
                self.tape.num(0)
            elif cmd == "1":
                self.tape.num(1)
            elif cmd == "?":
                if self.tape.checknum() != 0:
                    args[0] = args[0][:-1]
                    self.current_line = int(args[0]) #- 1
                    
                else:
                    self.current_line = int(args[1]) #- 1
            elif cmd == ".":
                break
            if cmd != "?":
                if args is not None:
                    self.current_line = int(args[0])
                else:
                    self.current_line += 1
                    

    def get_tape(self): #вывод всей ленты
        t = list(reversed(self.tape.left_tape))
        return "".join(map(str, t)) + "".join(map(str, self.tape.right_tape))
    
class Tape:
    def __init__(self):
        self.left_tape = [] # Левая часть ленты(она будет начинаться с -1)
        self.right_tape = [0]  # Правая часть ленты(а она с 0)
        self.pos_carriage = 0 #позиция каретки

    def right(self):
        self.pos_carriage += 1
        if self.pos_carriage > 0:
            if self.pos_carriage + 1 > len(self.right_tape): # если ленты не хватает добавляем ячейку
                self.right_tape.append(0)

    def left(self):
        self.pos_carriage -= 1
        if self.pos_carriage == -1:
            if len(self.left_tape) == 0: # добавляем элемент тк изначальна список пуст
                self.left_tape.append(0)
        if self.pos_carriage < -1:
            if abs(self.pos_carriage) >= len(self.left_tape): # если ленты не хватает добавляем ячейку
                self.left_tape.append(0) 

    def num (self, a):
        if self.pos_carriage < 0:
            self.left_tape[abs(self.pos_carriage) - 1] = a
        else:
            self.right_tape[self.pos_carriage] = a


    def checknum(self):
        if self.pos_carriage < 0:
            num=self.left_tape[abs(self.pos_carriage) - 1]
            return num
        else:
            num=self.right_tape[self.pos_carriage]# чтение числа из ячейки
            return num

if __name__ == "__main__":
    machine = PostMachine()
    
    machine.add_command("1 1")#0
    #если в ячейке 0 то выполняем вторую команду если нет то первую команду
    machine.add_command("? 2, 4")#1
    machine.add_command("0 3")#2
    machine.add_command("? 4, 5")#3
    machine.add_command("1 5")#4
    machine.add_command(". 6")#5

    

    machine.run()
    result = machine.get_tape()
    print("Результат на ленте:", result)
