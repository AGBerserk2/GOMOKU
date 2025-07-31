from juego import jugar
import os
from Menu import Menu

if __name__ == "__main__":
    while True:
        opcion_seleccionada = Menu.mostrar_menu()
        if opcion_seleccionada == 1:
            jugar()
            
        elif opcion_seleccionada == 2:
            pass
        
        elif opcion_seleccionada == 3:
            pass
        
        elif opcion_seleccionada == 4:
            os.system('cls' if os.name == 'nt' else 'clear')  
            print("¿Seguro que quieres salir? (s/n)")  
            if input().lower() == 's':  
                break
        
