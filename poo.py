from random import randint
from time import sleep

# Listas globais com informacoes sobre os objetos
idsUsadosFuncionario = []
idsUsadosOnibus = []

fiscaisDisponiveisObj = []
fiscaisOcupadosObj = []


motoristasDisponiveisObj = []
motoristasOcupadosObj = []


onibusObj_semMotorista = []
onibusObj_comMotorista = []
onibusObj_comFiscal = []
onibusObj_semFiscal = []


# Legenda de instrucao
menu = '''
            "m" - Criar Motorista
            "f" - Criar Fiscal
            "o" - Criar Onibus
            "Am" - Assignar Motorista
            "Af" - Assignar Fiscal
            "Dp" - Definir/Alterar Paradas Onibus
            "Mo" - Mostrar Onibus
            "Mp" - Mostrar Paradas
            "Mm" - Mostrar Motoristas
            "Mf" - Mostrar Fiscais
            "Do" - Deletar Onibus
            "Dm" - Deletar Motorista
            "Df" - Deletar Fiscal
            "ADf" - Alterar Dados Fiscal
            "ADm" - Alterar Dados Motorista
            "ADo" - Alterar Dados Onibus
            "s" - Sair
            
'''



# Onde usuario pode interagir com o programa
def main():
    while True:
        
        # Da opcoes e espera comando do usuario
        sleep(.5)
        print(menu)
        cmd = input("Qual comando: ")

        # Se comando "s", sai do programa
        if cmd == "s":
            print("Obrigado por usar o programa!")
            break
    
        elif cmd == "m":
            criarMotorista()
        
        elif cmd == "f":
            criarFiscal()

        elif cmd == "o":
            criarOnibus()

        elif cmd == "Am":
            assignarMotorista()

        elif cmd == "Af":
            assignarFiscal()
        
        elif cmd == "Dp":
            definirParadas()

        elif cmd == "Mo":
            mostrarOnibus()

        elif cmd == "Mp":
            mostrarParadas()

        elif cmd == "Mm":
            mostrarMotoristas()
        
        elif cmd == "Mf":
            mostrarFiscais()
        
        elif cmd == "Do":
            deletarOnibus()

        elif cmd == "Dm":
            deletarMotorista()

        elif cmd == "Df":
            deletarFiscal()

        elif cmd == "ADf":
            alterarDadosFiscal()
        
        elif cmd == "ADm":
            alterarDadosMotorista()

        elif cmd == "ADo":
            alterarDadosOnibus()


# Altera dados do Onibus
def alterarDadosOnibus():
    onibusObj_TOTAIS = list(set(onibusObj_semMotorista + onibusObj_comMotorista))
    if not onibusObj_TOTAIS:
        print("Primeiro é preciso criar um Onibus")
        return

    idsDisponiveisOnibusLocal = []
    print("Onibus Disponiveis:  \nNome     Id")
    for onibus in onibusObj_TOTAIS:
        idsDisponiveisOnibusLocal.append(onibus.id)
        print(f"{onibus.nome}: {onibus.id}")

    idOnibusDesejado = str(input("Id do Onibus que deseja: "))

    if idOnibusDesejado not in idsDisponiveisOnibusLocal:
        print("Id não encontrado")
        return

    for onibus in onibusObj_TOTAIS:
        if idOnibusDesejado == onibus.id:
            onibusDesejadoObj = onibus
            break
    
    novoNome = input("Alterar nome: ")
    onibusDesejadoObj.alterarDados(novoNome)
    print("Dados alterados com sucesso!")


# Altera dados do Motorista
def alterarDadosMotorista():
    motoristaObj_TOTAIS = list(set(motoristasDisponiveisObj + motoristasOcupadosObj))

    if not motoristaObj_TOTAIS:
        print("Não há Motoristas dísponiveis")
        return

    idsDisponiveisMotoristasLocal = []
    print("Fiscais Disponiveis: \nNome     Id")
    for motorista in motoristaObj_TOTAIS:
        idsDisponiveisMotoristasLocal.append(motorista.id)
        print(f"{motorista.nome}: {motorista.id}")

    idMotoristaDesejado = str(input("Id do Motorista que deseja: "))

    if idMotoristaDesejado not in idsDisponiveisMotoristasLocal:
        print("Id não encontrado")
        return

    for motorista in motoristaObj_TOTAIS:
        if idMotoristaDesejado == motorista.id:
            motoristaDesejadoObj = motorista
            break
    
    novoNome = input("Alterar nome: ")
    motoristaDesejadoObj.alterarDados(novoNome)
    print("Dados alterados com sucesso!")


