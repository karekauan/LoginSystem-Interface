#imports#
import sys
import sqlite3
import PyQt5
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
#-------#

#Criando o bd e seu cursor#
bd = sqlite3.connect('Cadastros.db')
cursor = bd.cursor()
#--------------------------#

app = QtWidgets.QApplication(sys.argv) #Criando a variável de execução
Screen_Log = uic.loadUi('Login.ui') #Atribuindo o respectivo arquivos da janela
Screen_Cad = uic.loadUi('Cadastro.ui') #               |         |
Screen_Logout = uic.loadUi('Logout.ui') #              |         |  

def Abre_Cadastro():
    Screen_Cad.show()
    
def Fecha_Cadastro():
    Screen_Cad.close()
    
def Cadastro(): #Função para cadastrar dados no bd
    User = Screen_Cad.Input_Name.text() #Obtendo os dados do input
    Email = Screen_Cad.Input_Email.text() #       |     |
    Pass = Screen_Cad.Input_Pass.text() #         |     |
    Pass_Confirm = Screen_Cad.Input_Pass_Confirm.text() #    |    |
    
    if (Pass == Pass_Confirm):
        try:
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastros(nome text, email text, senha text)")
            cursor.execute("INSERT INTO cadastros VALUES('"+User+"', '"+Email+"', '"+Pass+"')")
            
            bd.commit()
            Screen_Cad.Warning_Same_Pass.setText("Usuário Cadastrado")
        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ", erro)
    else:
        Screen_Cad.Warning_Same_Pass.setText("Senhas não correpsondentes")
        
    Screen_Cad.Input_Name.setText("") #Resetando o valor dos inputs 
    Screen_Cad.Input_Email.setText("") #          |    |
    Screen_Cad.Input_Pass.setText("") #           |    |
    Screen_Cad.Input_Pass_Confirm.setText("") #   |    |   

def Login(): # Função para logar na conta
    Email = Screen_Log.Input_User.text()
    Key = Screen_Log.Input_Key.text()
    try:
        cursor.execute("SELECT senha FROM cadastros WHERE email = '"+Email+"'")
        Key_bd = cursor.fetchall()
        if (Key == Key_bd[0][0]):
            Screen_Logout.show()
            Screen_Log.close()
                
            cursor.execute("SELECT nome FROM cadastros WHERE email = '"+Email+"'")
            User_Name = cursor.fetchall()
            Screen_Logout.Ornament_Functional.setText(User_Name[0][0])
            
        else:
            Screen_Log.Warning_Wrong_Credencial.setText("Senha Incorreta")
    except:
        Screen_Log.Warning_Wrong_Credencial.setText("Email Incorreto")
        
    Screen_Log.Input_User.setText("")
    Screen_Log.Input_Key.setText("")
        
        

def Logout(): #Função para deslogar da conta
    Screen_Logout.close()
    Screen_Log.show()
    Screen_Log.Warning_Wrong_Credencial.setText("") #Zera o valor do aviso de erro
    
#Atribuindo funções aos Buttons#
Screen_Log.Button_Log.clicked.connect(Login)
Screen_Logout.Button_Out.clicked.connect(Logout)
Screen_Log.Button_Reg.clicked.connect(Abre_Cadastro)
Screen_Cad.Button_Back.clicked.connect(Fecha_Cadastro)
Screen_Cad.Button_Cad.clicked.connect(Cadastro)
#------------------------------#    

Screen_Log.show() #Exeibindo a tela inicial
sys.exit(app.exec_()) #Rodando a aplicação