import argparse
import os
import shutil
import logging
from progress.bar import Bar


def difference(lstOne, lstTwo):
    return sorted(list(set(lstOne)-set(lstTwo)))


def copyFolderDisk(lstFold, fromDisk, to):
    bar = Bar('Processing', fill='*', suffix='%(percent)d%%', max=len(lstFold))

    for fold in lstFold:
        logging.debug("Le dossier {0} est entrain d'être copié".format(fold))
        try:
            shutil.move(fromDisk+fold, to+fold)
            logging.info(
                "Copie réussi pour le dossier {0} dans {1}".format(fold, to))
        except:
            logging.warning("Erreur au niveau de la copie de {0} vers {1}".format(
                fromDisk+fold, to+fold))
            bar.next()
            continue

        bar.next()
    bar.finish()
    return


def listingRep(fromDisk, to):
    lstFrom = []
    lstTo = []

    # Test Répertoire
    try:
        os.listdir(to)
    except:
        logging.info("Le répertoire {0} a été crée !".format(to))
        os.mkdir(to)

    # Lecture des répertoires

    for folder in os.listdir(fromDisk):
        if folder != "/transfer.log":
            lstFrom.append("/"+folder)

    for folder in os.listdir(to):
        lstTo.append("/"+folder)

    return lstFrom, lstTo


def init():

    # Init parser
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument("-from", dest='fromDisk', type=str)
    parser.add_argument("-rep", dest='repository', type=str)
    parser.add_argument("-to", dest='saveDisk', type=str)

    args = parser.parse_args()

    return args


def main():
    # Get le disk à transfer + le répertoire ( obligoire, pour éviter de tout transférer ) + le disk de sauvegarde
    args = init()

    # Si les arguments ne sont pas saisies alors on quitte le programme
    if args.fromDisk is None or args.repository is None or args.saveDisk is None:
        print("Have a problem !")
        return

    fromDisk, to = args.fromDisk+"/" + \
        args.repository, args.saveDisk+"/"+args.repository

    # Init Logging
    logging.basicConfig(filename=fromDisk +
                        '/transfert.log', format='%(levelname)s:%(asctime)s:%(message)s', level=logging.DEBUG)

    lstFrom, lstTo = listingRep(fromDisk, to)
    lstFolder = difference(lstFrom, lstTo)

    logging.debug("Démarrage de la copie des dossiers")

    copyFolderDisk(lstFolder, fromDisk, to)

    logging.debug("Fin de la copie des dossiers")


if __name__ == "__main__":
    main()
