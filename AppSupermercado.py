
# -*- coding: utf-8 -*-
"""
IFPB-CAMPINA GRANDE-PB
ALUNOS:ADRIANO
       ANDRE LUIZ
 
PROTÓTIPO DE APLICATIVO DE COMPRAS EM SUPERMERCADOS

"""

#GPS - GOOGLE MAPS
#GEOLOCATION = FERRAMENTA DO GOOGLE MAPS
import googlemaps


#CHAVE DE ACESSO A FERRAMENTA DO GOOGLE MAPS OBTIDA ATRAVÉS DE CADASTRO FEITO NO GOOGLE
#google_maps = GoogleMaps(api_key='AIzaSyB3f3Gyvor4KQAtBTmHY69DNy42Q3gA4xk')
gmaps = googlemaps.Client(key='AIzaSyB3f3Gyvor4KQAtBTmHY69DNy42Q3gA4xk')

# LISTA DOS TRÊS SUPERMERCADOS QUE O CLIENTE VAI EFETUAR AS COMPRAS
supermercado1=['REDE COMPRAS',' AV.MAL.FLORIANO PEIXOTO,912,CENTRO,CAMPINA GRANDE-PB ',5.0]
supermercado2=['IDEAL','R. VIGOLVINO VANDERLEI, 290 - CONCEIÇÃO, CAMPINA GRANDE - PB',3.0]
supermercado3=['HIPER BOMPREÇO',' AV.PROF.ALMEIDA BARRETO,85,CENTRO,CAMPINA GRANDE-PB ',1.0]
#CRIA UMA LISTA VAZIA PARA LISTA_REDE, LISTA_HIPER E LISTA_IDEAL 
LISTA_REDE =[]
LISTA_HIPER= []
LISTA_IDEAL= []

# LISTA DE LISTA DOS SUPERMERCADOS
supermercado=[supermercado1,supermercado2,supermercado3]

