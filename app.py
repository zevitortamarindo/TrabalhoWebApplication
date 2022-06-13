from flask import Flask, render_template, request
from uuid import uuid4

app = Flask(__name__)

musicas = [
    {'id': uuid4(), 'artista':'Michel Teló', 'titulo':'Ai se eu te pego', 'ano':'2011', 'album':'Na Balada', 'reproducoes':'204,7 milhões'},
    {'id': uuid4(), 'artista':'Los Hermanos', 'titulo':'Anna Júlia', 'ano':'1999', 'album':'Los Hermanos', 'reproducoes':'63,4 milhões'},
    {'id': uuid4(), 'artista':'Anitta', 'titulo':'Show das Poderosas', 'ano':'2013', 'album':'Anitta', 'reproducoes':'25,4 milhões'},
    {'id': uuid4(), 'artista':'Turma do Pagode', 'titulo':'Camisa 10', 'ano':'2010', 'album':'Esse é o Clima', 'reproducoes':'57,7 milhões'}
]

@app.route('/')
def index():
    return render_template('index.html', musicas=musicas)


@app.route('/create')
def create():
    return render_template('create.html')


app.run(debug = True)