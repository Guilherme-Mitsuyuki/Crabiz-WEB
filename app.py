from flask import Flask,session, render_template, request, redirect,jsonify
from conexao import Conexao
from hashlib import sha256
from usuario import Usuario
from chat import Chat
from contato import Contato


usuarios_cadastrados=[]

app= Flask (__name__)
app.secret_key ='yuki'
mensagens=["seja bem vindo ao Crabiz"]
@app.route("/",methods=["GET","POST"])
def cadastro():
    if request.method == "GET":
     session.clear()
     return render_template("cadastro.html")
    else:
        
        nome = request.form["nome"]
        senha= request.form["senha"]
        tel=request.form["telefone"]
        usuario=Usuario()
        usuario.cadastrar(tel,nome,senha)
        session['usuario_logado'] = {'nome':usuario.nome,'telefone':usuario.telefone}
        return render_template("login.html")
@app.route("/login",methods=["GET","POST"])
def logar():
    if request.method == "GET":
     return render_template("logar.html")
    else:
        senha= request.form["senha"]
        tel=request.form["telefone"]
        usuario=Usuario()
        usuario.logar(tel,senha)
        if usuario.logado==True:
            session['usuario_logado'] = {'nome':usuario.nome,'telefone':usuario.telefone}
            return render_template("chat.html")
        else:
           return "Não Possível logar"
@app.route("/get/usuarios")
def api_get_usuarios():
    nome_usuario = session["usuario_logado"]["nome"]
    telefone_usuario = session["usuario_logado"]["telefone"]
    chat=Chat(nome_usuario,telefone_usuario)
    contatos=chat.retornar_contato()
    return jsonify(contatos),200
           
    
@app.route("/get/mensagens/<tel_destinatario>")
def api_get_mensagens(tel_destinatario):
    contato=Contato("",tel_destinatario)
    nome_usuario = session["usuario_logado"]["nome"]
    telefone_usuario = session["usuario_logado"]["telefone"]
    chat=Chat(nome_usuario,telefone_usuario)
    mensagens=chat.verificar_mensagem(0,contato)
    return jsonify(mensagens),200


@app.route("/enviar_via_ajax/", methods=["POST"])
def post_cadastro_ajax():
         #Pegando os dados que foram enviados
    dados = request.get_json()


    telefone = dados ["telefone"]

    mensagem = dados["mensagem"]

     #Instanciando o objeto usuário

    nome_usuario = session["usuario_logado"]["nome"]
    telefone_usuario = session["usuario_logado"]["telefone"]
    chat=Chat(nome_usuario,telefone_usuario)

        #Cadastrando e retornando se deu certo ou não
    destinatario=Contato("",telefone)
    if chat.enviar_mensagem(mensagem, destinatario) == True: 
        return jsonify({'mensagem':'Cadastro'}), 200

    else:
        return jsonify({'mensagem':'ERRO'}), 500
app.run(debug=True)
