def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se ha encontrado el archivo config.txt!")
    except IsADirectoryError:
        print("Se encontró config.txt pero es un directorio, no se puede abrir")
    except (BlockingIOError, TimeoutError):
        print("Sistema de archivos con mucha carga, no se puede completar la lectura del archivo")


if __name__ == '__main__':
    main()