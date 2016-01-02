# ----*-- coding: utf-8 --*----

# Form implementation generated from reading ui file 'app2.ui'
#
# Created: Mon Sep 28 06:21:18 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import cubicsolve,math
import cadgenerator

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        self.count = 1
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 600)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 81, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 81, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 81, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 220, 101, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(40, 280, 66, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 400, 111, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(480, 40, 66, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(480, 100, 66, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(480, 160, 121, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(480, 220, 101, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(480, 280, 66, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(480, 340, 66, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(480, 410, 66, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(480, 480, 66, 17))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(290, 550, 66, 17))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(180, 30, 104, 31))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit_2 = QtGui.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 100, 104, 31))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_3 = QtGui.QTextEdit(Form)
        self.textEdit_3.setGeometry(QtCore.QRect(180, 160, 104, 31))
        self.textEdit_3.setObjectName(_fromUtf8("textEdit_3"))
        self.textEdit_4 = QtGui.QTextEdit(Form)
        self.textEdit_4.setGeometry(QtCore.QRect(180, 220, 104, 31))
        self.textEdit_4.setObjectName(_fromUtf8("textEdit_4"))
        self.textEdit_5 = QtGui.QTextEdit(Form)
        self.textEdit_5.setGeometry(QtCore.QRect(180, 280, 104, 31))
        self.textEdit_5.setObjectName(_fromUtf8("textEdit_5"))
        self.textEdit_6 = QtGui.QTextEdit(Form)
        self.textEdit_6.setGeometry(QtCore.QRect(180, 340, 104, 31))
        self.textEdit_6.setObjectName(_fromUtf8("textEdit_6"))
        self.textEdit_7 = QtGui.QTextEdit(Form)
        self.textEdit_7.setGeometry(QtCore.QRect(180, 400, 104, 31))
        self.textEdit_7.setObjectName(_fromUtf8("textEdit_7"))
        self.textEdit_8 = QtGui.QTextEdit(Form)
        self.textEdit_8.setGeometry(QtCore.QRect(610, 30, 104, 31))
        self.textEdit_8.setObjectName(_fromUtf8("textEdit_8"))
        self.textEdit_9 = QtGui.QTextEdit(Form)
        self.textEdit_9.setGeometry(QtCore.QRect(610, 90, 104, 31))
        self.textEdit_9.setObjectName(_fromUtf8("textEdit_9"))
        self.textEdit_10 = QtGui.QTextEdit(Form)
        self.textEdit_10.setGeometry(QtCore.QRect(610, 150, 104, 31))
        self.textEdit_10.setObjectName(_fromUtf8("textEdit_10"))
        self.textEdit_11 = QtGui.QTextEdit(Form)
        self.textEdit_11.setGeometry(QtCore.QRect(610, 210, 104, 31))
        self.textEdit_11.setObjectName(_fromUtf8("textEdit_11"))
        self.textEdit_12 = QtGui.QTextEdit(Form)
        self.textEdit_12.setGeometry(QtCore.QRect(610, 270, 104, 31))
        self.textEdit_12.setObjectName(_fromUtf8("textEdit_12"))
        self.textEdit_13 = QtGui.QTextEdit(Form)
        self.textEdit_13.setGeometry(QtCore.QRect(610, 330, 104, 31))
        self.textEdit_13.setObjectName(_fromUtf8("textEdit_13"))
        self.textEdit_14 = QtGui.QTextEdit(Form)
        self.textEdit_14.setGeometry(QtCore.QRect(610, 390, 104, 31))
        self.textEdit_14.setObjectName(_fromUtf8("textEdit_14"))
        self.textEdit_15 = QtGui.QTextEdit(Form)
        self.textEdit_15.setGeometry(QtCore.QRect(610, 470, 104, 31))
        self.textEdit_15.setObjectName(_fromUtf8("textEdit_15"))
        self.textEdit_16 = QtGui.QTextEdit(Form)
        self.textEdit_16.setGeometry(QtCore.QRect(370, 540, 104, 31))
        self.textEdit_16.setObjectName(_fromUtf8("textEdit_16"))
        self.label_17 = QtGui.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(40, 470, 100, 17))#81,480
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.textEdit_17 = QtGui.QTextEdit(Form)
        self.textEdit_17.setGeometry(QtCore.QRect(180, 470, 104, 31))
        self.textEdit_17.setObjectName(_fromUtf8("textEdit_17"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(40, 340, 111, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 540, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 540, 98, 27))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton"))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "GearSoft", None))
        self.label.setText(_translate("Form", "Gear Ratio", None))
        self.label_2.setText(_translate("Form", "Power (kW)", None))
        self.label_3.setText(_translate("Form", "RPM(Input)", None))
        self.label_4.setText(_translate("Form", "Teeth (Pinion)", None))
        self.label_5.setText(_translate("Form", "BHN", None))
        self.label_7.setText(_translate("Form", "StrengthG (Mpa)", None))
        self.label_8.setText(_translate("Form", "Ka", None))
        self.label_9.setText(_translate("Form", "Kb", None))
        self.label_10.setText(_translate("Form", "Face Width Factor", None))
        self.label_11.setText(_translate("Form", "Velocity Factor", None))
        self.label_12.setText(_translate("Form", "Ep(Mpa)", None))
        self.label_13.setText(_translate("Form", "Eg(Mpa)", None))
        self.label_14.setText(_translate("Form", "Grade", None))
        self.label_15.setText(_translate("Form", "FOS", None))
        self.label_16.setText(_translate("Form", "Module", None))
        self.label_17.setText(_translate("Form", "Teeth Type(1,2,3)", None))
        self.label_6.setText(_translate("Form", "StrengthP(Mpa)", None))
        self.pushButton.setText(_translate("Form", "Calculate", None))
        self.pushButton_2.setText(_translate("Form", "Generate", None))

    def calculate(self):
        
    #input of parameters...
        g=float(self.textEdit.toPlainText())
        p=float(self.textEdit_2.toPlainText())
        n=float(self.textEdit_3.toPlainText())
        t=float(self.textEdit_4.toPlainText())
        BHN=float(self.textEdit_5.toPlainText())
        sigmap=float(self.textEdit_6.toPlainText())
        sigmag=float(self.textEdit_7.toPlainText())
        qws=str(self.textEdit_17.toPlainText())
        FOS=float(self.textEdit_15.toPlainText())
        ka=float(self.textEdit_8.toPlainText())
        kb=float(self.textEdit_9.toPlainText())
        bfactor=float(self.textEdit_10.toPlainText())
        kvfactor=float(self.textEdit_11.toPlainText())
        Ep=float(self.textEdit_12.toPlainText())
        Eg=float(self.textEdit_13.toPlainText())
        grade=str(self.textEdit_14.toPlainText())
        #libraries generated

        qws_lib={'1':(0.55,2.642),'2':(0.484,2.865),'3':(0.39,2.148)}
        grade_lib = {'1':(0.8,0.06),'2':(1.25,0.1),'3':(2,0.16),'4':(3.2,0.25),'5':(5,0.4),'6':(8,0.63),'7':(11,0.9),'8':(16,1.25),'9':(22,1.8),'10':(32,2.5),'11':(45,3.55),'12':(63,5)}
    #--------------------------------------------------------------------
        T=g*t
        q=2*T/(T+t)
        K=(0.000016)*((BHN)**2)
        yp=qws_lib[qws][0]-(qws_lib[qws][1]/t)
        yg=qws_lib[qws][0]-(qws_lib[qws][1]/T)
        #bending and wear %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        if yp*sigmap<=yg*sigmag:
            y=yp
            sigma=sigmap
        else:
            y=yg
            sigma=sigmag
    
        bending_coefficient=bfactor*sigma*y/3.0
        vel_coefficient=3.142*t*n/60000.0
        tgt_coefficient=ka*kb*p*1000.0/vel_coefficient
        wearing_coefficient=q*K*t*bfactor

        A2=wearing_coefficient*kvfactor/FOS
        A1=bending_coefficient*kvfactor/FOS
        #-------------------------------------------------------------------
        if A1<=A2:
            A=A1
            print "criteria is bending strength"
        else:
            A=A2
            print "criteria is wear strength"
    #-------------------------------------------------------------------
        B=0
        C=-tgt_coefficient*vel_coefficient
        D=-kvfactor*tgt_coefficient                  #Am^3+Bm^2+Cm+D=0 solve
    #-------------------------------------------------------------------
        CF = [A,B,C,D]
        M = cubicsolve.solve(A,B,C,D,0.00001)
        print "Module  = ",M
        m=math.ceil(M)
    #------------------------------------------------------------------
        if m>0:
    #effective load
            b=bfactor*m
            d=m*t
            D=m*T
            v=vel_coefficient*m
            Ft=p*1000/v

            ep=(grade_lib[grade][0])+ (grade_lib[grade][1])*(m+.25*(d)**0.5)
            eg=(grade_lib[grade][0])+ (grade_lib[grade][1])*(m+.25*(D)**0.5)
            e=(ep+eg)*0.001                                       #.............e comes in microns
            c=.111*e*(Ep*Eg/(Ep+Eg))
            Ftmax=ka*kb*Ft
            am=b*c+Ftmax
            Fd=21*v*am/(21*v+(am)**(0.5))
            Feff=Ftmax+Fd
            FOS1=(A*FOS/6)*(m**2)/Feff
            while FOS1<FOS:
                m=m+1
                b=10*m
                d=m*t
                v=vel_coefficient*m
                Ft=p/v
                ep=8+.63*(m+.25*(d)**0.5)
                eg=8+.63*(m+.25*(D)**0.5)
                e=(ep+eg)*0.001     
                c=.111*e*(Ep*Eg/(Ep+Eg))
                Ftmax=ka*kb*Ft
                am=b*c+Ftmax
                Fd=21*v*am/(21*v+(am)**(0.5))
                Feff=Ftmax+Fd
                FOS1=(A*FOS/6)*(m**2)/Feff                      #bending or wear which ever is big
            print "FOS by buckingham principle is%f with final module %d"%(FOS1,m)
        else:
            print "Given values of parameters are not possible to manufacture gear system"
        D=T*m
        d=t*m
        self.textEdit_16.insertPlainText(str(m))
        self.mod = m
        self.tooth = t
        self.geardia=D
        self.piniondia=d
        
        #--------------------------------------------------------------------------------------
# redefining parameters for pdf generation
        D=T*m
        d=t*m
        bending_force=str(math.floor(bending_coefficient*m*m))
        wear_force=str(math.floor(wearing_coefficient*m**2))
        velocity=str(math.floor(vel_coefficient*m))
        Feff=math.floor(Feff)
        self.geardia=D
        self.piniondia=d
        self.b1=b
        self.bending_force1=bending_force
        self.wear_force1=wear_force
        self.velocity1=velocity
        self.Feff1=Feff
        self.FOS11=FOS1
        self.bfactor1=bfactor
        self.gearratio=g
        self.pdf_file_name="report.pdf"
        self.pdf_file_name="report"+str(self.count)+".pdf"
        print self.count

    def generator_file(self,D,d,m,b,bending_force,wear_force,velocity,Feff,FOS1,pdf_file_name):
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.pagesizes import portrait
        #from reportlab.platypus import image

        
        c=canvas.Canvas(pdf_file_name, pagesize=portrait(letter))
        c.setFont('Helvetica', 30 , leading=None)
        c.drawCentredString(320,750,'Final report generation')
        c.setFont('Helvetica', 25 , leading=None)
        c.drawString(10,700,"Unknown Parameters")
        c.drawString(500,700,"Values")
        c.setFont('Helvetica', 20 , leading=None)
        c.drawString(10,650,'Final Module =')
        c.drawString(500,650,str(m)+"mm")
        c.drawString(10,600,'Diameter of Gear=')
        c.drawString(500,600,str(D)+"mm")
        c.drawString(10,550,'Diameter of Pinion=')
        c.drawString(500,550,str(d)+"mm")
        c.drawString(10,500,'Deddendum=')
        c.drawString(500,500,str(m)+"mm")
        c.drawString(10,450,'Addendum=')
        c.drawString(500,450,str(1.25*m)+"mm")
        c.drawString(10,400,'Facewidth=')
        c.drawString(500,400,str(b)+"mm")
        c.drawString(10,350,'Permissible Bending force=')
        c.drawString(500,350,bending_force+"N")
        c.drawString(10,300,'Permissible Wear force=')
        c.drawString(500,300,wear_force+"N")
        c.drawString(10,250,'Velocity=')
        c.drawString(500,250,velocity+"m/s")
        c.drawString(10,200,'Available Factor of safty=')
        c.drawString(500,200,str(FOS1))
        c.drawString(10,150,'Maximum Effective force=')
        c.drawString(500,150,str(Feff))
        c.drawString(0,120,"------------------------------------------------------------------------------------------------")
        c.setFont('Helvetica', 30 , leading=None)
        c.drawString(200,75,"THANK YOU")
        self.count = self.count + 1

        c.showPage()
        c.save()
        

    def gen(self):
        cadgenerator.generateGear(self.mod,self.tooth,self.bfactor1,self.gearratio,self.count)
        self.generator_file(self.geardia,self.piniondia,self.mod,self.b1,self.bending_force1,self.wear_force1,self.velocity1,self.Feff1,self.FOS11,self.pdf_file_name)
        

    def click(self,Form):
        self.pushButton.clicked.connect(self.calculate)
        self.pushButton_2.clicked.connect(self.gen)
        
        
        

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.click(Form)
    Form.show()
    sys.exit(app.exec_())