# Altera dados do Fiscal
def alterarDadosFiscal():
    # Fiscal
    fiscaisObj_TOTAIS = list(set(fiscaisDisponiveisObj + fiscaisOcupadosObj))

    if not fiscaisObj_TOTAIS:
        print("Não há Fiscais dísponiveis")
        return

    idsDisponiveisFiscaisLocal = []
    print("Fiscais Disponiveis: \nNome     Id")
    for fiscal in fiscaisObj_TOTAIS:
        idsDisponiveisFiscaisLocal.append(fiscal.id)
        print(f"{fiscal.nome}: {fiscal.id}")

    idFiscalDesejado = str(input("Id do Fiscal que deseja: "))

    if idFiscalDesejado not in idsDisponiveisFiscaisLocal:
        print("Id não encontrado")
        return

    for fiscal in fiscaisObj_TOTAIS:
        if idFiscalDesejado == fiscal.id:
            fiscalDesejadoObj = fiscal
            break
    
    novoNome = input("Alterar nome: ")
    fiscalDesejadoObj.alterarDados(novoNome)
    print("Dados alterados com sucesso!")


# Deleta Fiscal
def deletarFiscal():
    if not fiscaisDisponiveisObj:
        print("Não há Fiscais dísponiveis")
        return

    # Anota ids Existentes para ver se input do usuario existe 
    idsDisponiveisOnibusLocal = []
    print("Fiscais Disponiveis:  \nNome     Id")
    for fiscais in fiscaisDisponiveisObj:
        idsDisponiveisOnibusLocal.append(fiscais.id)
        print(f"{fiscais.nome}: {fiscais.id}")

    idFiscalDesejado = str(input("Id do Fiscal que deseja: "))

    if idFiscalDesejado not in idsDisponiveisOnibusLocal:
        print("Id não encontrado")
        return

    # Pega fiscal com id inserido pelo usuario
    for fiscal in fiscaisDisponiveisObj:
        if idFiscalDesejado == fiscal.id:
            fiscalDesejadoObj = fiscal
            break
    
    # Se procurar fiscal e este nao existir, ignora a execao
    try:
        fiscaisDisponiveisObj.remove(fiscalDesejadoObj)
    except:
        pass

    # Deleta objeto
    del fiscalDesejadoObj
    print("Fiscal deletado com sucesso!")


# Deleta Motorista
def deletarMotorista():
    if not motoristasDisponiveisObj:
        print("Não há Motoristas dísponiveis")
        return

    idsDisponiveisOnibusLocal = []
    print("Motoristas Disponiveis:  \nNome     Id")
    for motorista in motoristasDisponiveisObj:
        idsDisponiveisOnibusLocal.append(motorista.id)
        print(f"{motorista.nome}: {motorista.id}")

    idMotoristaDesejado = str(input("Id do Motorista que deseja: "))

    if idMotoristaDesejado not in idsDisponiveisOnibusLocal:
        print("Id não encontrado")
        return

    for motorista in motoristasDisponiveisObj:
        if idMotoristaDesejado == motorista.id:
            motoristaDesejadoObj = motorista
            break

    try:
        motoristasDisponiveisObj.remove(motoristaDesejadoObj)
    except:
        pass

    del motoristaDesejadoObj
    print("Motorista deletado com sucesso!")


# Deleta Fiscal
# So e possivel deletar onibus que nao possua motoristas nem fiscal associados
def deletarOnibus():
    totalOnibus = list(set(onibusObj_semMotorista + onibusObj_semFiscal))
    if not  totalOnibus:
        print("Nenhum onibus disponivel para deletar")
        return
    
    idsDisponiveisOnibusLocal = []
    print("Onibus Disponiveis:  \nNome     Id")
    for onibus in totalOnibus:
        idsDisponiveisOnibusLocal.append(onibus.id)
        print(f"{onibus.nome}: {onibus.id}")

    idOnibusDesejado = str(input("Id do onibus que deseja: "))

    if idOnibusDesejado not in idsDisponiveisOnibusLocal:
        print("Id não encontrado")
        return

    for onibus in totalOnibus:
        if idOnibusDesejado == onibus.id:
            onibusDesejadoObj = onibus
            break
    try:
        onibusObj_semMotorista.remove(onibusDesejadoObj)
        onibusObj_semFiscal.remove(onibusDesejadoObj)
    except:
        pass
    del onibusDesejadoObj
    print("Onibus deletado com sucesso!")


