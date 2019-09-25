# sql
import mysql.connector as mysql
import logging

logging.basicConfig(level=logging.WARNING)


def connexion(base_de_donne='Gestibank', user='root', password=''): #@TODO cree user "gestiUser" sur sql
    try:
        cnx = mysql.connection.MySQLConnection(user=user, password=password,
                                         host='127.0.0.1', database=base_de_donne)


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

def errorlog(e):
    logging.warning("Error code:", e.errno)  # error number
    logging.warning("SQLSTATE value:", e.sqlstate) # SQLSTATE value
    logging.warning("Error message:", e.msg)  # error message
    logging.warning("Error:", e)  # errno, sqlstate, msg values
    s = str(e)
    logging.warning("Error:", s)  # errno, sqlstate, msg valu


if __name__=="__main__":
    cnx=connexion()