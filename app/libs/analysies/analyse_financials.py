# https://en.wikipedia.org/wiki/Piotroski_F-score
# Le score F de Piotroski est un nombre compris entre 0 et 9 qui est utilisé pour évaluer la solidité de la situation financière de l'entreprise
#
# Rentabilité
#  - Rendement des actifs (1 point s'il est positif dans l'année en cours, 0 sinon);
#  - Cash Flow opérationnel (1 point s'il est positif dans l'année en cours, 0 dans le cas contraire);
#  - Variation du rendement des actifs (ROA) (1 point si le ROA est plus élevé dans l'année en cours par rapport à la précédente, 0 dans le cas contraire);
#  - Accruals (1 point si le cash flow opérationnel / l'actif total est supérieur au ROA de l'année en cours, 0 dans le cas contraire);
# Effet de levier, liquidité et source des fonds
#  - Évolution du ratio de levier (long terme) (1 point si le ratio est inférieur cette année par rapport à la précédente, 0 sinon);
#  - Changement du ratio courant (1 point s'il est plus élevé dans l'année en cours par rapport à la précédente, 0 sinon);
#  - Modification du nombre d'actions (1 point si aucune nouvelle action n'a été émise au cours de l'année écoulée);
# Efficacité opérationnelle
#  - Variation de la marge brute (1 point si elle est plus élevée dans l'année en cours par rapport à la précédente, 0 dans le cas contraire);
#  - Évolution du ratio de rotation des actifs (1 point s'il est plus élevé dans l'année en cours par rapport à la précédente, 0 dans le cas contraire);

import datetime
from pprint import pprint
from utils import utils as utl
from libs.yahoo_fin import stock_info as sf
from .analyse import AnalyseData

