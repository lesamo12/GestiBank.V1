#client
from compte_user.user import User
from compte_bancaire.compte import Compte
from sql.sql import connexion
import logging


class Client(User):
    def __init__(self, id):
        super().__init__("Client", id)
        cnx=connexion()
        cursor=cnx.cursor()
        data =("SELECT ID_compte FROM `compte` WHERE ID_client = "+id)
        logging.debug(data)
        cursor.execute(data)
        res=cursor.fetchall()
        self.liste_compte= []
        for colon in res :
            self.liste_compte.append(Compte(colon[0]))


    def modifMDP(self, oldMDP, newMDP):
        cnx = connexion()
        cnx.autocommit = True
        cursor = cnx.cursor()
        try:

            data = ("SELECT PASSWORD FROM login WHERE id = " + self.id +
                    " and Password = PASSWORD('" + oldMDP + "')")
            logging.debug(data)
            cursor.execute(data)
            changement = ("UPDATE login set Password = PASSWORD('" + newMDP +
                          "') where ID =" + self.id)

            logging.debug(changement)
            cursor.execute(changement)

            print("changement reussi")

        except Exception as e:
            logging.warning("Erreur de recherche ", e)
            logging.error(cursor.statement)
        cnx.close()

    def __str__(self):
        test = (self.id,
                self.nom,
                self.prenom,
                self.type_user,
                self.mail,
                self.tel,
                self.adresse,
                self.justificatif,
                self.liste_compte)

        return str(test)

    def realiser_virement (self,info_destinataire : dict , compte_emetteur: Compte,montant_transaction): # TODO envoi envoyer (notif) et Argent
        compte_emetteur.solde
        if (compte_emetteur.solvabilite()== True):
            compte_emetteur.solde = compte_emetteur.solde - montant_transaction
            logging.warning("solde positif == Transaction réussie")
            # TODO  effectuer_transaction ()
           #TODO  compte_emetteur.miseajour ('solde' : compte_emetteur.solde)

        #if (compte_emetteur.solvabilite()== False and self.CC_decouverte == True):
            #self.solde = self.solde - montant
            #logging.warning("solde negatif et CC autorise decouverte == Transaction réussie")
            #return self.solde
        if (Compte.solvabilite()== False ):
            logging.warning("solde negatif et CC non autorise decouverte == Transaction refusée")



    def mise_a_jour(self):
        list_arg = dict({"nom": self.nom,
                         "prenom": self.prenom,
                         "mail": self.mail,
                         "tel": self.tel,
                         "adresse": self.adresse,

                         })
        User.update("client", self.id, **list_arg)


# if __name__ == "__main__":
#
#  x=Client("145")
#  print(x)
#  print(x.liste_compte[0])
#
#
