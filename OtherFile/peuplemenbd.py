# baseDeDonne2
import random
from errno import errorcode
from mysql.connector import connection
import coloredlogs
import logging

coloredlogs.install(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%m-%y %H:%M:%S')


def connexion(base_de_donne='gestibank'):
    try:
        cnx = connection.MySQLConnection(user='root', password='',
                                         host='127.0.0.1', database=base_de_donne)
    except connection.errors.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            logging.debug("Il y a un problème avec votre user name ou password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            logging.debug("La base n’existe pas")
        else:
            logging.debug(err)
    else:
        logging.info(" connexion reussi")
        return cnx


def affiche_donne_curs(curs):
    for ligne in curs:
        print(ligne)


def select_all(cnx, table):
    cursor = cnx.cursor()
    select_stmt = "SELECT * FROM " + table
    print(select_stmt)
    cursor.execute(select_stmt)
    logging.debug("affiche table {}".format(table))
    affiche_donne_curs(cursor)
    cnx.close()


def peuplement_agent(ligne_bd, cnx):
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO `agent`(`ID`, `NOM`, `PRENOM`, `TYPE_USER`, `MATRICULE`, `EMAIL`, `TEL`, `DEBUT_CONTRAT`) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    )
    cursor.execute(insert_stmt, ligne_bd)
    logging.debug(cursor)
    cnx.commit()
    cnx.close()
def peuplement_compte(ligne_bd, cnx):
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO `agent`(`ID`, `NOM`, `PRENOM`, `TYPE_USER`, `MATRICULE`, `EMAIL`, `TEL`, `DEBUT_CONTRAT`) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    )
    cursor.execute(insert_stmt, ligne_bd)
    logging.debug(cursor)
    cnx.commit()
    cnx.close()




def peuplement_creacompte(ligne_bd, cnx):
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO demande_creacompte (`ID`, `NOM`, `PRENOM`, `MAIL`, `TEL`, `ADRESSE`, `JUSTIFICATIF`)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    )
    cursor.execute(insert_stmt, ligne_bd)
    logging.debug(cursor)
    cnx.commit()
    cnx.close()


for i in range(0, 10):
    ID = '100' + str(i)
    NOM = 'nom' + str(i)
    PRENOM = 'prenom_' + str(i)
    EMAIL = 'guest00{}@gestibank.com'.format(i)
    nombre = str(random.randint(1000000000, 9999999999))
    ligne = (ID, NOM, PRENOM, EMAIL, nombre, 'adresse', 'None')
    peuplement_creacompte(ligne, connexion())


def peuplement_creacompte(ligne_bd, cnx):
        cursor = cnx.cursor()
        insert_stmt = (
            "INSERT INTO demande_creacompte (`ID_compte`, `Type_compte`, `Date_creation`, `Rib`, `Valeur_depas`, `Solde`, `CC_Decouverte`, `AGIOS`)"
            "VALUES (%s, %s, %s, %s, %s, %b, %s)"
        )
        cursor.execute(insert_stmt, ligne_bd)
        logging.debug(cursor)
        cnx.commit()
        cnx.close()


for i in range(0, 10):
        ID_compte = '100' + str(i)
        Type_compte = 'nom' + str(i)
        Date_creation = 'prenom_' + str(i)
        Rib = str(random.randint(1000000000, 9999999999))
        Solde = str(random.randint(1000000000, 9999999999))

        ligne = (ID_compte, Type_compte, Date_creation, Rib, 'Valeur', Solde , 'None', 'Valeur')
        peuplement_creacompte(ligne, connexion())



def definit_user_type(login):
    cnx = connexion()
    cursor = cnx.cursor()
    try:

        cursor.execute("SELECT * FROM client where id = " + login)
    except mysql.Error as e:
        if e.errno == -1:
            try:
                cursor.execute("SELECT * FROM agent where id = " + login)
            except mysql.Error as f:
                if f.errno == -1:
                    try:
                        cursor.execute("SELECT * FROM admin where id = " + login)
                    except mysql.Error as g:
                        if g.errno == -1:
                            logging.warning("L'utilisateur n'existe pas")

                        else:
                            logging.info("L'utilisateur est du type admin")

                else:
                    logging.info("L'utilisateur est du type agent")
        else:
            logging.info("L'utilisateur est du type client")

