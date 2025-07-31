import subprocess
import sys

def main():
    """
    Script para executar a aplicação StudyCode
    """
    print(" Iniciando StudyCode Python...")
    print(" Plataforma de Organização de Estudos")
    print("-" * 50)
    
    try:
       
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py", "--server.port=8501"], check=True)
    except KeyboardInterrupt:
        print("\n Aplicação encerrada pelo usuário")
    except Exception as e:
        print(f" Erro ao executar a aplicação: {e}")
    except Exception as e:
        print(f" Para Cancelar a aplicação C + Ctrl: {e}")

if __name__ == "__main__":
    main()
