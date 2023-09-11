from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista para almacenar personas (simulando una base de datos)
personas = []

class Persona:
    def __init__(self, nombre, apellido, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

@app.route('/')
def index():
    return render_template('index.html', personas=personas)

@app.route('/crear_persona', methods=['POST'])
def crear_persona():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    correo = request.form['correo']
    persona = Persona(nombre, apellido, correo)
    personas.append(persona)
    return redirect('/')

@app.route('/actualizar_persona', methods=['POST'])
def actualizar_persona():
    num_persona = int(request.form['num_persona'])
    if 0 <= num_persona < len(personas):
        persona = personas[num_persona]
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        persona.nombre = nombre
        persona.apellido = apellido
        persona.correo = correo
    return redirect('/')

@app.route('/eliminar_persona', methods=['POST'])
def eliminar_persona():
    num_persona = int(request.form['num_persona'])
    if 0 <= num_persona < len(personas):
        personas.pop(num_persona)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
