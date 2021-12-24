from source.funcionario import *

empregados = []
agendas = {"mensal":[5], "semanal":[1,8,15,21], "bi-semanal": [15, 30]}
dias_passados = 0
id = 0

while True:
    entrada = int(input("Digite 0 para sair\nDigite 1 para adicionar um empregado\nDigite 2 para remover um empregado\nDigite 3 para adicionar um ponto ao funcionario\nDigite 4 para adicionar uma venda a um funcionario\nDigite 5 para adicionar uma taxa ao funcionario\nDigite 6 para alterar os dados de um funcionaro\nDigite 7 para passar os dias da folha de pagamento\nDigite 8 para criar uma nova agenda de pagamento\n"))
    if entrada == 0:
        exit(0)
    elif entrada == 1:
        nome = input("Digite o nome do empregado: ")
        tipo = input("Digite o tipo do empregado: ")
        metodo_de_pagemento = input("Digite o metodo de pagemento: ")
        sindicato = input("O empregado é do sindicato: ")
        if sindicato.lower() == "sim":
            taxa_de_sindicato = float(input("Taxa sindical: "))
        else: taxa_de_sindicato = 0
        endereco = input("Digite o endereço do empregado: ")
        agenda_de_pagamento = input("Digite a agenda de pagamento do funcionaro: ")
        percentual_de_comissao = float(input("Percentual da comissao: "))
        salario_hora = float(input("Salario Hora: "))
        salario_base = float(input("Salario base: "))
        funcionario = Funcionario(id, nome, tipo, metodo_de_pagemento, sindicato, taxa_de_sindicato, endereco, agendas[agenda_de_pagamento], percentual_de_comissao, salario_hora, salario_base)
        empregados.append(funcionario)
        funcionario.exibir()
        id += 1
    elif entrada == 2:
        id = int(input("Digite o ID do empregado: "))
        empregados[id] = None
    elif entrada == 3:
        id = int(input("Digite o ID do funcionario: "))
        entrada_ponto = float(input("Digite o horario de entrada: "))
        saida_ponto = float(input("Digite o horario de saida: "))
        funcionario = empregados[id]
        funcionario.pontos.append((entrada_ponto, saida_ponto))
    elif entrada == 4:
        id = int(input("Digite o ID do funcionario: "))
        venda = float(input("Digite o valor da venda: "))
        funcionario = empregados[id]
        funcionario.vendas.append(venda)
    elif entrada == 5:
        id = int(input("Digite o ID do funcionario: "))
        taxa = float(input("Digite o valor da Taxa: "))
        funcionario = empregados[id]
        funcionario.taxas_de_servico.append(taxa)
    elif entrada == 6:
        id = int(input("Digite o ID do funcionario: "))
        print("Digite os novos dados do funcionario ou deixe em branco para manter o mesmo")
        nome = input("Digite o Nome do funcionario: ")
        endereco = input("Digite o endereço do funcionario: ")
        tipo = input("Digite o tipo do funcionario: ")
        metodo_de_pagamento = input("Digite o metodo de pagamento do funcionario: ")
        sindicato = bool(input("Digite se o funcionario pertence ao sindicato: "))
        if sindicato.lower() == "sim":
            taxa_de_sindicato = float(input("Taxa sindical: "))
        else: taxa_de_sindicato = 0
        agenda_de_pagamento = input("Digite agenda de pagemento: ")
        percentual_de_comissao = input("Percentual da comissao: ")
        salario_hora = input("Salario Hora: ")
        empregado_alterado = empregados[id]
        if nome: empregado_alterado.nome = nome
        if endereco: empregado_alterado.endereco = endereco
        if tipo: empregado_alterado.tipo = tipo
        if metodo_de_pagamento: empregado_alterado.metodo_de_pagamento = metodo_de_pagamento
        if sindicato: empregado_alterado.sindicato = sindicato
        if taxa_de_sindicato: empregado_alterado.taxa_de_sindicato = taxa_de_sindicato
        if agenda_de_pagamento: empregado_alterado.dias_de_pagamento = agendas[agenda_de_pagamento]
        if percentual_de_comissao: empregado_alterado.percentual_de_comissao = float(percentual_de_comissao)
        if salario_hora: empregado_alterado.salario_hora = float(salario_hora)
        empregados[id] =  empregado_alterado
        empregados[id].exibir()
    elif entrada == 7:
        dias = int(input("Quantos dias devem ser passados ?"))
        for i in range(dias):
            dia_atual = dias_passados%31
            for funcionario in empregados:
                if funcionario:
                    funcionario.pagamento(dia_atual)
            dias_passados += 1
    elif entrada == 8:
        nome_da_agenda = input("Digite o nome da agenda")
        dias_de_pagamento = []
        while True:
            dia = int(input("adicione mais um dia de pagamento (ou um valor negativo para salvar os anteriores): "))
            if dia < 0: break
            else: dias_de_pagamento.append(dia)
        agendas[nome_da_agenda] = dias_de_pagamento
        print("Nome da Agenda, dias de pagemento: ", dias_de_pagamento)
