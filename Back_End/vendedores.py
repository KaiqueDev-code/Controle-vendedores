while True != 0:
    #Menu do Sistema
    print("=" * 30)
    print("MENU SISTEMA")
    print("=" * 30)
    print(
    '''

    [1] Registrar vendedores e suas vendas
    [2] Relatorio de Carga Horaria
    [3] Calcular Apenas o Bonus
    [0] Sair
    
    '''
    )

    menu = int(input("Escolha uma opção: "))
    comissao = []
    vendedor = []
    total_vendas = []

    # Saindo do Sistema
    if menu == 0:
        print("Saindo do sistema...")
        break
   
     # Opção Cadastro dados
    elif menu == 1:
        while True:
        
            vendedor  = input('Digite os nomes dos vendedores em ordem: ').split(', ')
            total_vendas = input("Digite o total de vendas de cada um em ordem: ").split(', ')
                    

            # Convertendo os valores de total_vendas para float
            total_vendas = [float(valor) for valor in total_vendas] 

            

            for i in range(len(vendedor)):
                nome = vendedor[i]
                valor = total_vendas[i]

                if valor == 5000:
                    comissao = valor * 0.3
                    print(f"O vendedor {nome},  vendeu {valor}, com a comição {comissao}")
                elif 5001 < valor <= 10000:
                    comissao = valor * 0.5
                    print(f"O vendedor {nome},  vendeu {valor}, com a comição {comissao}")
                else:
                    comissao = valor * 0.7
                    print(f"O vendedor {nome},  vendeu {valor}, com a comição {comissao}")

            voltar = input("Deseja Voltar [sim/não] ?").lower()
            if voltar == "sim":
                break
            
                
        # Sistema de Relatorio de Carga horaria
    elif menu == 2:
         while True:    
            dias_base = 24
            carga_horaria = int(input("Quantos dias o Vendedor Trabalhou? "))
            nome_carga = input("Qual o nome do vendedor ? ")
                    
            if carga_horaria < dias_base :
                print("Carga horaria não Concluida")
                print(f"Faltam {dias_base - carga_horaria}, para o vendedor {nome_carga}")

            elif carga_horaria == dias_base:
                print("Carga horaria Concluida, Parabens!")

            else:
                print("Carga Horaria ultrapassada, verifique o seu cadastro")
                    
            voltar = input("Deseja Voltar ?").lower()
            if voltar == "sim":
                break
                    
        # Sistema de Metas e Bonus
    elif menu == 3:
        while True:
            def mt_vendedores(bonus=300, metas=10000):
                if metas > 10000:
                    print(f"Meta de vendas concluida !\n Seu bonus adicional foi de {bonus}")
                else:
                    print("Meta não concluida, Não Desanime")

                # Função Voltar
                voltar = input("Deseja Voltar ?").lower
            if voltar == "sim":
                break
        

        mt_vendedores()

    else:
        print("Escolha uma Opção valida!")
        break