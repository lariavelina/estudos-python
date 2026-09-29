prev_usuarios = int(input("Digite a quantidade prevista de usuarios: "))
quant_serv_dispo = int(input("Digite a quantidade de servidores disponiveis: "))
cap_max_servidor = int(input("Digite a capacidade maxima de usuarios por servidor: "))
lat_atual_platfor = float(input("Digite a latencia atual da plataforma em ms: "))
quant_erros_criticos_encontrados = int(input("Digite a quantidade de erros criticos encontrados: "))
uso_atual_disco = float(input("Digite a porcentagem do uso atual do disco do servidor: "))
 
 
if quant_serv_dispo == 0:
 
    print("LANCAMENTO BLOQUEADO: não existem servidores disponíveis.")
 
else:
    prev_usuarios_servidor = prev_usuarios / quant_serv_dispo
 
    if prev_usuarios_servidor > cap_max_servidor:
        print("LANCAMENTO BLOQUEADO: a quantidade de usuarios prevista por servidor excede a capacidade maxima do servidor.")
 
    elif quant_erros_criticos_encontrados >= 1:
        print("LANCAMENTO BLOQUEADO: existem erros criticos encontrados.")
 
    elif lat_atual_platfor > 300:
        print("LANCAMENTO ADIADO: desempenho precisa ser revisado.")
 
    elif uso_atual_disco > 90:
        print("LANCAMENTO COM ALERTA: pouco espaco em disco.")
 
    else:
        print("LANCAMENTO AUTORIZADO!")