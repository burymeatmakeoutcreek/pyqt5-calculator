from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidget,QTableWidgetItem

a=""
operation=""
ans="0"

def check():
    global operation
    a=form.first.text()
    l=len(a)
    if operation=="":
        if not l==0:
            if not 48<=ord(a[l-1])<=57:
                form.first.setText(a[:l-1])
    else:
        print(operation)
        p1=a.find(operation)
        print(a,l,p1)
        if l>p1+1:
            car=a[l-1]
            if not (48<=ord(car)<=57):
                form.first.setText(a[:l-1])

    
def result(r):
    global ans, operation
    if float(r).is_integer():
        x=int(float(r))
        form.res.setText(str(x))
        operation=""
    else:
        form.res.setText(str(r))
        operation=""
    ans=form.res.text()
    form.first.clear()
    form.first.setFocus()

    
def ans1():
    global ans
    a=form.first.text()
    form.first.setText(a+str(ans))
    
def ans2():
    global ans, a
    a1=form.first.text()
    a=form.first.setText(a1+str(ans))

def diviser():
    global a, operation
    a=form.first.text()
    operation="/"
    ch=a+operation
    if ch=="/":
        QMessageBox.critical(form,"PROBLEM","You haven't put your first number.")
        form.first.clear()
        operation=""
    else:
        form.first.setText(ch)
        form.first.setFocus()

def multiply():
    global a, operation
    a=form.first.text()
    operation="x"
    ch=a+operation
    if ch=="x":
        QMessageBox.critical(form,"PROBLEM","You haven't put your first number.")
        form.first.clear()
    else:
        form.first.setText(ch)
        form.first.setFocus()

def add():
    global a, operation
    a=form.first.text()
    operation="+"
    ch=a+operation
    if ch=="+":
        QMessageBox.critical(form,"PROBLEM","You haven't put your first number.")
        form.first.clear()
    else:
        form.first.setText(ch)
        form.first.setFocus()

def sub():
    global a, operation
    a=form.first.text()
    operation="-"
    ch=a+operation
    if ch=="-":
        QMessageBox.critical(form,"PROBLEM","You haven't put your first number.")
        form.first.clear()
    else:
        form.first.setText(ch)
        form.first.setFocus()
    
def diviser2():
    a=form.first.text()
    p1=a.find("/")
    b1=a[p1+1:]
    a1=a[:p1]
    if b1=="":
        QMessageBox.critical(form,"PROBLEM","Must choose second number.")
    elif b1=="0":
        QMessageBox.critical(form,"PROBLEM","Cannot divide by Zero.")
    else:
        r=str(float(a1)/float(b1))
        result(r)

def multiply2():
    a=form.first.text()
    p1=a.find("x")
    b1=a[p1+1:]
    a1=a[:p1]
    if b1=="":
        b1="0"
    r=str(float(a1)*float(b1))
    result(r)

def add2():
    a=form.first.text()
    p1=a.find("+")
    b1=a[p1+1:]
    a1=a[:p1]
    if b1=="":
        b1="0"
    r=str(float(a1)+float(b1))
    result(r)

def sub2():
    a=form.first.text()
    p1=a.find("-")
    b1=a[p1+1:]
    a1=a[:p1]
    if b1=="":
        b1="0"
    r=str(float(a1)-float(b1))
    result(r)
    
def go():
    if operation=="":
        QMessageBox.critical(form,"PROBLEM","You haven't selected an operation yet.")
    if operation=="/":
        diviser2()
    if operation=="x":
        multiply2()
    if operation=="+":
        add2()
    if operation=="-":
        sub2()
        
app = QApplication([])
form = loadUi ("first.ui")
form.show()
form.first.textChanged.connect(check)
form.divide.clicked.connect(diviser)
form.multiply.clicked.connect(multiply)
form.plus.clicked.connect(add)
form.subtract.clicked.connect(sub)
form.ans.clicked.connect(ans1)
form.equal.clicked.connect(go)
app.exec_()