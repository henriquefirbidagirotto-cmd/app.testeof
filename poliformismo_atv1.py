import streamlit as st

# ## **Exercícios extra com Streamlit…**

# **Classe Livro** – crie uma classe com atributos título, autor, ano. Adicione um método `__str__`. Crie uma subclasse `LivroDigital` que adiciona atributo `formato` e sobrescreva `__str__`.

# **Classe Abstrata Veiculo** – defina uma classe abstrata com método `mover`. Implemente `Carro` e `Bicicleta` com comportamentos diferentes. Teste o polimorfismo.

# **Sobrecarga de operador** – crie uma classe `Vetor` com atributos x, y e implemente `__add__`, `__sub__`, `__mul__` (escalar).

# **Classe anônima** – use `type` para criar uma classe dinâmica com um método `saudacao`. Instancie-a.

class executando:
    def executar(self):
        return 'Carregando'

class Livro(executando):
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

class LivroDigital(Livro, executando):
    def __str__(self):
        return f'Titulo {self.titulo} autor { self.autor} ano {self.ano}'
    
class Veiculo(executando):
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def abstrata(self):
        self.carro = 'Aro 20'
        self.bicicleta = 'Aro 29'

    def carrouni(self, carro):
        if carro == 'nao':
            print('Bicicleta')
            return self.bicicleta
        elif carro == 'sim':
            return f'Carro Modelo: {self.modelo} ano {self.ano} {self.carro}'
        else:
            return 'Erro'

class Vetor(executando):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self, add):
        self.adicionar = add
        return 'adicionou', self.adicionar
    
    def __sub__(self, sub):
        self.substituir = sub
        return 'substituir', self.substituir
    
    def __escalar__(self,escalar):
        self.escalar = escalar
        return 'Escala', self.escalar
    
    def __str__(self):
        return f'Adicionou {self.adicionar} Substituiu {self.substituir} Escalou {self.escalar}'

Liv = Livro('48 leis do poder', 'robert grecce', '1999')
veic = Veiculo('Ford ka', '2010')
veic.carrouni('sim')
vet = Vetor(20,20)
vet.__add__('Henrique')
vet.__sub__('Arthur')
vet.__escalar__('Henrique')


st.title('POO - TEST POLIFORMISMO')
st.write('Escolha Uma ...')

opcao = st.selectbox(

        'escolha entre livro e carro ou bicicleta',
        ['Livro', 'Carro', 'Vetor']

)

if opcao == 'Livro':
    Livro = LivroDigital()
elif opcao == 'Carro':
    Veiculo = ()
elif opcao == 'Vetor':
    Vetor = ()

st.subheader('RESULTADO')
st.success(executando.executar())