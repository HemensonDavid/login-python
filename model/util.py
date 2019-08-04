from model.models import User

def isAutenticarLogin(email, password):
    '''
    Função responsável por autenticar o login
    '''
    user = User.select().where(User.email == email and User.password == password)
    return user.count() > 0