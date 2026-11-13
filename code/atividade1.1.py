# Importações das bibliotecas padrão
import matplotlib.pyplot as plt
import numpy as np


caminho_dados = 'data/test2_125e125_fluidoagua_2_25_transdutor3_5.m2k'


data = file_m2k.read(caminho_dados, freq_transd=5, bw_transd=0.5, tp_transd='gaussian', sel_shots=0)




axis_scan = data.ascan_data[:, 124, 126]


plt.show()

