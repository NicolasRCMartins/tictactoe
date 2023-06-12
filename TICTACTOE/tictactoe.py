import random
import os
import math
import time

def iniciarMenu3x3(slots):
    print("------TIC TAC TOE 3X3------\n")
    print(" TEMPO REAL     COORDENADAS")
    print(" %s | %s | %s       7 | 8 | 9 " % (slots[2][0],slots[2][1],slots[2][2]))
    print("------------    -----------")
    print(" %s | %s | %s       4 | 5 | 6 " % (slots[1][0],slots[1][1],slots[1][2]))
    print("------------    -----------")
    print(" %s | %s | %s       1 | 2 | 3 " % (slots[0][0],slots[0][1],slots[0][2]))
    print("\n---------------------------")

def iniciarMenu5x5(slots):
    print("--------------TIC TAC TOE 5X5-------------------\n")
    print("    TEMPO REAL                COORDENADAS")
    print(" %s | %s | %s | %s | %s       21 | 22 | 23 | 24 | 25" % (slots[4][0],slots[4][1],slots[4][2],slots[4][3],slots[4][4]))
    print("-------------------     ------------------------")
    print(" %s | %s | %s | %s | %s       16 | 17 | 18 | 19 | 20" % (slots[3][0],slots[3][1],slots[3][2],slots[3][3],slots[3][4]))
    print("-------------------     ------------------------")
    print(" %s | %s | %s | %s | %s       11 | 12 | 13 | 14 | 15" % (slots[2][0],slots[2][1],slots[2][2],slots[2][3],slots[2][4]))
    print("-------------------     ------------------------")
    print(" %s | %s | %s | %s | %s       06 | 07 | 08 | 09 | 10" % (slots[1][0],slots[1][1],slots[1][2],slots[1][3],slots[1][4]))
    print("-------------------     ------------------------")
    print(" %s | %s | %s | %s | %s       01 | 02 | 03 | 04 | 05" % (slots[0][0],slots[0][1],slots[0][2],slots[0][3],slots[0][4]))
    print("\n------------------------------------------------")

def iniciarMenu7x7(slots):
    print("----------------------TIC TAC TOE 5X5-----------------------------\n")
    print("        TEMPO REAL                          COORDENADAS")
    print(" %s | %s | %s | %s | %s | %s | %s       43 | 44 | 45 | 46 | 47 | 48 | 49" % (slots[6][0],slots[6][1],slots[6][2],slots[6][3],slots[6][4],slots[6][5],slots[6][6]))
    print("---------------------------     ----------------------------------")
    print(" %s | %s | %s | %s | %s | %s | %s       36 | 37 | 38 | 39 | 40 | 41 | 42" % (slots[5][0],slots[5][1],slots[5][2],slots[5][3],slots[5][4],slots[5][5],slots[5][6]))
    print("---------------------------     ----------------------------------")
    print(" %s | %s | %s | %s | %s | %s | %s       29 | 30 | 31 | 32 | 33 | 34 | 35" % (slots[4][0],slots[4][1],slots[4][2],slots[4][3],slots[4][4],slots[4][5],slots[4][6]))
    print("---------------------------     ----------------------------------")
    print(" %s | %s | %s | %s | %s | %s | %s       22 | 23 | 24 | 25 | 26 | 27 | 28" % (slots[3][0],slots[3][1],slots[3][2],slots[3][3],slots[3][4],slots[3][5],slots[3][6]))
    print("---------------------------     ----------------------------------")
    print(" %s | %s | %s | %s | %s | %s | %s       15 | 16 | 17 | 18 | 19 | 20 | 21" % (slots[2][0],slots[2][1],slots[2][2],slots[2][3],slots[2][4],slots[2][5],slots[2][6]))
    print("---------------------------     ----------------------------------")
    print(" %s | %s | %s | %s | %s | %s | %s       08 | 09 | 10 | 11 | 12 | 13 | 14" % (slots[1][0],slots[1][1],slots[1][2],slots[1][3],slots[1][4],slots[1][5],slots[1][6]))
    print("---------------------------     ----------------------------------")
    print(" %s | %s | %s | %s | %s | %s | %s       01 | 02 | 03 | 04 | 05 | 06 | 07" % (slots[0][0],slots[0][1],slots[0][2],slots[0][3],slots[0][4],slots[0][5],slots[0][6]))
    print("\n------------------------------------------------------------------")

def verificaVitoriaPrimeiroJogador3x3(slots):
    for index in range(0,3):
        for jIndex in range(0,3):
            if slots[index][jIndex] == "X":
                vitoria = True
            else:
                vitoria = False
                break
        if vitoria:
            return vitoria
                
    for index in range(0,3):
        for jIndex in range(0,3):
            if slots[jIndex][index] == "X":
                vitoria = True
            else:
                vitoria = False
                break
        if vitoria:
            return vitoria
            
    for index in range(0,3):
        if slots[index][index] == "X":
            vitoria = True
        else:
            vitoria = False
            break
        
    if vitoria:
        return vitoria
        
    index = 0
    jIndex = 2
        
    while index < 3:
        if slots[index][jIndex] == "X":
            vitoria = True
            index += 1
            jIndex -= 1
        else:
            vitoria = False
            break
            
    return vitoria    

