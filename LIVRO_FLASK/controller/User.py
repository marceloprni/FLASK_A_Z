from model.User import User 

class UserController():
    def __init__(self):
        self.user_model = User()
    
    def login(self, email, password):
        """
        Pega os dados de e-mail e salva no atributo da model de usuario.
        """
        self.user_model.email = email
        """
        Verifica se o usuário existe no banco de dados
        """
        result = self.user_model.get_user_by_email()

        """
        Caso o usuário exista o result não será none
        """

        if result is not None:
            """         
            Verifica se o password que o usuario enviou, agora e convertido em hash,            
            é igual ao password que foi pego no banco de dados para usuario     
            """
            
            res = self.user_model.verify_password(password, result.password)
        
        # Se for o moesmo retornará true
        if res:
            return result
        else:
            return {}
        return {}

    def recovery(email):
        """
        Trabalhando com serviços de e-mail.
        """
        return ''
