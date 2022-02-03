#imports#
from re import A
import sys
import sqlite3
import PyQt5
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import *
from pyrsistent import dq
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
    
def Same_User():
    User = Screen_Cad.Input_Name.text()
    cursor.execute("SELECT nome FROM cadastros WHERE nome = '"+User+"'")
    bd_User = cursor.fetchall()
    if (User == bd_User[0][0]):
        Screen_Cad.Warning_Same_Pass.setText("Nome indisponível")
                
def Same_Email():
    Email = Screen_Cad.Input_Email.text()
    cursor.execute("SELECT email FROM cadastros WHERE email = '"+Email+"'")
    bd_Email = cursor.fetchall()
    if (Email == bd_Email[0][0]):
        Screen_Cad.Warning_Same_Pass.setText("Email indisponível")
        
def Cadastra():
    User = Screen_Cad.Input_Name.text() #Obtendo os dados do input
    Email = Screen_Cad.Input_Email.text() #       |     |
    Pass = Screen_Cad.Input_Pass.text()
    cursor.execute("CREATE TABLE IF NOT EXISTS cadastros(nome text, email text, senha text)")
    cursor.execute("INSERT INTO cadastros VALUES('"+User+"', '"+Email+"', '"+Pass+"')")
                    
    bd.commit()
    Screen_Cad.Warning_Same_Pass.setText("Usuário Cadastrado")
    
def Loga():
    Email = Screen_Log.Input_User.text()
    Key = Screen_Log.Input_Key.text()
    cursor.execute("SELECT senha FROM cadastros WHERE email = '"+Email+"'")
    bd_Key = cursor.fetchall()
    if (Key == bd_Key[0][0]):
        Screen_Logout.show()
        Screen_Log.close()
                
        cursor.execute("SELECT nome FROM cadastros WHERE email = '"+Email+"'")
        User_Name = cursor.fetchall()
        Screen_Logout.Ornament_Functional.setText(User_Name[0][0])
            
    else:
        Screen_Log.Warning_Wrong_Credencial.setText("Senha Incorreta")

def Reseta_Cad():
    Screen_Cad.Input_Name.setText("")
    Screen_Cad.Input_Email.setText("")
    Screen_Cad.Input_Pass.setText("")
    Screen_Cad.Input_Pass_Confirm.setText("")
    Screen_Log.Warning_Wrong_Credencial.setText("")
    
def Reseta_Log():
    Screen_Log.Input_User.setText("")
    Screen_Log.Input_Key.setText("")
 
def Logout(): #Função para deslogar da conta
    Screen_Logout.close()
    Screen_Log.show()
    Screen_Log.Warning_Wrong_Credencial.setText("") #Zera o valor do aviso de erro
   
def Cadastro(): #Função para cadastrar dados no bd
    Pass = Screen_Cad.Input_Pass.text()
    Pass_Confirm = Screen_Cad.Input_Pass_Confirm.text()
    
    if (Pass == Pass_Confirm):
        try:
            Same_User()
        except:
            try:
                Same_Email()
            except:
                try:
                    Cadastra()
                except sqlite3.Error as erro:
                    print("Erro ao inserir os dados: ", erro)
    else:
        Screen_Cad.Warning_Same_Pass.setText("Senhas não correpsondentes")
    Reseta_Cad()  

def Login(): # Função para logar na conta
    try:
        Loga()
    except:
        Screen_Log.Warning_Wrong_Credencial.setText("Email Incorreto")
    Reseta_Log()
    
#Atribuindo funções aos Buttons#
Screen_Log.Button_Log.clicked.connect(Login)
Screen_Logout.Button_Out.clicked.connect(Logout)
Screen_Log.Button_Reg.clicked.connect(Abre_Cadastro)
Screen_Cad.Button_Back.clicked.connect(Fecha_Cadastro)
Screen_Cad.Button_Cad.clicked.connect(Cadastro)
#------------------------------#    

Screen_Log.show() #Exeibindo a tela inicial
sys.exit(app.exec_()) #Rodando a aplicação