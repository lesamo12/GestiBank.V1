import mysql.connector as mysql
import logging
logging.basicConfig(level=logging.DEBUG)
def connexion(user='root', password=''): #@TODO cree user "gestiUser" sur sql
    try:
        cnx = mysql.connection.MySQLConnection(user=user, password=password,
                                         host='127.0.0.1')


    except mysql.connection.errors.Error as err:
        if err.errno == mysql.errorcode.ER_ACCESS_DENIED_ERROR:
            logging.debug("Il y a un problème avec votre user name ou password")
        elif err.errno == mysql.errorcode.ER_BAD_DB_ERROR:
            logging.debug("La base n’existe pas")
        else:
            logging.debug(err)
    else:
        logging.info(" connexion reussi")
        return cnx

cnx=connexion()
cursor=cnx.cursor()
for line in open("database.sql"):
    try:
        cursor.execute(line)
        cnx.commit()
    except Exception as e:
        logging.warning("erreur",e)
    else:
        print(line)