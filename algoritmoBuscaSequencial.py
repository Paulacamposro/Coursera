''' Algoritmo de busca'''

def busca_sequencial(seq, x):
    '''(lis, float) -> bool'''
    for i in range(len(seq)):
        if seq[i] == x:
            return True
    return False
