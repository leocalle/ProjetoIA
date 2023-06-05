from flask import Flask, jsonify, render_template, request

from math import sqrt
app = Flask(__name__)

# Dados de exemplo com atributos dos produtos
produtos = [
    {'src': 'static/imagem/violao A.jpg','nome': 'Violão A', 'categoria': 'violoes', 'preco': 500, 'caracteristica': 'acustico' },
    { 'src': 'static/imagem/violao B.jpg','nome': 'Violão B', 'categoria': 'violoes', 'preco': 800, 'caracteristica': 'eletroacustico',},
    {'src': 'static/imagem/violão C.jpg','nome': 'Violão C', 'categoria': 'violoes', 'preco': 1200, 'caracteristica': 'eletroacustico' },
    {'src': 'static/imagem/violao D.jpg','nome': 'Violão D', 'categoria': 'violoes', 'preco': 2200, 'caracteristica': 'eletroacustico' },
    {'src': 'static/imagem/violão E.jpg','nome': 'Violão E', 'categoria': 'violoes', 'preco': 4000, 'caracteristica': 'eletroacustico'},

    {'src': 'static/imagem/teclado A.jpg','nome': 'Teclado A', 'categoria': 'teclados', 'preco': 500, 'caracteristica': 'acustico' },
    { 'src': 'static/imagem/teclado B.jpg','nome': 'Teclado B', 'categoria': 'teclados', 'preco': 800, 'caracteristica': 'eletroacustico',},
    {'src': 'static/imagem/teclado C.jpg','nome': 'Teclado C', 'categoria': 'teclados', 'preco': 1200, 'caracteristica': 'eletroacustico' },
    {'src': 'static/imagem/teclado D.jpg','nome': 'Teclado D', 'categoria': 'teclados', 'preco': 2200, 'caracteristica': 'eletroacustico' },
    {'src': 'static/imagem/teclado E.jpg','nome': 'Teclado E', 'categoria': 'teclados', 'preco': 4000, 'caracteristica': 'eletroacustico'},


    {'src': 'static/imagem/bateria A.jpg','nome': 'Bateria A', 'categoria': 'baterias', 'preco': 500, 'caracteristica': 'acustico' },
    { 'src': 'static/imagem/bateria B.jpg','nome': 'Bateria B', 'categoria': 'baterias', 'preco': 800, 'caracteristica': 'eletroacustico',},
    {'src': 'static/imagem/bateria C.jpg','nome': 'Bateria C', 'categoria': 'baterias', 'preco': 1200, 'caracteristica': 'eletroacustico' },
    {'src': 'static/imagem/bateria D.jpg','nome': 'Bateria D', 'categoria': 'baterias', 'preco': 2200, 'caracteristica': 'eletroacustico' },
    {'src': 'static/imagem/bateria E.jpg','nome': 'Bateria E', 'categoria': 'baterias', 'preco': 4000, 'caracteristica': 'eletroacustico'},



    
    {'src': 'static/imagem/guitarra A.jpg','nome': 'Guitarra A', 'categoria': 'guitarras', 'preco': 500, 'caracteristica': 'acustico' },
    { 'src': 'static/imagem/guitarra B.jpg','nome': 'Guitarra B', 'categoria': 'guitarras', 'preco': 800, 'caracteristica': 'eletroacustico',},
    {'src': 'static/imagem/guitarra C.jpg','nome': 'Guitarra C', 'categoria': 'guitarras', 'preco': 1200, 'caracteristica': 'eletroacustico' },
    {'src': 'static/imagem/guitarra D.jpg','nome': 'Guitarra D', 'categoria': 'guitarras', 'preco': 2200, 'caracteristica': 'eletroacustico' },
    {'src': 'static/imagem/guitarra E.jpg','nome': 'Guitarra E', 'categoria': 'guitarras', 'preco': 4000, 'caracteristica': 'eletroacustico'},


]






# Função para calcular a similaridade entre produtos com base na distância euclidiana
def calcular_similaridade(produto1, produto2):
    atributos1 = [produto1['preco']]
    atributos2 = [produto2['preco']]
   
    distance = sqrt((produto1['preco'] -produto2['preco'] ) ** 2)

   
    similaridade = 1 / (1 + distance)

    return similaridade




def recomendar_produtos(produto_alvo, produtos):
    produto_similar = None
    maior_similaridade = -1

    for produto in produtos:
        if produto != produto_alvo and produto['categoria'] == produto_alvo['categoria']:
            similaridade = calcular_similaridade(produto_alvo, produto)
            if similaridade > maior_similaridade:
                maior_similaridade = similaridade
                produto_similar = produto

    return produto_similar











# Rota inicial da página
@app.route('/')
def index():
   
    
    return render_template('index.html')

@app.route("/comparar-produto", methods=["POST"])
def processar_valor():
    data = request.get_json()
    valor = data.get("valor")
    
    for produto in produtos:
        if produto['nome'] == valor:
            produto_referencia = {'src': produto['src'],'nome': produto['nome'], 'categoria': produto['categoria'], 'preco': produto['preco'], 'caracteristica': produto['caracteristica']}
            produto_similar = recomendar_produtos(produto_referencia, produtos)
            return jsonify({'produto': produto_similar})
       
  


if __name__ == '__main__':
    app.run(debug=True)
