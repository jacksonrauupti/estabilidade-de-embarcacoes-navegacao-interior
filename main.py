 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Colocar print em todas as etapas dos calculos

import pandas as pd #Para leitura de arquivos csv como data.frame
import tkinter as tk #Para abrir janela de leitura de dados
from tkinter import filedialog #Para abrir janela de leitura de dados
import numpy
import time #Para pausas de tempo para o usuario fazer leitura de informacao importante
import math

#### Janela para encontrar o diretorio. ####
## Diretorio particularidades ##
### Suspendi essa sessao para ver se esses dados realmente sera usados

#print("Selecione o arquivo de particularidades da embarcacao \n")


## Diretorio Navio Leve ##

print("Informe os dados do Navio Leve \n")
Deslocamento_Leve= input("Informe o valor do Deslocamento leve da embarcacao -> ")
VCG_Leve= input("Informe o valor do VCG leve da embarcacao -> ")
LCG_Leve= input("Informe o valor do LCG leve da embarcacao -> ")
Boca_Navio=float(input("Informe o valor da boca do navio -> "))
Pontal_Navio=float(input("informe o valor do pontal da embarcação -> "))


## Diretorio Curvas Hidrostaticas ##

print("Selecione o arquivo de Curvas Hidrostaticas da embarcacao \n")
time.sleep(3)
Janela=tk.Tk() #objeto Janela1 e a janela que o tkinter abre
C_Hidrostaticas_Path=filedialog.askopenfilename()
Janela.destroy() #fechando a janela do tkinter
#Colocando o caminho encontrado pelo usuario na funcao de leitura de dataset
C_Hidrostaticas=pd.read_csv(C_Hidrostaticas_Path, sep = ";",decimal=",")


## Diretorio Curvas Cruzadas ##

print("Selecione o arquivo de Curvas Cruzadas da embarcacao \n \n \n")
time.sleep(3)
Janela=tk.Tk() #objeto Janela1 e a janela que o tkinter abre
C_Cruzadas_Path=filedialog.askopenfilename()
Janela.destroy() #fechando a janela do tkinter
#Colocando o caminho encontrado pelo usuario na funcao de leitura de dataset
C_Cruzadas=pd.read_csv(C_Cruzadas_Path, sep = ";",decimal=",")


#### Escolha dos criterios de Estabilidade ####

