# class Funcionario:
#     def __init__(self, nome, cpf, salario):
#         self.nome = nome
#         self.cpf = cpf
#         self.salario = salario
#
#     def exibirDados(self):
#         print(f"Nome: {self.nome}")
#         print(f"CPF: {self.cpf}")
#         print(f"Salário: {self.salario}")
#
#
# class Professor(Funcionario):
#     def __init__(self, nome, cpf, salario, turmas):
#         super().__init__(nome, cpf, salario)
#         self.turmas = turmas
#     def exibirDados(self):
#         super().exibirDados()
#         print(f"Turma: {self.turmas}")
#
#
#
# class Coordenador(Funcionario):
#     pass
#
# class Secretario(Funcionario):
#     pass
#
#
# prof1 = Professor('João', '283.249.603-23', 2500, ['A', 'B'])
#
# prof1.exibirDados()

# class Pessoa:
#     def __init__(self, nome, endereco, rendimento):
#         self.nome = nome
#         self.endereco= endereco
#         self.rendimento = rendimento
#
#     def exibirDados(self):
#         print(f"Nome: {self.nome}")
#         print(f"Endereço: {self.endereco}")
#         print(f"Rendimento: {self.rendimento}")
#
# class PessoaJuridica(Pessoa):
#     def __init__(self, nome, endereco, rendimento, cnpj):
#         super().__init__(nome, endereco, rendimento)
#         self.cnpj = cnpj
#
#     def exibirDados(self):
#         super().exibirDados()
#         print(f"CNPJ: {self.cnpj}")
#
#
# class PessoaFisica(Pessoa):
#     def __init__(self, nome, endereco, rendimento, cpf):
#         super().__init__(nome, endereco, rendimento)
#         self.cpf = cpf
#     def exibirDados(self):
#         super().exibirDados()
#         print(f"CPF: {self.cpf}")
#
# pessJur = PessoaJuridica('Infinity', 'Av.Santos', 250000, '60.110.0000/01')
#
# pessFis = PessoaFisica('Cláudio', 'Rua: Pereira', 2000, '283.249.603-23')
#
# pessJur.exibirDados()
# pessFis.exibirDados()


# class Veiculo:
#     def __init__(self, modelo, cor, velocidadeMax, limitePassageiros):
#         self.modelo = modelo
#         self.cor = cor
#         self.velocidadeMax = velocidadeMax
#         self.limitePassageiros = limitePassageiros
#         self.velocidadeAtual = 0
#         self.ligado = False
#
#     def ligar(self):
#         if self.ligado == False:
#             self.ligado = True
#
#     def desligar(self):
#         if self.ligado == True:
#             self.ligado = False
#
#     def exibirDados(self):
#         print(f"Modelo: {self.modelo}")
#         print(f"Cor: {self.cor}")
#         print(f"Velocidade  máxima: {self.velocidadeMax}")
#         print(f"LImite de passageiros: {self.limitePassageiros}")
#
# class Carro(Veiculo):
#     def __init__(self, modelo, cor, velocidadeMax, limitePassageiros, capacidadeBagageiro, airBag):
#         super().__init__(modelo, cor, velocidadeMax, limitePassageiros)
#         self.capacidadePassageiro = capacidadeBagageiro
#         self.airBag = airBag
#
#     def exibirDados(self):
#         super().exibirDados()
#         print(f"A capacidade de passageiros: {self.capacidadePassageiro}")
#         print(f"AirBag: {self.airBag}")
#
#
# class Moto(Veiculo):
#     def __init__(self, modelo, cor, velocidadeMax, limitePassageiros, cilindradas):
#         super().__init__(modelo, cor, velocidadeMax, limitePassageiros)
#         self.cilindradas = cilindradas
#
#     def exibirDados(self):
#         super().exibirDados()
#         print(f"As cilindradas: {self.cilindradas}")
#
#
# car = Carro('argo', 'grafite', 150, 5, 20, True)
# car.exibirDados()

class Conta:
    def __init__(self, agencia, cliente, saldo):
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo+=valor

class ContaCorrente(Conta):
    def __init__(self, agencia, cliente, saldo, chequeEspecial):

        super().__init__(agencia, cliente, saldo)
        self.chequeEspecial = chequeEspecial

    def sacar(self, valor):
        if self.saldo - valor >= 0 - self.chequeEspecial:
            self.saldo-=valor
            print(f'Saco realizado com sucesso')
            print(f"Saldo: {self.saldo}")

cont = ContaCorrente('445', 'claudio', 15000, 2000)
cont.sacar(3000)
