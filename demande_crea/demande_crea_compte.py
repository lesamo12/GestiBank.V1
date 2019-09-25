"""Le front renvoi un dictionnaire contenant toutes les valeurs"""
import logging
from sql.sql import connexion


class DemandCreaCompte:

    def __init__(self, valeur):
        # logging.debug(type(valeur))
        if type(valeur) == type(dict()):
            # logging.debug("inside dict")
            self.nom = valeur["nom"]
            self.prenom = valeur["prenom"]
            self.id = valeur["id"]
            self.mail = valeur["mail"]
            self.tel = valeur["tel"]
            self.adresse = valeur["adresse"]
            self.justificatif = valeur["justificatif"]
            self.valid = None
            self.affect = None

        elif type(valeur) == type(tuple()):
            # logging.debug("inside tuple")
            self.nom = valeur[0]
            self.prenom = valeur[1]
            self.id = valeur[2]
            self.mail = valeur[3]
            self.tel = valeur[4]
            self.adresse = valeur[5]
            self.justificatif = valeur[6]
            self.valid = valeur[7]
            self.affect = valeur[8]

    def enregistrement(self):  # Stocakge d'une demmande dans la base de donnee (table demande)
        cnx = connexion()
        cursor = cnx.cursor()

        try:
            insert_stmt = ("INSERT into demande_creation (nom,prenom,id,mail,telephone,adresse,justificatif)"
                           "VALUES (%s ,%s, %s, %s,%s ,%s, %s)")
            data = [(self.nom, self.prenom, self.id, self.mail, self.tel, self.adresse, self.justificatif)]
            cursor.execute(insert_stmt, data)
            cnx.commit()

        except:
            logging.warning("Problème a l'insertion")
            return False

        else:
            return True
        finally:
            cnx.close()

    def affectation(self, agent):  # l'admin affect un client a un agent
        cnx = connexion()
        cursor = cnx.cursor()
        self.affect = agent
        try:
            affectation = ("UPDATE demande_creacompte SET affect = " + self.affect + " WHERE  id =" + self.id)
            logging.debug(affectation)
            cursor.execute(affectation)
            cnx.commit()

        except:
            logging.warning("Problème d'affectation")
            return False
        else:
            return True
        finally:
            cnx.close()

    def validation(self, valide):  # L'agent valide le client
        cnx = connexion()
        cursor = cnx.cursor()
        self.valid = valide
        try:
            validation = ("UPDATE demande_creacompte SET valide = " + self.valid + " WHERE  id =" + self.id)
            logging.debug(validation)
            cursor.execute(validation)
            cnx.commit()

        except:
            logging.warning("Problème de  validation")
            return False
        else:
            return True
        finally:
            cnx.close()

    def __str__(self):
        test = (
            self.nom,
            self.prenom,
            self.id,
            self.mail,
            self.tel,
            self.adresse,
            self.justificatif,
            self.valid,
            self.affect
        )
        return str(test)

    def creation_compte_client(self):
        cnx = connexion()
        cursor = cnx.cursor()
        

        ajout_clien = ("INSERT INTO client (ID, NOM, PRENOM, MAIL, TEL, ADRESSE, JUSTIFICATIF, id_agent)"
                       "VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)")
        demande_clien = (self.id, self.nom, self.prenom, self.mail, self.tel, self.adresse, self.justificatif,
                         self.affect)
        try:
            cursor.execute(ajout_clien, demande_clien)
            cnx.commit()

        except Exception as e:
            logging.warning("problème d'insertion ", e)
        finally:
            cnx.close()



# if __name__ == "__main__":
    # cnx = connexion()
    # test = {"nom": "dieoz",
    #         "prenom": "marc",
    #         "id": "145",
    #         "mail": "truc@mac.com",
    #         "tel": "01546843",
    #         "adresse": "5 rue de la voie rouge 91216  Lamotte",
    #         "justificatif": "repertoir\distant\ ",
    #         "affect" :  "999"
    #         }
    #
    # objet_test = DemandCreaCompte(test)
    #
    # # objet_test2=DemandCreaCompte(('dieoz', 'marc', '145', 'truc@mac.com', '01546843', '5 rue de la voie rouge 91216  Lamotte', 'repertoir\\distant\\ ', None, None)
    # objet_test.validation(True)
    # objet_test.affectation("999")
    # print(objet_test)
    # objet_test.creation_compte_client()

