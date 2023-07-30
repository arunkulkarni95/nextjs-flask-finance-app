class Assumptions:
    def __init__(self, last_reported_year, ticker, number_years, operating_cash_percent=None, wacc=None, cv_noplat=None, cv_roiv=None, cv_g=None, shares_outstanding=None):
        self.LastReportedYear = last_reported_year
        self.ticker = ticker
        self.number_years = number_years
        self.OperatingCashPercent = operating_cash_percent
        self.WACC = wacc
        self.CVNOPLAT = cv_noplat
        self.CVROIV = cv_roiv
        self.CVG = cv_g
        self.SharesOutstanding = shares_outstanding
