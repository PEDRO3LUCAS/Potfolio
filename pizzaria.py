
print("________PIZZARIA COMA BASTANTE - sejam bem vindos___________")
print("________CARDÁPIO - PREÇOS_____________")
print(" ")
print("******pizzas-SABORES*****")
print("CALABREZA,MODA,MARGUERITA")
print("******PIZZAS - TAMANHO******")
print("  pizza pequena  $10,00  ")
print("  pizza média  $15,00  ")
print("  pizza grande $20,00  ")
print("********REFRIGERANTES*********")
print("  coca-cola    $7,00  ")
print("  guaraná      $6,00  ")
print("  fanta        $5,00  ")
print("__________________________")
print("  ")
print("FAÇA SEU PEDIDO PARA PIZZA")
print("1  CALABREZA ")
print("2  A MODA ")
print("3  MARGUERITA ")


pedidopizza = int(input())

print("DIGITE O TAMANHO DA PIZZA")
print("p  -  PEQUENA")
print("m  -  MÉDIA")
print("g  -  GRANDE")
print("______________________")

tampizza = input().upper()

print("FAÇA SEU PEDIDO PARA REFRIGERANTE: ")
print("1  -  coca-cola")
print("2  -  pepsi    ")
print("3  -  guaraná  ")













if (pedidopizza == 1) and (tampizza == "p") and ("pedidorefri" == 1):
    precopagar = 10.00 + 7.00
    pedidos = "CALABREZA, PEQUENA ,COCA-COLA"
elif (pedidopizza == 1) and (tampizza == "p") and ("pedidorefri" == 2):
    precopagar = 10.00 + 6.00
    pedidos = "CALABREZA, PEQUENA,GUARANÁ"
elif (pedidopizza == 1) and (tampizza == "p") and ("pedidorefri" == 3):
    precopagar = 10.00 + 5.00
    pedidos = "CALABREZA, PEQUENA,FANTA" 
elif (pedidopizza == 1) and (tampizza == "m") and ("pedidorefri" == 1):
    precopagar = 10.00 + 7.00
    pedidos = "CALABREZA, MÉDIA ,COCA-COLA"
elif (pedidopizza == 1) and (tampizza == "m") and ("pedidorefri" == 2):
    precopagar = 10.00 + 6.00
    pedidos = "CALABREZA, MÉDIA ,GUARANÁ"
elif (pedidopizza == 1) and (tampizza == "m") and ("pedidorefri" == 3):
    precopagar = 10.00 + 5.00
    pedidos = "CALABREZA, MÉDIA ,FANTA"
elif (pedidopizza == 1) and (tampizza == "G") and ("pedidorefri" == 1):
    precopagar = 10.00 + 7.00
    pedidos = "CALABREZA, GRANDE ,COCA-COLA"
elif (pedidopizza == 1) and (tampizza == "G") and ("pedidorefri" == 2):
    precopagar = 10.00 + 6.00
    pedidos = "CALABREZA, GRANDE ,GUARANÁ"
elif (pedidopizza == 1) and (tampizza == "G") and ("pedidorefri" == 3):
    precopagar = 10.00 + 5.00
    pedidos = "CALABREZA, GRANDE ,FANTA"
elif (pedidopizza == 2) and (tampizza == "p") and ("pedidorefri" == 1):
    precopagar = 10.00 + 7.00
    pedidos = "A MODA, PEQUENA ,COCA-COLA"
elif (pedidopizza == 2) and (tampizza == "p") and ("pedidorefri" == 2):
    precopagar = 10.00 + 6.00
    pedidos = "A MODA, PEQUENA ,GUARANÁ"
elif (pedidopizza == 2) and (tampizza == "p") and ("pedidorefri" == 3):
    precopagar = 10.00 + 5.00
    pedidos = "A MODA, PEQUENA ,FANTA"
elif (pedidopizza == 2) and (tampizza == "m") and ("pedidorefri" == 1):
    precopagar = 10.00 + 7.00
    pedidos = "A MODA, MÉDIA ,COCA-COLA"
elif (pedidopizza == 2) and (tampizza == "m") and ("pedidorefri" == 2):
    precopagar = 10.00 + 6.00
    pedidos = "A MODA, MÉDIA ,GUARANÁ"
elif (pedidopizza == 2) and (tampizza == "m") and ("pedidorefri" == 3):
    precopagar = 10.00 + 5.00
    pedidos = "A MODA, MÉDIA ,FANTA"
elif (pedidopizza == 2) and (tampizza == "G") and ("pedidorefri" == 1):
    precopagar = 10.00 + 7.00
    pedidos = "A MODA, GRANDE ,COCA-COLA"
elif (pedidopizza == 2) and (tampizza == "G") and ("pedidorefri" == 2):
    precopagar = 10.00 + 6.00
    pedidos = "A MODA, GRANDE ,GUARANÁ" 
elif (pedidopizza == 2) and (tampizza == "G") and ("pedidorefri" == 3):
    precopagar = 10.00 + 5.00
    pedidos = "A MODA, GRANDE ,FANTA"
elif (pedidopizza == 3) and (tampizza == "p") and ("pedidorefri" == 1):
    precopagar = 10.00 + 7.00
    pedidos = "MARGUERITA, PEQUENA ,COCA-COLA" 
elif (pedidopizza == 3) and (tampizza == "p") and ("pedidorefri" == 2):
    precopagar = 10.00 + 6.00
    pedidos = "MARGUERITA, PEQUENA ,GUARANÁ" 
elif (pedidopizza == 3) and (tampizza == "p") and ("pedidorefri" == 3):
    precopagar = 10.00 + 5.00
    pedidos = "MARGUERITA, PEQUENA ,FANTA" 
elif (pedidopizza == 3) and (tampizza == "m") and ("pedidorefri" == 1):
    precopagar = 10.00 + 7.00
    pedidos = "MARGUERITA, MÉDIA ,COCA-COLA" 
elif (pedidopizza == 3) and (tampizza == "m") and ("pedidorefri" == 2):
    precopagar = 10.00 + 6.00
    pedidos = "MARGUERITA, MÉDIA ,GUARANÁ"
elif (pedidopizza == 3) and (tampizza == "m") and ("pedidorefri" == 3):
    precopagar = 10.00 + 5.00
    pedidos = "MARGUERITA, MÉDIA ,FANTA"
elif (pedidopizza == 3) and (tampizza == "G") and ("pedidorefri" == 1):
    precopagar = 10,00 + 7.00
    pedidos = "MARGUERITA, GRANDE ,COCA-COLA" 
elif (pedidopizza == 3) and (tampizza == "G") and ("pedidorefri" == 2):
    precopagar = 10.00 + 6.00
    pedidos = "MARGUERITA, GRANDE ,GUARANÁ"
elif (pedidopizza == 3) and (tampizza == "G") and ("pedidorefri" == 3):
    precopagar = 10.00 + 5.00
    pedidos = "MARGUERITA, GRANDE ,FANTA"
else:
    precopagar = 0.0
    pedidos = "PEDIDO INVÁLIDO"

#exibe o resumo do pedido e o preço total a pagar
print("_____________________________________")
print(f"O TOTAL A PAGAR É:. R$ {precopagar:.2f}")
print(f"OS PEDIDOS FORAM {pedidos}")
print("______________________________________")
print("BOM APETITE E SEJA BEM VINDO")
print("____________RESUlTADO____________")





