# Mostra Paradas do Onibus existentes
def mostrarParadas():

    # Pega total de onibus existentes
    onibusObj_TOTAIS = list(set(onibusObj_semMotorista + onibusObj_comMotorista))
    if not onibusObj_TOTAIS:
        print("Não há Rotas dísponiveis")
        return

    # Passa por todos objetos de onibus e pega suas paradas e nome
    # Formata as paradas e o nome do onibus para ser exibido
    idsDisponiveisOnibusLocal = []
    print("Rotas Disponiveis:  \nOnibus    Preço    Rota    ")
    for onibus in onibusObj_TOTAIS:
        try:
            idsDisponiveisOnibusLocal.append(onibus.paradas)
            print(f"{onibus.nome}: R${onibus.precoPassagem}: {str(list(onibus.paradas.values())).replace('[','').replace(']','')}")
        except:
            print("Não há rotas dísponiveis")


# Mostra Motoristas existentes
def mostrarMotoristas():
    # Pega motoristas totais existentes
    motoristasObj_TOTAIS = list(set(motoristasDisponiveisObj + motoristasOcupadosObj))
    if not motoristasObj_TOTAIS:
        print("Não há Motoristas dísponiveis")
        return

    # Passa por todos objetos de Motoristas e exibe seu nome e id
    print("Motoristas Disponiveis:  \nNome     Id")
    for motorista in motoristasObj_TOTAIS:
        print(f"{motorista.nome}: {motorista.id}")
    

# Mostra Fiscais existentes
def mostrarFiscais():
    # Pega fiscais totais existentes
    fiscaisObj_TOTAIS = list(set(fiscaisDisponiveisObj + fiscaisOcupadosObj))

    if not fiscaisObj_TOTAIS:
        print("Não há Fiscais dísponiveis")
        return

    # Passa por todos objetos de Motoristas e exibe seu nome e id
    print("Fiscais Disponiveis: \nNome     Id")
    for fiscal in fiscaisObj_TOTAIS:
        print(f"{fiscal.nome}: {fiscal.id}")
    

# Mostra Onibus existentes
def mostrarOnibus():
    # Pega onibus totais existentes
    onibusObj_TOTAIS = list(set(onibusObj_semMotorista + onibusObj_comMotorista))
    if not onibusObj_TOTAIS:
        print("Primeiro é preciso criar um Onibus")
        return

    # Passa por todos objetos de Motoristas e exibe seu nome e id
    print("Onibus Disponiveis:  \nNome     Id")
    for onibus in onibusObj_TOTAIS:
        print(f"{onibus.nome}: {onibus.id}")


# Define paradas das rotas
def definirParadas():

    if not onibusObj_semMotorista:
        print("Não há Onibus dísponiveis")
        return

    idsDisponiveisOnibusLocal = []
    print("Onibus Disponiveis:  \nNome     Id")
    for onibus in onibusObj_semMotorista:
        idsDisponiveisOnibusLocal.append(onibus.id)
        print(f"{onibus.nome}: {onibus.id}")

    idOnibusDesejado = str(input("Id do onibus que deseja: "))

    if idOnibusDesejado not in idsDisponiveisOnibusLocal:
        print("Id não encontrado")
        return

    for onibus in onibusObj_semMotorista:
        if idOnibusDesejado == onibus.id:
            onibusDesejadoObj = onibus
            break

    # Cria rota a partir de quantas paradas quer possuir
    try:
        qntParadas = int(input("Quantidade de Paradas (ex: 1,3,5): "))
    except:
        print("Numero de paradas invalido")
    labelParadas = {}

    try:
        if onibusDesejadoObj.paradas:
            print("Paradas Atuais:")
            counter = 0 
            paradasDict = onibusDesejadoObj.paradas
            for parada in (paradasDict):
                counter += 1
                print(f"Parada {counter}: {paradasDict[parada]}")
                print("Novas Paradas")
    except:
        print("Exemplos de Paradas Disponiveis: RJ, SP, MG")

    # Previni que 'ids' se repitam
    for parada in range(qntParadas):
        paradaInput = str(input(f"Parada número {parada+1}: "))
        if paradaInput in labelParadas.values():
            continue
        labelParadas[parada] = paradaInput

    onibusDesejadoObj.definirParadas(labelParadas, qntParadas)
    print("Paradas registradas com sucesso!")


