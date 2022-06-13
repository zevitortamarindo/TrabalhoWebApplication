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
    musicas.append({"id": uuid4(), "artista": artista, "titulo": titulo, "ano": ano, "album": album, "reproducoes": reproducoes})
    with open('musicas.csv', 'wt') as file_out:
        escritor = csv.DictWriter(file_out, ['id', 'artista', 'titulo', 'ano', 'album', 'reproducoes']) 
        escritor.writeheader()
        escritor.writerows(musicas)
    return redirect(url_for('index'))



app.run(debug = True)