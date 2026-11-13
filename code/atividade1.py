import numpy as np
import matplotlib.pyplot as plt
from framework import file_m2k
caminho_dados = 'data/test2_125e125_fluidoagua_2_25_transdutor3_5.m2k'




# AQUI FALTA UM PASSO NO SEU CÓDIGO ORIGINAL:
# Você precisa usar o script ou biblioteca da sua disciplina para ler a pasta.
# Exemplo hipotético (substitua pelo comando que seu professor passou):
# data = funcao_que_le_m2k(caminho_dados)


# Só depois de carregar a variável "data" você pode fazer o recorte:
axis_scan = data.ascan_data[:, 124, 126]




-----------




import numpy as np
import matplotlib.pyplot as plt
from framework import file_m2k
caminho_dados = 'data/test2_125e125_fluidoagua_2_25_transdutor3_5.m2k'


print("Carregando os dados...")
data = file_m2k.read(caminho_dados, freq_transd=5,
                    bw_transd=0.5, tp_transd='gaussian', sel_shots=0)


# 3. Seleciona o sinal A-scan
# O formato exato depende de como o equipamento salvou (emissor/receptor)
# Aqui estamos pegando todas as amostras de tempo (:) do primeiro canal configurado
# Se der erro de índice, pode ser necessário ajustar dependendo da matriz do equipamento
sinal_ascan = data.ascan_data[:, 0]


# 4. Plota o sinal no domínio do tempo
plt.figure(figsize=(10, 4))
plt.plot(sinal_ascan, color='blue')


# Configurações do gráfico
plt.title('A-scan: Sinal Recebido (Through-transmission)')
plt.xlabel('Amostras (Tempo)')
plt.ylabel('Amplitude (Tensão)')
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5) # Linha zero para referência


print("Gerando gráfico...")
plt.show()