#Criando variavel de escolha
Escolha_Criterios_Estabilidade = 0
while Escolha_Criterios_Estabilidade != 1 or Escolha_Criterios_Estabilidade != 2:
    print("Escolha os criterios de estabilidade, sabendo que \n - Normam 01 = Paranavegacao em mar aberto; e \n - Normam 02 = Paranavegacao em aguas interiores.\n \n ")
    Escolha_Criterios_Estabilidade=input("Digite 1 para escolher a Normam 01 e 2 para escolher a Normam 02 -> ")
    Escolha_Criterios_Estabilidade=int(Escolha_Criterios_Estabilidade)
    
    
    #Condicional da escolha da NORMAM
    if(Escolha_Criterios_Estabilidade==2):
        
        #Condicional escolha do tipo de embarcacao
        Tipo_Embarcacao= input("Selecione o tipo de embarcacao desejada para os calculos. Digite o numero correspondente \n 1 - Embarcacoes de Passageiros; \n 2 - Embarcacoes de Carga; \n 3 - Rebocadores e Empurradores; \n 4 - Embarcacoes de Pesca; e \n 5 - Embarcacoes que Transportam Carga no Conves. -> ")
        Tipo_Embarcacao= int(Tipo_Embarcacao)
        
        #Para embarcacoes de passageiros
        if(Tipo_Embarcacao==1):
          ##Condicoes de carregamento
          
          ###Perguntas necessarias para os calculos                  
          ####Conveses passageiros
          Qtd_Conveses_Passageiros= input("Qual a quantidade de conveses de passageiros? -> ")
          Qtd_Conveses_Passageiros= int(Qtd_Conveses_Passageiros)
          Qtd_Conveses_Passageiros= list(range(1,Qtd_Conveses_Passageiros+1,1)) #Soma +1, pois o python inicia a contagem a partir do 0, portanto para compensar e ir ate o numero desejado pelo usuario deve somar +1
          
          
          Qtd_Passageiros=list()
          Peso_Passageiros=list()
          LCG_Passageiros=list()
          VCG_Passageiros=list()
          for i in Qtd_Conveses_Passageiros: # A quantidade de passageiros no conves i vai esta alocada na posicao i-1
              Qtd_Passageiros.append(   int( input("Quantos passageiros cabem no conves {} -> ".format(i)) )   )
              Peso_Passageiros.append(float( 0.075*Qtd_Passageiros[i-1]))
              LCG_Passageiros.append(   float( input("Qual a posicao do LCG dos passageiros no conves {} -> ".format(i)) )   )
              VCG_Passageiros.append(   float( input("Qual a posicao do VCG dos passageiros no conves {} -> ".format(i)) )   )
              print("\n \n")
              
          ##### TRIPULANTES E PERTENCES
          Qtd_Tripulantes=int( input("Informe a quantidade de tripulantes na embarcacao -> "))
          ###Peso e peso do passageiro mais bagagem
          Peso_Tripulantes=float((0.075+0.025)*Qtd_Tripulantes )
          LCG_Tripulantes =  float( input("Informe posicao do LCG dos tripulantes -> " ) )
          VCG_Tripulantes =  float( input("Informe posicao do VCG dos tripulantes -> " ) )
          
          ##### Tanques
          Qtd_Tanques=input("Qual a quantidade de tanques que existem no navio? Incluindo agua, oleo e qualquer outros tanques -> ")
          Qtd_Tanques=int(Qtd_Tanques)
          Qtd_Tanques=list(range(1,Qtd_Tanques+1,1)) #Soma +1, pois o python inicia a contagem a partir do 0, portanto para compensar e ir ate o numero desejado pelo usuario deve somar +1
          
          #####Informacoes da variavel Dados_Tanque#####
          # A variavel MSL_Tanques_Com_K ira funcionar de forma que exista lista dentro de lista
          # Cada lista dentro dessa variavel, que e uma lista, sera um tanque diferente
          
          
          Comprimento_Tanques=list()
          Largura_Tanques=list()
          Altura_Tanques=list()
          Densidade_Tanques=list()
          VCG_Tanque=list()
          LCG_Tanque=list()
          Volume_informado_Tanques=list()
          Volume_Calc_Tanques=list()
          Peso_Tanque=list()
          MSL_Tanque_Sem_K=list()
          MSL_Tanque_Com_K=list()
          for i in Qtd_Tanques:
              Comprimento_Tanques.append(   float( input("Qual o comprimento do tanque {} -> ".format(i)) )   )
              Largura_Tanques.append(    float( input("Qual o largura do tanque {} -> ".format(i)) )   )
              Altura_Tanques.append(     float( input("Qual o altura do tanque {} -> ".format(i)) )  )
              Densidade_Tanques.append(   float( input("Qual a densidade do fluido no tanque {} em t/m3-> ".format(i)) )    )
              VCG_Tanque.append(    float( input("Qual o valor centro de gravidade vertical (VCG) do tanque {} -> ".format(i))  )     )
              LCG_Tanque.append(    float( input("Qual o valor do centro de gravidade longitudinal (LCG) do tanque {} -> ".format(i))   )       )
              Volume_informado_Tanques.append(    float( input("Qual o volume util informado do tanque {} -> ".format(i))  )     )
              Volume_Calc_Tanques.append(     Comprimento_Tanques[i-1]*Largura_Tanques[i-1]*Altura_Tanques[i-1]   )
              Peso_Tanque.append(    Volume_informado_Tanques[i-1]*Densidade_Tanques[i-1]     )                              
              
              #Calculo do coeficiente adimensional de efeito de superficie livre. Fonte: NORMAM 02. 
              Coef_K=list()
              for theta in numpy.arange(0,90+0.25,0.25): #A posicao do do grau desejado vai ser dado por regra de 3 que resulta na formula Grau_Desejado = (((Quantidade de espacos no vetor)*(Grau desejado))/(Limite superior de grau))-1 -> Menos devido ao sistema de alocacao do python que comeca no zero
                  if(theta==0):
                      continue
                  if( 1/(math.tan(math.radians(theta)))>=(Largura_Tanques[i-1]/Altura_Tanques[i-1])):
                      Coef_K.append(   (math.sin(math.radians(theta))/12)*(1+((math.tan(math.radians(theta)))*(math.tan(math.radians(theta))))/2)*(Largura_Tanques[i-1]/Altura_Tanques[i-1])    )
                  elif(1/(math.tan(math.radians(theta)))<=(Largura_Tanques[i-1]/Altura_Tanques[i-1])):
                      Coef_K.append(   (math.cos(math.radians(theta))/8)*(1+((math.tan(math.radians(theta)))/(Largura_Tanques[i-1]/Altura_Tanques[i-1])))-((math.cos(math.radians(theta))/(12*(Largura_Tanques[i-1]/Altura_Tanques[i-1])*(Largura_Tanques[i-1]/Altura_Tanques[i-1])))*(1+((1/math.tan(math.radians(theta)))*(1/math.tan(math.radians(theta))))/2))     )
              
              #MSL sem e com K
              
              MSL_Tanque_Sem_K.append(   Volume_informado_Tanques[i-1]*Largura_Tanques[i-1]*Densidade_Tanques[i-1]*math.sqrt(Volume_informado_Tanques[i-1]/Volume_Calc_Tanques[i-1])   )
              MSL_Tanque_Com_K.append( list( numpy.multiply(MSL_Tanque_Sem_K[i-1],Coef_K) )  )
              
              print("\n \n \n")
              
              
              
              
              
          #### Bagaens ####
          # ++ Realmente e necessario perguntar a qtd de bagagens?
          Qtd_Conveses_Bagagens=int(input("Informe a quantidade de conveses que transportam bagagens -> "))
          Qtd_Conveses_Bagagens=list(range(1, Qtd_Conveses_Bagagens+1,1))
          
          
          Qtd_Bagagens=list()
          Peso_Bagagens=list()
          LCG_Bagagens=list()
          VCG_Bagagens=list()
          
          for i in Qtd_Conveses_Bagagens:
              Qtd_Bagagens.append(  float( input("Informe a quantidade de bagagens embarcada no conves {} -> ".format(i)) )  )
              Peso_Bagagens.append(  float( Qtd_Bagagens[i-1]*0.025 )  )
              VCG_Bagagens.append(  float( input("Informe o VCG das bagagens embarcada no conves {} -> ".format(i)) )  )
              LCG_Bagagens.append(  float( input("Informe o LCG das bagagens embarcada no conves {} -> ".format(i)) )  )
          
          #### Coisas que podem ou nao possuir na embarcacao ####
          
          # Nesse ponto as variaveis terao um coeficiente de existencia
          # que varia nos valores 0 ou 1 que sera informado pelo usuario
          # em caso de existencia tera peso UM no calculo de estabilidade
          # ou, seja, sera considerado; caso nao exista tera peso ZERO
          # sendo, desse modo, desconsiderado do calculo.
          
          ### Carga nos poroes ###
          Coef_Exist_Carga_Poroes=int( input("A embarcacao possui carga nos poroes? Digite 1 para SIM, Digite 0 para NAO -> "))
          if(Coef_Exist_Carga_Poroes==1):
              Qtd_Carga_Poroes=int( input(" Quantas cargas diferentes existem no porao? -> "))
              Qtd_Carga_Poroes=list(range(1, Qtd_Carga_Poroes+1,1))
              
              Volume_Carga_Poroes=list()
              Peso_Carga_Poroes=list()
              LCG_Carga_Poroes=list()
              VCG_Carga_Poroes=list()
              for i in Qtd_Carga_Poroes:
                  Volume_Carga_Poroes.append( float( input("Informe o volume da carga {} -> ".format(i)))  )
                  Peso_Carga_Poroes.append( float( input("Informe o peso da carga {} -> ".format(i)))  )
                  LCG_Carga_Poroes.append( float( input("Informe o VCG da carga {} -> ".format(i)))  )
                  VCG_Carga_Poroes.append( float( input("Informe o LCG da carga {} -> ".format(i)))  )
                  
                  
          ### Carga no conves principal ###
          Coef_Exist_Carga_Conves_Principal=int( input("A embarcacao possui cargas no Conves principal? Digite 1 para SIM, Digite 0 para NAO -> "))
          if(Coef_Exist_Carga_Conves_Principal==1):
              Qtd_Carga_Conves_Principal=int( input(" Quantas cargas diferentes existem no conves principal? -> "))
              Qtd_Carga_Conves_Principal=list(range(1, Qtd_Carga_Conves_Principal+1,1))
              
              Volume_Carga_Conves_Principal=list()
              Peso_Carga_Conves_Principal=list()
              LCG_Carga_Conves_Principal=list()
              VCG_Carga_Conves_Principal=list()
              for i in Qtd_Carga_Poroes:
                  Volume_Carga_Conves_Principal.append( float( input("Informe o volume da carga {} -> ".format(i)))  )
                  Peso_Carga_Conves_Principal.append( float( input("Informe o peso da carga {} -> ".format(i)))  )
                  LCG_Carga_Conves_Principal.append( float( input("Informe o VCG da carga {} -> ".format(i)))  )
                  VCG_Carga_Conves_Principal.append( float( input("Informe o LCG da carga {} -> ".format(i)))  )
                  
                  
          ### Lastro Fixo ###
          Coef_Exist_Lastro_Fixo=int( input("A embarcacao possui Lastro Fixo? Digite 1 para SIM, Digite 0 para NAO -> "))
          if(Coef_Exist_Lastro_Fixo==1):
              Qtd_Lastro_Fixo=int( input(" Quantas Lastros Fixos diferentes existem na embarcacao? -> "))
              Qtd_Lastro_Fixo=list(range(1, Qtd_Lastro_Fixo+1,1))
              
              Volume_Lastro_Fixo=list()
              Peso_Lastro_Fixo=list()
              LCG_Lastro_Fixo=list()
              VCG_Lastro_Fixo=list()
              for i in Qtd_Carga_Poroes:
                  Volume_Lastro_Fixo.append( float( input("Informe o volume do lastro fixo {} -> ".format(i)))  )
                  Peso_Lastro_Fixo.append( float( input("Informe o peso do lastro fixo {} -> ".format(i)))  )
                  LCG_Lastro_Fixo.append( float( input("Informe o VCG do lastro fixo {} -> ".format(i)))  )
                  VCG_Lastro_Fixo.append( float( input("Informe o LCG do lastro fixo {} -> ".format(i)))  )
                  
          ################  CALCULOS DE ESTABILIDADE ##################        
          
          #### Momento e Centro de gravidade dos liquidos ####
          Momento_Vert_Tanques=list()
          Momento_Long_Tanques=list()
          
          for i in  Qtd_Tanques:
              Momento_Vert_Tanques.append(Peso_Tanque[i-1]*VCG_Tanque[i-1])
              Momento_Long_Tanques.append(Peso_Tanque[i-1]*LCG_Tanque[i-1])
          
          Peso_Final_Tanques=sum(Peso_Tanque)
          LCG_Final_Tanques=sum(Momento_Long_Tanques)/Peso_Final_Tanques
          VCG_Final_Tanques=sum(Momento_Vert_Tanques)/Peso_Final_Tanques

          #### Momento e centro de gravidade de cargas, passageiros, tripulacao ####
          Momento_Vert_Passageiros=list()
          Momento_Long_Passageiros=list()
          
          Momento_Vert_Tripulantes=Peso_Tripulantes*VCG_Tripulantes
          Momento_Long_Tripulantes=Peso_Tripulantes*LCG_Tripulantes
          
          Momento_Vert_Bagagens=list()
          Momento_Long_Bagagens=list()
          
          Momento_Vert_Carga_Conves_Principal=list()
          Momento_Long_Carga_Conves_Principal=list()
          
          Momento_Vert_Carga_Poroes=list()
          Momento_Long_Carga_Poroes=list()
          
          Momento_Vert_Lastro_Fixo=list()
          Momento_Long_Lastro_Fixo=list()
          
          for i in  Qtd_Conveses_Passageiros:
              Momento_Vert_Passageiros.append(Peso_Passageiros[i-1]*VCG_Passageiros[i-1])
              Momento_Long_Passageiros.append(Peso_Passageiros[i-1]*LCG_Passageiros[i-1])
              
          for i in  Qtd_Conveses_Bagagens:
              Momento_Long_Bagagens.append(Peso_Bagagens[i-1]*LCG_Bagagens[i-1])
              Momento_Vert_Bagagens.append(Peso_Bagagens[i-1]*VCG_Bagagens[i-1])
          
          
          if(Coef_Exist_Carga_Conves_Principal==1):
              for i in Qtd_Carga_Conves_Principal:
                  Momento_Vert_Carga_Conves_Principal.append(Peso_Carga_Conves_Principal[i-1]*VCG_Carga_Conves_Principal[i-1])
                  Momento_Long_Carga_Conves_Principal.append(Peso_Carga_Conves_Principal[i-1]*LCG_Carga_Conves_Principal[i-1])
                  
             
          if(Coef_Exist_Carga_Poroes==1):
              for i in Qtd_Carga_Poroes: 
                  Momento_Vert_Carga_Poroes.append(Peso_Carga_Poroes[i-1]*VCG_Carga_Poroes[i-1])
                  Momento_Long_Carga_Poroes.append(Peso_Carga_Poroes[i-1]*LCG_Carga_Poroes[i-1])
          
                  
          if(Coef_Exist_Lastro_Fixo==1):  
              for i in Qtd_Lastro_Fixo:
                  Momento_Vert_Lastro_Fixo.append(Peso_Lastro_Fixo[i-1]*VCG_Lastro_Fixo[i-1])
                  Momento_Long_Lastro_Fixo.append(Peso_Lastro_Fixo[i-1]*LCG_Lastro_Fixo[i-1])
          
          
          
          Peso_Final_Passageiros=sum(Peso_Passageiros)
          LCG_Final_Passageiros=sum(Momento_Long_Passageiros)/Peso_Final_Passageiros
          VCG_Final_Passageiros=sum(Momento_Vert_Passageiros)/Peso_Final_Passageiros
          
          Peso_Final_Tripulantes=Peso_Tripulantes
          LCG_Final_Tripulantes=Momento_Long_Tripulantes/Peso_Final_Tripulantes
          VCG_Final_Tripulantes=Momento_Vert_Tripulantes/Peso_Final_Tripulantes
          
          Peso_Final_Bagagens=sum(Peso_Bagagens)
          LCG_Final_Bagagens=sum(Momento_Long_Bagagens)/Peso_Final_Bagagens
          VCG_Final_Bagagens=sum(Momento_Vert_Bagagens)/Peso_Final_Bagagens
          
          
          if(Coef_Exist_Carga_Conves_Principal==1):
              Peso_Final_Carga_Conves_Principal=sum(Peso_Carga_Conves_Principal)
              LCG_Final_Carga_Conves_Principal=sum(Momento_Long_Carga_Conves_Principal)/Peso_Final_Carga_Conves_Principal
              VCG_Final_Carga_Conves_Principal=sum(Momento_Vert_Carga_Conves_Principal)/Peso_Final_Carga_Conves_Principal
          
          elif(Coef_Exist_Carga_Conves_Principal==0):
              Peso_Final_Carga_Conves_Principal=0
              LCG_Final_Carga_Conves_Principal=0
              VCG_Final_Carga_Conves_Principal=0
          
          
          if(Coef_Exist_Carga_Poroes==1):
              Peso_Final_Carga_Poroes=sum(Peso_Carga_Poroes)
              LCG_Final_Carga_Poroes=sum(Momento_Long_Carga_Poroes)/Peso_Final_Carga_Poroes
              VCG_Final_Carga_Poroes=sum(Momento_Vert_Carga_Poroes)/Peso_Final_Carga_Poroes
          
          elif(Coef_Exist_Carga_Poroes==0):
              Peso_Final_Carga_Poroes=0
              LCG_Final_Carga_Poroes=0
              VCG_Final_Carga_Poroes=0

              
          if(Coef_Exist_Lastro_Fixo==1):
              Peso_Final_Lastro_Fixo=sum(Peso_Lastro_Fixo)
              LCG_Final_Lastro_Fixo=sum(Momento_Long_Lastro_Fixo)/Peso_Final_Lastro_Fixo
              VCG_Final_Lastro_Fixo=sum(Momento_Vert_Lastro_Fixo)/Peso_Final_Lastro_Fixo
          
          elif(Coef_Exist_Lastro_Fixo==0):
              Peso_Final_Lastro_Fixo=0
              LCG_Final_Lastro_Fixo=0
              VCG_Final_Lastro_Fixo=0

          #### Momento e centro de gravidade da embarcação completa ####
          """
          A Normam nos dá 6condições de carregamento que seguem abaixo
              
          """
          Peso_Final_Navio_Completo=list()
          LCG_Final_Navio_Completo=list()
          VCG_Final_Navio_Completo=list()
          #Condição 1
          Peso_Final_Navio_Completo.append(Peso_Final_Passageiros + Peso_Final_Tanques + Peso_Final_Tripulantes + Peso_Final_Lastro_Fixo + Peso_Final_Carga_Conves_Principal + Peso_Final_Bagagens + Peso_Final_Carga_Poroes + Deslocamento_Leve)
          LCG_Final_Navio_Completo.append((Peso_Final_Passageiros*LCG_Final_Passageiros + Peso_Final_Tanques*LCG_Final_Tanques + Peso_Final_Tripulantes*LCG_Final_Tripulantes + Peso_Final_Lastro_Fixo*LCG_Final_Lastro_Fixo + Peso_Final_Carga_Conves_Principal*LCG_Final_Carga_Conves_Principal + Peso_Final_Bagagens*LCG_Final_Bagagens + Peso_Final_Carga_Poroes*LCG_Final_Carga_Poroes + Deslocamento_Leve*LCG_Leve)/Peso_Final_Navio_Completo[0])
          VCG_Final_Navio_Completo.append((Peso_Final_Passageiros*VCG_Final_Passageiros + Peso_Final_Tanques*VCG_Final_Tanques + Peso_Final_Tripulantes*VCG_Final_Tripulantes + Peso_Final_Lastro_Fixo*VCG_Final_Lastro_Fixo + Peso_Final_Carga_Conves_Principal*VCG_Final_Carga_Conves_Principal + Peso_Final_Bagagens*VCG_Final_Bagagens + Peso_Final_Carga_Poroes*VCG_Final_Carga_Poroes + Deslocamento_Leve*VCG_Leve)/Peso_Final_Navio_Completo[0])
          
          #Condição 2
          Peso_Final_Navio_Completo.append(Peso_Final_Passageiros + 0.1*Peso_Final_Tanques + Peso_Final_Tripulantes + Peso_Final_Lastro_Fixo + Peso_Final_Carga_Conves_Principal + Peso_Final_Bagagens + Peso_Final_Carga_Poroes + Deslocamento_Leve)
          LCG_Final_Navio_Completo.append((Peso_Final_Passageiros*LCG_Final_Passageiros + 0.1*Peso_Final_Tanques*LCG_Final_Tanques + Peso_Final_Tripulantes*LCG_Final_Tripulantes + Peso_Final_Lastro_Fixo*LCG_Final_Lastro_Fixo + Peso_Final_Carga_Conves_Principal*LCG_Final_Carga_Conves_Principal + Peso_Final_Bagagens*LCG_Final_Bagagens + Peso_Final_Carga_Poroes*LCG_Final_Carga_Poroes + Deslocamento_Leve*LCG_Leve)/Peso_Final_Navio_Completo[1])
          VCG_Final_Navio_Completo.append((Peso_Final_Passageiros*VCG_Final_Passageiros + 0.1*Peso_Final_Tanques*VCG_Final_Tanques + Peso_Final_Tripulantes*VCG_Final_Tripulantes + Peso_Final_Lastro_Fixo*VCG_Final_Lastro_Fixo + Peso_Final_Carga_Conves_Principal*VCG_Final_Carga_Conves_Principal + Peso_Final_Bagagens*VCG_Final_Bagagens + Peso_Final_Carga_Poroes*VCG_Final_Carga_Poroes + Deslocamento_Leve*VCG_Leve)/Peso_Final_Navio_Completo[1])
          
          #Condição 3
          Peso_Final_Navio_Completo.append(Peso_Final_Passageiros + Peso_Final_Tanques + Peso_Final_Tripulantes + Peso_Final_Lastro_Fixo + 0*Peso_Final_Carga_Conves_Principal + Peso_Final_Bagagens + 0*Peso_Final_Carga_Poroes + Deslocamento_Leve)
          LCG_Final_Navio_Completo.append((Peso_Final_Passageiros*LCG_Final_Passageiros + Peso_Final_Tanques*LCG_Final_Tanques + Peso_Final_Tripulantes*LCG_Final_Tripulantes + Peso_Final_Lastro_Fixo*LCG_Final_Lastro_Fixo + 0*Peso_Final_Carga_Conves_Principal*LCG_Final_Carga_Conves_Principal + Peso_Final_Bagagens*LCG_Final_Bagagens + 0*Peso_Final_Carga_Poroes*LCG_Final_Carga_Poroes + Deslocamento_Leve*LCG_Leve)/Peso_Final_Navio_Completo[2])
          VCG_Final_Navio_Completo.append((Peso_Final_Passageiros*VCG_Final_Passageiros + Peso_Final_Tanques*VCG_Final_Tanques + Peso_Final_Tripulantes*VCG_Final_Tripulantes + Peso_Final_Lastro_Fixo*VCG_Final_Lastro_Fixo + 0*Peso_Final_Carga_Conves_Principal*VCG_Final_Carga_Conves_Principal + Peso_Final_Bagagens*VCG_Final_Bagagens + 0*Peso_Final_Carga_Poroes*VCG_Final_Carga_Poroes + Deslocamento_Leve*VCG_Leve)/Peso_Final_Navio_Completo[2])
          
          #Condição 4
          Peso_Final_Navio_Completo.append(Peso_Final_Passageiros + 0.1*Peso_Final_Tanques + Peso_Final_Tripulantes + Peso_Final_Lastro_Fixo + 0*Peso_Final_Carga_Conves_Principal + Peso_Final_Bagagens + 0*Peso_Final_Carga_Poroes + Deslocamento_Leve)
          LCG_Final_Navio_Completo.append((Peso_Final_Passageiros*LCG_Final_Passageiros + 0.1*Peso_Final_Tanques*LCG_Final_Tanques + Peso_Final_Tripulantes*LCG_Final_Tripulantes + Peso_Final_Lastro_Fixo*LCG_Final_Lastro_Fixo + 0*Peso_Final_Carga_Conves_Principal*LCG_Final_Carga_Conves_Principal + Peso_Final_Bagagens*LCG_Final_Bagagens + 0*Peso_Final_Carga_Poroes*LCG_Final_Carga_Poroes + Deslocamento_Leve*LCG_Leve)/Peso_Final_Navio_Completo[3])
          VCG_Final_Navio_Completo.append((Peso_Final_Passageiros*VCG_Final_Passageiros + 0.1*Peso_Final_Tanques*VCG_Final_Tanques + Peso_Final_Tripulantes*VCG_Final_Tripulantes + Peso_Final_Lastro_Fixo*VCG_Final_Lastro_Fixo + 0*Peso_Final_Carga_Conves_Principal*VCG_Final_Carga_Conves_Principal + Peso_Final_Bagagens*VCG_Final_Bagagens + 0*Peso_Final_Carga_Poroes*VCG_Final_Carga_Poroes + Deslocamento_Leve*VCG_Leve)/Peso_Final_Navio_Completo[3])
          
          #Condição 5
          Peso_Final_Navio_Completo.append(0*Peso_Final_Passageiros + Peso_Final_Tanques + Peso_Final_Tripulantes + Peso_Final_Lastro_Fixo + Peso_Final_Carga_Conves_Principal + 0*Peso_Final_Bagagens + Peso_Final_Carga_Poroes + Deslocamento_Leve)
          LCG_Final_Navio_Completo.append((0*Peso_Final_Passageiros*LCG_Final_Passageiros + Peso_Final_Tanques*LCG_Final_Tanques + Peso_Final_Tripulantes*LCG_Final_Tripulantes + Peso_Final_Lastro_Fixo*LCG_Final_Lastro_Fixo + Peso_Final_Carga_Conves_Principal*LCG_Final_Carga_Conves_Principal + 0*Peso_Final_Bagagens*LCG_Final_Bagagens + Peso_Final_Carga_Poroes*LCG_Final_Carga_Poroes + Deslocamento_Leve*LCG_Leve)/Peso_Final_Navio_Completo[4])
          VCG_Final_Navio_Completo.append((0*Peso_Final_Passageiros*VCG_Final_Passageiros + Peso_Final_Tanques*VCG_Final_Tanques + Peso_Final_Tripulantes*VCG_Final_Tripulantes + Peso_Final_Lastro_Fixo*VCG_Final_Lastro_Fixo + Peso_Final_Carga_Conves_Principal*VCG_Final_Carga_Conves_Principal + 0*Peso_Final_Bagagens*VCG_Final_Bagagens + Peso_Final_Carga_Poroes*VCG_Final_Carga_Poroes + Deslocamento_Leve*VCG_Leve)/Peso_Final_Navio_Completo[4])
          
          #Condição 6
          Peso_Final_Navio_Completo.append(0*Peso_Final_Passageiros + 0.1*Peso_Final_Tanques + Peso_Final_Tripulantes + Peso_Final_Lastro_Fixo + Peso_Final_Carga_Conves_Principal + 0*Peso_Final_Bagagens + Peso_Final_Carga_Poroes + Deslocamento_Leve)
          LCG_Final_Navio_Completo.append((0*Peso_Final_Passageiros*LCG_Final_Passageiros + 0.1*Peso_Final_Tanques*LCG_Final_Tanques + Peso_Final_Tripulantes*LCG_Final_Tripulantes + Peso_Final_Lastro_Fixo*LCG_Final_Lastro_Fixo + Peso_Final_Carga_Conves_Principal*LCG_Final_Carga_Conves_Principal + 0*Peso_Final_Bagagens*LCG_Final_Bagagens + Peso_Final_Carga_Poroes*LCG_Final_Carga_Poroes + Deslocamento_Leve*LCG_Leve)/Peso_Final_Navio_Completo[5])
          VCG_Final_Navio_Completo.append((0*Peso_Final_Passageiros*VCG_Final_Passageiros + 0.1*Peso_Final_Tanques*VCG_Final_Tanques + Peso_Final_Tripulantes*VCG_Final_Tripulantes + Peso_Final_Lastro_Fixo*VCG_Final_Lastro_Fixo + Peso_Final_Carga_Conves_Principal*VCG_Final_Carga_Conves_Principal + 0*Peso_Final_Bagagens*VCG_Final_Bagagens + Peso_Final_Carga_Poroes*VCG_Final_Carga_Poroes + Deslocamento_Leve*VCG_Leve)/Peso_Final_Navio_Completo[5])
          
          #### Interpolaçao das propriedades hidorstaticas ####
          
          ### Interpolação KMt ####
          """
          Para esta etapa do calculo consideramos:
              x -> Deslocamento
              y -> KMt
          """
          KMt=list()
          Calado=list()
          Momento_Trim_MT=list()
          Long_Center_Flut_LCF=list()
          Long_Center_Buoyancy_LCB=list()
          GM_Sem_Correcao_Vertical=list()
          Angulo_Alagamento=list()
          for j in list(range(len(Peso_Final_Navio_Completo))):
              xa = Peso_Final_Navio_Completo[j]
              i=1
              while xa > C_Hidrostaticas.iloc[i-1,2]:
                    x1 = C_Hidrostaticas.iloc[i-1,2]
                    x2 = C_Hidrostaticas.iloc[i,2]
                    y1 = C_Hidrostaticas.iloc[i-1,6] #KMt
                    y2 = C_Hidrostaticas.iloc[i,6]   #KMt  
                    y3 = C_Hidrostaticas.iloc[i-1,0] #Calado
                    y4 = C_Hidrostaticas.iloc[i,0]   #Calado
                    y5 = C_Hidrostaticas.iloc[i-1,8] #MT
                    y6 = C_Hidrostaticas.iloc[i,8]   #MT
                    y7 = C_Hidrostaticas.iloc[i-1,7] #LCF
                    y8 = C_Hidrostaticas.iloc[i,7]   #LCF
                    y9 = C_Hidrostaticas.iloc[i-1,3] #LCB
                    y10 = C_Hidrostaticas.iloc[i,3]  #LCB
                    
                    i=i+1
                    
                              
              ya = y1 + ((xa-x1)/(x2-x1))*(y2-y1) #KMt
              yb = y3 + ((xa-x1)/(x2-x1))*(y4-y3) #Calado
              yc = y5 + ((xa-x1)/(x2-x1))*(y6-y5) #MT
              yd = y7 + ((xa-x1)/(x2-x1))*(y8-y7) #LCF
              ye = y9 + ((xa-x1)/(x2-x1))*(y10-y9) #LCB
              KMt.append(ya)
              Calado.append(yb)
              Momento_Trim_MT.append(yc)
              Long_Center_Flut_LCF.append(yd)
              Long_Center_Buoyancy_LCB.append(y7)
              Angulo_Alagamento.append(math.degrees(math.atan((Pontal_Navio-Calado[j])/(Boca_Navio/2))))
              
              #### Condição de Equilibrio (Encontrar o GM da embarcacao) ####
              #Falta implementar a correção devido ao efeito de superfície livre
              
              GM_Sem_Correcao_Vertical.append(KMt[j]-VCG_Final_Navio_Completo[j])
          
          d={"Calado":Calado,"Deslocamento":Peso_Final_Navio_Completo,"MTI":Momento_Trim_MT,"LCF":Long_Center_Flut_LCF,"LCG":LCG_Final_Navio_Completo,"LCB":Long_Center_Buoyancy_LCB,"KG/VCG":VCG_Final_Navio_Completo,"KMt":KMt,"GM":GM_Sem_Correcao_Vertical,"Angulo Alagamento":Angulo_Alagamento}
          index1={"Condição 1":0,"Condição 2":1,"Condição 3":2,"Condição 4":3,"Condição 5":4,"Condição 6":5}
          Tabela_Hidrostaticas_Interpoladas=pd.DataFrame(d,index1)
          #### Curvas de estabilidade e braços de endireitamento ####
          
          #### Criterios de estabilidade e critérios alternativos ####
          
          #### Estabilidade dinâmica ####
          
          #### Criterios Jogos e Ventos ####
          
          
          
        
        #Para embarcacoes de carga
        elif(Tipo_Embarcacao==2):
            break
        #Para embarcacoes Rebocadores e empurradores
        elif(Tipo_Embarcacao==3):
            break
        #Para embarcacoes de pesca
        elif(Tipo_Embarcacao==4):
            break
        #Para embarcacoes que Transportam Carga no Conves
        elif(Tipo_Embarcacao==5):
            break
        
        
        print("Caculos para os criterios de estabilidade estabelecidos pela NORMAM 02")
        break
    
    
    elif(Escolha_Criterios_Estabilidade==1):
        Tipo_Embarcacao = input("Selecione o tipo de embarcacao desejada para os caculos. Digite o numero correspondente \n 1 - Embarcacoes de Passageiros; \n 2 - Embarcacoes de Carga; \n 3 - Rebocadores e Empurradores; \n 4 - Embarcacoes de Pesca; e \n 5 - Embarcacoes que Transportam Carga no Conves. -> ")
        ### CODNDICIONAIS AINDA FALTAM
        print("Caculos para os criterios de estabilidade estabelecidos pela NORMAM 01")
        break
    else:
        print("\n \n \n \n \n \n Valor digitado invalido, tente novamente.")
        time.sleep(3)
        print("\n \n") 



#Tabela_Hidrostaticas_Interpoladas.to_excel("C:\Users\Usuario\Documents\EFOMM\3º Ano 2021\TCCteste.xlsx") Exportar dados 