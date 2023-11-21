import unittest
from post import PostMachine

class TestPostMachine(unittest.TestCase):
    
    def setUp(self):
        self.machine = PostMachine() #Создаём глобальный экземпляр класса Машины Поста
    
# Проверяется, что программа машины содержит только одну команду ">".
    def test_add_command(self):
        self.machine.add_command(">") # вывается метод add_command с аргументом ">", который добавляет команду ">" в программу машины.
        self.assertEqual(self.machine.program, [">"]) 

    def test_right(self):
        self.machine.tape.right()  #Вызывается метод right у ленты машины, который перемещает каретку на одну позицию вправо.
        self.assertEqual(self.machine.tape.pos_carriage, 1) #Проверяется, что позиция каретки равна 1.
        
    def test_left(self): #Аналогично с тестом test_right, только в другую сторону. Проверка, что будет -1
        self.machine.tape.left()
        self.assertEqual(self.machine.tape.pos_carriage, -1)
        
  
   #- Вызывается метод num у ленты машины с аргументом 0, который записывает значение 0 на текущую позицию ленты.
   # - Проверяется, что содержимое ленты равно "0".
    def test_num(self):
        self.machine.tape.num(0)
        self.assertEqual(self.machine.get_tape(), "0")
    
    
    # Вызывается метод num у ленты машины с аргументом 1, который записывает значение 1 на текущую позицию ленты.
    # Вызывается метод checknum у ленты машины, который возвращает значение на текущей позиции ленты.
    # Проверяется, что возвращенное значение равно 1.
    def test_checknum(self):
        self.machine.tape.num(1)
        self.assertEqual(self.machine.tape.checknum(), 1)
    
    
    
    
    

if __name__ == "__main__":
    print("Тесты выполнены.")
    unittest.main()
    
    