def verificaVitoriaSegundoJogador3x3(slots):
    for index in range(0,3):
        for jIndex in range(0,3):
            if slots[index][jIndex] == "O":
                vitoria = True
            else:
                vitoria = False
                break
        if vitoria:
            return vitoria
                
    for index in range(0,3):
        for jIndex in range(0,3):
            if slots[jIndex][index] == "O":
                vitoria = True
            else:
                vitoria = False
                break
        if vitoria:
            return vitoria
            
    for index in range(0,3):
        if slots[index][index] == "O":
            vitoria = True
        else:
            vitoria = False
            break
        
    if vitoria:
        return vitoria
        
    index = 0
    jIndex = 2
        
    while index < 3:
        if slots[index][jIndex] == "O":
            vitoria = True
            index += 1
            jIndex -= 1
        else:
            vitoria = False
            break
            
    return vitoria   
  
def verificaEmpate3x3(slots):
    empate = True
    
    for index in range(0,3):
        for jIndex in range(0,3):
            if slots[index][jIndex] == " ":
                empate = False
                
    return empate

def verificaVitoriaPrimeiroJogador5x5(slots):
    for index in range(0,5):
        for jIndex in range(0,5):
            if slots[index][jIndex] == "X":
                vitoria = True
            else:
                vitoria = False
                break
        if vitoria:
            return vitoria
                
    for index in range(0,5):
        for jIndex in range(0,5):
            if slots[jIndex][index] == "X":
                vitoria = True
            else:
                vitoria = False
                break
        if vitoria:
            return vitoria
            
    for index in range(0,5):
        if slots[index][index] == "X":
            vitoria = True
        else:
            vitoria = False
            break
        
    if vitoria:
        return vitoria
        
    index = 0
    jIndex = 4
        
    while index < 5:
        if slots[index][jIndex] == "X":
            vitoria = True
            index += 1
            jIndex -= 1
        else:
            vitoria = False
            break
            
    return vitoria    

def verificaVitoriaSegundoJogador5x5(slots):
    for index in range(0,5):
        for jIndex in range(0,5):
            if slots[index][jIndex] == "O":
                vitoria = True
            else:
                vitoria = False
                break
        if vitoria:
            return vitoria
                
    for index in range(0,5):
        for jIndex in range(0,5):
            if slots[jIndex][index] == "O":
                vitoria = True
            else:
                vitoria = False
                break
        if vitoria:
            return vitoria
            
    for index in range(0,5):
        if slots[index][index] == "O":
            vitoria = True
        else:
            vitoria = False
            break
        
    if vitoria:
        return vitoria
        
    index = 0
    jIndex = 4
        
    while index < 5:
        if slots[index][jIndex] == "O":
            vitoria = True
            index += 1
            jIndex -= 1
        else:
            vitoria = False
            break
            
    return vitoria    

def verificaEmpate5x5(slots):
    empate = True
    
    for index in range(0,5):
        for jIndex in range(0,5):
            if slots[index][jIndex] == " ":
                empate = False
                
    return empate    

def verificaVitoriaPrimeiroJogador7x7(slots):
    for index in range(0,7):
        for jIndex in range(0,7):
            if slots[index][jIndex] == "X":
                vitoria = True
            else:
                vitoria = False
                break
        if vitoria:
            return vitoria
                
    for index in range(0,7):
        for jIndex in range(0,7):
            if slots[jIndex][index] == "X":
                vitoria = True
            else:
                vitoria = False
                break
        if vitoria:
            return vitoria
            
    for index in range(0,7):
        if slots[index][index] == "X":
            vitoria = True
        else:
            vitoria = False
            break
        
    if vitoria:
        return vitoria
        
    index = 0
    jIndex = 6
        
    while index < 7:
        if slots[index][jIndex] == "X":
            vitoria = True
            index += 1
            jIndex -= 1
        else:
            vitoria = False
            break
            
    return vitoria
        
def verificaVitoriaSegundoJogador7x7(slots):
    for index in range(0,7):
        for jIndex in range(0,7):
            if slots[index][jIndex] == "O":
                vitoria = True
            else:
                vitoria = False
                break
        if vitoria:
            return vitoria
                
    for index in range(0,7):
        for jIndex in range(0,7):
            if slots[jIndex][index] == "O":
                vitoria = True
            else:
                vitoria = False
                break
        if vitoria:
            return vitoria
            
    for index in range(0,7):
        if slots[index][index] == "O":
            vitoria = True
        else:
            vitoria = False
            break
        
    if vitoria:
        return vitoria
        
    index = 0
    jIndex = 6
        
    while index < 7:
        if slots[index][jIndex] == "O":
            vitoria = True
            index += 1
            jIndex -= 1
        else:
            vitoria = False
            break
            
    return vitoria  

