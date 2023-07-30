from models.assumptions import Assumptions

class CompanyConcept:
    def __init__(self, data, assumptions: Assumptions):
        # Extracting properties from the data
        self.fy = assumptions.LastReportedYear
        self.ticker = assumptions.ticker
        self.url = data.get("url", None)
        
        revenues = data.get("Revenues", None)
        sales_revenue_net = data.get("SalesRevenueNet", None)
        revenue_from_contract_ex_tax = data.get("RevenueFromContractWithCustomerExcludingAssessedTax", None)
        revenue_from_contract_inc_tax = data.get("RevenueFromContractWithCustomerIncludingAssessedTax", None)

        if (revenues != None):
            self.Revenue = revenues
        elif (sales_revenue_net != None):
            self.Revenue = sales_revenue_net
        elif (revenue_from_contract_ex_tax != None):
            self.Revenue = revenue_from_contract_ex_tax
        elif (revenue_from_contract_inc_tax != None):
            self.Revenue = revenue_from_contract_inc_tax
        else:
            self.Revenue = None 
        
        self.Interest_Expense = data.get("InterestExpense", None)
        
        #TODO logic to calculate this from the other fields if it is found to be null - otherwise forecast it based on historical trend % of sales
        self.Depreciation_and_Amortization = data.get("DepreciationDepletionAndAmortization", None)
        self.Pretax_Income = data.get("IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest", None)
        self.Operating_Income = data.get("OperatingIncomeLoss", None)
        # self.EBITDA = self.Operating_Income + self.Depreciation_and_Amortization if self.Operating_Income is not None and self.Depreciation_and_Amortization is not None else None
        self.Income_Tax_Expense = data.get("IncomeTaxExpenseBenefit", None)
        self.Net_Income_Before_Minority_Interest = data.get("ProfitLoss", None)
        self.Minority_Interests = data.get("NetIncomeLossAttributableToNoncontrollingInterest", None)
        self.Net_Income_Available_to_Common_Shareholders = data.get("NetIncomeLoss", None)
        self.Total_Cash_Preferred_Dividends = data.get("CommonStockDividendsPerShareDeclared", None)
        self.Other_Adjustments = data.get("EffectiveIncomeTaxRateReconciliationOtherAdjustments", None)
        self.Dividends_Paid = data.get("PaymentsOfDividends", None)
        # self.Chg_Retained_Earnings = self.Net_Income_Before_Minority_Interest - self.Dividends_Paid if self.Net_Income_Before_Minority_Interest is not None and self.Dividends_Paid is not None else None
        # self.Operating_Cash = data.get("SalesRevenueNet", None) * assumptions.OperatingCashPercent if data.get("SalesRevenueNet", None) is not None else None
        # self.Excess_Cash = data.get("CashAndCashEquivalentsAtCarryingValue", None) + data.get("ShortTermInvestments", None) - self.Operating_Cash if data.get("CashAndCashEquivalentsAtCarryingValue", None) is not None and data.get("ShortTermInvestments", None) is not None and self.Operating_Cash is not None else None
        
        ar_net_current = data.get("AccountsReceivableNetCurrent", None)
        r_net_current = data.get("ReceivablesNetCurrent", None)
        
        if (ar_net_current == None):
            self.Accounts_Notes_Receivable = r_net_current
        else:
            self.Accounts_Notes_Receivable = ar_net_current
        
        inventory_net = data.get("InventoryNet", None)
        assets_for_sale = data.get("AssetsHeldForSaleNotPartOfDisposalGroupCurrent", None)

        if (inventory_net == None):
            self.Inventories = assets_for_sale
        else:
            self.Inventories = inventory_net

        self.Other_Current_Assets = data.get("PrepaidExpenseAndOtherAssetsCurrent", None)
        # self.Total_Current_Assets = data.get("AssetsCurrent", None) + self.Operating_Cash + self.Excess_Cash + data.get("AccountsReceivableNetCurrent", None) + data.get("InventoryNet", None) + data.get("PrepaidExpenseAndOtherAssetsCurrent", None) if data.get("AssetsCurrent", None) is not None and self.Operating_Cash is not None and self.Excess_Cash is not None and data.get("AccountsReceivableNetCurrent", None) is not None and data.get("InventoryNet", None) is not None and data.get("PrepaidExpenseAndOtherAssetsCurrent", None) is not None else None
        # self.Net_Goodwill = data.get("Goodwill", None) + data.get("IntangibleAssetsNetExcludingGoodwill", None) if data.get("Goodwill", None) is not None and data.get("IntangibleAssetsNetExcludingGoodwill", None) is not None else None
        # self.Other_LT_Assets = data.get("NoncurrentAssets", None) - (data.get("AvailableForSaleSecuritiesNoncurrent", None) + data.get("PropertyPlantAndEquipmentNet", None) + data.get("IntangibleAssetsNetExcludingGoodwill", None)) if data.get("NoncurrentAssets", None) is not None and data.get("AvailableForSaleSecuritiesNoncurrent", None) is not None and data.get("PropertyPlantAndEquipmentNet", None) is not None and data.get("IntangibleAssetsNetExcludingGoodwill", None) is not None else None
        # self.Long_Term_Borrowings = data.get("LongTermDebt", None) - data.get("LongTermDebtCurrent", None) if data.get("LongTermDebt", None) is not None and data.get("LongTermDebtCurrent", None) is not None else None
        # self.Total_LT_Liabilities = data.get("Liabilities", None) - data.get("LiabilitiesCurrent", None) if data.get("Liabilities", None) is not None and data.get("LiabilitiesCurrent", None) is not None else None
        self.Total_Liabilities_and_Equity = data.get("LiabilitiesAndStockholdersEquity", None)
        self.Total_Assets = data.get("Assets", None)

    def to_dict(self):
        # Convert CompanyConcept instance to a dictionary
        return {
            "Fiscal Year (FY)": self.fy,
            "SEC URL": self.url,
            "Ticker": self.ticker,
            "Revenue": self.Revenue,
            "Interest Expense": self.Interest_Expense,
            "Depreciation and Amortization": self.Depreciation_and_Amortization,
            "Pretax Income": self.Pretax_Income,
            "Operating Income": self.Operating_Income,
            # "EBITDA": self.EBITDA,
            "Income Tax Expense": self.Income_Tax_Expense,
            "Net Income Before Minority Interest": self.Net_Income_Before_Minority_Interest,
            "Minority Interests (IS)": self.Minority_Interests,
            "Net Income Available to Common Shareholders": self.Net_Income_Available_to_Common_Shareholders,
            "Total Cash Preferred Dividends": self.Total_Cash_Preferred_Dividends,
            "Other Adjustments": self.Other_Adjustments,
            "Dividends Paid": self.Dividends_Paid,
            # "Chg_Retained_Earnings": self.Chg_Retained_Earnings,
            # "Operating_Cash": self.Operating_Cash,
            # "Excess_Cash": self.Excess_Cash,
            "Accounts & Notes Receivable": self.Accounts_Notes_Receivable,
            "Inventories": self.Inventories,
            "Other Current Assets": self.Other_Current_Assets,
            # "Total_Current_Assets": self.Total_Current_Assets,
            # "Net_Goodwill": self.Net_Goodwill,
            # "Other_LT_Assets": self.Other_LT_Assets,
            # "Long_Term_Borrowings": self.Long_Term_Borrowings,
            # "Total_LT_Liabilities": self.Total_LT_Liabilities,
            "Total Liabilities and Equity": self.Total_Liabilities_and_Equity,
            "Total Assets": self.Total_Assets
        }