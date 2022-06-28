# ...
# INSTALL
# pip install PyQt5

# COMPILE
# pyinstaller -F -w main.py
# ...

import sys
import PyQt5
import PyQt5.QtWidgets
import PyQt5.QtCore
import PyQt5.QtGui


# класс главного окна
class Window(PyQt5.QtWidgets.QMainWindow):
    """Класс главного окна"""

    # описание главного окна
    def __init__(self):
        super(Window, self).__init__()

        # ГЛАВНОЕ ОКНО, надпись на нём и размеры
        self.setWindowTitle('Транслитерация ФИО в логин')
        self.setGeometry(600, 200, 470, 290)
        self.setFixedSize(470, 290)
        self.setWindowFlag(PyQt5.QtCore.Qt.WindowStaysOnTopHint)

        # ОБЪЕКТЫ НА ФОРМЕ
        # label_enter_fio
        self.label_enter_fio = PyQt5.QtWidgets.QLabel(self)
        self.label_enter_fio.setObjectName('label_enter_fio')
        self.label_enter_fio.setText('Введите ФИО:')
        self.label_enter_fio.setGeometry(PyQt5.QtCore.QRect(10, 10, 100, 40))
        font = PyQt5.QtGui.QFont()
        font.setPointSize(12)
        self.label_enter_fio.setFont(font)
        self.label_enter_fio.adjustSize()
        self.label_enter_fio.setToolTip(self.label_enter_fio.objectName())

        # lineEdit_fio_rus
        self.lineEdit_fio_rus = PyQt5.QtWidgets.QLineEdit(self)
        self.lineEdit_fio_rus.setObjectName('lineEdit_fio_rus')
        self.lineEdit_fio_rus.setText('Фамилия Имя Отчество')
        self.lineEdit_fio_rus.setGeometry(PyQt5.QtCore.QRect(10, 40, 450, 40))
        font = PyQt5.QtGui.QFont()
        font.setPointSize(16)
        self.lineEdit_fio_rus.setFont(font)
        self.lineEdit_fio_rus.setClearButtonEnabled(True)
        self.lineEdit_fio_rus.setEnabled(True)
        self.lineEdit_fio_rus.setToolTip(self.lineEdit_fio_rus.objectName())

        # pushButton_translit
        self.pushButton_translit = PyQt5.QtWidgets.QPushButton(self)
        self.pushButton_translit.setObjectName('pushButton_translit')
        self.pushButton_translit.setEnabled(True)
        self.pushButton_translit.setText('затранслитеризировать строку')
        self.pushButton_translit.setGeometry(PyQt5.QtCore.QRect(10, 90, 450, 25))
        self.pushButton_translit.clicked.connect(self.translit_fio)
        self.pushButton_translit.setToolTip(self.pushButton_translit.objectName())

        # lineEdit_translit_full
        self.lineEdit_translit_full = PyQt5.QtWidgets.QLineEdit(self)
        self.lineEdit_translit_full.setObjectName('lineEdit_translit_full')
        self.lineEdit_translit_full.setText('')
        self.lineEdit_translit_full.setGeometry(PyQt5.QtCore.QRect(10, 130, 450, 40))
        font = PyQt5.QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_translit_full.setFont(font)
        self.lineEdit_translit_full.setEnabled(True)
        self.lineEdit_translit_full.setReadOnly(True)
        self.lineEdit_translit_full.setToolTip(self.lineEdit_translit_full.objectName())

        # lineEdit_translit_user
        self.lineEdit_translit_user = PyQt5.QtWidgets.QLineEdit(self)
        self.lineEdit_translit_user.setObjectName('lineEdit_translit_user')
        self.lineEdit_translit_user.setText('')
        self.lineEdit_translit_user.setGeometry(PyQt5.QtCore.QRect(10, 180, 450, 40))
        font = PyQt5.QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_translit_user.setFont(font)
        self.lineEdit_translit_user.setEnabled(True)
        self.lineEdit_translit_user.setReadOnly(False)
        self.lineEdit_translit_user.setToolTip(self.lineEdit_translit_user.objectName())

        # button_exit
        self.button_exit = PyQt5.QtWidgets.QPushButton(self)
        self.button_exit.setObjectName('button_exit')
        self.button_exit.setText('Выход')
        self.button_exit.setGeometry(PyQt5.QtCore.QRect(10, 250, 180, 25))
        self.button_exit.setFixedWidth(50)
        self.button_exit.clicked.connect(self.click_on_btn_exit)
        self.button_exit.setToolTip(self.button_exit.objectName())

    # функция транслитерации введённого теста
    def translit_fio(self):
        # очистка полей
        self.lineEdit_translit_full.setText(None)
        self.lineEdit_translit_user.setText(None)

        # получаю текст из поля ввода
        fio_rus = self.lineEdit_fio_rus.text()

        # если поле непустое, то разбираю на слова, пробел - разделитель
        if fio_rus:
            # создание списка из текста
            fio_rus_list = fio_rus.strip().split()[:3]

            # тут транслитерируется английскими буквами
            fio_eng = latinizator(' '.join(fio_rus_list), alfa_dic)
            self.lineEdit_translit_full.setText(fio_eng)

            # разделяю по словам в список
            if len(fio_rus_list) == 1:
                fam_val = fio_rus_list[0]

                # тут делается пользователь английскими буквами
                fio_user = latinizator(fam_val, alfa_dic)
                self.lineEdit_translit_user.setText(fio_user)

            elif len(fio_rus_list) == 2:
                fam_val = fio_rus_list[0]
                imya_val = fio_rus_list[1]

                # тут делается пользователь английскими буквами
                fio_user = latinizator(fam_val + '.' + imya_val[0], alfa_dic)
                self.lineEdit_translit_user.setText(fio_user)

            else:
                fam_val = fio_rus_list[0]
                imya_val = fio_rus_list[1]
                otch_val = fio_rus_list[2]

                # тут делается пользователь английскими буквами
                fio_user = latinizator(fam_val + '.' + imya_val[0] + '.' + otch_val[0], alfa_dic)
                self.lineEdit_translit_user.setText(fio_user)

    # событие - нажатие на кнопку Выход
    @staticmethod
    def click_on_btn_exit():
        exit()


# словарь для соответствия русских символов и английских
alfa_dic = {'а': 'A', 'б': 'B', 'в': 'V', 'г': 'G', 'д': 'D', 'е': 'E', 'ё': 'E', 'ж': 'ZH', 'з': 'Z', 'и': 'I',
            'й': 'I', 'к': 'K', 'л': 'L', 'м': 'M', 'н': 'N', 'о': 'O', 'п': 'P', 'р': 'R', 'с': 'S', 'т': 'T',
            'у': 'U', 'ф': 'F', 'х': 'H', 'ц': 'TS', 'ч': 'CH', 'ш': 'SH', 'щ': 'SHCH', 'ъ': '', 'ы': 'Y', 'ь': '',
            'э': 'E', 'ю': 'IU', 'я': 'IA', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E',
            'Ё': 'E', 'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
            'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'TS', 'Ч': 'CH', 'Ш': 'SH',
            'Щ': 'SHCH', 'Ъ': '', 'Ы': 'Y', 'Ь': '', 'Э': 'E', 'Ю': 'IU', 'Я': 'IA'}


# чужая функция транслитерация, поправил
def latinizator(stroka, dic):
    for key, value in dic.items():
        stroka = stroka.replace(key, value)
    return stroka


# создание основного окна
def main_app():
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app_window_main = Window()
    app_window_main.show()
    sys.exit(app.exec_())


# запуск основного окна
if __name__ == '__main__':
    main_app()
