from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from pyqtdesign  import*
from random import randint
from time import sleep
from PyQt5.QtCore import *

class Game(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.score=0     
        self.speed=200
        self.checker = True
        self.checker2 = True
        
        try:
            with open("D:/record.txt", "r") as file:
                self.ui.label_17.setText(f"record is {file.read()}")
        except:
            pass
        
        self.ui.label_18.setText("score"+"     "+str(self.score))
        self.ls1=[
                  [self.ui.pushButton, self.ui.pushButton_2, self.ui.pushButton_3, self.ui.pushButton_4, self.ui.pushButton_5, self.ui.pushButton_6, self.ui.pushButton_7, self.ui.pushButton_8, self.ui.pushButton_9, self.ui.pushButton_10, self.ui.pushButton_11, self.ui.pushButton_12, self.ui.pushButton_13, self.ui.pushButton_14, self.ui.pushButton_15, self.ui.pushButton_16],
                  [self.ui.pushButton_17, self.ui.pushButton_18, self.ui.pushButton_19, self.ui.pushButton_21, self.ui.pushButton_20, self.ui.pushButton_22, self.ui.pushButton_23, self.ui.pushButton_24, self.ui.pushButton_25, self.ui.pushButton_26, self.ui.pushButton_27, self.ui.pushButton_28, self.ui.pushButton_29, self.ui.pushButton_30, self.ui.pushButton_31, self.ui.pushButton_32],
                  [self.ui.pushButton_33, self.ui.pushButton_34, self.ui.pushButton_35, self.ui.pushButton_36, self.ui.pushButton_37, self.ui.pushButton_38, self.ui.pushButton_39, self.ui.pushButton_40, self.ui.pushButton_41, self.ui.pushButton_42, self.ui.pushButton_43, self.ui.pushButton_44, self.ui.pushButton_45, self.ui.pushButton_46, self.ui.pushButton_47, self.ui.pushButton_48],
                  [self.ui.pushButton_49, self.ui.pushButton_50, self.ui.pushButton_51, self.ui.pushButton_52, self.ui.pushButton_53, self.ui.pushButton_54, self.ui.pushButton_55, self.ui.pushButton_56, self.ui.pushButton_57, self.ui.pushButton_58, self.ui.pushButton_59, self.ui.pushButton_60, self.ui.pushButton_61, self.ui.pushButton_62, self.ui.pushButton_63, self.ui.pushButton_64],
                  [self.ui.pushButton_65, self.ui.pushButton_66, self.ui.pushButton_67, self.ui.pushButton_68, self.ui.pushButton_69, self.ui.pushButton_70, self.ui.pushButton_71, self.ui.pushButton_72, self.ui.pushButton_73, self.ui.pushButton_74, self.ui.pushButton_75, self.ui.pushButton_76, self.ui.pushButton_77, self.ui.pushButton_78, self.ui.pushButton_79, self.ui.pushButton_80],
                  [self.ui.pushButton_81, self.ui.pushButton_82, self.ui.pushButton_83, self.ui.pushButton_84, self.ui.pushButton_85, self.ui.pushButton_86, self.ui.pushButton_87, self.ui.pushButton_88, self.ui.pushButton_89, self.ui.pushButton_90, self.ui.pushButton_91, self.ui.pushButton_92, self.ui.pushButton_93, self.ui.pushButton_94, self.ui.pushButton_95, self.ui.pushButton_96],
                  [self.ui.pushButton_97, self.ui.pushButton_98, self.ui.pushButton_99, self.ui.pushButton_100, self.ui.pushButton_101, self.ui.pushButton_102, self.ui.pushButton_103, self.ui.pushButton_104, self.ui.pushButton_105, self.ui.pushButton_106, self.ui.pushButton_107, self.ui.pushButton_108, self.ui.pushButton_109, self.ui.pushButton_110, self.ui.pushButton_111, self.ui.pushButton_112],
                  [self.ui.pushButton_113, self.ui.pushButton_114, self.ui.pushButton_115, self.ui.pushButton_116, self.ui.pushButton_117, self.ui.pushButton_118, self.ui.pushButton_119, self.ui.pushButton_120, self.ui.pushButton_121, self.ui.pushButton_122, self.ui.pushButton_123, self.ui.pushButton_124, self.ui.pushButton_125, self.ui.pushButton_126, self.ui.pushButton_127, self.ui.pushButton_128],
                  [self.ui.pushButton_129, self.ui.pushButton_130, self.ui.pushButton_131, self.ui.pushButton_132, self.ui.pushButton_133, self.ui.pushButton_134, self.ui.pushButton_135, self.ui.pushButton_136, self.ui.pushButton_137, self.ui.pushButton_138, self.ui.pushButton_139, self.ui.pushButton_140, self.ui.pushButton_141, self.ui.pushButton_142, self.ui.pushButton_143, self.ui.pushButton_144],
                  [self.ui.pushButton_145, self.ui.pushButton_146, self.ui.pushButton_147, self.ui.pushButton_148, self.ui.pushButton_149, self.ui.pushButton_150, self.ui.pushButton_151, self.ui.pushButton_152, self.ui.pushButton_153, self.ui.pushButton_154, self.ui.pushButton_155, self.ui.pushButton_156, self.ui.pushButton_157, self.ui.pushButton_158, self.ui.pushButton_159, self.ui.pushButton_160],
                  [self.ui.pushButton_161, self.ui.pushButton_162, self.ui.pushButton_163, self.ui.pushButton_164, self.ui.pushButton_165, self.ui.pushButton_166, self.ui.pushButton_167, self.ui.pushButton_168, self.ui.pushButton_169, self.ui.pushButton_170, self.ui.pushButton_171, self.ui.pushButton_172, self.ui.pushButton_173, self.ui.pushButton_174, self.ui.pushButton_175, self.ui.pushButton_176],
                  [self.ui.pushButton_177, self.ui.pushButton_178, self.ui.pushButton_179, self.ui.pushButton_180, self.ui.pushButton_181, self.ui.pushButton_182, self.ui.pushButton_183, self.ui.pushButton_184, self.ui.pushButton_185, self.ui.pushButton_186, self.ui.pushButton_187, self.ui.pushButton_188, self.ui.pushButton_189, self.ui.pushButton_190, self.ui.pushButton_191, self.ui.pushButton_192],
                  [self.ui.pushButton_193, self.ui.pushButton_194, self.ui.pushButton_195, self.ui.pushButton_196, self.ui.pushButton_197, self.ui.pushButton_198, self.ui.pushButton_199, self.ui.pushButton_200, self.ui.pushButton_201, self.ui.pushButton_202, self.ui.pushButton_203, self.ui.pushButton_204, self.ui.pushButton_205, self.ui.pushButton_206, self.ui.pushButton_207, self.ui.pushButton_208],
                  [self.ui.pushButton_209, self.ui.pushButton_210, self.ui.pushButton_211, self.ui.pushButton_212, self.ui.pushButton_213, self.ui.pushButton_214, self.ui.pushButton_215, self.ui.pushButton_216, self.ui.pushButton_217, self.ui.pushButton_218, self.ui.pushButton_219, self.ui.pushButton_220, self.ui.pushButton_221, self.ui.pushButton_222, self.ui.pushButton_223, self.ui.pushButton_224],
                  [self.ui.pushButton_225, self.ui.pushButton_226, self.ui.pushButton_227, self.ui.pushButton_228, self.ui.pushButton_229, self.ui.pushButton_230, self.ui.pushButton_231, self.ui.pushButton_232, self.ui.pushButton_233, self.ui.pushButton_234, self.ui.pushButton_235, self.ui.pushButton_236, self.ui.pushButton_237, self.ui.pushButton_238, self.ui.pushButton_239, self.ui.pushButton_240],
                  [self.ui.pushButton_241, self.ui.pushButton_242, self.ui.pushButton_243, self.ui.pushButton_244, self.ui.pushButton_245, self.ui.pushButton_246, self.ui.pushButton_247, self.ui.pushButton_248, self.ui.pushButton_249, self.ui.pushButton_250, self.ui.pushButton_251, self.ui.pushButton_252, self.ui.pushButton_253, self.ui.pushButton_254, self.ui.pushButton_255, self.ui.pushButton_256]
                 ]
            
        self.ls2=[
                  [self.ui.pushButton_257, self.ui.pushButton_258, self.ui.pushButton_259, self.ui.pushButton_260, self.ui.pushButton_261, self.ui.pushButton_262, self.ui.pushButton_263, self.ui.pushButton_264],
                  [self.ui.pushButton_265, self.ui.pushButton_266, self.ui.pushButton_267, self.ui.pushButton_268, self.ui.pushButton_269, self.ui.pushButton_270, self.ui.pushButton_271, self.ui.pushButton_272],
                  [self.ui.pushButton_273, self.ui.pushButton_274, self.ui.pushButton_275, self.ui.pushButton_276, self.ui.pushButton_277, self.ui.pushButton_278, self.ui.pushButton_279, self.ui.pushButton_280],
                  [self.ui.pushButton_281, self.ui.pushButton_282, self.ui.pushButton_283, self.ui.pushButton_284, self.ui.pushButton_285, self.ui.pushButton_286, self.ui.pushButton_287, self.ui.pushButton_288],
                  [self.ui.pushButton_289, self.ui.pushButton_290, self.ui.pushButton_291, self.ui.pushButton_292, self.ui.pushButton_293, self.ui.pushButton_294, self.ui.pushButton_295, self.ui.pushButton_296],
                  [self.ui.pushButton_297, self.ui.pushButton_298, self.ui.pushButton_299, self.ui.pushButton_300, self.ui.pushButton_301, self.ui.pushButton_302, self.ui.pushButton_303, self.ui.pushButton_304],
                  [self.ui.pushButton_305, self.ui.pushButton_306, self.ui.pushButton_307, self.ui.pushButton_308, self.ui.pushButton_309, self.ui.pushButton_310, self.ui.pushButton_311, self.ui.pushButton_312],
                  [self.ui.pushButton_313, self.ui.pushButton_314, self.ui.pushButton_315, self.ui.pushButton_316, self.ui.pushButton_317, self.ui.pushButton_318, self.ui.pushButton_319, self.ui.pushButton_320],
                  [self.ui.pushButton_321, self.ui.pushButton_322, self.ui.pushButton_323, self.ui.pushButton_324, self.ui.pushButton_325, self.ui.pushButton_326, self.ui.pushButton_327, self.ui.pushButton_328],
                  [self.ui.pushButton_329, self.ui.pushButton_330]         
                 ]
        
        self.color=["#FF0000", "#FF8C00", "#FFE500", "#BEFF00", "#47FF00", "#00FF92", "#00F5FF", "#00A2FF", "#0057FF", "#8F00FF", "#D200FF", "#68952A", "#B22A67", "#122097"]
                
        self.ls3=[self.ui.pushButton_331, self.ui.pushButton_332, self.ui.pushButton_333, self.ui.pushButton_334, self.ui.pushButton_335, self.ui.pushButton_336, self.ui.pushButton_337, self.ui.pushButton_338, self.ui.pushButton_339, self.ui.pushButton_340, self.ui.pushButton_341, self.ui.pushButton_342, self.ui.pushButton_343, self.ui.pushButton_344, self.ui.pushButton_345, self.ui.pushButton_346, self.ui.pushButton_347]
        
        self.ls4=[self.ui.pushButton_m, self.ui.pushButton_m2, self.ui.pushButton_m3, self.ui.pushButton_m4, self.ui.pushButton_m5, self.ui.pushButton_m6, self.ui.pushButton_m7, self.ui.pushButton_m8, self.ui.pushButton_m9, self.ui.pushButton_m10, self.ui.pushButton_m11, self.ui.pushButton_m12, self.ui.pushButton_m13, self.ui.pushButton_m14, self.ui.pushButton_m15, self.ui.pushButton_m16]

        for i in range(5):
            self.ls3[i].setText("❤️")
            
        for i in range(16):
            self.ls4[i].clicked.connect(self.Pressls4)
        
        self.ui.nightbtn.clicked.connect(self.PressNight)
        
        self.ui.pushButton_348.clicked.connect(self.PressLR)     
        self.ui.pushButton_349.clicked.connect(self.PressLR)
             
        self.ui.pushButton_348.setStyleSheet("background: #41C5C3; color: red")     
        self.ui.pushButton_349.setStyleSheet("background: #41C5C3; color: red")    
        self.ui.label_17.setStyleSheet("color: red") 
        self.ui.label_18.setStyleSheet("color: red") 
        
        self.ChangeColorls2()
        self.Standartls4()
        self.HealthStrandartls3()
        
        self.timer1 = QTimer()
        self.timer1.setInterval(500)
        self.timer1.timeout.connect(self.CreateMoveFire)
        self.timer2 = QTimer()
        self.timer2.setInterval(self.speed)
        self.timer2.timeout.connect(self.CreateMoveBullet)
        self.timer1.start()
        self.timer2.start()
        
    
    def keyPressEvent(self,event) -> None:
        n=event.key()
        if n==16777234:
            if self.ls4[0].text()=='':
                for i in range(16):
                    if self.ls4[i].text()=="🛰":
                        break
                self.ls4[i].setText('')
                self.ls4[i-1].setText("🛰")
                
        elif n==16777236:
            if self.ls4[-1].text()=='':
                for i in range(16):
                    if self.ls4[i].text()=="🛰":
                        break
                self.ls4[i].setText('')
                self.ls4[i+1].setText("🛰")
     
       
    def ChangeColorls2(self):
        for i in range(9):
            for j in range(8):
                self.ls2[i][j].setStyleSheet(f"background: {self.color[randint(0,13)]}")
        self.ls2[9][0].setStyleSheet(f"background: {self.color[randint(0,13)]}")
        self.ls2[9][1].setStyleSheet(f"background: {self.color[randint(0,13)]}")
        
    def Standartls4(self):
        for i in range(16):
            self.ls4[i].setStyleSheet("background: #41C5C3; font-size: 30px")
               
    def HealthStrandartls3(self):
        for i in range(16):
            self.ls3[i].setStyleSheet("color: red; font-size: 30px")
            
    def PressNight(self):
        if self.ui.nightbtn.text()=="🌙":
            self.setStyleSheet('background: black')
            self.ui.nightbtn.setText("🌞")
        else:
            self.setStyleSheet("background: white")
            self.ui.nightbtn.setText("🌙")
            
    def PressLR(self):
        if self.sender().text()=='Left':
            if self.ls4[0].text()=='':
                for i in range(16):
                    if self.ls4[i].text()=="🛰":
                        break
                self.ls4[i].setText('')
                self.ls4[i-1].setText("🛰")
                        
        else:
            if self.ls4[-1].text()=='':
                for i in range(16):
                    if self.ls4[i].text()=="🛰":
                        break
                self.ls4[i].setText('')
                self.ls4[i+1].setText("🛰")
        
            
    def Pressls4(self):
        for i in range(16):
            if self.ls4[i].text()=="🛰":
                break
        self.ls4[i].setText('')
        if self.sender().objectName()=="pushButton_m":
            self.ls4[0].setText("🛰")
        elif self.sender().objectName()=="pushButton_m2":
            self.ls4[1].setText("🛰")
        elif self.sender().objectName()=="pushButton_m3":
            self.ls4[2].setText("🛰")
        elif self.sender().objectName()=="pushButton_m4":
            self.ls4[3].setText("🛰")
        elif self.sender().objectName()=="pushButton_m5":
            self.ls4[4].setText("🛰")
        elif self.sender().objectName()=="pushButton_m6":
            self.ls4[5].setText("🛰")
        elif self.sender().objectName()=="pushButton_m7":
            self.ls4[6].setText("🛰")
        elif self.sender().objectName()=="pushButton_m8":
            self.ls4[7].setText("🛰")
        elif self.sender().objectName()=="pushButton_m9":
            self.ls4[8].setText("🛰")
        elif self.sender().objectName()=="pushButton_m10":
            self.ls4[9].setText("🛰")
        elif self.sender().objectName()=="pushButton_m11":
            self.ls4[10].setText("🛰")
        elif self.sender().objectName()=="pushButton_m12":
            self.ls4[11].setText("🛰")
        elif self.sender().objectName()=="pushButton_m13":
            self.ls4[12].setText("🛰")
        elif self.sender().objectName()=="pushButton_m14":
            self.ls4[13].setText("🛰")
        elif self.sender().objectName()=="pushButton_m15":
            self.ls4[14].setText("🛰")
        elif self.sender().objectName()=="pushButton_m16":
            self.ls4[15].setText("🛰")
            
            
    def CreateMoveFire(self):
        lst1=list()
        lst2=list()
        for i in range(16):
            for j in range(16):
                if i<15 and self.ls1[i][j].text() == "🛸" and self.ls1[i+1][j].text()=="💥":
                    lst1.append((i,j))
                elif i<15 and self.ls1[i][j].text() == "❤️" and self.ls1[i+1][j].text()=="💥":
                    lst2.append((i,j))
                    
        lst=list()
        life=17
        for i in range(16):
            for j in range(16):
                if self.ls1[i][j].text() == "🛸":
                    lst.append((i,j))
        lstt=list()           
        for i in range(16):
            for j in range(16):
                if self.ls1[i][j].text() == "❤️":
                    lstt.append((i,j))
                    
        for i in lstt:
            if i[0]!=15:
                self.ls1[i[0]+1][i[1]].setText("❤️")
                self.ls1[i[0]][i[1]].setText("")
            else:
                self.ls1[15][i[1]].setText("")
            
        for i in lst:
            if i[0]!=15:
                self.ls1[i[0]+1][i[1]].setText("🛸")
                self.ls1[i[0]][i[1]].setText("")
            else:
                self.ls1[15][i[1]].setText("")
                for j in range(16,-1,-1):
                    if(self.ls3[j].text()!=""):
                        life=j
                        break        
                if life!=17:
                    self.ls3[life].setText("")
                    if life == 0:
                        for i in range(16):
                            for j in range(16):
                                self.ls1[i][j].setEnabled(False)
                        for i in range(16):
                            self.ls4[i].setEnabled(False)
                        self.ui.pushButton_348.setEnabled(False)
                        self.ui.pushButton_349.setEnabled(False)
                        self.timer1.stop()
                        self.timer2.stop()
                        for i in range(16):
                            for j in range(16):
                                self.ls1[i][j].setText("")
                        
                        self.FileFunc()
                        self.checker2 = False
                        
                    
                else:
                    for i in range(16):
                        for j in range(16):
                            self.ls1[i][j].setEnabled(False)
                    for i in range(16):
                        self.ls4[i].setEnabled(False)
                    self.ui.pushButton_348.setEnabled(False)
                    self.ui.pushButton_349.setEnabled(False)
                    self.timer1.stop()
                    self.timer2.stop()
                    
                    for i in range(16):
                        for j in range(16):
                            self.ls1[i][j].setText("")
                    self.FileFunc()
                    self.checker2 = False
                    
                    return   
        
        if self.speed>50 and self.checker2:
            self.timer2.stop()
            self.speed-=1
            self.timer2 = QTimer()
            self.timer2.setInterval(self.speed)
            self.timer2.timeout.connect(self.CreateMoveBullet)
            self.timer2.start()
        elif self.checker and self.checker2:
            self.checker = False
            self.timer1.stop()
            self.timer1 = QTimer()
            self.timer1.setInterval(300)
            self.timer1.timeout.connect(self.CreateMoveFire)
            self.timer1.start()
            
                
        
        for i in lst1:
            self.ls1[i[0]+1][i[1]].setText("")
            self.score+=1
            self.ui.label_18.setText("score"+"     "+str(self.score))
        
        for i in lst2:
            life=17
            self.ls1[i[0]+1][i[1]].setText("")
            for j in range(16,-1,-1):
                if(self.ls3[j].text()!=""):
                    life=j
                    break
            if life<16:
                self.ls3[life+1].setText("❤️")
            
        
        
        self.ls1[0][randint(0,15)].setText("🛸")
        
        for i in range(int(self.ui.label_18.text()[10::])//50):
            self.ls1[0][randint(0,15)].setText("🛸")
        
        ran = randint(0,100)
        
        if ran == 50:
            self.ls1[0][randint(0,15)].setText("❤️")
           
                
                
    def CreateMoveBullet(self):
        lst1=list()
        lst2=list()
        for i in range(16):
            for j in range(16):
                if i>0 and self.ls1[i][j].text() == "💥" and self.ls1[i-1][j].text()=="🛸":
                    lst1.append((i,j))
                elif i>0 and self.ls1[i][j].text() == "💥" and self.ls1[i-1][j].text()=="❤️":
                    lst2.append((i,j))
                    
        
        lst=list()
        for i in range(16):
            for j in range(16):
                if self.ls1[i][j].text() == "💥":
                    lst.append((i,j))
            
        for i in lst:
            if i[0]!=0:
                self.ls1[i[0]-1][i[1]].setText("💥")
                self.ls1[i[0]][i[1]].setText("")
            else:
                self.ls1[i[0]][i[1]].setText("")
        
        for i in lst1:
            self.ls1[i[0]-1][i[1]].setText("")
            self.score+=1
            self.ui.label_18.setText("score"+"     "+str(self.score))
            
        for i in lst2:
            life=17
            self.ls1[i[0]-1][i[1]].setText("")
            for j in range(16,-1,-1):
                if(self.ls3[j].text()!=""):
                    life=j
                    break
    
            if life<16:
                self.ls3[life+1].setText("❤️")
        
        for i in range(16):
            if self.ls4[i].text()=="🛰":
                break
        
        self.ls1[15][i].setText("💥")
        
    def FileFunc(self):
        try:
            with open("D:/record.txt", "r") as file:
                temp = file.read()
                if self.score>int(temp):
                    with open("D:/record.txt", "w") as writee:
                        writee.write(str(self.score))
        except:
            with open("D:/record.txt", "w") as writee:
                writee.write(str(self.score))
            
        
           
        
app=QApplication([])

win=Game()
win.show()

sys.exit(app.exec_())
