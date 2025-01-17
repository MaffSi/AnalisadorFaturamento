import json


def analise_vendas(json_file: str) -> dict:
  #Declarando variáveis
  dias_com_vendas_maiores = 0
  dia_melhor_faturamento = {'dia' : 'null', 'valor' : 0}
  dia_pior_faturamento = {'dia' : 'null', 'valor' : 0}
  soma_media = 0
  qt_dias_uteis = 0
  #Abrindo arquivo
  with open(json_file, 'r') as f:
    data = json.load(f)

  
  #Iterando os dias de venda, e verificando se o valor é maior que 0
  for vendas in data:
    if vendas['valor'] > 0:
      #Em seguida, adicioanndo o valor a soma_media, e incrementando a qt_dias_uteis. Para o cálculo da média.
      soma_media += float(vendas['valor'])
      qt_dias_uteis += 1
      #Verificando se o valor da venda atual, é menor que o valor do dia_pior_faturamento, e se for, atualizando o dia de pior faturamento com os dados do dia atual.
      if dia_pior_faturamento['valor'] > vendas['valor'] or dia_pior_faturamento['valor'] == 0:
        dia_pior_faturamento.update({'dia': vendas['dia'], 'valor': vendas['valor']})

      #Verificando se o valor da venda atual, é maior que o valor do dia de melhor faturamento, e se for, atualizando o dia de melhor faturamento com os dados atuais.
      if dia_melhor_faturamento['valor'] < vendas['valor']:
        dia_melhor_faturamento.update({'dia': vendas['dia'], 'valor': vendas['valor']})

  media = soma_media / qt_dias_uteis

  
  #Iterando sobre as vendas, e verificando se o valor é maior que a média, e se for, incrementar um no dias_com_vendas_maiores.
  for vendas in data:
    if vendas['valor'] > media:
      dias_com_vendas_maiores += 1
  
  #Retornado um dicionário com os dados solicitados.
  return {'MediaVenda': media, 
          'DiasMaiorMedia' :dias_com_vendas_maiores, 
          'MelhorFat': dia_melhor_faturamento,
          'PiorFat': dia_pior_faturamento}
  