import sys
import os


from modules.network_scan import network_scan
from modules.system_info import system_info
import modules.network_devices as network_devices
from core.colors import Colors

def main():
    while True:
        print(f"\n{Colors.RED}=== FSOCIETY 2.0 ==={Colors.RESET}")
        print("[1]. Informações Do Sistema")
        print("[2]. Scannear Rede (IP local)")
        print("[3]. Encontrar Dispositivos Na Rede")
        print("[0]. Sair")
        escolha = input("Selecione: ")
        if escolha == "1":
            system_info()
        elif escolha == "2":
            network_scan()
        elif escolha == "3":
            network_devices.find_devices()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Opção Inválida!")

if __name__ == "__main__":
    main()
