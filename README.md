Proyecto Web - Instrucciones de Uso

Este proyecto se trata de una aplicación web sencilla desarrollada utilizando el framework Flask y una base de datos Access para gestionar tareas. Los usuarios tienen la capacidad de realizar las siguientes acciones: ver la lista de tareas, añadir nuevas tareas, marcar tareas como completadas y eliminar tareas existentes.

Requisitos Previos

Antes de ejecutar esta aplicación, asegúrate de contar con los siguientes componentes instalados en tu entorno:

1. Python
2. Flask
3. pyodbc
4. Controlador Microsoft Access

Configuración

Sigue estos pasos para configurar la aplicación:

1. Clona o descarga el repositorio a tu computadora.

2. Asegúrate de tener una base de datos Access (.accdb) con una tabla llamada "Tareas" que contenga los campos siguientes:
   - Id (número de identificación único)
   - Descripción (texto, descripción de la tarea)
   - Estado (entero, 0 para tareas no completadas y 1 para tareas completadas)

3. Abre el archivo "app.py" y modifica la línea de conexión a la base de datos ("conn") para que apunte al archivo .accdb en tu ruta local:
   
   ```python
   conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' r'DBQ=/ruta/a/tu/ArchivoDB.accdb;')
   ```

4. Instala las dependencias de Python ejecutando el siguiente comando en la terminal: "pip install flask pyodbc".

Uso

Para utilizar la aplicación, sigue estos pasos:

1. Ejecuta la aplicación con el siguiente comando: "python app.py".

2. Abre tu navegador web y accede a "http://localhost:5000/" para visualizar la lista de tareas disponibles.

3. Puedes agregar nuevas tareas completando el formulario en la página principal.

4. Marca una tarea como completada haciendo clic en el enlace correspondiente junto a la tarea.

5. Para eliminar una tarea, utiliza el enlace de eliminación ubicado junto a la tarea deseada.

¡Disfruta gestionando tus tareas con esta aplicación web!
