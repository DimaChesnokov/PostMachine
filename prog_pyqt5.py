import sys
from PyQt5 import QtWidgets, uic
from post import PostMachine, Tape
from PyQt5.QtWidgets import QTableWidgetItem, QHBoxLayout, QPushButton
import tkinter as tk
from tkinter import filedialog


# Загрузка интерфейса из файла PostMachine.ui
class Ui(QtWidgets.QMainWindow):
    
    curentBut=15
    #Инициализация
    def __init__(self):
        
        super(Ui, self).__init__()
        uic.loadUi("PostMachine.ui", self)
        
        #Присвоение кнопкам методов
        self.pushButton.clicked.connect(self.start_machine)
        self.pushButton_addCommand.clicked.connect(self.data_save)
        self.pushButton_importFile.clicked.connect(self.import_command)
        self.pushButton_saveFile.clicked.connect(self.save_command)
        self.pushButton_Clear.clicked.connect(self.Clear_Table)
        
        self.pushButton_Right.clicked.connect(self.goRight)
        self.pushButton_Left.clicked.connect(self.goLeft)
        
        #Создание ленты
        Ui.createTape(self)
        
        #Настройка таблицы для вывода и ввода команд
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(("Команда","Номер следующей команды"))
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,250)
    
    #Метод для добавления команд в таблицу    
    def data_save(self):
        
        #Передача данных из ЛайнЭдитов в переменные
        com = self.lineEdit_com.text()
        nextCom = self.lineEdit_comNext.text()
        tchk="."
        row=self.tableWidget.rowCount()+1
        
        #Строка для проверки команд
        txtcom=".><10?"
        
        
        #Нахождение количества строк в таблице
        rowCount = self.tableWidget.rowCount()
        
        #Заполнение таблицы данными
        self.tableWidget.insertRow(rowCount)
        if com != "" and txtcom.find(com)!=-1:
            self.tableWidget.setItem(rowCount,0,QTableWidgetItem(com))
        else:
            self.tableWidget.setItem(rowCount,0,QTableWidgetItem(tchk))
            
        if nextCom !="" and Ui.checknum(self)!=-1:    
            self.tableWidget.setItem(rowCount,1,QTableWidgetItem(nextCom))
        else:
            self.tableWidget.setItem(rowCount,1,QTableWidgetItem(str(row)))
        
        #Переделываем номера строк для удобства    
        Ui.rowsEdit(self)
        
    #Метод для импорта программы из файла        
    def import_command(self):
        
        # Создать корневое окно
        root = tk.Tk()
        root.withdraw()  # Скрыть корневое окно

        # Открыть диалоговое окно выбора файла
        file_path = filedialog.askopenfilename()

        # После выбора файла, можно использовать `file_path` для обработки выбранного файла
        if file_path:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                self.tableWidget.setRowCount(len(lines))
                for i, line in enumerate(lines):
                    items = line.strip().split()  # Предполагаем, что данные разделены табуляцией
                    
                    for j, item in enumerate(items):
                        item = QTableWidgetItem(item)
                        self.tableWidget.setItem(i, j, item)
                        
        #Переделываем номера строк для удобства                    
        Ui.rowsEdit(self)

        # Закрыть корневое окно (необязательно, если вы завершили работу с диалоговым окном)
        root.destroy()
    
    #Метод для сохранения программы в текстовый файл    
    def save_command(self):
        
        # Укажите имя файла, который вы хотите создать
        file_name = self.lineEdit_FileName.text()
        
        #Проверка имени файла
        if file_name !="" and file_name.endswith(".txt"):
            # Откройте файл для записи (создаст новый файл или перезапишет существующий)
            with open(file_name, 'w', encoding='utf-8') as file:
                #Заполнение файла данными из 
                for row in range(self.tableWidget.rowCount()):
                    row_data = []
                    for column in range(self.tableWidget.columnCount()):
                        item = self.tableWidget.item(row, column)
                        if item is not None:
                            cell_data = item.text()
                            row_data.append(cell_data)
                        else:
                            row_data.append("")
                    file.write("\t".join(row_data) + "\n")
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка!", "Вы ввели недопустимое название файла!\n Или же не указали расширение (.txt)")
                    
    #Метод запуска программы
    def start_machine(self):
        
        #Создаем объект класса
        machine = PostMachine()

        #Добавляем команды из таблицы на выполнение
        for row in range(self.tableWidget.rowCount()):
            item0 = self.tableWidget.item(row,0)
            item1 = self.tableWidget.item(row,1)
            comText= (f"{item0.text()} {item1.text()}")
            machine.add_command(comText)
        
        #Запуск программы
        machine.run()
        result = machine.get_tape()
        
        #Выводим результат
        QtWidgets.QMessageBox.warning(self, "Результат", result)
        
    #Метод для очистки таблицы и ленты
    def Clear_Table(self):
        
        # Очистить содержимое ячеек
        self.tableWidget.clearContents()  
        
        # Установить количество строк в 0
        self.tableWidget.setRowCount(0) 
        
        hbox=self.horizontalLayout
        hbox2= self.horizontalLayout_2
        hbox3= self.horizontalLayout_3
        Ui.cleanTape(self,hbox)
        Ui.cleanTape(self,hbox2)
        Ui.cleanTape(self,hbox3)
        Ui.createTape(self)
    
    #Метод для создания ленты    
    def createTape(self):
        hbox=self.horizontalLayout
        hbox2= self.horizontalLayout_2
        hbox3= self.horizontalLayout_3
        k=-15
        for i in range(31):
            if(k==0):
                button = QPushButton("*")
                button.setStyleSheet("background-color: red; color: white;")
                hbox3.addWidget(button)
            else:
                hbox3.addWidget(QPushButton(""))
            hbox.addWidget(QPushButton("0"))
            hbox2.addWidget(QPushButton(str(k)))
            k=k+1
        
        self.setLayout(hbox)
        self.setLayout(hbox2)
        self.setLayout(hbox3)
        Ui.curentBut=15
    
    #Метод для очистки ленты
    def cleanTape(self,hbox):
        while hbox.count() > 0:
            item = hbox.takeAt(0)  # Извлекаем элемент с индексом 0
            widget = item.widget()  # Получаем виджет из элемента
            if widget is not None:
                widget.deleteLater()  # Удаляем виджет
            else:
                hbox.removeItem(item)  # Удаляем элемент из макета
                
    def goRight(self):
        hbox=self.horizontalLayout
        hbox2= self.horizontalLayout_2
        hbox3= self.horizontalLayout_3
        item = hbox3.itemAt(Ui.curentBut).widget()  
        item.setText("")
        item.setStyleSheet("background-color: white; color: black;")
        Ui.curentBut=Ui.curentBut+1
        item = hbox3.itemAt(Ui.curentBut).widget()  
        item.setStyleSheet("background-color: red; color: white;")
        item.setText("*")
        
    def goLeft(self):
        hbox=self.horizontalLayout
        hbox2= self.horizontalLayout_2
        hbox3= self.horizontalLayout_3
        item = hbox3.itemAt(Ui.curentBut).widget()  
        item.setText("")
        item.setStyleSheet("background-color: white; color: black;")
        Ui.curentBut=Ui.curentBut-1
        item = hbox3.itemAt(Ui.curentBut).widget()  
        item.setStyleSheet("background-color: red; color: white;")
        item.setText("*")
        
    
    #Метод для изменения нумерации ячеек    
    def rowsEdit(self):
        for i in range(self.tableWidget.rowCount()):
            item = QTableWidgetItem(str(i))
            self.tableWidget.setVerticalHeaderItem(i, item)
    
    #Провнрка на правильность введённых данных        
    def checknum(self):
        textNum="0123456789, "
        nextCom = self.lineEdit_comNext.text()
        for i in nextCom:
            if textNum.find(i)==-1:
                return -1
        return 1
        
#Настройка формы
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())