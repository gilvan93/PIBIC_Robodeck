import statistics as st
import numpy as np

def load_file(file):
    return [[float(x) for x in (colun.split())] for colun in file]

# DEFINICAO PARA PARA CARREGAR OS VALORES DO ARQUIVO DE DADOS DA ODOMETRIA
# RETORNA DOIS VETORES COM OS DADOS EXATOS E APROXIMADOS DOS VALORES
def load_values(name):

    f = open(str(name), 'r')
    y_medidas = load_file(f)
    y_exact = []
    y_approximate = []

    for linhas in y_medidas:
        y_exact.append(linhas[0])
        y_approximate.append(linhas[1])
    return y_exact, y_approximate


# CALCULA OS ERROS ABSOLUTO DE DOIS CONJUNTO DE DADOS; CALCULO DADO PELA FORMULA:
#
#   ea = |valor_exato - valor_aproximado|
#
def absolute_error(y_exact, y_approximate):
    n = len(y_exact) #tamanho de amostras
    if n == len(y_approximate):
        absolute_values = np.zeros(n)
        for i in range(n):
            absolute_values[i] = abs(y_approximate[i] - y_exact[i])
        return absolute_values
    return []


# CALCULA OS ERROS RELATIVO DE DOIS CONJUNTO DE DADOS; CALCULO DADO PELA FORMULA:
#
#            ea
#   er = -------------
#        valor_exato
#
def relative_error(y_exact, y_approximate):
    n = len(y_exact) #tamanho de amostras
    if n == len(y_approximate):
        relative_values = np.zeros(n)
        for i in range(n):
            relative_values[i] = abs(y_approximate[i] - y_exact[i])/y_exact[i]
        return relative_values
    return []

# CALCULA OS ERROS PERCENTUAL DAS AMOSTRAS, DADA COMO ENTRADA OS ERROS RELATIVOS:
#
#   e% = 100 * er
#

def percent_error(relative_error):
    n = len(relative_error)
    percent_values = np.zeros(n)
    for i in range(n):
        percent_values[i] = 100*relative_error[i]
    return percent_values

# CALCULA A MEDIA DE DETERMINADA AMOSTRA

def sample_mean(array_):
    return st.mean(array_)

# CALCULA O DESVIO PADRAO DE DETERMINADA AMOSTRA

def sample_dp(array_):
    return st.stdev(array_)


if __name__ == '__main__':

    # NOME DO ARQUIVO ONDE ESTAO OS DADOS
    dir_NC = 'DC/'
    name_file = 'C_360.txt'

    # CARREGANDO OS DADOS PARA y_e (exatos) e y_a (aproximados)
    y_e, y_a = load_values(dir_NC+name_file)

    # CRIANDO ARQUIVO PARA SALVAR DADOS DE ERRO DE CADA MEDIDA
    name_saved_file = dir_NC + 'saved_' + name_file
    f = open(name_saved_file, 'w+')

    # ABRINDO ARQUIVO PARA SALVAR DADOS ESTATISTICOS DE TODAS AS MEDIDAS
    # fall = open('dados_odometria_linear.txt', 'w+')

    # ESCREVENDO NOS ARQUIVOS
    f.write ('\t\tDADOS EXATOS:\n')
    f.write (str(y_e))
    f.write ('\nMEDIA: ' + str(sample_mean(y_e)) + '\nDESV PAD: ' + str(sample_dp(y_e)))

    f.write ('\n\n\n\t\tDADOS APROXIMADOS:\n')
    f.write (str(y_a))
    f.write ('\nMEDIA: ' + str(sample_mean(y_a)) + '\nDESV PAD: ' + str(sample_dp(y_a)))

    f.write ('\n\n\n\t\tCALCULO DOS ERROS')
    f.write ('\n\nERRO ABSOLUTO:\n')
    f.write (str(absolute_error(y_e, y_a)))
    f.write ('\nMEDIA: ' + str(sample_mean(absolute_error(y_e, y_a))))
    f.write ('\nDESV PAD: ' + str(sample_dp(absolute_error(y_e, y_a))))

    f.write ('\n\nERRO RELATIVO:\n')
    f.write (str(relative_error(y_e, y_a)))
    f.write ('\nMEDIA: ' + str(sample_mean(relative_error(y_e, y_a))))
    f.write ('\nDESV PAD: ' + str(sample_dp(relative_error(y_e, y_a))))

    f.write ('\n\nERRO PERCENTUAL:\n')
    f.write (str(percent_error(relative_error(y_e, y_a))))
    f.write ('\nMEDIA: ' + str(sample_mean(percent_error(relative_error(y_e, y_a)))))
    f.write ('\nDESV PAD: ' + str(sample_dp(percent_error(relative_error(y_e, y_a)))))

    '''
    # ARQUIVO GERAL COM DADOS DE MEDIA DOS VALORES APROXIMADOS E DOS ERROS
    fall.write('\n\t'+ name_file)
    fall.write('\n'+ str(sample_mean(y_a)))
    fall.write('\n'+ str(sample_dp(y_a)))
    fall.write('\n'+ str(sample_mean(absolute_error(y_e, y_a))))
    fall.write('\n'+ str(sample_dp(absolute_error(y_e, y_a)))+'\n\n')
    '''

    f.close
    # fall.close
