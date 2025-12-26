import subprocess

def run_command(cmd):
    try:
        resultado = subprocess.check_output(cmd, shell=True, text=True)
        print(resultado)
    except Exception as e:
        print(f"Erro Ao Executar: {e}")