# Cria objeto do Motorista
def criarMotorista():
    nomeMotorista = input("Nome do motorista: ")
    letraInicialFuncao = "M"
    motoristasDisponiveisObj.append(Motorista(letraInicialFuncao, nomeMotorista))
    print("Motorista criado com sucesso!\n")


# Cria objeto do Onibus
def criarOnibus():
    nomeOnibus = input("Nome do Onibus: ")
    onibus = Onibus(nomeOnibus)
    onibusObj_semMotorista.append(onibus)
    onibusObj_semFiscal.append(onibus)
    onibus = None
    print("Onibus criado com sucesso!\n")


# Cria objeto do Fiscal
def criarFiscal():
    nomeFiscal = input("Nome do Fiscal: ")
    letraInicialFuncao = "F"
    fiscaisDisponiveisObj.append(Fiscal(letraInicialFuncao, nomeFiscal))
    print("Fiscal criado com sucesso!\n")


# Assigna Motorista a um Onibus
def assignarMotorista():
    # Exibe Nome e Id de onibus existentes e pega seu objeto para colocar o id do Motorista
    if not motoristasDisponiveisObj:
        print("Não há Motoristas dísponiveis")
        return

    if not onibusObj_semMotorista:
        print("Não há Onibus dísponiveis")
        return

    idsDisponiveisOnibusLocal = []
    print("Onibus Disponiveis:  \nNome     Id")
    for onibus in onibusObj_semMotorista:
        idsDisponiveisOnibusLocal.append(onibus.id)
        print(f"{onibus.nome}: {onibus.id}")

    idOnibusDesejado = str(input("Id do onibus que deseja: "))

    if idOnibusDesejado not in idsDisponiveisOnibusLocal:
        print("Id não encontrado")
        return

    for onibus in onibusObj_semMotorista:
        if idOnibusDesejado == onibus.id:
            onibusDesejadoObj = onibus
            break


    # Pega objeto do motorista para inserir o id do Onibus
    idsDisponiveisMotoristasLocal = []
    print("Motoristas Disponiveis:  \nNome     Id")
    for motorista in motoristasDisponiveisObj:
        idsDisponiveisMotoristasLocal.append(motorista.id)
        print(f"{motorista.nome}: {motorista.id}")
    
    idMotoristaDesejado = str(input("Id do motorista deseja assignar:"))
    
    if idMotoristaDesejado not in idsDisponiveisMotoristasLocal:
        print("Id não encontrado")
        return 

    for motorista in motoristasDisponiveisObj:
        if idMotoristaDesejado == motorista.id:
            motoristaDesejadoObj = motorista
            break

    # Adiciona ao objeto
    motoristaDesejadoObj.assignar(idOnibusDesejado)
    onibusDesejadoObj.assignarMotorista(idMotoristaDesejado)

    # Adiciona onibus e motorista em lista de ocupados
    motoristasOcupadosObj.append(motoristaDesejadoObj)
    onibusObj_comMotorista.append(onibusDesejadoObj)

    # Remove da lista de disponiveis
    motoristasDisponiveisObj.remove(motoristaDesejadoObj)
    onibusObj_semMotorista.remove(onibusDesejadoObj)

    print(f'Motorista "{motoristaDesejadoObj.nome}"({motoristaDesejadoObj.id}) foi assignado ao onibus "{onibusDesejadoObj.nome}"({onibusDesejadoObj.id}) com sucesso!')
    sleep(0.5)    