class AnalyseFondamental(object):
    def __init__(self, ticker):

        self.per_datas = sf.get_quote_table(ticker)
        self.resultat_datas = sf.get_income_statement(ticker)
        self.balance_datas = sf.get_balance_sheet(ticker)
        self.cash_flow_datas = sf.get_cash_flow(ticker)
        self.statistic_datas = sf.get_stats(ticker)
        self.dividendes = sf.get_dividends(ticker)

        self.year_atual = self.resultat_datas.keys()[0]
        self.year_before = self.resultat_datas.keys()[1]

        # pprint(self.resultat_datas)
        # pprint(self.balance_datas)
        # pprint(self.cash_flow_datas)
        # pprint(self.per_datas)
        # pprint(self.statistic_datas)

        self.datas = {}
        self.data_analyse = {}

        self.get_histoty_prices(ticker)
        self.set_var()
        self.datas_dict()
        self.data_for_analyse()

        self.analyse = AnalyseData(self.data_analyse)
        self.extend_dict_data()

    def set_var(self):
        self.actions = None
        if self.statistic_datas['Value'][9][-1] == "B":
            self.actions = float(self.statistic_datas['Value'][9].replace('B', '')) * 1000000000
        if self.statistic_datas['Value'][9][-1] == "M":
            self.actions = float(self.statistic_datas['Value'][9].replace('M', '')) * 1000000

        self.price = self.per_datas['Quote Price']
        self.per = self.per_datas['PE Ratio (TTM)']
        self.bna = self.per_datas['EPS (TTM)']
        self.capitalisation = self.per_datas['Market Cap']

        self.ebitda = self.resultat_datas.loc['ebit']
        self.benefice_net = self.resultat_datas.loc['netIncome']
        self.revenue_total = self.resultat_datas.loc['totalRevenue']
        self.chiffre_affaire = self.resultat_datas.loc['grossProfit']  # benefice brut

        self.cash_flow = self.balance_datas.loc['cash']
        self.debt = self.balance_datas.loc['longTermDebt']
        self.actifs_total = self.balance_datas.loc['totalAssets']
        self.actifs_total_short_therm = self.balance_datas.loc['totalCurrentAssets']
        self.passif_total_short_therm = self.balance_datas.loc['totalCurrentLiabilities']
        self.total_capitaux_propre = self.balance_datas.loc['totalStockholderEquity']

        self.free_cash_flow = self.cash_flow_datas.loc['totalCashFromOperatingActivities']


    def profitability(self):
        #Scores  # 1 and 2 - net income
        net_income = self.benefice_net[self.year_atual]
        net_income_py = self.benefice_net[self.year_before]
        ni_score = 1 if net_income > 0 else 0
        ni_score_2 = 1 if net_income > net_income_py else 0

        # Score #3 - operating cash flow
        op_cf = self.free_cash_flow[self.year_atual]
        op_cf_score = 1 if op_cf > 0 else 0

        # Score #4 - change in RoA
        avg_assets = (self.actifs_total[self.year_atual]
                      + self.actifs_total[self.year_before]) / 2
        avg_assets_py = (self.actifs_total[self.year_before]
                         + self.actifs_total[self.resultat_datas.keys()[2]]) / 2
        roa = net_income / avg_assets
        roa_py = net_income_py / avg_assets_py
        roa_score = 1 if roa > roa_py else 0

        # Score #5 - Accruals
        total_assets = self.actifs_total[self.year_atual]
        accruals = op_cf / total_assets - roa
        ac_score = 1 if accruals > 0 else 0

        profitability_score = ni_score + ni_score_2 + op_cf_score + roa_score + ac_score
        return profitability_score


    def leverage(self):
        # Score #6 - long-term debt ratio
        try:
            lt_debt = self.debt[self.year_atual]
            total_assets = self.actifs_total[self.year_atual]
            debt_ratio = lt_debt / total_assets
            debt_ratio_score = 1 if debt_ratio < 0.4 else 0
        except:
            debt_ratio_score = 1

        # Score #7 - Current ratio
        current_assets = self.actifs_total_short_therm[self.year_atual]
        current_liab = self.passif_total_short_therm[self.year_atual]
        current_ratio = current_assets / current_liab
        current_ratio_score = 1 if current_ratio > 1 else 0

        leverage_score = debt_ratio_score + current_ratio_score
        return leverage_score


    def operating_efficiency(self):
        # Score #8 - Gross margin
        gp = self.chiffre_affaire[self.year_atual]
        gp_py = self.chiffre_affaire[self.year_before]
        revenue =self.revenue_total[self.year_atual]
        revenue_py = self.revenue_total[self.year_before]
        gm = gp / revenue
        gm_py = gp_py / revenue_py
        gm_score = 1 if gm > gm_py else 0

        # Score #9 - Asset turnover
        avg_assets = (self.actifs_total[self.year_atual]
                      + self.actifs_total[self.year_before]) / 2
        avg_assets_py = (self.actifs_total[self.year_before]
                         + self.actifs_total[self.resultat_datas.keys()[2]]) / 2

        at = revenue / avg_assets  # at = asset turnover
        at_py = revenue_py / avg_assets_py
        at_score = 1 if at > at_py else 0

        operating_efficiency_score = gm_score + at_score
        return operating_efficiency_score


    def total_score(self):
        profitability = self.profitability()
        leverage = self.leverage()
        efficiency = self.operating_efficiency()
        return profitability + leverage + efficiency


    def datas_dict(self):
        self.datas['YEAR'] = [date.strftime("%Y") for date in self.resultat_datas.keys().tolist()]
        self.datas['EBITDA'] = utl.format_data(self.ebitda.values.tolist())
        self.datas['Bénéfice Net'] = utl.format_data(self.benefice_net.values.tolist())
        self.datas['Revenus Total'] = utl.format_data(self.revenue_total.values.tolist())
        self.datas["Actifs Total"] = utl.format_data(self.actifs_total.values.tolist())
        self.datas["Chiffre d'affaires"] = utl.format_data(self.chiffre_affaire.values.tolist())
        self.datas["Trésorie"] = utl.format_data(self.cash_flow.values.tolist())
        self.datas["Capitaux Propre"] = utl.format_data(self.total_capitaux_propre.values.tolist())
        self.datas['Score'] = [self.total_score()]

        self.bna_years()
        self.per_years()
        self.debt_ratio()
        self.bvps_ratio()
        self.capitalisation_ratio()
        self.dividendes_ratio()
        self.roe_roa_ratio(roa=False)
        self.roe_roa_ratio(roa=True)


    def data_for_analyse(self):
        self.data_analyse['Actifs Total'] = self.datas['Actifs Total']
        self.data_analyse['BNA'] = self.datas['BNA']
        self.data_analyse['BVPS'] = self.datas['BVPS']
        self.data_analyse['Bénéfice Net'] = self.benefice_net.values.tolist()
        self.data_analyse['Capitaux Propre'] = self.total_capitaux_propre.values.tolist()
        self.data_analyse["Chiffre d'affaires"] = self.chiffre_affaire.tolist()
        self.data_analyse['Dividendes'] = self.datas['Dividendes']
        self.data_analyse['EBITDA'] = self.ebitda.values.tolist()
        self.data_analyse['PER'] = self.datas['PER']
        self.data_analyse['ROA'] = self.datas['ROA']
        self.data_analyse['ROE'] = self.datas['ROE']
        self.data_analyse['Revenus Total'] = self.revenue_total.values.tolist()
        self.data_analyse['Trésorie'] = self.cash_flow.values.tolist()
        self.data_analyse['YEAR'] = self.datas['YEAR']
        self.data_analyse['PRICE'] = self.price_dates


    def get_histoty_prices(self, tick):
        dates = self.resultat_datas.keys()
        self.history = sf.get_data(tick, interval="1d")['close']
        self.price_dates = []
        for date in dates:
            date_ = date.strftime("%Y-%m-%d")
            try:
                self.price_dates.append(self.history[date_])
            except:
                date_ = (date + datetime.timedelta(days=3)).strftime("%Y-%m-%d")
                self.price_dates.append(self.history[date_])


    def bna_years(self):
        bna = [round(float(resultat / int(self.actions)), 2) for resultat in self.benefice_net.values.tolist()]
        self.datas['BNA'] = bna


    def per_years(self):
        bna = self.datas['BNA']
        per = [round((j / i), 2) for i, j in zip(bna, self.price_dates)]
        per[0] = self.per
        self.datas["PER"] = per


    def debt_ratio(self):
        dettes = utl.remove_nan(self.debt.values.tolist())
        ebitda = utl.remove_nan(self.ebitda.values.tolist())
        dette_calcul = [round(i/j) for i, j in zip(dettes, ebitda)]
        self.datas["Dette"] = ["{}%".format(i) for i in dette_calcul]
        self.data_analyse['Dette'] = dette_calcul


    def bvps_ratio(self):
        # BVPS : capitaux propres / nbr actions
        capitaux = utl.remove_nan(self.total_capitaux_propre)
        self.datas['BVPS'] = [round((i/self.actions), 2) for i in capitaux]


    def capitalisation_ratio(self):
        # Capitalistion annee prece : prix * nbr actions
        capitalisation = [i*self.actions for i in self.price_dates]
        self.datas['Capitalisation'] = utl.format_data(capitalisation)
        self.data_analyse['Capitalisation'] = capitalisation


    def dividendes_ratio(self):
        # Dividende % : Dividende net par action / Cours de bourse
        dividendes = [list(set(self.dividendes.loc[year]['dividend'].tolist())) for year in self.datas['YEAR']]
        rendement = []
        for i, price in zip(dividendes, self.price_dates):
            if len(i) > 1:
                i = sum(i)
            else:
                i = float(i[0])
            price = round(float(price), 2)
            calcul_rend = (i/price)*100
            calcul_rend = round(calcul_rend, 2)
            rendement.append("{}€".format(calcul_rend))

        self.datas['Dividendes'] = dividendes
        self.datas['Dividendes Rendement'] = ["{}%".format(i) for i in rendement]


    def roe_roa_ratio(self, roa=False):
        # Le ROE mesure la rentabilité des capitaux propres que les actionnaires d’une entreprise
        # mettent à sa disposition. Il permet de calculer la rentabilité financière des fonds propres.
        # roe = Bénéfices / Capitaux Propre => %
        #
        # Le ROA permet de mesurer la capacité et l’efficacité d’une entreprise
        # à générer des profits avec ses actifs.
        # roa = Bénéfices / Actifs  => %
        #
        #
        capitaux = [int(i.replace(',','')) for i in self.datas["Capitaux Propre"]]
        benefce = [int(i.replace(',','')) for i in self.datas['Bénéfice Net']]
        actifs = [int(i.replace(',', '')) for i in self.datas["Actifs Total"]]

        data = capitaux
        if roa:
            data = actifs

        result = []
        for i, j in zip(benefce, data):
            try:
                calcul = round((i/j)*100, 2)
            except:
                calcul = 0
            result.append("{}%".format(calcul))

        if roa:
            self.datas['ROA'] = result
        else:
            self.datas['ROE'] = result


    def extend_dict_data(self):
        for title, data in self.analyse.analyse.items():
            self.datas[title].append(data)

if __name__ == '__main__':
    test = AnalyseFondamental("AAPL")
    pprint(test.data_analyse)
    pprint(test.analyse.__dict__)
    # testq = AnalyseFondamental("BN.PA")


