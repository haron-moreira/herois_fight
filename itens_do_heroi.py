from sqlalchemy import create_engine
from sqlalchemy.sql import text

engine = create_engine('sqlite:///rpg.db')


class ItemNaoExisteException(Exception):
    pass


def heroi_tem_item(id):
    with engine.connect() as con:
        statement = text ("""SELECT * FROM ItemDoHeroi WHERE idHeroi = :id_heroi""") 
        
        rs = con.execute(statement, id_heroi=id) #e usei esse buraco
        temItem = rs.fetchall()                 
        if temItem == []:                       
            return False
        return True
        

def heroi_quantos_itens(id):
    with engine.connect() as con:
        statement = text ("""SELECT * FROM ItemDoHeroi WHERE idHeroi = :id_heroi""") 
        
        rs = con.execute(statement, id_heroi=id) #e usei esse buraco
        itens = rs.fetchall()                 
        if itens == []:                       
            return 0
        return len(itens)



def itens_do_heroi(id):
    with engine.connect() as con:
        statement = text ("""SELECT * FROM ItemDoHeroi idh JOIN Item i on i.id = idh.idItem where idh.idHeroi = :id_heroi;""") 
        
        rs = con.execute(statement, id_heroi=id) #e usei esse buraco
        itens = rs.fetchall() 

        return itens



def itens_em_uso_por_nome_do_heroi(nomeHeroi):
      with engine.connect() as con:
        statement = text ("""SELECT i.id, i.nome, i.tipo, i.fisico, i.magia, i.agilidade, i.emUso, h.nome FROM ItemDoHeroi idh JOIN Item i on i.id = idh.idItem JOIN Heroi h ON h.id = idh.idHeroi WHERE h.nome = :nome AND i.emUso = 1""") 
        
        rs = con.execute(statement, nome=nomeHeroi) #e usei esse buraco
        itens = rs.fetchall() 
        
        return itens