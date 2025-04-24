# Dashboard de Valuation DCF

"""Created on Wed Apr 16 15:29:16 2025
@author: Mary V
"""
# Descrição: Calcula o valor de uma empresa utilizando o metodo DCF
# Ferramentas: Python, numpy, pandas, matplotlib


# Importar bibliotecas

import numpy as np  #Calculos matematicos
import pandas as pd  # Cria tabelas
import matplotlib.pyplot as plt  # Cria graficos

# Definir as entradas do modelo DCF

fluxos_caixa = [10,12,14,16,18] # Fluxos de caixa para 5 anos (em R$ milhões)
taxa_desconto = 0.10 # 10% (WACC)
crescimento_perpetuo = 0.02 # 2% (crescimento de longo prazo)

# Calcular o PV (Present Value - Valor Presente) dos fluxo de caixa

valor_presente = []
for t, fc in enumerate(fluxos_caixa, 1):
    vp = fc / (1 + taxa_desconto) ** t  # Fórmula: VP = FC/ (1 + r)^t
    valor_presente.append(vp)
    
# Calcular o valor terminal

ultimo_fluxo = fluxos_caixa[-1] #Último valor fluxo de caixa (18)
valor_terminal = (ultimo_fluxo * (1 + crescimento_perpetuo)) / (taxa_desconto - crescimento_perpetuo)
valor_terminal_descontado = valor_terminal / (1 + taxa_desconto) ** len(fluxos_caixa)

# Somar tudo para obter o valor da empresa
valor_empresa = sum(valor_presente) + valor_terminal_descontado

#Tabela com os resultados
dados = {
    "Ano": list(range(1, len(fluxos_caixa) + 1)) + ["Terminal"],
    "Fluxo de Caixa (R$ M)": fluxos_caixa + [valor_terminal],
    "Valor Presente (R$ M)": valor_presente + [valor_terminal_descontado]
    }
df = pd.DataFrame(dados)

#Exibir a tabela
print("\n=== Resultados do DCF ===")
print(df.round(2))

# Exibir o valor final

print(f"Valor da Empresa: R$ {valor_empresa:.2f} milhões")

#Gráfico de barras
plt.figure(figsize=(10,6))  #Tamanho do grafico
plt.bar(dados["Ano"][:-1], dados["Fluxo de Caixa (R$ M)"][:-1], label="Fluxos de Caixa", alpha=0.6, color="gray")
plt.bar("Terminal", dados["Fluxo de Caixa (R$ M)"][-1], label="Valor Terminal", alpha=0.3, color="purple")
plt.title("Valuation - Fluxos de Caixa e Valor Terminal")
plt.xlabel("Ano")
plt.ylabel("R$ Milhões")
plt.legend()  #Mostra a Legenda
plt.grid(True) #Adiciona grade
plt.show()

#Exportar tabela em CVS
df.to_csv("dcf_resultados.csv", index=False)
print("Resultados Salvos com Sucesso!")