# BANCO DE DADOS DOS SUPERMERCADOS
produto0=['ARROZ','Kg',3.28,'REDE COMPRAS']
produto1=['MACARRÃO','Kg',2.55,'REDE COMPRAS']
produto2=['FEIJÃO','Kg',5.65,'REDE COMPRAS']
produto3=['QUEIJO','Kg',18.15,'REDE COMPRAS']
produto4=['PÃO','Kg',2.15,'REDE COMPRAS']
produto5=['MORTADELA','Kg',3.65,'REDE COMPRAS']
produto6=['BATATA DOCE','Kg',1.25,'REDE COMPRAS']
produto7=['MAÇÃ','Kg',1.85,'REDE COMPRAS']
produto8=['LARANJA','Kg',7.25,'REDE COMPRAS']
produto9=['CAFÉ','Kg',2.39,'REDE COMPRAS']
produto10=['PRESUNTO','Kg',8.28,'REDE COMPRAS']
produto11=['AÇUCAR','Kg',4.55,'REDE COMPRAS']
produto12=['LEITE','Lt',4.65,'REDE COMPRAS']
produto13=['CARNE','Kg',19.15,'REDE COMPRAS']
produto14=['CUZCUZ','Kg',1.15,'REDE COMPRAS']
produto15=['COCA-COLA','Lt',6.65,'REDE COMPRAS']
produto16=['DETERGENTE','Lt',2.25,'REDE COMPRAS']
produto17=['UVA','Kg',1.85,'REDE COMPRAS']
produto18=['FAVA','Kg',15.25,'REDE COMPRAS']
produto19=['QUEIJO DO REINO','Kg',50.39,'REDE COMPRAS']
produto20=['ARROZ','Kg',4.28,'IDEAL']
produto21=['MACARRÃO','Kg',3.55,'IDEAL']
produto22=['FEIJÃO','Kg',6.65,'IDEAL']
produto23=['QUEIJO','Kg',19.15,'IDEAL']
produto24=['PÃO','Kg',3.15,'IDEAL']
produto25=['MORTADELA','Kg',4.65,'IDEAL']
produto26=['BATATA DOCE','Kg',1.25,'IDEAL']
produto27=['MAÇÃ','Kg',2.85,'IDEAL']
produto28=['LARANJA','Kg',2.25,'IDEAL']
produto29=['CAFÉ','Kg',4.39,'IDEAL']
produto30=['PRESUNTO','Kg',9.28,'IDEAL']
produto31=['AÇUCAR','Kg',5.55,'IDEAL']
produto32=['LEITE','Lt',6.65,'IDEAL']
produto33=['CARNE','Kg',18.15,'IDEAL']
produto34=['CUZCUZ','Kg',3.15,'IDEAL']
produto35=['COCA-COLA','Lt',7.65,'IDEAL']
produto36=['DETERGENTE','Lt',2.25,'IDEAL']
produto37=['UVA','Kg',2.85,'IDEAL']
produto38=['FAVA','Kg',16.25,'IDEAL']
produto39=['QUEIJO DO REINO','Kg',52.39,'IDEAL']
produto40=['ARROZ','Kg',2.28,'HIPER BOMPREÇO']
produto41=['MACARRÃO','Kg',4.55,'HIPER BOMPREÇO']
produto42=['FEIJÃO','Kg',7.65,'HIPER BOMPREÇO']
produto43=['QUEIJO','Kg',16.15,'HIPER BOMPREÇO']
produto44=['PÃO','Kg',4.15,'HIPER BOMPREÇO']
produto45=['MORTADELA','Kg',1.65,'HIPER BOMPREÇO']
produto46=['BATATA DOCE','Kg',5.25,'HIPER BOMPREÇO']
produto47=['MAÇÃ','Kg',1.85,'HIPER BOMPREÇO']
produto48=['LARANJA','Kg',4.25,'HIPER BOMPREÇO']
produto49=['CAFÉ','Kg',6.39,'HIPER BOMPREÇO']
produto50=['PRESUNTO','Kg',1.28,'REDE COMPRAS']
produto51=['AÇUCAR','Kg',5.55,'HIPER BOMPREÇO']
produto52=['LEITE','Lt',7.65,'HIPER BOMPREÇO']
produto53=['CARNE','Kg',20.15,'HIPER BOMPREÇO']
produto54=['CUZCUZ','Kg',4.15,'HIPER BOMPREÇO']
produto55=['COCA-COLA','Lt',2.65,'HIPER BOMPREÇO']
produto56=['DETERGENTE','Lt',5.25,'HIPER BOMPREÇO']
produto57=['UVA','Kg',5.85,'HIPER BOMPREÇO']
produto58=['FAVA','Kg',16.25,'HIPER BOMPREÇO']
produto59=['QUEIJO DO REINO','Kg',48.39,'HIPER BOMPREÇO']

# lISTA DE LISTA DOS PRODUTOS
produto=[produto0,produto1,produto2,produto3,produto4,produto5,produto6,produto7,
        produto8,produto9,produto10,produto11,produto12,produto13,produto14,produto15,
        produto16,produto17,produto18,produto19,produto20,produto21,produto22,produto23,
        produto24,produto25,produto26,produto27,produto28,produto29,produto30,produto31,produto32,produto33,produto34,produto35,
        produto36,produto37,produto38,produto39,produto40,produto41,produto42,produto43,
        produto44,produto45,produto46,produto47,produto48,produto49,produto50,produto51,produto52,produto53,
        produto54,produto55,produto56,produto57,produto58,produto59]
#FUNÇÃO QUE FAZ A PESQUISA NA LISTA
def search (lista, valor):
  return [(lista.index(x), x.index(valor)) for x in lista if valor in x]

# (EXCL)= EXISTE CLIENTE
EXCL='SIM' 
#ENQUANTO HOUVER CLIENTE CONFIRMA COM (SIM) 
while (EXCL=='SIM'):

