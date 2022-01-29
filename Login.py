# Importação de Bibliotecas #
import PySimpleGUI as sg
import sqlite3 
#---------------------------#

# Criação do bd e seu cursor #
bd = sqlite3.connect('Cadastros.db')
cursor = bd.cursor()
#----------------------------#

# Criação dos layouts no esquema linha/coluna e escolha do tema#
sg.theme('Dark Gray 11')

Login_Layout = [
    [sg.Text('Email:  '), sg.Input(key='Log', size=(30, 1))],
    [sg.Text('Senha: '), sg.Input(key='Pass', size=(30, 1), password_char='*')],
    [sg.Button('Login'), sg.Text('', size=(30, 1)), sg.Button('Cadastrar')]
]

Cadastro_Layout = [
    [sg.Text('Informe seu email:   '), sg.Input(key='User', size=(30, 1))],
    [sg.Text('Informe sua senha:  '), sg.Input(key='Key', size=(30, 1))],
    [sg.Button('Cadastrar')],
]
#--------------------------------------------#

Login_Tela = sg.Window('Tela de Login', Login_Layout) # Instanciando a janela de login
Cadastro_Tela = sg.Window('Tela de Cadastro', Cadastro_Layout) # Instanciando a janela de cadastro

def Login(): # Função para verificar campos vazios e conferir igualdade de credenciais
    a
    
    
def Cadastrar(): # Função para verificar campos vazios e cadastrar as credenciais nos arquivos
    if Cadastro_event == 'Cadastrar':
     cursor.execute("CREATE TABLE IF NOT EXISTS cadastros (email text, senha text)")   
    if Cadastro_values['User'] != '' and Cadastro_values['Key'] != '':
        email = Cadastro_values['User']
        senha = Cadastro_values['Key']
        cursor.execute(f"INSERT INTO cadastros VALUES('{email}', '{senha}')")
        bd.commit()
        Cadastro_Tela.close()      
    else:
        sg.popup_error('Campo vazio, preencha e tente novamente')

while True: # Laço principal para repetição infinita
    Login_event, Login_values = Login_Tela.read() # Obtenção dos valores e eventos da janela
    if Login_event == sg.WINDOW_CLOSED or Login_event == 'Exit': # Encerramento do laço principal
        break
    if Login_event == 'Login':
        Login()
    if Login_event == 'Cadastrar':
            Cadastro_event, Cadastro_values = Cadastro_Tela.read() # Obtenção dos valores e eventos da janela
            if Cadastro_event == sg.WINDOW_CLOSED or Cadastro_event == 'Exit': # Encerramento da janela
                Cadastro_Tela.close()
            Cadastrar()