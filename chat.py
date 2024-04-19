from usuario import Usuario
from mensagem import Mensagem
from conexao import Conexao
from contato import Contato
class Chat:
    def __init__(self,nome:str,telefone:str):
        self.nome_usuario= nome
        self.telefone_usuario=telefone

    def enviar_mensagem(self,conteudo:str,contato_escolhido:Contato)->bool:
        #try:
            # conectando ao banco de dados
                mydb =Conexao.conectar()
                # criando o cursor
                mycursor = mydb.cursor()
         

            # segunda forma
                sql = f"INSERT INTO tb_mensagem (tel_remetente,mensagem,tel_destinatario) VALUES ('{self.telefone_usuario}','{conteudo}','{contato_escolhido.telefone}')"
                mycursor.execute(sql)
                mydb.commit()


                mydb.close()
                
                return True

        #except:
                return False
        
    def verificar_mensagem(self,quantidade:int,contato_escolhido):
         mydb =Conexao.conectar()
                # criando o cursor
         mycursor = mydb.cursor()
        #  sql="SELECT nome,tel_remetente,mensagem FROM tb_mensagem m INNER JOIN tb_usuario u ON u.tel = m.tel_remetente "
         sql=f"SELECT u.nome,m.mensagem from tb_mensagem m inner join tb_usuario u on m.tel_remetente= u.tel where tel_remetente='{contato_escolhido.telefone}'and tel_destinatario='{self.telefone_usuario}' or tel_destinatario= '{contato_escolhido.telefone}' and tel_remetente ='{self.telefone_usuario}'" 
         
         mycursor.execute(sql)
         resultado = mycursor.fetchall()
         mensagens=[]
         for linha in resultado:
               mensagem = {"nome":linha[0],"mensagem":linha[1]}
               mensagens.append(mensagem)
         return (mensagens)
    def retornar_contato(self,):
        mydb =Conexao.conectar()
                # criando o cursor
        mycursor = mydb.cursor()
        sql="select nome,tel from tb_usuario order by nome"
        mycursor.execute(sql)
        resultado= mycursor.fetchall()
        contatos=[]
        for linha in resultado:
              
              contatos.append({"Nome":linha[0],"telefone":linha[1]})
        return (contatos)

    