from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Bem vindo a página inicial. Verificando mudanças."


@app.route("/admin")
def admin():
    return "Bem-Vindo ao Admin!!! :)"


@app.route("/soma/<int:n1>/<int:n2>")
def soma(n1,n2):
    soma = n1 + n2
    return f"O valor da soma de {n1} + {n2} é: {soma}"


@app.route("/numero/<string:nome>/<int:numero>")
def numero(nome, numero):
    return f"Olá {nome}, seu número passado na URL foi: {numero}"


#Métodos HTTP
@app.route("/perfil/<nome>", methods=["GET"])
def perfil(nome):
    return f"Esse é o perfil de: {nome}"

@app.route("/perfil/email", methods=["POST"])
def perfil_email():
    data = request.get_json()
    email = data["email"]
    senha = data["senha"]
    return f"<h1>Email: {email} Senha: {senha}</h1>"


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    senha = data["senha"]
    if senha == '123456':
        return render_template('profile.html', email=email)
    else:
        return 'Acesso não autorizado!!!'
        





if __name__ == "__main__":
    app.run(debug=True)