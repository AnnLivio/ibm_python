import os, pickle
from colorama import init, Fore, Back, Style
init(autoreset=True)

class Task:
    def __init__(self, name):
        self.name = name
        self.state = False

    def change_state(self):
        self.state = not self.state
        
    def __str__(self):
        state_str = "✔" if self.state else " "
        return f"{self.name} {state_str}"
    
class UserInterface:
    menu = ["[1]·Agregar tarea", " [2]· Marcar ✔"," [3]·Mostrar tareas"," [4]·Borrar tarea","\n[5]·Salir y guardar"]

    @staticmethod
    def show_main_menu():
        print(f"\n{Fore.WHITE}{Back.MAGENTA} M E N U {Style.RESET_ALL}\n(Introduzca el número correspondiente) ")
        print("1· Agrega una Tarea\n2· Marca/Desmarca una tarea como completada\n3· Muestra la lista completa\n4· Borra Tarea\n5· Salir y Guardar")
    
    def show_menu(self):
        print()
        print(*self.menu)

    @staticmethod
    def print_tasks(tasks): 
        '''Imprime la lista ordenada dejando a lo último las tareas que están ✔.
           Cada tarea lleva su ID para interactuar con el usuario'''
        print(f"{Fore.CYAN}{Style.BRIGHT}{'·'*35} \n T A R E A S  P E N D I E N T E S\n{'·'*50}{Style.RESET_ALL}")
        if len(tasks):
            sorted_list = sorted(tasks, key=lambda task : task.state)
            for task in sorted_list:
                print(f" {tasks.index(task)+1} · {task}\n{'-' * 50}")
        else:
            print("Parece que estás al día!")

class TaskManager:
    def __init__(self):
        self.tasks = []

    def len_tasks(self):
        return len(self.tasks)

    def add_task(self, name):
        name = name.capitalize()
        for task in self.tasks:
            if task.name == name:
                return "La tarea ya existe"
        self.tasks.append(Task(name))
        return "\n··> Perfecto! La tarea ha sido agregada."

    def delete_task(self, id):
        if 1 <= id <= len(self.tasks):
           deleted_task = self.tasks[id-1].name
           del self.tasks[id-1]
           return f"\n··> Has eliminado: {deleted_task.upper()}"
    
    def check_task(self, id):
        if 1 <= id <= len(self.tasks):
           self.tasks[id-1].change_state()    

    def load_list(self, file_name):
        if os.path.exists(file_name):
            with open(file_name, 'rb') as file:
                self.tasks = pickle.load(file)

    def save_list(self, file_name):
         with open(file_name, "wb") as f:
                pickle.dump(self.tasks, f)

def main():
    #NOMBRE FICHERO DONDE GUARDAR LA LISTA
    file_name= "lista.txt"

    #ELECCION DEL USUARIO RESPECTO DEL MENU
    action = 0

    tasks = TaskManager()
    useri = UserInterface()
    print("\n>>> PRÁCTICO FINAL: ANASTASIA LIVIO <<<\n")

    # Comprueba si el fichero existe y no está vacío
    tasks.load_list(file_name)

    #IMPRIME LA LISTA AL INICIO
    useri.print_tasks(tasks.tasks)
    
    #MENU DESPLEGADO ANTES DE COMENZAR
    useri.show_main_menu()
    
    while True:
        try:
            action = int(input(f"\n{Fore.WHITE}{Back.MAGENTA} ¿Qué deseas hacer? {Style.RESET_ALL} ").strip())
            
            # AGREGAR TAREA
            if action == 1:
                print(f"\n{Fore.BLUE} AGREGAR TAREA ")
                new_task = input("Introduce la Tarea: ").strip()
                if not new_task == "0":
                   print(tasks.add_task(new_task))
                   useri.print_tasks(tasks.tasks)
                        
            # MARCAR/DESMARCAR TAREA
            elif action == 2 and tasks.len_tasks():
                print(f"\n{Fore.GREEN} MARCAR/DESMARCAR TAREA ")
                id = get_valid_id(tasks.len_tasks())
                if not id == 0:
                    tasks.check_task(id)
                    useri.print_tasks(tasks.tasks)

            # MOSTRAR TODAS
            elif action == 3:
                useri.print_tasks(tasks.tasks) 
            
            # BORRAR TAREA
            elif action == 4 and tasks.len_tasks():
                print(f"\n{Fore.RED} ELIMINAR TAREA ")
                id = get_valid_id(tasks.len_tasks())
                if not id == 0:
                    tasks.delete_task(id)
                    useri.print_tasks(tasks.tasks)

            # SALIR Y GUARDAR LISTA
            elif action == 5:
                try: 
                    tasks.save_list(file_name)  
                    print("Hemos guardado los cambios.")              
                except:
                    print("Houston, we have a problem!\n Lo sentimos, no hemos podido guardar tu lista.")
                print("\n¡Hasta luego, Mari Carmen!\n")
                break
            if 0 < action <= 5:
                useri.show_menu()

        except:
            pass

def get_valid_id(len_list):
    "Obtiene un ID válido en relación a la lista impresa. Permite el 0 para cancelar la acción."
    while True:
        try:
            task_id = int(input("Ingresa el Nº de la Tarea (0 para cancelar): "))
            if 0 <= task_id <= len_list:
                return task_id
        except ValueError:
            print("El ID no es válido")

if __name__ == "__main__":
    main()
