class Aluno(object):
    def __init__(self, nome, mensalidade, idade):
        self.nome = nome
        self.mensalidade = mensalidade
        self.idade = idade
    
    def get_idade(self):
        return self.idade
   
    def get_nome(self):
        return self.nome

    def get_mensalidade(self):
        return self.mensalidade       

    def set_nome(self, novo_nome):
        self.nome = novo_nome
        
    def set_mensalidade(self, nova_mensalidade):
        self.mensalidade = nova_mensalidade
       
    def set_idade(self, nova_idade):
        self.idade = nova_idade

if __name__ == "__main__":
    NN = str(input("Digite o nome do novo aluno: "))
    NI = int(input("Digite a idade do novo aluno: "))
    NM = int(input("Digite a mensalidade do novo aluno: ")) 
    aluno1 = Aluno("Mateus",1200,18)
    aluno2 = Aluno("Rafael",1500,19)
    aluno3 = Aluno("Ricardo",1300,17)
    aluno4 = Aluno(NN,NM,NI)
    print(aluno2.get_mensalidade())
    print(aluno3.get_idade())
    print(aluno1.get_nome())    
    print(aluno3.get_mensalidade())
    print(aluno4.get_nome())
    print(aluno4.get_idade())
    print(aluno4.get_mensalidade())

