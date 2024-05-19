# TO·DO LIST
## Notas y Autoría
Ejercicio final para el _Curso de Python, Abril-Mayo 2024._ Bejobs - IBM!

+ **Desarrollado por:** _Ann Livio
+ **Archivos adjuntos:** todo_list.py / requirements.txt / README.md / 5 capturas de pantalla en png.

## Interface de usuario
Uso de números para interactuar con el usuario. Al inicio, se imprime la lista si ya existe y el menú en un formato más detallado. Posteriormente el menú se simplifica.

* #### MENU:
  + [1] Agregar Tarea
  + [2] Marcar/Desmarcar como completada
  + [3] Mostrar la Lista de tareas
  + [4] Borrar una tarea
  + [5] Salir y guardar
  
**[0]** Queda reservado para que el usuario pueda cancelar las acciones: _Agregar, marcar y borrar._

**[5]** En esta opción me interesaría añadir que el usuario pudiera confirmar si quiere salir.

## Classes
La clase Task() para las tareas, con atributos name (str para el nombre) y state (booleano para marcar si está marcada o no).
Clase TaskManager() para gestionar el diccionario donde se guardan las tareas, además de cargarlo de un fichero externo al comenzar y guardarlo nuevamente al salir.
Clase UserInterface() para manejar la parte más visual, imprimir en pantalla tanto títulos, menú o las propias tareas.

## Variables
```python
#Nomnbre del archivo donde se guardará y se cargará la lista  
file_name= "lista.txt"

#ELECCION DEL USUARIO RESPECTO DEL MENU
action = 0

tasks = TaskManager()
useri = UserInterface()

```

## Libraries

* _COLORAMA:_ para darle un poco de color al terminal y jerarquizar títulos y acciones.
* _PICKLE:_ permite manejar una amplia gama de objetos de Python, incluidas las instancias de clases personalizadas y serializarlas en un formato binario.

