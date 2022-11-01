from sqlalchemy import create_engine
from sqlalchemy.sql import text
engine = create_engine('sqlite:///rpg.db')


class ItemNaoExisteException(Exception):
    pass


def consultar_item(id_i):
    with engine.connect() as con:  #conecta no meu banco de dados
        #query com "buraco" com o nome jogador    
        statement = text ("""SELECT * FROM Item WHERE id = :item""") 
        # :jogador -> buraco que vai ser preenchido quando eu chamar con.execute
        # :jogador -> O ":" marca o buraco. Sem ":" nao tem buraco, e coisas estranhas vao acontecer
        
        rs = con.execute(statement, item=id_i) #e usei esse buraco
        itens = rs.fetchall()                 
        #fetchall pega uma lista, com um objeto representando cada linha do resultado da query
        if itens == []:                       
            raise ItemNaoExisteException
        return dict(itens[0])


def nome_para_id_item(nome):
    with engine.connect() as con:  

        statement = text ("""SELECT * FROM Item WHERE nome = :nome""") 

        rs = con.execute(statement, nome=nome) #e usei esse buraco
        itens = rs.fetchall()    

        return itens[0][0]

def criar_item(tipo,nome,fisico,agilidade,magia):
    with engine.connect() as con:
        try:
            statement = text ("""INSERT INTO Item (nome, tipo, fisico, magia, agilidade, emUso) 
                                VALUES (:nome, :tipo, :fisico, :magia, :agilidade, 0);""") 
            
            rs = con.execute(statement, nome=nome, tipo=tipo, agilidade=agilidade, fisico=fisico, magia=magia) #e usei esse buraco
            return True
        except Exception as e:
            print(e)
            return False