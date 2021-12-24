class Funcionario(object):
    """docstring for ."""

    def __init__(self, id, nome, tipo, metodo_de_pagemento, sindicato, taxa_de_sindicato, endereco, dias_de_pagamento, percentual_de_comissao, salario_hora, salario_base):
         self.id = id
         self.nome = nome
         self.tipo = tipo
         self.metodo_de_pagemento = metodo_de_pagemento
         self.sindicato = sindicato
         self.taxa_de_sindicato = taxa_de_sindicato
         self.pontos = []
         self.endereco = endereco
         self.vendas = []
         self.taxas_de_servico = []
         self.dias_de_pagamento = dias_de_pagamento
         self.percentual_de_comissao = percentual_de_comissao
         self.salario_hora = salario_hora
         self.salario_base = salario_base

    def pagamento(self, dia):
        if dia in self.dias_de_pagamento:
            print("Pagando ao funcionario: ", self.nome)
            salario = 0
            if self.tipo == "horista":
                for ponto in self.pontos:
                    salario += (ponto[1] - ponto[0]) * self.salario_hora
                self.pontos = []

            elif self.tipo == "comissionado":
                salario += self.salario_base
                for venda in self.vendas:
                    salario += venda * self.percentual_de_comissao
                self.vendas = []
            elif self.tipo == "mensalista":
                salario += self.salario_base


            for taxa in self.taxas_de_servico:
                salario -= taxa
            self.taxa_de_servico = []
            print("Salario Pago: ", salario)

    def exibir(self):
         print("ID: ", self.id)
         print("Nome: ", self.nome)
         print("Tipo: ", self.tipo)
         print("Metodo de pagamento: ", self.metodo_de_pagemento)
         print("Participa do sindicato: ", self.sindicato)
         print("Endereço: ", self.endereco)
