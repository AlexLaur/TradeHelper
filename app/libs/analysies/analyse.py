from utils import utils as utl
from pprint import pprint

class AnalyseData:
    def __init__(self, data):
        self.data = data
        self.analyse = {}
        # pprint(self.data)

        self.bvps_analyse()
        self.per_analyse()
        self.dette_analyse()
        self.chiffre_affaire_analyse()


    def bvps_analyse(self):
        bvps, index = utl.get_last_value(self.data['BVPS'])
        analyse = ""
        if float(bvps) < float(self.data['PRICE'][index]):
            analyse = "Prix SUR-COTE à sa valeur intrasèque : {} €.".format(bvps)
        elif float(bvps) > float(self.data['PRICE'][index]):
            analyse = "Prix SOUS-COTE à sa valeur intrasèque : {}€".format(bvps)
        self.analyse['BVPS'] = analyse


    def per_analyse(self):
        per, index = utl.get_last_value(self.data['PER'])
        analyse = ""
        if per <= 0:
            analyse = "PER %s NégatifG" % per
        elif per >= 17:
            analyse = "PER %s Eleve , Entreprise SUR-COTE." % per
        elif 10 <= per < 17:
            analyse = "PER %s Normal , Entreprise OK." % per
        elif per < 10:
            analyse = "PER %s < 10, Entreprise SOUS-COTE." % per
        self.analyse['PER'] = analyse


    def dette_analyse(self):
        dette, index = utl.get_last_value(self.data['Dette'])
        analyse = ""
        try:
            if 0 < dette <= 2:
                analyse = 'Dette Controle'
            elif dette <= 0:
                analyse = 'Dette Aucune'
            elif dette > 2:
                analyse = 'Dette Eleve'
        except:
            analyse = 'Pas de Dette'
        self.analyse['Dette'] = analyse


    def chiffre_affaire_analyse(self):
        chiffre = self.data["Chiffre d'affaires"]
        if chiffre[0] > chiffre[1]:
            analyse = "Chiffre d'affaire en croissance."
        else:
            analyse = "Chiffre d'affaire en décroissance."
        self.analyse["Chiffre d'affaires"] = analyse

