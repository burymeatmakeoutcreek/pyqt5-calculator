from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidget,QTableWidgetItem

a=""
operation=""
b=""

def result(r):
    form.res.setText(str(r))
    
def diviser():
    global a, operation
    a=form.first.text()
    operation="/"
    form.second.setFocus()

def multiply():
    global a, operation
    a=form.first.text()
    operation="x"
    form.second.setFocus()

def diviser2():
    global a,b
    b=form.second.text()
    r=str(float(a)/float(b))
    result(r)

def multiply2():
    global a,b
    b=form.second.text()
    r=str(float(a)*float(b))
    result(r)

def go():
    if operation=="/":
        diviser2()
    if operation=="x":
        multiply2()
    
app = QApplication([])
form = loadUi ("first.ui")
form.show()
form.divide.clicked.connect(diviser)
form.multiply.clicked.connect(multiply)
form.equal.clicked.connect(go)
app.exec_()