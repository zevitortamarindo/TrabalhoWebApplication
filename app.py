from flask import Flask, render_template, request, redirect, url_for
from uuid import uuid4
from os.path import exists
import csv

app = Flask(__name__)

musicas = [
    {'id': uuid4(), 'artista':'Michel Teló', 'titulo':'Ai se eu te pego', 'ano':'2011', 'album':'Na Balada', 'reproducoes':'204,7 milhões'},
    {'id': uuid4(), 'artista':'Los Hermanos', 'titulo':'Anna Júlia', 'ano':'1999', 'album':'Los Hermanos', 'reproducoes':'63,4 milhões'},
    {'id': uuid4(), 'artista':'Anitta', 'titulo':'Show das Poderosas', 'ano':'2013', 'album':'Anitta', 'reproducoes':'25,4 milhões'},
    {'id': uuid4(), 'artista':'Turma do Pagode', 'titulo':'Camisa 10', 'ano':'2010', 'album':'Esse é o Clima', 'reproducoes':'57,7 milhões'}
]

if not exists('musicas.csv'):
    with open('musicas.csv', 'wt') as file_out:
        escritor = csv.DictWriter(file_out, ['id', 'artista', 'titulo', 'ano', 'album', 'reproducoes']) 
        escritor.writeheader()
        escritor.writerows(musicas)
else:
    with open('musicas.csv', 'rt') as file_in:
        leitor = csv.DictReader(file_in)
        musicas = []
        for linha in leitor:
            musica = dict(linha)
            musicas.append(musica)

@app.route('/')
def index():
    return render_template('index.html', musicas=musicas)


@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    artista = request.form['artista']
    titulo = request.form['titulo']
    ano = request.form['ano']
    album = request.form['album']
    reproducoes = request.form['reproducoes']
    musicas.append({"id": uuid4(), "artista": artista.title(), "titulo": titulo.title(), "ano": ano, "album": album.title(), "reproducoes": reproducoes})
    with open('musicas.csv', 'wt') as file_out:
        escritor = csv.DictWriter(file_out, ['id', 'artista', 'titulo', 'ano', 'album', 'reproducoes']) 
        escritor.writeheader()
        escritor.writerows(musicas)
    return redirect(url_for('index'))

@app.route('/delete/<id>')
def delete(id):
    idMusica = id
    for musica in musicas:
        if(str(musica.get('id')) == idMusica):
            musicas.remove(musica)
    with open('musicas.csv', 'wt') as file_out:
        escritor = csv.DictWriter(file_out, ['id', 'artista', 'titulo', 'ano', 'album', 'reproducoes']) 
        escritor.writeheader()
        escritor.writerows(musicas)
    
    return render_template('index.html', musicas=musicas)

@app.route('/edit/<id>')
def edit(id):
    for musica in musicas:
        if str(musica['id']) == str(id):
            musica_selecionada = musica

    return render_template('edit_musica.html', musica=musica_selecionada)
    
    

@app.route('/save-edit', methods=['POST'])
def save_edit():
    id_edit = request.form['id_new']
    artista_edit = request.form['artista_new']
    titulo_edit = request.form['titulo_new']
    ano_edit = request.form['ano_new']
    album_edit = request.form['album_new']
    reproducoes_edit = request.form['reproducoes_new']

    for musica in musicas:
        if str(musica['id']) == str(id_edit):
            musica['artista'] = artista_edit.title()
            musica['titulo'] = titulo_edit.title()
            musica['ano'] = ano_edit
            musica['album'] = album_edit.title()
            musica['reproducoes'] = reproducoes_edit

    return redirect(url_for('index'))



app.run(debug = True)