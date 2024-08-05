from flask import Flask, jsonify, request


app = Flask (__name__)

livros = [
    {
        'id': 1,
        'livro': 'A arte da guerra',
        'autor': 'Sun Tzu'
    },
    {
        'id': 2,
         'livro': 'Pai pobre e pai rico',
         'autor': 'Robert'
    
    },
    {
        'id': 3,
        'livro': 'Do mil ao milhao',
        'autor': 'Thiago Nigro'
    
    },
]

@app.route('/livros', methods=['GET'])
def consultar_livros() :
    return jsonify (livros)



@app.route('/livros/<int:id>', methods=['GET'])
def consultar_livros_por_id(id) :
 for livro in livros:
    if livro.get ('id') == id :
        return jsonify(livro)

@app.route('/livros', methods=['POST'])
def cadastrar_livros () :
    novo_livro = request.get_json ()
    livros.append (novo_livro)
    return jsonify (livros)

@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_por_id (id) :
    livro_atualizado = request.get_json ()
    for indice, livro in enumerate (livros) :
        if livro.get('id') ==id :
            livros [indice] .updete (livro_atualizado)
            return jsonify (livro[indice])


@app.route('/livros/int:id>', methods=['DELETE'])
def excluir_livro_por_id(id) :
    for indice,livro in enumerate (livro) :
        if livro.get('id') ==id:
            del livros[indice]
    return jsonify(livro)



app.run(port=8080, host='localhost', debug=True)

