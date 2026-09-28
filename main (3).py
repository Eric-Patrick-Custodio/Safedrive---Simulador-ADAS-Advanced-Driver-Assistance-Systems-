# item A escolhe sempre o sensor que ta entre o maior e o menor (mediana)
def mediana(sensor1, sensor2, sensor3):
    if (sensor1>=sensor2 and sensor1<=sensor3):
        return sensor1
    elif (sensor1>=sensor3 and sensor1<=sensor2):
       return sensor1
    elif (sensor2>=sensor1 and sensor2<=sensor3):
        return sensor2
    elif (sensor2>=sensor3 and sensor2<=sensor1):
        return sensor2
    elif (sensor3>=sensor1 and sensor3<=sensor2):
        return sensor3
    elif (sensor3>=sensor2 and sensor3<=sensor1):
      return sensor3

# item B modo de condução
def modofun(modo):
  if modo == 1:
    tempo = 1.0
  elif modo == 2:
    tempo = 1.5
  else:
    tempo = 2.0
  return tempo

# conta da distancia segura
def distancia(vel,tempo,atrito):
  atrito = 2*atrito*9.81
  vel = vel/3.6
  distancia_segura = (vel*tempo)+vel**2/atrito
  return distancia_segura

#item C analise de colisão frontal
def colisaofun(velAtual, velFrente, distancia_validada, distancia_segura):
  velRelativa = velAtual-velFrente
  if(velRelativa<=0):
    status = "SEGURO"
    aeb = "NÃO ACIONADO"
  elif distancia_validada>= distancia_segura:
    status = "SEGURO"
    aeb = "NÃO ACIONADO"
  elif distancia_validada<distancia_segura and distancia_validada >= (distancia_segura/2):
    status = "ATENÇÃO"
    aeb = "NÃO ACIONADO"
  elif distancia_validada<(distancia_segura/2):
    status = "RISCO DE COLISÃO"
    aeb = "ACIONADO"
  return status, aeb

#item D ajuste das faixas
def faixas(dis,velAtual):
  base = 0.50
  if velAtual>80:
    base+=0.01*(velAtual-80)

  if dis<base:
    status = "PERIGO DE INVASÃO"
  elif dis<(base+0.20):
    status = "ATENÇÃO"
  else:
    status = "NORMAL"
  return status, base

  #item E decisão geral
def geralfun(fxdireita,fxesquerda,colisao):
  if fxdireita == "PERIGO DE INVASÃO" or fxesquerda == "PERIGO DE INVASÃO" or colisao == "RISCO DE COLISÃO":
    geral = "INTERVENÇÃO CRÍTICA EXIGIDA"
  elif fxdireita == "ATENÇÃO" or fxesquerda == "ATENÇÃO" or colisao == "ATENÇÃO":
    geral = "ATENÇÃO"
  else:
    geral = "NORMAL"
  return geral


def chama():
  #declarando as variaveis
  velAtual = float(input())
  velFrente = float(input())
  sensor1 = float(input())
  sensor2 = float(input())
  sensor3 = float(input())
  atrito = float(input())
  modo = int(input())
  esquerda = float(input())
  direita = float(input())

  #chamando as funções
  distancia_validada = mediana(sensor1,sensor2,sensor3)
  modo = modofun(modo)
  distancia_segura = distancia(velAtual,modo,atrito)
  colisao, aeb = colisaofun(velAtual,velFrente,distancia_validada,distancia_segura)
  esquerda, margem = faixas(esquerda,velAtual)
  direita, margem = faixas(direita,velAtual)
  geral = geralfun(esquerda,direita,colisao)

#saida
  print(f"Distância validada: {distancia_validada:.2f} m")
  print(f"Distância segura: {distancia_segura:.2f} m")
  print(f"Status frontal: {colisao}")
  print(f"AEB: {aeb}")
  print(f"Margem lateral exigida: {margem:.2f} m")
  print(f"Faixa esquerda: {esquerda}")
  print(f"Faixa direita: {direita}")
  print(f"STATUS GERAL: {geral}")

chama()