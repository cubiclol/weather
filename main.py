import sys, pyowm
import config
from PyQt5 import QtCore, QtGui, QtWidgets
from weather import Ui_Dialog
from pyowm import OWM

# создание приложения
app = QtWidgets.QApplication(sys.argv)

# инициализация
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

# логика
def get_weather_city():
	owm = pyowm.OWM(config.TOKEN)
	city = ui.lineEdit.text()

	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(city)
	w = observation.weather
	temperature = w.temperature('celsius')['temp']

	ui.label.setText( f'Температура: {temperature} градусов по Цельсию')

ui.pushButton.clicked.connect (get_weather_city)


# главный запуск
sys.exit(app.exec_())