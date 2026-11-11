from Conta_Bancária import *

def main():
    c1 = Nubank(123, 'Exemplo1', 1_500)
    c2 = Picpay(456, 'Exemplo2', 3_000)
    c3 = Itaú(789, 'Exemplo3', 5_000)

    print(c1)
    print(c2)
    print(c3)

if __name__ == '__main__':
    main()