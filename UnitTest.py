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
    

if __name__ == "__main__":
    unittest.main()
