
import numpy as np
import matplotlib.pyplot as plt
from framework import file_m2k

caminho_dados = '../data/<arquivo_do_caminho>'


print("Carregando os dados...")
data = file_m2k.read(caminho_dados, freq_transd=5,
                    bw_transd=0.5, tp_transd='gaussian', sel_shots=0)

emissor = 126
receptor = 124

axis_scan = data.ascan_data[:, emissor, receptor]

# A-scan
plt.figure(figsize=(10, 4))

# Plota o sinal da onda no domínio do tempo
plt.plot(axis_scan, color='blue', label=f'emissor: {emissor + 1} e receptor: {receptor + 1}')

# Config
plt.title(f'A-scan: Ensaio de Through-transmission | Tx: {emissor + 1} e Rx: {receptor + 1}')
plt.xlabel('Amostras (Tempo de Voo)')
plt.ylabel('Amplitude (Atenuação)')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--') # Linha de referência zero
plt.grid(True, alpha=0.6)
plt.legend()

plt.show()
