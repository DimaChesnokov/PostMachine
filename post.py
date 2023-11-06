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
                if self.tape.checknum == 0:
                    self.current_line = int(args[0]) #- 1
                else:
                    self.current_line = int(args[1]) #- 1
            elif cmd == ".":
                break
            if cmd != "?":
                if not args:
                    self.current_line += 1
                else:
                    self.current_line = int(args[0])

    def get_tape(self): #вывод всей ленты
        t = list(reversed(self.tape.left_tape))
        return "".join(map(str, t)) + "".join(map(str, self.tape.right_tape))
    
class Tape:
    def __init__(self):
        self.left_tape = [] # Левая часть ленты(она будет начинаться с -1)
        self.right_tape = [0]  # Правая часть ленты(а она с 0)
        self.pos_carriage = 0 #позиция каретки

    def right(self):
        print(self.pos_carriage)
        self.pos_carriage += 1
        if self.pos_carriage > 0:
            print("pos " + str(self.pos_carriage) + " r " + str(len(self.right_tape)))
            if self.pos_carriage + 1 > len(self.right_tape): # если ленты не хватает добавляем ячейку
                self.right_tape.append(0)

    def left(self):
        print(self.pos_carriage)
        self.pos_carriage -= 1
        if self.pos_carriage == -1:
            if len(self.left_tape) == 0: # добавляем элемент тк изначальна список пуст
                print("pos " + str(self.pos_carriage) + " l " + str(len(self.left_tape)))
                self.left_tape.append(0)
        if self.pos_carriage < -1:
            if abs(self.pos_carriage) >= len(self.left_tape): # если ленты не хватает добавляем ячейку
                print("pos " + str(self.pos_carriage) + " l " + str(len(self.left_tape)))
                self.left_tape.append(0) 

    def num (self, a):
        if self.pos_carriage < 0:
            self.left_tape[abs(self.pos_carriage) - 1] = a
        else:
            self.right_tape[self.pos_carriage] = a


    def checknum(self):
        if self.pos_carriage < 0:
            return self.left_tape[abs(self.pos_carriage) - 1]
        else:
            return self.right_tape[self.pos_carriage]# чтение числа из ячейки

if __name__ == "__main__":
    machine = PostMachine()
    machine.add_command(">")#1  00
    #machine.add_command("<")#2  00
    machine.add_command("1")#3  10
    #machine.add_command("? 6, 5")#4 10
    machine.add_command(">")#5 10
    #machine.add_command("<")#6 10
    machine.add_command("1")#7 10
    machine.add_command(".")#8
    
    machine.run()
    result = machine.get_tape()
    print("Результат на ленте:", result)