#(CL)=CLIENTE                                      
  
  CL=input('DIGITE O NOME DO CLIENTE:') #IMPRIME DIGITE O NOME DO CLIENTE
  
  #(DESTINO)= DESTINO DE ENTREGA DOS PRODUTOS DE ACORDO COM O ENDEREÇO DO CLIENTE
  destino=input('DIGITE O ENDEREÇO DO CLIENTE:')
  
   
  
 #(NPROD)=NÚMERO DE PRODUTOS
 #(PROD)=PRODUTOS
 #(QUANT)=QUANTIDADE
 #(SOMA=0)=INICIALIZAÇÃO DO VETOR
  NPROD=int(input('DIGITE O NUMERO DE PRODUTOS PEDIDO:'))
  P0 = [0]*2     #ELE CRIA O INICIO DA LISTA E FORMA UMA LISTA COM DOIS ELEMENTOS
  P1 = [P0]*NPROD # P0 X NPROD EM LISTA DE LISTA ELE PEGA DUAS COLUNAS E O NUMERO DE PRODUTOS, PREENCHE DENTRO DO FOR ABAIXO
  PROD=[] #LISTA VAZIA 
  QUANT=[] #LISTA VAZIA
  
  SOMA=0 # INICIALIZAÇÃO DA SOMA
 #(FOR)= LAÇO DO PROCESSAMENTO DO PRODUTO 
  for i in range (0,NPROD ):
  #IMPRIME
   #aux.upper= TRANSFORMA OS CARACTERES EM MAIUSCULO OU MENÚSCULO 
    print ('=== PRODUTO NUMERO ',i+1,'===')  
    aux1 = input('ENTRE COM O NOME DO PRODUTO =')
    aux1=aux1.upper()
    aux2 = input('ENTRE COM A QUANTIDADE DE PRODUTO =')
    P1[i] = [aux1,aux2]
    # [i] VARIA DE 0 A NPROD, CRIA UMA MATRIZ DE DUAS COLUNAS E A LOCALIZAÇÃO DE PRODUTO E QUANTIDADE
   
    
    
    
    #(LEN)COMPRIMENTO DO VETOR PROD
 
  print('==================================================')
  print('LISTA DOS PRODUTOS A SEREM ENTREGUE')
  print('NOME DO CLIENTE=',CL)
  print('ENDEREÇO DO CLIENTE=',destino)
  print('==================================================')
  print('PRODUTO QUANTIDADE')
  print('==================================================')
  for i in range (0,NPROD): #FAZ O LOOP DE RELATÓRIO DE PRODUTOS E QUANTIDADES
      print(P1[i][0],P1[i][1])  #IMPRIMI O VETOR P1 QUE FOI CRIADO ANTES E O FOR VARIA O [I] ENTRE 0 E NPROD
  print('==================================================')  
  print() 
  print()   
  
  #FAZ UMA VARREDURA NA LISTA 
  for J in range (0,NPROD ): #  É O PRIMEIRO PRODUTO DA LISTA E FAZ A PESQUISA NO BANCO DE DADOS
     
   
    
    #PROCURA O PRODUTO NA LISTA
    Y=search(produto, P1[J][0]) # J É A LINHA E 0 É A PRIMEIRA COLUNA
    
    #QUANTIDADE DE PRODUTOS QUE CONTÉM NO SUPERMERCADO
    tamanho=len(Y) #PEGA TODOS OS VALORES DOS SUPERMERCADOS, E DOS PRODUTOS SOLICITADOS E COLOCA EM NO MÁXIMO 3 LINHAS
   

    
    L4=[]      #CRIA UMA LISTA VAZIA
    for I in range(0,tamanho): # CHAMA A LINHA DA LISTA DE LISTA QUE ENCONTROU
      L4.append(produto [Y[I][0]]) # COPIA DA LISTA PRODUTO E ACRESECENTA EM L4
      #VETOR Y QUE ARMAZENOU O [I] LINHA E A COLUNA 0
     
    
   #(MIN)ENCONTAR O PRODUTO QUE ESTEJA COM MENOR VALOR ENTRE OS SUPERMERCADOS 
    menor=min(L4)  #MENOR VALOR DA LISTA L4 (MIN) MENOR VALOR
    menor.append( P1[J][1]) #COLOCA NA LINHA E NA SEGUNDA COLUNA O VALOR L4 OU MENOR
    #ATUALIZAÇÃO DO MENOR VALOR
    SUP=menor[3] #SUP=MENOR[3] = NA LISTA DOS PRODUTOS ELE VAI ENCONTRAR O SUPERMERCADO COM O MENOR VALOR NA LINHA DE CADA PRODUTO 
    
    if (SUP == 'REDE COMPRAS'):#ATUALIZAÇÃO DA LISTA DA LISTA DO REDE COMPRAS
        LISTA_REDE.append(menor)
        
    if (SUP == 'HIPER BOMPREÇO'):#ATUALIZAÇÃO DA LISTA DO HIPER BOMPREÇO
        LISTA_HIPER.append(menor)
        
    if (SUP == 'IDEAL'):#ATUALIZAÇÃO DA LISTA DO IDEAL
        LISTA_IDEAL.append(menor)
        
  print('==================================================')       
  print('LISTA DO REDE COMPRAS')
  print('--------------------------------------------------') 
  print('PRODUTO  PREÇO UNITARIO QUANTIDADE')
  print('--------------------------------------------------') #ORGANIZAR ESPAÇOS 
  PARCIAL1 = 0
  for I in LISTA_REDE:  #LOOP PARA IMPRIMIR CADA PRODUTO ESCOLHIDO
      VALOR_UNITARIO = float(I[2])#CONVERTE DE STRING PARA NÚMERO
      QUANTIDADE =  float(I[4])   #CONVERTE DE STRING PARA NÚMERO
      PARCIAL1 = PARCIAL1 + VALOR_UNITARIO * QUANTIDADE #VALOR PARCIAL DA COMPRA
      print(I [0], I[2], I[4])#POSIÇÃO DOS ITENS DO VETOR (I)  
  print('--------------------------------------------------') 
  origem1 = supermercado1 [1] 

  itens = gmaps.distance_matrix(origem1, destino) ['rows'][0]['elements'][0]             #FERRAMENTA DO GOOGLEMAPS PARA OBTER A DISTANCIA EM KILOMETROS ENTRE SUPERMERCADO E CLIENTE
  print(itens['distance']['value'])
  DIST=itens['distance']['value']
  
  TAXA1 = 1.5 * float(DIST)/1000   #FLOAT PEGA O VALOR DA DISTANCIA, TRANSFORMA PARA UM VALOR NÚMERICO E MULTIPLICA POR 1.5 (TAXA DE SERVIÇO)
  PARCIAL1 = PARCIAL1   
  print('VALOR PARCIAL', PARCIAL1)
  print('DISTÂNCIA ENTRE SUPERMERCADO E ENDEREÇO DO CLIENTE EM km =', DIST/1000)
  
  
  print('==================================================')
  
  print('==================================================')       
  print('LISTA DO IDEAL')
  print('--------------------------------------------------') 
  print('PRODUTO  PREÇO UNITARIO QUANTIDADE')
  print('--------------------------------------------------') 
  PARCIAL2 = 0
  
  
  for I in LISTA_IDEAL: #LOOP PARA IMPRIMIR CADA PRODUTO ESCOLHIDO
      VALOR_UNITARIO = float(I[2]) #CONVERTE DE STRING PARA NÚMERO
      QUANTIDADE =  float(I[4])   #CONVERTE DE STRING PARA NÚMERO
      PARCIAL2 = PARCIAL2 + VALOR_UNITARIO * QUANTIDADE #VALOR PARCIAL DA COMPRA
      print(I [0], I[2], I[4]) #POSIÇÃO DOS ITENS DO VETOR (I)
  print('--------------------------------------------------') 
  origem2 = supermercado2 [1]
 
  itens = gmaps.distance_matrix(origem2, destino) ['rows'][0]['elements'][0] #FERRAMENTA DO GOOGLEMAPS PARA OBTER A DISTANCIA EM KILOMETROS ENTRE SUPERMERCADO E CLIENTE
  DIST=itens['distance']['value']
  TAXA2 = 1.5 * float(DIST)/1000  #FLOAT PEGA O VALOR DA DISTANCIA, TRANSFORMA PARA UM VALOR NÚMERICO E MULTIPLICA POR 1.5 (TAXA DE SERVIÇO)
  PARCIAL2 = PARCIAL2 
  print('VALOR PARCIAL', PARCIAL2)
  print('DISTÂNCIA ENTRE SUPERMERCADO E ENDEREÇO DO CLIENTE EM Km =', DIST/1000)
  print('==================================================')
  
  print('==================================================')       
  print('LISTA DO HIPER BOMPREÇO')
  print('--------------------------------------------------') 
  print('PRODUTO  PREÇO UNITARIO QUANTIDADE')
  print('--------------------------------------------------') 
  PARCIAL3 = 0
  for I in LISTA_HIPER: #LOOP PARA IMPRIMIR CADA PRODUTO ESCOLHIDO
      VALOR_UNITARIO = float(I[2]) #CONVERTE DE STRING PARA NÚMERO
      QUANTIDADE =  float(I[4])   #CONVERTE DE STRING PARA NÚMERO
      PARCIAL3= PARCIAL3 + VALOR_UNITARIO * QUANTIDADE #VALOR PARCIAL DA COMPRA
      print(I [0], I[2], I[4])  #POSIÇÃO DOS ITENS DO VETOR (I)
  print('--------------------------------------------------') 
  origem3 = supermercado3 [1]

  itens = gmaps.distance_matrix(origem3, destino) ['rows'][0]['elements'][0] #FERRAMENTA DO GOOGLEMAPS PARA OBTER A DISTANCIA EM KILOMETROS ENTRE SUPERMERCADO E CLIENTE
  DIST=itens['distance']['value']
  TAXA3 = 1.5 * float(DIST)/1000  #FLOAT PEGA O VALOR DA DISTÂNCIA, TRANSFORMA PARA UM VALOR NÚMERICO E MULTIPLICA POR 1.5 (TAXA DE SERVIÇO)
  PARCIAL3 = PARCIAL3  
  print('VALOR PARCIAL', PARCIAL3)
  print('DISTÂNCIA ENTRE SUPERMERCADO E ENDEREÇO DO CLIENTE EM Km =', DIST/1000)
  print('==================================================')
  TAXA = (TAXA1*len(LISTA_REDE) + TAXA2*len(LISTA_IDEAL) + 
          TAXA3* len(LISTA_HIPER)) /(len(LISTA_REDE) + len(LISTA_IDEAL) 
          + len(LISTA_HIPER))#ELE PEGA A QUANTIDADE DE ITENS  DE CADA SUPERMERCADO, MULTIPLICA QUANTIDADE PELA TAXA  E DEPOIS DIVIDE PELO NÚMERO TOTAL DE PRODUTOS PARA OBTER O VALOR
  TOTAL = PARCIAL1 + PARCIAL2 + PARCIAL3 + TAXA # FAZ A SOMA DAS 3 PARCIAIS E SOMA COM A TAXA DE SERVIÇO PARA DAR O VALOR TOTAL.
  print('VALOR TOTAL = R$ ', TOTAL)#IMPRIME O VALOR TOTAL
  EXCL=input(  'EXISTE MAIS ALGUM CLIENTE (SIM OU NAO)?'   ) # PERGUNTA SE EXISTE MAIS ALGUM CLIENTE, SE SIM ELE FAZ UM NOVO PROGRAMA, SE NÃO ELE ENCERRA.
