
import pandas as pd
import numpy as np

def alocacao_ativos(df, capital, seed = 0, melhores_pesos = []):
  df = df.copy()

  if seed != 0:
    np.random.seed(seed)

  if len(melhores_pesos) > 0:
    pesos = melhores_pesos
  else:
    pesos = np.random.random(len(df.columns) - 1)
    pesos = pesos / pesos.sum()

  colunas = df.columns[1:]

  for i in colunas:
    df[i] = (df[i] / df[i][0])

  for i, k in enumerate(df.columns[1:]):
    df[k] = df[k] * pesos[i] * capital

  df['soma valor'] = df.iloc[:, 1:].sum(axis = 1)

  datas = df['Date']

  df.drop(labels = ['Date'], axis = 1, inplace = True)
  df['taxa retorno'] = 0.0

  for i in range(1, len(df)):
    df['taxa retorno'][i] = ((df['soma valor'][i] / df['soma valor'][i - 1]) - 1) * 100

  acoes_pesos = pd.DataFrame(data = {'Ações': colunas, 'Pesos': pesos * 100})
  return df, datas, acoes_pesos, df.loc[len(df) - 1]['soma valor']


def visualiza_carteira(resultado):
  df = pd.read_csv('carteira.csv')
  acoes = df.columns[1:]
  for i in range(len(resultado)):
    print(f'{acoes[i]} tem {resultado[i] * 100:.2f}% da carteira')


def alocacao_markowitz(df, capital, i, n):
  df = df.copy()
  df_original = df.copy()

  ls_txe = []
  ls_vole = []
  ls_sr = []

  melhor_sr = 1 - sys.maxsize
  melhores_p = np.empty
  melhor_vol = 0
  melhor_tx = 0

  for _ in range(n):
    pesos = np.random.random(len(df.columns)-1)
    pesos = pesos / pesos.sum()

    for w in df.columns[1:]:
      df[w] = df[w] / df[w][0]

    for w, k in enumerate(df.columns[1:]):
      df[k] = df[k] * pesos[w] * capital

    df.drop(labels = ['Date'], axis = 1, inplace=True)

    retorno_carteira = np.log(df / df.shift(1))
    matriz_cov = retorno_carteira.cov()

    df['soma valor'] = df.sum(axis = 1)
    df['taxa retorno'] = 0.0

    for w in range(1, len(df)):
      df['taxa retorno'][w] = np.log(df['soma valor'][w] / df['soma valor'][w - 1])

    retorno_esperado = np.sum(df['taxa retorno'].mean() * pesos) * 246
    vol_esperada = np.sqrt(np.dot(pesos, np.dot(matriz_cov * 246, pesos)))
    sharpe_ratio = (retorno_esperado - i) / vol_esperada

    if sharpe_ratio > melhor_sr:
      melhor_sr = sharpe_ratio
      melhores_p = pesos
      melhor_vol = vol_esperada
      melhor_tx = retorno_esperado

    ls_txe.append(retorno_esperado)
    ls_vole.append(vol_esperada)
    ls_sr.append(sharpe_ratio)

    df = df_original.copy()

  return melhor_sr, melhores_p, ls_txe, ls_vole, ls_sr, melhor_vol, melhor_tx

