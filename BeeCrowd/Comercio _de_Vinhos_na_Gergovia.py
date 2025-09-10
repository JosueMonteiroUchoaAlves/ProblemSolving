habitantes = input()
comercios = list(map(int, input().split()))

def organizarComercio(c):
    #não sera mais 0-indexed para facilitar o calculo
    negativos =[]
    positivos_e_zeros = []
    
    for index,item in enumerate(c):
        if item < 0:
            negativos.append([index, item])
            continue
        positivos_e_zeros.append([index, item])
    
    return negativos, positivos_e_zeros

custoTotal = 0
while habitantes != '0':
    comerciosOrganizados = organizarComercio(comercios)
    #print(comerciosOrganizados)
    vendedores = comerciosOrganizados[0]
    compradores = comerciosOrganizados[1]
    for vendedor in vendedores:
        indexDoVendedor, quantidadeParaVenda = vendedor[0],-vendedor[1]
        while quantidadeParaVenda:
            if not compradores:
                break
            indexDoComprador, quantidadeParaCompra = compradores[0][0], compradores[0][1]
            if quantidadeParaVenda >= quantidadeParaCompra:
                quantidadeParaVenda -= quantidadeParaCompra
                custoTotal += quantidadeParaCompra* (abs(indexDoComprador-indexDoVendedor))
                compradores.pop(0) # removeu aquele comprador
                continue
            elif quantidadeParaVenda < quantidadeParaCompra:
                compradores[0][1] -= quantidadeParaVenda
                custoTotal += quantidadeParaVenda * (abs(indexDoComprador-indexDoVendedor)) # calculo com so o que foi possivel vender
                quantidadeParaVenda = 0

                # nao removeu ainda removeu aquele comprador
    print(custoTotal)
    custoTotal = 0
    try:
        habitantes = input()
        comercios = list(map(int, input().split()))
    except:
        break
