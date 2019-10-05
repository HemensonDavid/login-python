import os
from hashlib import sha256
from login.view.telaDeLogin import iniciarTela
from login.model.models import createTables, DATABASE, User

#Iniciando pela primeira vez
if not os.path.exists(DATABASE):
    #Requerindo os dados necessários para o cadastro
    username = input('Digite seu nome: ')
    password = sha256(input('Digite sua senha: ').encode('ascii')).hexdigest()
    email = input('Digite seu email: ')

    #Criando as tabelas
    createTables()

    #Registrando no banco
    try:
        User.create(username=username, password=password, email=email)
    except Exception as e:
        print('Erro: {}'.format(e.__str__()))



#iniciando a tela
iniciarTela()
