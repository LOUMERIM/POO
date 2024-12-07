class Veiculo(object):
    todos_veiculos=[]
    def __init__(self,modelo,numres,fabnome,**kwargs):
        self.modelo=modelo
        self.numres=numres
        self.fabnome=fabnome
        Veiculo.todos_veiculos.append(self)

    def __str__(self):
        return f"Modelo:{self.modelo}\n Número de Registro: {self.numres}\n Fabricante: {self.fabnome}"

    def mostrar_detalhes(self):
        print(str(self))

class DonoInfo(object):
    def __init__(self,nome,contato,**kwargs):
        self.nome=nome
        self.contato=contato

    def __str__(self):
        return f"Nome do proprietário:{self.nome}\n Número de contato:{self.contato}"
    
    def mostrar_detalhes(self):
        print(str(self))

class VeiculoTerrestre(Veiculo,DonoInfo):
    def __init__(self,num_rodas,tipo_comb, **kwargs):
        Veiculo.__init__(self, **kwargs)
        DonoInfo.__init__(self, **kwargs)
        self.num_rodas=num_rodas
        self.tipo_comb=tipo_comb

    def __str__(self):
        return f"Veículo Terrestre:\n {Veiculo.__str__(self)}\n {DonoInfo.__str__(self)}\n Número de rodas: {self.num_rodas}\n Tipo de combustível: {self.tipo_comb}"

    def mostrar_detalhes(self):
        print(str(self))

class VeiculoAquatico(Veiculo,DonoInfo):
    def __init__(self,comp_emb,tipo_prop,**kwargs):
        Veiculo.__init__(self, **kwargs)
        DonoInfo.__init__(self, **kwargs)
        self.comp_emb=comp_emb
        self.tipo_prop=tipo_prop

    def __str__(self):
        return f"Veículo Aquatico:\n{Veiculo.__str__(self)}\n {DonoInfo.__str__(self)}\n Comprimento da Embarcação:  {self.comp_emb}m\n Tipo de propulsão: {self.tipo_prop}"

    def mostrar_detalhes(self):
        print(str(self))

veiculo1 = VeiculoTerrestre(modelo="Regera", numres="0116006", fabnome="Koenigsegg",num_rodas=4, tipo_comb="Hibrído", nome="Filipe Dwan", contato="8202-7640")
veiculo1.mostrar_detalhes()
veiculo2 = VeiculoTerrestre(modelo="F4 RR", numres="0614543", fabnome="MV Augusta",num_rodas=2,tipo_comb="Gasolina",nome="Loumerim", contato="8425-4339")
veiculo2.mostrar_detalhes()
veiculo3 = VeiculoAquatico(modelo="Focker", numres="0911008", fabnome="Yamaha", comp_emb=4.88,tipo_prop="Motor de popa",nome="Cachorro Belga", contato="9408-5646")
veiculo3.mostrar_detalhes()

#DESAFIO ADICIONAL
class Veiculo:
    todos_veiculos=[]
    def __init__(self,modelo,numres,fabnome,dono=None):
        self.modelo=modelo
        self.numres=numres
        self.fabnome=fabnome
        self.dono=dono
        Veiculo.todos_veiculos.append(self)

    def __str__(self):
        return f"Modelo:{self.modelo}\n Número de Registro: {self.numres}\n Fabricante: {self.fabnome}"

    def mostrar_detalhes(self):
        print(str(self))
        if self.dono:
            print(self.dono)

class DonoInfo:
    def __init__(self,nome,contato):
        self.nome=nome
        self.contato=contato

    def __str__(self):
        return f"Nome do proprietário:{self.nome}\n Número de contato:{self.contato}"
    
    def mostrar_detalhes(self):
        print(str(self))

class VeiculoTerrestre(Veiculo):
    def __init__(self,num_rodas,tipo_comb,**kwargs):
        super().__init__(**kwargs)
        self.num_rodas=num_rodas
        self.tipo_comb=tipo_comb
        

    def __str__(self):
        return f"Veículo Terrestre:\n {Veiculo.__str__(self)}\n Número de rodas: {self.num_rodas}\n Tipo de combustível: {self.tipo_comb}"

    def mostrar_detalhes(self):
        print("Detalhes do Veículo Terrestre:")
        super().mostrar_detalhes() 
        print(f"Número de rodas: {self.num_rodas}")
        print(f"Tipo de combustível:  {self.tipo_comb}")

class VeiculoAquatico(Veiculo):
    def __init__(self,comp_emb,tipo_prop,**kwargs):
        super().__init__(**kwargs)
        self.comp_emb=comp_emb
        self.tipo_prop=tipo_prop

    def __str__(self):
        return f"{Veiculo.__str__(self)}\n Comprimento da Embarcação:  {self.comp_emb}m\n Tipo de propulsão: {self.tipo_prop}"

    def mostrar_detalhes(self):
        print("Detalhes do Veículo Aquático:")
        super().mostrar_detalhes()
        print(f"Comprimento da Embarcação:  {self.comp_emb}m")
        print(f"Tipo de propulsão: {self.tipo_prop}")

dono1=DonoInfo(nome="Filipe Dwan", contato="8202-7640")
veiculo1 = VeiculoTerrestre(modelo="Regera", numres="0116006", fabnome="Koenigsegg",num_rodas=4, tipo_comb="Hibrído",dono=dono1)
veiculo1.mostrar_detalhes()

dono2=DonoInfo(nome="Loumerim", contato="8425-4339")
veiculo2 = VeiculoTerrestre(modelo="F4 RR", numres="0614543", fabnome="MV Augusta",num_rodas=2,tipo_comb="Gasolina",dono=dono2)
veiculo2.mostrar_detalhes()

dono3=DonoInfo(nome="Cachorro Belga", contato="9408-5646")
veiculo3 = VeiculoAquatico(modelo="Focker", numres="0911008", fabnome="Yamaha", comp_emb=4.88,tipo_prop="Motor de popa",dono=dono3)
veiculo3.mostrar_detalhes()

for veiculo in Veiculo.todos_veiculos:
    print("\n--- Detalhes do Veículo da Lista ---")
    veiculo.mostrar_detalhes()
