import logging
from sql.sql import connexion
import random
from compte_user.user import User
from datetime import date

class Compte:
    def __init__(self, id_compte):

        cnx = connexion()
        cursor = cnx.cursor()
        param = ("SELECT `ID_compte`, `Type_compte`, `Date_creation`, `Rib`,`Solde`,`ID_client`"
                 " FROM `compte` WHERE ID_compte = " + str(id_compte))
        cursor.execute(param)
        element = cursor.fetchone()
        logging.debug(element)
        self.id_compte = element[0]
        self.type_compte = element[1]
        self.date_creation = element[2]
        self.rib = element[3]
        self.solde = element[4]
        self.id_client = element[5]

    @classmethod
    def creation_compteban(self, id_client):
        if User.trouver_id('client', id_client) is True:
            cnx = connexion()
            cursor = cnx.cursor()
            id_compte = (random.randint(1000000000, 9999999999))
            type_compte = 'COURANT'
            date_creation =  str (date.today())
            rib = str(random.randint(1000000000, 9999999999))
            solde = 0.0

            ajout_clien = ("INSERT INTO `compte` (`id_compte`, `id_client`, `type_compte`, `rib`,"
                           " `solde`, `date_creation`) VALUES ( %s, %s, %s, %s, %s, %s)")
            demande_clien = (id_compte, id_client, type_compte, rib,solde, date_creation);

            logging.debug(ajout_clien + str(demande_clien))
            try:
                cursor.execute(ajout_clien, demande_clien)
                cnx.commit()
                logging.info("insertion réussi")
            except Exception as e:
                logging.warning("Erreur insertion", e)
            finally:
                cnx.close()
        else:
            logging.warning("Utilisateur n'existe pas ")

    def __str__(self):
        test = (self.id_compte,
                self.type_compte,
                self.date_creation,
                self.rib,
                self.solde,
                self.id_client)

        return str(test)

    def solvabilite(self,valeur_virement=0):
        return self.sode >= valeur_virement

if __name__ == "__main__":
    Compte.creation_compteban('145')