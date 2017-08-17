# coding=utf-8
"""
Bar chart demo with pairs of bars grouped for easy comparison.
"""
import numpy as np
import matplotlib.pyplot as plt

#Dados  corrigidos
n_groups = 12

dados_exatos = (23.0,53.0,89.6,120.6,151.8,180.8,207.6,237.2,262.6,283.2,319.8, 342.4)
desvio_padraoEXATO = (3.67423461417,2.44948974278,5.12835256198,6.38748776907,3.11448230048,2.58843582111,2.30217288664,5.40370243444,3.28633534503,7.85493475466,5.67450438364,4.66904701197)

dados_aproximados = (33.71714588,61.76299401,96.209344684,125.42652662,153.63970812,182.73139004,212.61790552,246.22758924,275.4866045,303.36511922,334.2138018,361.75764972)
desvio_padraoAPROX = (2.63084879386,0.894783966269,5.15968205047,5.38700831805,4.04779544931,1.62289677744,1.87434884996,5.12437193346,3.39082462854,2.08433378116,2.410414249,1.09687968595)



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
