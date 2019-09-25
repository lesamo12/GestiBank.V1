import logging
from sql.sql import connexion
from datetime import date
from compte_user.user import User
from demande_crea.demande_crea_compte import DemandCreaCompte
from compte_user.admin import Admin
from compte_user.agent import Agent
from compte_user.client import Client
import os



retour_type=User.login("12","bonjour")
print("login valider : ",retour_type)
Administrateur=Admin("12")
print("Voila l'administarteur: {}".format(Administrateur))
os.system("pause")
print("-----------------------------------------------------------------------------")


Agentn01 = {"nom": "Agent",
            "prenom": "marc",
            "id": "007",
            "mail": "truc@mac.com",
            "tel": "01546843"
            }


Administrateur.cree_compte_agent(Agentn01)
Agent007=Agent("007")
print("Voila l'agent: {}".format(Agent007))
os.system("pause")
print("-----------------------------------------------------------------------------")


#Administrateur.suprimer_agent("007")
#Administrateur.cree_compte_agent(Agentn01)
#Agent007=Agent("007")
#print(Agent007)
#print("-----------------------------------------------------------------------------")
# os.system("pause")
demande_compte = {"nom": "dieoz",
                  "prenom": "marc",
                  "id": "145",
                  "mail": "truc@mac.com",
                  "tel": "01546843",
                  "adresse": "5 rue de la voie rouge 91216  Lamotte",
                  "justificatif": "repertoir\distant\ "
                  }
demande_no1 = DemandCreaCompte(demande_compte)
Administrateur.affecter_demande(demande_no1,"007")
print(demande_no1)
os.system("pause")
print("-----------------------------------------------------------------------------")

retour_type=User.login("007","bonjour")
print("le retour est ",retour_type)
os.system("pause")
print("-----------------------------------------------------------------------------")


Agent007.validation_Crea(demande_no1,False)
print(demande_no1)
Agent007.validation_Crea(demande_no1,True)
print(demande_no1)
Client001=Client("145")
print(Client001)
modif={"nom": "autre",
       "prenom": "edie",
       "id": "145",
       "mail": "truc@mac.com",
       "tel": "01546843",
       "adresse": "5 rue de la voie rouge 91216  Lamotte"}
print("-----------------------------------------------------------------------------")
os.system("pause")
Agent007.modif_compte_client(Client001, modif)
print(Client001)
print(Client001.liste_compte[0])




