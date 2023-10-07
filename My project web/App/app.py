import pyodbc
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Conexión a la base de datos Access
db_path = r'C:\Users\danim\.vscode\My project web\Data Bases\TasksDB.accdb'
conn_str = f"DRIVER={{Microsoft Access Driver (*.mdb, *.accdb)}};DBQ={db_path};"
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Función para conectar a la base de datos
def conectar_bd():
    return pyodbc.connect(conn_str)

# Rutas de la aplicación

@app.route('/')
def mostrar_tareas():
    cursor.execute('SELECT * FROM Tareas')
    tareas = cursor.fetchall()
    return render_template('mostrar_tareas.html', tareas=tareas)

@app.route('/agregar_tarea', methods=['POST'])
def agregar_tarea():
    if request.method == 'POST':
        descripcion = request.form['descripcion']
        estado = 'No Completado'  
        cursor.execute("INSERT INTO Tareas (descripcion, estado) VALUES (?, ?)", (descripcion, estado))
        conn.commit()
    return redirect(url_for('mostrar_tareas'))

@app.route('/completar_tarea/<int:id>')
def completar_tarea(id):
    cursor.execute("UPDATE Tareas SET estado='Completado' WHERE id=?", (id,))
    conn.commit()
    return redirect(url_for('mostrar_tareas'))

@app.route('/eliminar_tarea/<int:id>')
def eliminar_tarea(id):
    cursor.execute("DELETE FROM Tareas WHERE id=?", (id,))
    conn.commit()
    return redirect(url_for('mostrar_tareas'))

if __name__ == '__main__':
    app.run(debug=True)
