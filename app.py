
from flask import Flask
from flask import render_template

app=Flask(__name__)



#rotas
@app.route('/')
def homepage():
    return render_template('index.html') #retorna templates

@app.route('/contato')
def contato():
    return render_template('contato.html')










if __name__ == '__main__':
    app.run(debug=True)


