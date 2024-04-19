from conexao import Conexao
from hashlib import sha256

class Usuario:
    def __init__(self):
        self.telefone=None
        self.nome=None
        self.senha=None
        self.logado= False

    def cadastrar (self,telefone,nome,senha):
        senha = sha256(senha.encode()).hexdigest()
        try:
            # conectando ao banco de dados
            mydb =Conexao.conectar()
            # criando o cursor
            mycursor = mydb.cursor()
            # primeira forma
            # sql = "INSERT INTO tb_usuario (telefone,nome,senha) VALUES (%s, %s,%s)"
            # val = (self.telefone,self.nome,self.senha)
            

            # segunda forma
            sql = f"INSERT INTO tb_usuario (tel,nome,senha) VALUES ('{telefone}','{nome}','{senha}')"
            mycursor.execute(sql)
            mydb.commit()


            mydb.close()
            self.telefone=telefone
            self.nome=nome
            self.senha=senha
            self.logado=True
            return True
        
        except:
            return False
        
    def logar(self,telefone,senha):
        senha = sha256(senha.encode()).hexdigest()
        mydb= Conexao.conectar()
        mycursor = mydb.cursor()

        sql=(f"SELECT tel,nome,senha FROM tb_usuario where tel ='{telefone}' and senha ='{senha}'")
        mycursor.execute(sql)

        resultado= mycursor.fetchone()

        if not resultado == None:
            self.telefone= resultado[0]
            self.nome= resultado[1]
            self.senha= resultado[2]
            self.logado= True
        else:
            self.logado = False

        

    

            
        