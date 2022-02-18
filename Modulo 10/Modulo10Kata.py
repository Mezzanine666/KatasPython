#Tracebacks

def main():
  open("/path/to/marte.jpg")

if __name__ == '__main__':
  main()

#Try - Except

try:
    open('config.txt')
except FileNotFoundError:
    print("Couldn't find the config.txt file!")