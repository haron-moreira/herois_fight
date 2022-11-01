from sqlalchemy import create_engine
from sqlalchemy.sql import text

# Essa classe só representa uma exception com
#novo nome. Não mexa dentro dela.
# Escreva os imports (acima dela)
# E suas funcoes (depois dela)
class HeroiNaoExisteException(Exception):
    pass

#escreva suas funcoes aqui

# SELECT * from Heroi where id = 10;

engine = create_engine('sqlite:///rpg.db')

def heroi_existe(id_h):
    with engine.connect() as con:  #conecta no meu banco de dados
        #query com "buraco" com o nome jogador    
        statement = text ("""SELECT * FROM Heroi WHERE id = :heroi""") 
        # :jogador -> buraco que vai ser preenchido quando eu chamar con.execute
        # :jogador -> O ":" marca o buraco. Sem ":" nao tem buraco, e coisas estranhas vao acontecer
        
        rs = con.execute(statement, heroi=id_h) #e usei esse buraco
        jogadores = rs.fetchall()                 
        #fetchall pega uma lista, com um objeto representando cada linha do resultado da query
        if jogadores == []:                       
            return False
        return True 

def consultar_heroi(id_h):
    with engine.connect() as con:  #conecta no meu banco de dados
        #query com "buraco" com o nome jogador    
        statement = text ("""SELECT * FROM Heroi WHERE id = :heroi""") 
        # :jogador -> buraco que vai ser preenchido quando eu chamar con.execute
        # :jogador -> O ":" marca o buraco. Sem ":" nao tem buraco, e coisas estranhas vao acontecer
        
        rs = con.execute(statement, heroi=id_h) #e usei esse buraco
        jogadores = rs.fetchall()                 
        #fetchall pega uma lista, com um objeto representando cada linha do resultado da query
        if jogadores == []:                       
            raise HeroiNaoExisteException
        return dict(jogadores[0])

def consultar_heroi_por_nome(nome_h):
    with engine.connect() as con:
        statement = text ("""SELECT * FROM Heroi WHERE nome = :heroi""") 
        
        rs = con.execute(statement, heroi=nome_h) #e usei esse buraco
        jogadores = rs.fetchall()                 
        if jogadores == []:                       
            raise HeroiNaoExisteException
        return dict(jogadores[0])



def criar_novo_heroi(nome, agilidade, fisico, magia):
    with engine.connect() as con:
        try:
            statement = text ("""INSERT INTO Heroi (nome, fisico, magia, agilidade) 
                                VALUES (:nome, :fisico, :magia, :agilidade);""") 
            
            rs = con.execute(statement, nome=nome, agilidade=agilidade, fisico=fisico, magia=magia) #e usei esse buraco
            return True
        except Exception as e:
            print(e)
            return False
'''
Ex2 (correçao as 19h43)
O arquivo herois deve conter uma funcao 
consultar_heroi.
ela recebe uma id de heroi e retorna 
um dicionario com todos os dados do heroi
(por exemplo, a chave 'nome' conterá o valor
da coluna 'nome' associada a essa id).

se receber uma id invalida, a funcao levanta 
uma HeroiNaoExisteException 
'''

'''
20h11, voltamos pra resolver
esses testes
Exs 3:
fazer pro item o que a gente já fez pro heroi

Exs 4 e 5 

1) Voce já sabe fazer a consulta por id
Agora, vai começar a fazer por nome

2) Voce vai fazer a consulta por nome no arquivo heroi,
a funcao heroi_pronto_por_nome vai chamar essa funcao pra dar o resultado

3) (teste 5) a funcao heroi_pronto_por_nome vai adicionar a vida ao heroi ao
dicionario do heroi, mas nao ao banco de dados, sendo que vida=fisico*10

testar rodando o arquivo model

'''