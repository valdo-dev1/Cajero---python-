

saldo_acordado = 13000  #cantidad acordada 
print (f'tienes { saldo_acordado} disponibles')

retiro = int(input( '¿cuanto quieres retirar? '))
if retiro <= saldo_acordado:
	print ( f'retiro permitido : {retiro}')
	saldo_restante = saldo_acordado - retiro
	print (f'te queda {saldo_restante}' )
	print  (' tack ! (  ¡ gracias en sueco ! ) ' )
else : 
    print (f'no se puede retirar ${retiro}')
    print (f'solo tienes {saldo_acordado} acordados ' ) 
