#importação de biblioteca
import threading #importador de módulo para trabalhar com 1 ou mais thread
import time      #importador de módulo funções de tempo
import math      #importador de módulo funções de matematica
#Estrutura da Thread
def estruturaThread(nome, inicio, fim):
    for i in range(inicio, fim +1): #estrutura de repetição
        print(f"{nome} -> {i}")      #vai imprimir o valor
        #tempo de processamento que vai aparecer a resultado

        time.sleep(1) #tempo que vai levar para a contagem

thread1 = threading .Thread(target=estruturaThread, args=("Thread1", 1 ,10))#execução das thread, onde vai começar a contagem até acabar
thread2 = threading .Thread(target=estruturaThread, args=("Thread2", 50 ,60))#execução das thread, onde vai começar a contagem até acabar
      
thread1.start() #inicia a execução
thread2.start() #inicia a execução