# Assigna Fiscal a um Onibus
def assignarFiscal():
    # Exibe Nome e Id de onibus existentes e pega seu objeto para colocar o id do Fiscal
    if not fiscaisDisponiveisObj:
        print("Não há Fiscais dísponiveis")
        return

    if not onibusObj_semFiscal:
        print("Não há Onibus dísponiveis")
        return

    idsDisponiveisOnibusLocal = []
    print("Onibus Disponiveis:  \nNome     Id")
    for onibus in onibusObj_semFiscal:
        idsDisponiveisOnibusLocal.append(onibus.id)
        print(f"{onibus.nome}: {onibus.id}")

    idOnibusDesejado = str(input("Id do onibus que deseja: "))

    if idOnibusDesejado not in idsDisponiveisOnibusLocal:
        print("Id não encontrado")
        return

    for onibus in onibusObj_semFiscal:
        if idOnibusDesejado == onibus.id:
            onibusDesejadoObj = onibus
            break

    # Pega objeto do fiscal para inserir o id do Onibus
    idsDisponiveisFiscaisLocal = []
    print("Fiscais Disponiveis: \nNome     Id")
    for fiscal in fiscaisDisponiveisObj:
        idsDisponiveisFiscaisLocal.append(fiscal.id)
        print(f"{fiscal.nome}: {fiscal.id}")
    
    idFiscalDesejado = str(input("Id do Fiscal deseja assignar:"))
    
    if idFiscalDesejado not in idsDisponiveisFiscaisLocal:
        print("Id não encontrado")
        return 

    for fiscal in fiscaisDisponiveisObj:
        if idFiscalDesejado == fiscal.id:
            fiscalDesejadoObj = fiscal
            break

    # Adiciona ao objeto
    fiscalDesejadoObj.assignar(idOnibusDesejado)
    onibusDesejadoObj.assignarFiscal(idFiscalDesejado)

    # Adiciona onibus e fiscal em lista de ocupados
    fiscaisOcupadosObj.append(fiscalDesejadoObj)
    onibusObj_comFiscal.append(onibusDesejadoObj)

    # Remove da lista de disponiveis
    fiscaisDisponiveisObj.remove(fiscalDesejadoObj)
    onibusObj_semFiscal.remove(onibusDesejadoObj)

    print(f'Fiscal "{fiscalDesejadoObj.nome}"({fiscalDesejadoObj.id}) foi assignado ao onibus "{onibusDesejadoObj.nome}"({onibusDesejadoObj.id}) com sucesso!')
    sleep(0.5)


# Classe com caracteristicas comuns entre Fiscal e Motorista
class Funcionario:
    # Recebe id do onibus que esta associado
    def __init__(self, letraInicialFuncao, nome):
        self.letraInicialFuncao = letraInicialFuncao
        self.nome = nome

        # Pega letra para diferenciar funcao entre motorista e fiscal
        # Roda funcao quando objeto e criado
        self.gerarId(self.letraInicialFuncao)

    # Gera id unico para funcionario
    def gerarId(self, idInicial):
        numAleatorio = randint(1,10000)
        preview_id = f"{idInicial}{numAleatorio}"
        

        for id in idsUsadosFuncionario:
            if str(preview_id) == str(id):
                self.gerarId(self.letraInicialFuncao)

        self.id = str(f"{idInicial}{numAleatorio}")
        idsUsadosFuncionario.append(str(self.id))
        return self.id
    
    # Adiciona o id do onibus que pertence
    def assignar(self, idOnibus):
        self.idOnibus = idOnibus
    
    # Altera dados de quando objeto foi criado
    def alterarDados(self, novoNome):
        self.nome = novoNome


# Classe que herda caracteristicas de Funcionario
class Fiscal(Funcionario):
    pass


# Classe que herda caracteristicas de Funcionario
class Motorista(Funcionario):
    pass


# Classe com caracteristicas do Onibus
class Onibus:
    def __init__(self, nome):
        self.nome = nome
        self.taxa_por_parada = 7.23

        # Roda funcoes quando objeto criada
        self.gerarId()

    # Gera id unico para funcionario
    def gerarId(self):
        numAleatorio = randint(1,10000)
        idInicial = str(f"O{numAleatorio}")
        
        for id in idsUsadosOnibus:
            if str(idInicial) == str(id):
                self.gerarId()

        self.id = idInicial
        idsUsadosOnibus.append(str(self.id))
        return self.id
    
    # Calcula preco da passagem baseado em quantas paradas possui
    def definirPrecoPassagem(self):
        self.precoPassagem = round(self.taxa_por_parada * self.qntParadas, 2)
        return self.precoPassagem

    # Ordena rotas e garante que não possui rotas repetidas
    def ordenarRotas(self):
        self.paradas = self.paradas

    # Associa id do motorista ao onibus
    def assignarMotorista(self, idMotorista):
        self.motorista = idMotorista

    # Associa id do fiscal ao onibus
    def assignarFiscal(self, idFiscal):
        self.fiscal = idFiscal
    
    # Associa as paradas ao onibus
    def definirParadas(self, paradas, qntParadas):
        self.paradas = paradas
        self.qntParadas = qntParadas
        
        self.definirPrecoPassagem()
    
    # Altera dados de quando objeto foi criado
    def alterarDados(self, novoNome):
        self.nome = novoNome
        
        





if __name__ == "__main__":
    main()  