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
            if cmd !="?":
                if not args:
                    self.current_line += 1
                else:
                    self.current_line = int(args[0])

    def get_tape(self): #вывод всей ленты
        return "".join(map(str, self.tape.left_tape)) + "".join(map(str, self.tape.right_tape))
    
class Tape:
    def __init__(self):
        self.left_tape = [] # Левая часть ленты(она будет начинаться с -1)
        self.right_tape = [0]  # Правая часть ленты(а она с 0)
        self.cur_tape = self.right_tape #та лента где каретка
        self.pos_carriage = 0 #позиция каретки

    def right(self):
        self.pos_carriage += 1
        if self.pos_carriage == 0:
            self.cur_tape = self.right_tape # не добовляем элементов тк он имеется
        if self.pos_carriage > 0:
            if self.pos_carriage > len(self.right_tape): # если ленты не хватает добавляем ячейку
                self.right_tape.append(0)

    def left(self):
        self.pos_carriage -= 1
        if self.pos_carriage == -1:
            if len(self.left_tape) == 0: # добавляем элемент тк изначальна список пуст
                self.left_tape.append(0)
            self.cur_tape = self.left_tape
        if self.pos_carriage < -1:
            if abs(self.pos_carriage) >= len(self.left_tape): # если ленты не хватает добавляем ячейку
                self.left_tape.append(0) 

    def num (self, a):
        self.cur_tape.insert(self.pos_carriage, a) # запись числа а в ячейку

    def checknum(self):
        return self.cur_tape[self.pos_carriage] # чтение числа из ячейки

if __name__ == "__main__":
    machine = PostMachine()
    machine.add_command(">")
    machine.add_command("<")
    machine.add_command("1")
    machine.add_command("? 6, 5")
    machine.add_command("> 6")
    machine.add_command("<")
    machine.add_command("1")
    machine.add_command(".")
    
    machine.run()
    result = machine.get_tape()
    print("Результат на ленте:", result)
