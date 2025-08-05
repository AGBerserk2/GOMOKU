from juego import jugar, jugar_con_ia, jugar_ia_vs_ia 
import os
from Menu import Menu

def main():
    while True:
        opcion_seleccionada = Menu.mostrar_menu()
        if opcion_seleccionada == 1:
            jugar()
            
        elif opcion_seleccionada == 2:
            jugar_con_ia('minimax')  # 1 para IA Aleatoria, 2 para IA Minimax, 3 para IA Greedy
        
        elif opcion_seleccionada == 3:
            jugar_con_ia('greedy')
            
        elif opcion_seleccionada == 4:
            jugar_con_ia('random')
            
        elif opcion_seleccionada == 5:
            # IA vs IA: puedes elegir los tipos aquí, por ejemplo, minimax vs greedy
            jugar_ia_vs_ia('minimax', 'greedy')
            
        elif opcion_seleccionada == 6:
            os.system('cls' if os.name == 'nt' else 'clear')  
            print("¿Seguro que quieres salir? (s/n)")  
            if input().lower() == 's':  
                break

if __name__ == "__main__":
    main()