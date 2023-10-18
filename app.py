from flask import Flask, render_template

app = Flask(__name__)

konten = [{
    'penulis': 'tim writer',
    'judul': 'postingan',
    'sinopsis': 'ini adalah postingan pertama',
    'isi': 'ini adalah isi postingan',
    'tanggal': '6 april 2022',
    'jam': '18.00'
}
]


@app.route('/')
def home():
    return render_template('home.html', konten=konten, judul='Beranda')


@app.route("/tentang/")
def tentang():
    return render_template('tentang.html', judul='Tentang')


@app.route("/daftar")
def daftar():
    return render_template('daftar.html', judul='Daftar')


@app.route("/masuk")
def masuk():
    return render_template('masuk.html', judul='Masuk')


@app.route("/akun")
def akun():
    return render_template('akun.html')


@app.route("/post")
def post():
    return render_template('post.html')
