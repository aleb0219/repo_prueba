from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    form = '''
    <h1>¡Hola desde Entropia!</h1>
    <form method="POST">
        <input type="text" name="user_text" placeholder="Escribe algo aquí">
        <button type="submit">Enviar</button>
    </form>
    '''
    
    if request.method == 'POST':
        user_text = request.form['user_text']
        return f'{form}<p>Texto ingresado: {user_text}</p>'
    
    return form

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)