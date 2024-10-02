
from dataclasses import dataclass

@dataclass
class Pessoa:
     codigo: int
     nome: str
     cpf: str
     email: str
     profissao: str
     endereco: str
     telefone: str
    
    #destrutor
    
     def __del__(self):
        return f'Objeto {self.nome} de codigo {self.codigo} foi destruído'