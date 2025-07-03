#Definição da função de saudação ao cliente 

def saudacao(): 

    print("Bem-vindo a Loja de Gelados do Luis Gustavo!") 

#Exibição do menu de preços formatado 

def exibir_tabela_precos(): 

    print("--" * 8, "Cardapio", "--" * 11) 

    print("--" * 24) 

    print ("---  | Tamanho  | Cupuaçu (CP)| Açaí (AC)  | ---") 

    precos = {"P": (9.00, 11.00), "M": (14.00, 16.00), "G": (18.00, 20.00)} 

    for tamanho, (preco_cp, preco_ac) in precos.items(): 

        print(f"---  | {tamanho:<7}  | R${preco_cp:<8}  | R${preco_ac:<7}  | ---") 

        print("--" * 24) 

#Coleta e validação do sabor e do tamanho escolhidos pelo usuário 

def obter_sabor_e_tamanho(): 

    while True: 

        sabor = input ("\nEntre com o sabor desejado (CP/AC): ").upper() 

        if sabor not in {"CP", "AC"}: 

            print("\nSabor inválido. Tente novamente") 

            continue 

        tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper() 

        if tamanho not in {"P", "M", "G"}: 

            print("\nTamanho inválido, tente novamente") 

            continue 

        return sabor, tamanho  

#Cálculo do preço com base no sabor e tamanho escolhidos pelo usuário 

def calcular_preco(sabor, tamanho): 

    precos = { 

    "CP": {"P": 9, "M": 14, "G": 18}, 

    "AC": {"P": 11, "M": 16, "G": 20} 

} 

    return precos [sabor] [tamanho] 

#Função principal do programa 

def main(): 

    saudacao() 

    exibir_tabela_precos() 

    total_pedidos = 0 

    while True: 

        sabor, tamanho = obter_sabor_e_tamanho() 

        preco = calcular_preco (sabor, tamanho) 

        total_pedidos += preco 

        #Exibição do pedido detalhado 

        sabor_nome = "Cupuaçu" if sabor == "CP" else "Açaí" 

        print(f"Você pediu um {sabor_nome} no tamanho {tamanho}: R${preco:.2f}") 

#Pergunta ao usuário se o pedido está completo e se falta algo 

        mais_pedidos = input("\nDeseja mais alguma coisa? (S/N): ").strip().lower() 

        if mais_pedidos not in {"sim", "s"}: 

            break 

#Exibe o valor total a ser pago 

    print(f"\nO valor total a ser pago: R${total_pedidos:.2f}") 

# Chama a função principal para iniciar o programa 

main()