# for i in range(0, 20):
#     ID = '000' + str(i)
#     NOM = 'nom_agent_0' + str(i)
#     PRENOM = 'prenom_agent_0' + str(i)
#     MATRICULE = 'AGT00' + str(i)
#     EMAIL = 'agent00{}@gestibank.com'.format(i)
#     nombre = str(random.randint(1000000000, 9999999999))
#     ligne = (ID, NOM, PRENOM, 'agent', MATRICULE, EMAIL, nombre, '2019-09-03')
#     peuplement_agent(ligne, connexion())

# for i in range(30,50):
#     ID='003' + str(i)
#     NOM='nom_client'+ str(i)
#     PRENOM='prenom_client_0'+ str(i)
#     EMAIL='client00{}@gestibank.com'.format(i)
#     nombre =str(random.randint(1000000000,9999999999))
#     ligne=(ID,NOM,PRENOM ,EMAIL ,nombre,'adresse','None')
#     peuplement_client(ligne, connexion())
"""

def creation_table(cnx, table='Employer'):
    cursor = cnx.cursor()
    insert_creat_table = ("CREATE TABLE " + table + "("
                                                    "id INT not null auto_increment primary key,"
                                                    "nom VARCHAR(20), prenom VARCHAR(20), datnais VARCHAR(20), ville VARCHAR(20),"
                                                    "sexe VARCHAR(01)) "
                          )
    logging.debug(insert_creat_table)
    cursor.execute(insert_creat_table)
    cnx.commit()
    logging.info("table crée")
    cnx.close()



def rempli_auto(cnx):
    cursor = cnx.cursor()
    with open("table.txt") as table:
        for ligne_bd in table:
            logging.debug(tuple((ligne_bd[:-1]).split(',')))
            ss = tuple((ligne_bd[:-1]).split(','))

            insert_stmt = (
                "INSERT INTO Employer (id, nom, prenom, datnais, ville, sexe ) "
                "VALUES (%s, %s, %s, %s, %s, %s)"
            )

            cursor.execute(insert_stmt, ss)
            cnx.commit()
    cnx.close()


def rempli(ligne_bd, cnx=connexion()):
    cursor = cnx.cursor()
    insert_stmt = (
        "INSERT INTO Employer (id, nom, prenom, datnais, ville, sexe ) "
        "VALUES (%s, %s, %s, %s, %s, %s)"
    )

    cursor.execute(insert_stmt,ligne_bd)
    cnx.commit()
    cnx.close()




def select_all(cnx, table):
    cursor = cnx.cursor()
    select_stmt = "SELECT * FROM " + table
    print(select_stmt)
    cursor.execute(select_stmt)
    logging.debug("affiche table")
    affiche_donne_curs(cursor)
    cnx.close()


def select_tuple(cnx, condition, table):
    cursor = cnx.cursor()
    select_stmt = "SELECT * FROM " + table + " WHERE " + condition
    logging.debug("affiche tuple")
    cursor.execute(select_stmt)
    affiche_donne_curs(cursor)
    cnx.close()


def select_colonne(cnx, colonne, table):
    logging.debug("affiche colonne")
    cursor = cnx.cursor()
    select_stmt = "SELECT " + colonne + " FROM " + table
    cursor.execute(select_stmt)
    affiche_donne_curs(cursor)
    cnx.close()


def drop_table(cnx, table):
    cursor = cnx.cursor()
    select_stmt = "DROP TABLE " + table
    logging.debug(select_stmt)
    cursor.execute(select_stmt)
    cnx.close()
    logging.info("table supprimé")


def miseajour(cnx, champ, valeur, condition, table='Employer'):
    cursor = cnx.cursor()
    update_stmt = "UPDATE " + table + " SET " + champ + " = '" + valeur + "' WHERE " + condition
    #update_stmt = "UPDATE %(employer)s SET %(champ)s = '%(valeur)s' WHERE %(condition)s"
    #update_param = {'employer': 'Employer', 'champ':'nom', 'valeur':'TITI', 'condition' :'id=726'}
    logging.debug(update_stmt)
    #cursor.execute(update_stmt, update_param)
    cursor.execute(update_stmt)
    cnx.commit()
    cnx.close()



if __name__ == "__main__":




    drop_table(connexion(), 'Employer')
    creation_table(connexion())
    rempli_auto(connexion())
    select_all(connexion(), 'Employer')
    rempli((111, '111', '111', '111', '111', '1'), connexion())
    select_tuple(connexion(), 'id=726', 'Employer')
    select_colonne(connexion(), 'nom', 'Employer')

    miseajour(connexion(), 'nom', 'TOUTOU', 'id=726', 'Employer')"""
