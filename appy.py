
from flask import Flask, render_template, request

app = Flask(__name__)


# ==================================
# PÁGINA PRINCIPAL
# ==================================

@app.route('/')
def home():
    return render_template('Aplicacion Flask.html')


# ==================================
# EJERCICIO 1: PROMEDIO DE NOTAS
# ==================================

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():

    if request.method == 'POST':

        # Recibir las notas del formulario
        nota1 = float(request.form.get('nTotal1'))
        nota2 = float(request.form.get('nTotal2'))
        nota3 = float(request.form.get('nTotal3'))
        asistencia = float(request.form.get('asistencia'))

        # Calcular el promedio
        promedio = (nota1 + nota2 + nota3) / 3

        # Mostrar el resultado
        return render_template(
            'Formulario.html',
            promedio=round(promedio, 2)
        )

    return render_template('Formulario.html')


# ==================================
# EJERCICIO 2: NOMBRE MÁS LARGO
# ==================================

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():

    if request.method == 'POST':

        # Recibir los tres nombres
        nombre1 = request.form.get('nombre1')
        nombre2 = request.form.get('nombre2')
        nombre3 = request.form.get('nombre3')

        # Guardar los nombres en una lista
        nombres = [nombre1, nombre2, nombre3]

        # Buscar el nombre más largo
        mayor = max(nombres, key=len)

        # Contar sus caracteres
        cantidad = len(mayor)

        # Mostrar el resultado
        return render_template(
            'Formulario2.html',
            nombre_mayor=mayor,
            cantidad=cantidad
        )

    return render_template('Formulario2.html')


# ==================================
# INICIAR LA APLICACIÓN FLASK
# ==================================

if __name__ == '__main__':
    app.run(debug=True)
