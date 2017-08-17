# coding=utf-8
"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt

#Dados não corrigidos
n_groups = 12

dados_exatos = (30.1,55.4,80.8,101.6,121.2,139.8,158.3, 179.7,202.4,223.5,243.4, 264.0)
desvio_padraoEXATO = (0.74161984871,5.02991053598,4.38178046004,3.0495901364,4.08656334834,2.58843582111,2.72946881279,1.48323969742,3.64691650576,4.8733971724,3.18982758155,1.41421356237)

dados_aproximados = (32.86267958,61.07669096,92.95370364,122.61354878,155.41089518,182.64440598,213.55925164,243.59559686,272.83710854,302.41328698,332.44963222,363.23897782)
desvio_padraoAPROX = (1.75430919004,0.533272669922,2.51261422403, 2.40950654304,2.84112820061,2.11971692427,1.06654533494,1.65757226162,2.6523795613,2.53342298244,2.17674160409, 1.55544696857)



fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, dados_exatos, bar_width,
                 alpha=opacity,
                 color='b',
                 yerr=desvio_padraoEXATO,
                 error_kw=error_config,
                 label='Dado Exatos')

rects2 = plt.bar(index + bar_width, dados_aproximados, bar_width,
                 alpha=opacity,
                 color='r',
                 yerr=desvio_padraoAPROX,
                 error_kw=error_config,
                 label='Dados Aproximados')

plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.xticks(index + bar_width / 2, ('30', '60', '90', '120', '150','180','210','240', '270','300', '330', '360'))
plt.legend()

plt.tight_layout()
plt.show()