def verificaEmpate7x7(slots):
    empate = True
    
    for index in range(0,7):
        for jIndex in range(0,7):
            if slots[index][jIndex] == " ":
                empate = False
                
    return empate

def jogoNormal3x3():      
    linha = coluna = 3
    slots = [[0 for linhas in range(linha)] for colunas in range(coluna)]

    for index in range(0,3):
        for jIndex in range(0,3):
            slots[index][jIndex] = " "

    while True:
        os.system("CLS")
        iniciarMenu3x3(slots)
        
        if verificaVitoriaPrimeiroJogador3x3(slots):
            print("\nPARABÉNS!!! O primeiro jogador venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador3x3(slots):
            print("\nPARABÉNS!!! O segundo jogador venceu!")
            time.sleep(2)
            break
        elif verificaEmpate3x3(slots):
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
        
        while True:
            opcao = int(input("\nVez do primeiro jogador! Digite um número de 1-9: "))

            if opcao <= 0 or opcao > 9:
                print("Insira um número válido!")
            else:
                if opcao < 3:
                    if slots[0][opcao-1] != " ":
                        print("Posição já ocupada! Tente outra!")
                    else:
                        slots[0][opcao-1] = "X"
                        break
                else:
                    primeiroSlot = opcao / 3
                    primeiroSlot = math.ceil(primeiroSlot)
                    primeiroSlot = int(primeiroSlot - 1)
                    segundoSlot = opcao % 3
                    segundoSlot = math.ceil(segundoSlot)  
                    segundoSlot = int(segundoSlot - 1)
                        
                    if slots[primeiroSlot][segundoSlot] != " ":
                        print("Posição já ocupada! Tente outra!")
                    else:
                        slots[primeiroSlot][segundoSlot] = "X"
                        break
        
        os.system("CLS")
        iniciarMenu3x3(slots)
        
        if verificaVitoriaPrimeiroJogador3x3(slots):
            print("\nPARABÉNS!!! O primeiro jogador venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador3x3(slots):
            print("\nPARABÉNS!!! O segundo jogador venceu!")
            time.sleep(2)
            break
        elif verificaEmpate3x3(slots):
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
        
        while True:
            opcao = int(input("\nVez do primeiro jogador! Digite um número de 1-9: "))

            if opcao <= 0 or opcao > 9:
                print("Insira um número válido!")
            else:
                if opcao < 3:
                    if slots[0][opcao-1] != " ":
                        print("Posição já ocupada! Tente outra!")
                    else:
                        slots[0][opcao-1] = "O"
                        break
                else:
                    primeiroSlot = opcao / 3
                    primeiroSlot = math.ceil(primeiroSlot)
                    primeiroSlot = int(primeiroSlot - 1)
                    segundoSlot = opcao % 3
                    segundoSlot = math.ceil(segundoSlot)  
                    segundoSlot = int(segundoSlot - 1)
                        
                    if slots[primeiroSlot][segundoSlot] != " ":
                        print("Posição já ocupada! Tente outra!")
                    else:
                        slots[primeiroSlot][segundoSlot] = "O"
                        break
                    
def jogoCPUPrimeiroJogador3x3():
    sequenciaNumeros = [1,2,3,4,5,6,7,8,9]
    linha = coluna = 3
    slots = [[0 for linhas in range(linha)] for colunas in range(coluna)]

    for index in range(0,3):
        for jIndex in range(0,3):
            slots[index][jIndex] = " "
            
    while True: 
        os.system("CLS")
        iniciarMenu3x3(slots)
        
        if verificaVitoriaPrimeiroJogador3x3(slots):
            print("\nPARABÉNS!!! O primeiro jogador venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador3x3(slots):
            print("\nGAME OVER!!! A CPU venceu!")
            time.sleep(2)
            break
        elif verificaEmpate3x3(slots):
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
        
        while True:
                opcao = int(input("\nVez do primeiro jogador! Digite um número de 1-9: "))

                if opcao <= 0 or opcao > 9:
                    print("Insira um número válido!")
                else:
                    if opcao < 3:
                        if slots[0][opcao-1] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[0][opcao-1] = "X"
                            sequenciaNumeros.remove(opcao)
                            break
                    else:
                        tempOpcao = opcao 
                        primeiroSlot = opcao / 3
                        primeiroSlot = math.ceil(primeiroSlot)
                        primeiroSlot = int(primeiroSlot - 1)
                        segundoSlot = opcao % 3
                        segundoSlot = math.ceil(segundoSlot)  
                        segundoSlot = int(segundoSlot - 1)
                        
                        if slots[primeiroSlot][segundoSlot] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[primeiroSlot][segundoSlot] = "X"
                            sequenciaNumeros.remove(tempOpcao)
                            break
        
        if verificaVitoriaPrimeiroJogador3x3(slots):
            os.system("CLS")
            iniciarMenu3x3(slots)
            print("\nPARABÉNS!!! O primeiro jogador venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador3x3(slots):
            os.system("CLS")
            iniciarMenu3x3(slots)
            print("\nGAME OVER!!! A CPU venceu!")
            time.sleep(2)
            break
        elif verificaEmpate3x3(slots):
            os.system("CLS")
            iniciarMenu3x3(slots)
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
                    
        opcaoCPU = random.choice(sequenciaNumeros)
            
        sequenciaNumeros.remove(opcaoCPU) 
        if opcaoCPU < 3:
            slots[0][opcaoCPU-1] = "O"
        else:
            primeiroSlot = opcaoCPU / 3
            primeiroSlot = math.ceil(primeiroSlot)
            primeiroSlot = int(primeiroSlot - 1)
            segundoSlot = opcaoCPU % 3
            segundoSlot = math.ceil(segundoSlot)  
            segundoSlot = int(segundoSlot - 1)
            slots[primeiroSlot][segundoSlot] = "O"     

def jogoCPUSegundoJogador3x3():
    sequenciaNumeros = [1,2,3,4,5,6,7,8,9]
    linha = coluna = 3
    slots = [[0 for linhas in range(linha)] for colunas in range(coluna)]

    for index in range(0,3):
        for jIndex in range(0,3):
            slots[index][jIndex] = " "
            
    while True:
        opcaoCPU = random.choice(sequenciaNumeros)
            
        sequenciaNumeros.remove(opcaoCPU)
        if opcaoCPU < 3:
            slots[0][opcaoCPU-1] = "X"
        else:
            primeiroSlot = opcaoCPU / 3
            primeiroSlot = math.ceil(primeiroSlot)
            primeiroSlot = int(primeiroSlot - 1)
            segundoSlot = opcaoCPU % 3
            segundoSlot = math.ceil(segundoSlot)  
            segundoSlot = int(segundoSlot - 1)
            slots[primeiroSlot][segundoSlot] = "X"
             
        os.system("CLS")
        iniciarMenu3x3(slots)
        
        if verificaVitoriaPrimeiroJogador3x3(slots):
            print("\nGAME OVER!!! A CPU venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador3x3(slots):
            print("\nPARABÉNS!!! O segundo jogador venceu!")
            time.sleep(2)
            break
        elif verificaEmpate3x3(slots):
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
        
        while True:
                opcao = int(input("\nVez do primeiro jogador! Digite um número de 1-9: "))

                if opcao <= 0 or opcao > 9:
                    print("Insira um número válido!")
                else:
                    if opcao < 3:
                        if slots[0][opcao-1] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[0][opcao-1] = "O"
                            sequenciaNumeros.remove(opcao)
                            break
                    else:
                        tempOpcao = opcao 
                        primeiroSlot = opcao / 3
                        primeiroSlot = math.ceil(primeiroSlot)
                        primeiroSlot = int(primeiroSlot - 1)
                        segundoSlot = opcao % 3
                        segundoSlot = math.ceil(segundoSlot)  
                        segundoSlot = int(segundoSlot - 1)
                        
                        if slots[primeiroSlot][segundoSlot] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[primeiroSlot][segundoSlot] = "O"
                            sequenciaNumeros.remove(tempOpcao)
                            break
                    
        if verificaVitoriaPrimeiroJogador3x3(slots):
            os.system("CLS")
            iniciarMenu3x3(slots)
            print("\nGAME OVER!!! A CPU venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador3x3(slots):
            os.system("CLS")
            iniciarMenu3x3(slots)
            print("\nPARABÉNS!!! O segundo jogador venceu!")
            time.sleep(2)
            break
        elif verificaEmpate3x3(slots):
            os.system("CLS")
            iniciarMenu3x3(slots)
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break      

def jogoNormal5x5():
    linha = coluna = 5
    slots = [[0 for linhas in range(linha)] for colunas in range(coluna)]

    for index in range(0,5):
        for jIndex in range(0,5):
            slots[index][jIndex] = " "
            
    while True:
        os.system("CLS")
        iniciarMenu5x5(slots)
        
        if verificaVitoriaPrimeiroJogador5x5(slots):
            print("\nPARABÉNS!!! O primeiro jogador venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador5x5(slots):
            print("\nPARABÉNS!!! O segundo jogador venceu!")
            time.sleep(2)
            break
        elif verificaEmpate5x5(slots):
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
        
        while True:
            opcao = int(input("\nVez do primeiro jogador! Digite um número de 1-25: "))

            if opcao <= 0 or opcao > 25:
                print("Insira um número válido!")
            else:
                if opcao < 5:
                    if slots[0][opcao-1] != " ":
                        print("Posição já ocupada! Tente outra!")
                    else:
                        slots[0][opcao-1] = "X"
                        break
                else:
                    primeiroSlot = opcao / 5
                    primeiroSlot = math.ceil(primeiroSlot)
                    primeiroSlot = int(primeiroSlot - 1)
                    segundoSlot = opcao % 5
                    segundoSlot = math.ceil(segundoSlot)  
                    segundoSlot = int(segundoSlot - 1)
                        
                    if slots[primeiroSlot][segundoSlot] != " ":
                        print("Posição já ocupada! Tente outra!")
                    else:
                        slots[primeiroSlot][segundoSlot] = "X"
                        break
                    
        os.system("CLS")
        iniciarMenu5x5(slots)
        
        if verificaVitoriaPrimeiroJogador5x5(slots):
            print("\nPARABÉNS!!! O primeiro jogador venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador5x5(slots):
            print("\nPARABÉNS!!! O segundo jogador venceu!")
            time.sleep(2)
            break
        elif verificaEmpate5x5(slots):
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
        
        while True:
            opcao = int(input("\nVez do primeiro jogador! Digite um número de 1-25: "))

            if opcao <= 0 or opcao > 25:
                print("Insira um número válido!")
            else:
                if opcao < 5:
                    if slots[0][opcao-1] != " ":
                        print("Posição já ocupada! Tente outra!")
                    else:
                        slots[0][opcao-1] = "O"
                        break
                else:
                    primeiroSlot = opcao / 5
                    primeiroSlot = math.ceil(primeiroSlot)
                    primeiroSlot = int(primeiroSlot - 1)
                    segundoSlot = opcao % 5
                    segundoSlot = math.ceil(segundoSlot)  
                    segundoSlot = int(segundoSlot - 1)
                        
                    if slots[primeiroSlot][segundoSlot] != " ":
                        print("Posição já ocupada! Tente outra!")
                    else:
                        slots[primeiroSlot][segundoSlot] = "O"
                        break
        
def jogoCPUPrimeiroJogador5x5():
    sequenciaNumeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    linha = coluna = 5
    slots = [[0 for linhas in range(linha)] for colunas in range(coluna)]

    for index in range(0,5):
        for jIndex in range(0,5):
            slots[index][jIndex] = " "
            
    while True:
        os.system("CLS")
        iniciarMenu5x5(slots)
        
        if verificaVitoriaPrimeiroJogador5x5(slots):
            print("\nPARABÉNS!!! O primeiro jogador venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador5x5(slots):
            print("\nGAME OVER!!! A CPU venceu!")
            time.sleep(2)
            break
        elif verificaEmpate5x5(slots):
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
        
        while True:
                opcao = int(input("\nVez do primeiro jogador! Digite um número de 1-25: "))

                if opcao <= 0 or opcao > 25:
                    print("Insira um número válido!")
                else:
                    if opcao < 5:
                        if slots[0][opcao-1] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[0][opcao-1] = "X"
                            sequenciaNumeros.remove(opcao)
                            break
                    else:
                        tempOpcao = opcao 
                        primeiroSlot = opcao / 5
                        primeiroSlot = math.ceil(primeiroSlot)
                        primeiroSlot = int(primeiroSlot - 1)
                        segundoSlot = opcao % 5
                        segundoSlot = math.ceil(segundoSlot)  
                        segundoSlot = int(segundoSlot - 1)
                        
                        if slots[primeiroSlot][segundoSlot] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[primeiroSlot][segundoSlot] = "X"
                            sequenciaNumeros.remove(tempOpcao)
                            break
                    
        if verificaVitoriaPrimeiroJogador5x5(slots):
            os.system("CLS")
            iniciarMenu5x5(slots)
            print("\nPARABÉNS!!! O primeiro jogador venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador5x5(slots):
            os.system("CLS")
            iniciarMenu5x5(slots)
            print("\nGAME OVER!!! A CPU venceu!")
            time.sleep(2)
            break
        elif verificaEmpate5x5(slots):
            os.system("CLS")
            iniciarMenu5x5(slots)
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
                    
        opcaoCPU = random.choice(sequenciaNumeros)
            
        sequenciaNumeros.remove(opcaoCPU) 
        if opcaoCPU < 5:
            slots[0][opcaoCPU-1] = "O"
        else:
            primeiroSlot = opcaoCPU / 5
            primeiroSlot = math.ceil(primeiroSlot)
            primeiroSlot = int(primeiroSlot - 1)
            segundoSlot = opcaoCPU % 5
            segundoSlot = math.ceil(segundoSlot)  
            segundoSlot = int(segundoSlot - 1)
            slots[primeiroSlot][segundoSlot] = "O"  

def jogoCPUSegundoJogador5x5():
    sequenciaNumeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    linha = coluna = 5
    slots = [[0 for linhas in range(linha)] for colunas in range(coluna)]

    for index in range(0,5):
        for jIndex in range(0,5):
            slots[index][jIndex] = " "
            
    while True:
        opcaoCPU = random.choice(sequenciaNumeros)
            
        sequenciaNumeros.remove(opcaoCPU)
        if opcaoCPU < 5:
            slots[0][opcaoCPU-1] = "X"
        else:
            primeiroSlot = opcaoCPU / 5
            primeiroSlot = math.ceil(primeiroSlot)
            primeiroSlot = int(primeiroSlot - 1)
            segundoSlot = opcaoCPU % 5
            segundoSlot = math.ceil(segundoSlot)  
            segundoSlot = int(segundoSlot - 1)
            slots[primeiroSlot][segundoSlot] = "X"
            
        os.system("CLS")
        iniciarMenu5x5(slots)
        
        if verificaVitoriaPrimeiroJogador5x5(slots):
            print("\nGAME OVER!!! A CPU venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador5x5(slots):
            print("\nPARABÉNS!!! O segundo jogador venceu!")
            time.sleep(2)
            break
        elif verificaEmpate5x5(slots):
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
            
        while True:
                opcao = int(input("\nVez do primeiro jogador! Digite um número de 1-25: "))

                if opcao <= 0 or opcao > 25:
                    print("Insira um número válido!")
                else:
                    if opcao < 5:
                        if slots[0][opcao-1] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[0][opcao-1] = "O"
                            sequenciaNumeros.remove(opcao)
                            break
                    else:
                        tempOpcao = opcao 
                        primeiroSlot = opcao / 5
                        primeiroSlot = math.ceil(primeiroSlot)
                        primeiroSlot = int(primeiroSlot - 1)
                        segundoSlot = opcao % 5
                        segundoSlot = math.ceil(segundoSlot)  
                        segundoSlot = int(segundoSlot - 1)
                        
                        if slots[primeiroSlot][segundoSlot] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[primeiroSlot][segundoSlot] = "O"
                            sequenciaNumeros.remove(tempOpcao)
                            break
                    
        if verificaVitoriaPrimeiroJogador5x5(slots):
            os.system("CLS")
            iniciarMenu5x5(slots)
            print("\nGAME OVER!!! A CPU venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador5x5(slots):
            os.system("CLS")
            iniciarMenu5x5(slots)
            print("\nPARABÉNS!!! O segundo jogador venceu!")
            time.sleep(2)
            break
        elif verificaEmpate5x5(slots):
            os.system("CLS")
            iniciarMenu5x5(slots)
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break 

def jogoNormal7x7():
    linha = coluna = 7
    slots = [[0 for linhas in range(linha)] for colunas in range(coluna)]

    for index in range(0,7):
        for jIndex in range(0,7):
            slots[index][jIndex] = " "
            
    while True:
        os.system("CLS")
        iniciarMenu7x7(slots)
        
        if verificaVitoriaPrimeiroJogador7x7(slots):
            print("\nPARABÉNS!!! O primeiro jogador venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador7x7(slots):
            print("\nPARABÉNS!!! O segundo jogador venceu!")
            time.sleep(2)
            break
        elif verificaEmpate7x7(slots):
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
        
        while True:
                opcao = int(input("\nVez do primeiro jogador! Digite um número de 1-49: "))

                if opcao <= 0 or opcao > 49:
                    print("Insira um número válido!")
                else:
                    if opcao < 7:
                        if slots[0][opcao-1] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[0][opcao-1] = "X"
                            break
                    else:
                        primeiroSlot = opcao / 7
                        primeiroSlot = math.ceil(primeiroSlot)
                        primeiroSlot = int(primeiroSlot - 1)
                        segundoSlot = opcao % 7
                        segundoSlot = math.ceil(segundoSlot)  
                        segundoSlot = int(segundoSlot - 1)
                        
                        if slots[primeiroSlot][segundoSlot] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[primeiroSlot][segundoSlot] = "X"
                            break
    
        os.system("CLS")
        iniciarMenu7x7(slots)
        
        if verificaVitoriaPrimeiroJogador7x7(slots):
            print("\nPARABÉNS!!! O primeiro jogador venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador7x7(slots):
            print("\nPARABÉNS!!! O segundo jogador venceu!")
            time.sleep(2)
            break
        elif verificaEmpate7x7(slots):
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
        
        while True:
                opcao = int(input("\nVez do segundo jogador! Digite um número de 1-49: "))

                if opcao <= 0 or opcao > 49:
                    print("Insira um número válido!")
                else:
                    if opcao < 7:
                        if slots[0][opcao-1] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[0][opcao-1] = "O"
                            break
                    else:
                        primeiroSlot = opcao / 7
                        primeiroSlot = math.ceil(primeiroSlot)
                        primeiroSlot = int(primeiroSlot - 1)
                        segundoSlot = opcao % 7
                        segundoSlot = math.ceil(segundoSlot)  
                        segundoSlot = int(segundoSlot - 1)
                        
                        if slots[primeiroSlot][segundoSlot] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[primeiroSlot][segundoSlot] = "O"
                            break

def jogoCPUPrimeiroJogador7x7():
    sequenciaNumeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
    linha = coluna = 7
    slots = [[0 for linhas in range(linha)] for colunas in range(coluna)]

    for index in range(0,7):
        for jIndex in range(0,7):
            slots[index][jIndex] = " "
            
    while True:
        os.system("CLS")
        iniciarMenu7x7(slots)
        
        if verificaVitoriaPrimeiroJogador7x7(slots):
            print("\nPARABÉNS!!! O primeiro jogador venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador7x7(slots):
            print("\nGAME OVER!!! A CPU venceu!")
            time.sleep(2)
            break
        elif verificaEmpate7x7(slots):
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
        
        while True:
                opcao = int(input("\nVez do primeiro jogador! Digite um número de 1-49: "))

                if opcao <= 0 or opcao > 49:
                    print("Insira um número válido!")
                else:
                    if opcao < 7:
                        if slots[0][opcao-1] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[0][opcao-1] = "X"
                            sequenciaNumeros.remove(opcao)
                            break
                    else:
                        tempOpcao = opcao 
                        primeiroSlot = opcao / 7
                        primeiroSlot = math.ceil(primeiroSlot)
                        primeiroSlot = int(primeiroSlot - 1)
                        segundoSlot = opcao % 7
                        segundoSlot = math.ceil(segundoSlot)  
                        segundoSlot = int(segundoSlot - 1)
                        
                        if slots[primeiroSlot][segundoSlot] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[primeiroSlot][segundoSlot] = "X"
                            sequenciaNumeros.remove(tempOpcao)
                            break
                        
        if verificaVitoriaPrimeiroJogador7x7(slots):
            os.system("CLS")
            iniciarMenu7x7(slots)
            print("\nPARABÉNS!!! O primeiro jogador venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador7x7(slots):
            os.system("CLS")
            iniciarMenu7x7(slots)
            print("\nGAME OVER!!! A CPU venceu!")
            time.sleep(2)
            break
        elif verificaEmpate7x7(slots):
            os.system("CLS")
            iniciarMenu7x7(slots)
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
        
        opcaoCPU = random.choice(sequenciaNumeros)
            
        sequenciaNumeros.remove(opcaoCPU)
        if opcaoCPU < 7:
            slots[0][opcaoCPU-1] = "O"
        else:
            primeiroSlot = opcaoCPU / 7
            primeiroSlot = math.ceil(primeiroSlot)
            primeiroSlot = int(primeiroSlot - 1)
            segundoSlot = opcaoCPU % 7
            segundoSlot = math.ceil(segundoSlot)  
            segundoSlot = int(segundoSlot - 1)
            slots[primeiroSlot][segundoSlot] = "O"

def jogoCPUSegundoJogador7x7():
    sequenciaNumeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
    linha = coluna = 7
    slots = [[0 for linhas in range(linha)] for colunas in range(coluna)]

    for index in range(0,7):
        for jIndex in range(0,7):
            slots[index][jIndex] = " "
            
    while True:
        opcaoCPU = random.choice(sequenciaNumeros)
        
        sequenciaNumeros.remove(opcaoCPU)
        if opcaoCPU < 7:
            slots[0][opcaoCPU-1] = "X"
        else:
            primeiroSlot = opcaoCPU / 7
            primeiroSlot = math.ceil(primeiroSlot)
            primeiroSlot = int(primeiroSlot - 1)
            segundoSlot = opcaoCPU % 7
            segundoSlot = math.ceil(segundoSlot)  
            segundoSlot = int(segundoSlot - 1)
            slots[primeiroSlot][segundoSlot] = "X"
            
        os.system("CLS")
        iniciarMenu7x7(slots)
        
        if verificaVitoriaPrimeiroJogador7x7(slots):
            print("\nGAME OVER!!! A CPU venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador7x7(slots):
            print("\nPARABÉNS!!! O segundo jogador venceu!")
            time.sleep(2)
            break
        elif verificaEmpate7x7(slots):
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break
        
        while True:
                opcao = int(input("\nVez do primeiro jogador! Digite um número de 1-49: "))

                if opcao <= 0 or opcao > 49:
                    print("Insira um número válido!")
                else:
                    if opcao < 7:
                        if slots[0][opcao-1] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[0][opcao-1] = "O"
                            sequenciaNumeros.remove(opcao)
                            break
                    else:
                        tempOpcao = opcao 
                        primeiroSlot = opcao / 7
                        primeiroSlot = math.ceil(primeiroSlot)
                        primeiroSlot = int(primeiroSlot - 1)
                        segundoSlot = opcao % 7
                        segundoSlot = math.ceil(segundoSlot)  
                        segundoSlot = int(segundoSlot - 1)
                        
                        if slots[primeiroSlot][segundoSlot] != " ":
                            print("Posição já ocupada! Tente outra!")
                        else:
                            slots[primeiroSlot][segundoSlot] = "O"
                            sequenciaNumeros.remove(tempOpcao)
                            break
                        
        if verificaVitoriaPrimeiroJogador7x7(slots):
            os.system("CLS")
            iniciarMenu7x7(slots)
            print("\nGAME OVER!!! A CPU venceu!")
            time.sleep(2)
            break
        elif verificaVitoriaSegundoJogador7x7(slots):
            os.system("CLS")
            iniciarMenu7x7(slots)
            print("\nPARABÉNS!!! O segundo jogador venceu!")
            time.sleep(2)
            break
        elif verificaEmpate7x7(slots):
            os.system("CLS")
            iniciarMenu7x7(slots)
            print("\nTIE!!! O Jogo terminou em empate!")
            time.sleep(2)
            break

def menuInicial():
    while True:
        os.system("CLS")

        print("----------MENU INICIAL----------\n")
        print("1. PADRÃO (3X3)\n2. EXTENDIDO (5X5)\n3. HARDCORE (7X7)\n9. ENCERRAR\n")
        print("--------------------------------\n")
        opcao = input("Escolha uma das opções acima: ")
        
        if opcao == '1':
            menuInicial3x3()
        elif opcao == '2':
            menuInicial5x5()
        elif opcao == '3':
            menuInicial7x7()
        elif opcao == '9':
            os.system("CLS")
            print("PROGRAMA ENCERRADO")
            time.sleep(2)  
            break
        else:
            os.system("CLS")
            print("Erro! Escolha uma opção adequada!")
            time.sleep(2)

def menuInicial3x3():
    while True:
        os.system("CLS")

        print("----------MENU INICIAL 3X3----------\n")
        print("1. JOGADOR VS JOGADOR\n2. JOGADOR VS CPU\n9. VOLTAR\n")
        print("------------------------------------\n")
        opcao = input("Escolha uma das opções acima: ")
        
        if opcao == '1':
            jogoNormal3x3()
            break
        elif opcao == '2':
            menuInicialCPU3x3()
            break
        elif opcao == '9':
            break
        else:
            os.system("CLS")
            print("Erro! Escolha uma opção adequada!")
            time.sleep(2)

def menuInicialCPU3x3():
    while True:
        os.system("CLS")

        print("----------CPU 3X3----------\n")
        print("1. PRIMEIRO JOGADOR\n2. SEGUNDO JOGADOR\n9. VOLTAR\n")
        print("---------------------------\n")
        opcao = input("Escolha uma das opções acima: ")
        
        if opcao == '1':
            jogoCPUPrimeiroJogador3x3()
            break
        elif opcao == '2':
            jogoCPUSegundoJogador3x3()
            break
        elif opcao == '9':
            menuInicial3x3()
            break
        else:
            os.system("CLS")
            print("Erro! Escolha uma opção adequada!")
            time.sleep(2)

def menuInicial5x5():
    while True:
        os.system("CLS")

        print("----------MENU INICIAL 5X5----------\n")
        print("1. JOGADOR VS JOGADOR\n2. JOGADOR VS CPU\n9. VOLTAR\n")
        print("------------------------------------\n")
        opcao = input("Escolha uma das opções acima: ")
        
        if opcao == '1':
            jogoNormal5x5()
            break
        elif opcao == '2':
            menuInicialCPU5x5()
            break
        elif opcao == '9':
            break
        else:
            os.system("CLS")
            print("Erro! Escolha uma opção adequada!")
            time.sleep(2)
            
def menuInicialCPU5x5():
    while True:
        os.system("CLS")

        print("----------CPU 5X5----------\n")
        print("1. PRIMEIRO JOGADOR\n2. SEGUNDO JOGADOR\n9. VOLTAR\n")
        print("---------------------------\n")
        opcao = input("Escolha uma das opções acima: ")
        
        if opcao == '1':
            jogoCPUPrimeiroJogador5x5()
            break
        elif opcao == '2':
            jogoCPUSegundoJogador5x5()
            break
        elif opcao == '9':
            menuInicial5x5()
            break
        else:
            os.system("CLS")
            print("Erro! Escolha uma opção adequada!")
            time.sleep(2)

def menuInicial7x7():
    while True:
        os.system("CLS")

        print("----------MENU INICIAL 7X7----------\n")
        print("1. JOGADOR VS JOGADOR\n2. JOGADOR VS CPU\n9. VOLTAR\n")
        print("------------------------------------\n")
        opcao = input("Escolha uma das opções acima: ")
        
        if opcao == '1':
            jogoNormal7x7()
            break
        elif opcao == '2':
            menuInicialCPU7x7()
            break
        elif opcao == '9':
            break
        else:
            os.system("CLS")
            print("Erro! Escolha uma opção adequada!")
            time.sleep(2)
            
def menuInicialCPU7x7():
    while True:
        os.system("CLS")

        print("----------CPU 7X7----------\n")
        print("1. PRIMEIRO JOGADOR\n2. SEGUNDO JOGADOR\n9. VOLTAR\n")
        print("----------------------------\n")
        opcao = input("Escolha uma das opções acima: ")
        
        if opcao == '1':
            jogoCPUPrimeiroJogador7x7()
            break
        elif opcao == '2':
            jogoCPUSegundoJogador7x7()
            break
        elif opcao == '9':
            menuInicial7x7()
            break
        else:
            os.system("CLS")
            print("Erro! Escolha uma opção adequada!")
            time.sleep(2)        
        
menuInicial()