from pprint import pprint
from utils import utils as utls


class AnalyseData(object):
    def __init__(self, data=None):
        self.data = data["data_site"]

        # pprint(self.data)
        self.nom_entreprise = data["entreprise"]
        self.data = data["data_site"]
        self.prix = self.data["prix"]
        self.tresorie = self.data["Tresorie"]

        self.analyse = {}

        self.annee_en_cour = 3
        self.annee_prec = 2

        self.launcher()

    def launcher(self):
        self.bvps()
        self.per()
        self.dette()
        self.capitalisaton()
        self.chiffreAffaire()
        self.bna()
        self.dividende()
        self.roe_roa()
        # self.tauxDistri()

    def bvps(self):
        bvps = self.data["BVPS"][self.annee_prec].replace(",", ".")
        analyse = ""
        if float(bvps) < float(self.prix):
            analyse = "Prix SUR-COTE à sa valeur intrasèque : {} €.".format(
                bvps
            )
        elif float(bvps) > float(self.prix):
            analyse = "Prix SOUS-COTE à sa valeur intrasèque : {}€".format(
                bvps
            )
        self.analyse["BVPS"] = analyse

    def per(self):
        per = float(self.data["PER"][self.annee_prec][:-1].replace(",", "."))
        analyse = ""
        if per <= 0:
            analyse = "PER %s NEGATIG" % per
        elif per >= 17:
            analyse = "PER %s eleve , Entreprise SUR-COTE." % per
        elif 10 <= per < 17:
            analyse = "PER %s Normal , Entreprise OK." % per
        elif per < 10:
            analyse = "PER %s < 10, Entreprise SOUS-COTE." % per
        self.analyse["PER"] = analyse

    def dette(self):
        dette = self.data["Dette Nette"]
        leverage = self.data["Leverage"]
        analyse = ""
        anal_leverage = []
        dette, leverage = utls.refacto_dette(dette, leverage)
        for i in leverage[:3]:
            try:
                if 0 < i <= 2:
                    anal_leverage.append("Controle")
                elif i <= 0:
                    anal_leverage.append("Aucune")
                elif i > 2:
                    anal_leverage.append("Eleve")
            except:
                anal_leverage.append("Pas de Dette")
        count_ana = {
            "controle": anal_leverage.count("Controle"),
            "aucun": anal_leverage.count("Aucune"),
            "eleve": anal_leverage.count("Eleve"),
        }
        for i, cout in count_ana.items():
            if cout == max(count_ana.values()):
                if i == "aucun":
                    analyse = "Aucune Dette"
                elif i == "controle":
                    analyse = "Dette Controle"
                elif i == "eleve":
                    analyse = "Sur-Endette"
        leverage = leverage[:3]
        leverage.append(analyse)
        self.analyse["Dette"] = analyse

    def capitalisaton(self):
        capitalisation = self.data["Capitalisation"][self.annee_prec]
        if int(capitalisation.replace(" ", "")) > 100:
            analyse_capit = "Grosse Entreprise {} M €".format(capitalisation)
        else:
            analyse_capit = "Petite Entreprise {} M €".format(capitalisation)
        self.analyse["Capitalisation"] = analyse_capit

    def chiffreAffaire(self):
        chiffreA = self.data["Chiffre d'affaires"][:3]
        chiffre = []
        for i in chiffreA:
            chiffre.append(i.replace(" ", ""))
        croi, decroi = utls.croissance(chiffre)
        if croi > decroi:
            analyse = (
                "Chiffre d'affaire en croissance sur les 3 dernieres années."
            )
        elif croi < decroi and chiffre[-1] > chiffre[1]:
            analyse = "Chiffre d'affaire en décroissance mais Chiffre d'affaire en hausse la derniere année."
        else:
            analyse = (
                "Chiffre d'affaire en décroissance sur les 3 dernieres années."
            )
        # chiffreA.append(analyse)
        self.analyse["Chiffre d'affaires"] = analyse

    def bna(self):
        bna = self.data["BNA"][:3]
        crois, decrois = utls.croissance(bna)
        if crois > decrois:
            analyse = "BNA en croissance sur les 3 dernieres années."
        elif crois < decrois and bna[-1] > bna[1]:
            analyse = "BNA en décroissance mais Chiffre d'affaire en hausse la derniere année."
        else:
            analyse = "BNA en décroissance sur les 3 dernieres années."
        self.analyse["BNA"] = analyse

    def dividende(self):
        dividendes = self.data["Dividende"]
        try:
            all_div = []
            for div in dividendes[: self.annee_en_cour]:
                all_div.append(div)
            croi, decroi = utls.croissance(dividendes)
            if croi > decroi:
                analyse = "Dividende en croissance."
            else:
                analyse = "Dividende en décroissances."
        except:
            analyse = "No Data"
        self.analyse["Dividende"] = analyse

    # A VOIR
    # def bna_dividend(self):
    #     bna = self.analyse['BNA']
    #     if bna[3].split(' ')[2] == "croissance" and dividende['analyse'][2] == "croissance":
    #         analyse = "BNA et Dividende en croissance "
    #     elif bna[3].split(' ')[2] == "décroissances" and dividende['analyse'][2] == "croissance":
    #         analyse = "BNA en décroissance mais Dividende en croissance"
    #     else:
    #         analyse = "BNA et Dividende en décroissance"
    #     div = []
    #     for annee, prix in dividende.items():
    #         div.append(prix)
    #
    #

    def tauxDistri(self):
        year = self.data["Année"][:3]
        bna = self.data["BNA"][:3]
        dividende = self.data["Dividende"][:3]
        dividend_ = []
        bna_ = []
        for anne, div in dividende.items():
            if anne not in year:
                continue
            dividend_.append(float(div[:-1].replace(",", ".")))
        for bn in bna:
            bna_.append(float(bn.replace(",", ".")))

        tauxdistri = []
        zip_object = zip(dividend_, bna_)
        for list1_i, list2_i in zip_object:
            tauxdistri.append("%.2f" % ((list1_i / list2_i) * 100))

        croi, decroi = utls.croissance(tauxdistri)
        if croi > decroi:
            analyse = "Croissance"
        else:
            analyse = "Decroissance"
        tauxdistri.append(analyse)
        self.analyse["Taux distribution"] = tauxdistri

    def roe_roa(self):
        self.analyse["ROE"] = self.data["ROE"]
        self.analyse["ROA"] = self.data["ROA"]
