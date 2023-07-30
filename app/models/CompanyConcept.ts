// CompanyConcept.ts
export interface CompanyConcept {
    fy: number;
    Revenue?: number;
    Interest_Expense?: number;
    Depreciation_and_Amortization?: number;
    Pretax_Income?: number;
    Operating_Income?: number;
    EBITDA?: number | null;
    Income_Tax_Expense?: number;
    Net_Income_Before_Minority_Interest?: number;
    Minority_Interests?: number;
    Net_Income_Available_to_Common_Shareholders?: number;
    Total_Cash_Preferred_Dividends?: number;
    Other_Adjustments?: number;
    Dividends_Paid?: number;
    Chg_Retained_Earnings?: number | null;
    Operating_Cash?: number | null;
    Excess_Cash?: number | null;
    Accounts_Notes_Receivable?: number;
    Inventories?: number;
    Other_Current_Assets?: number;
    Total_Current_Assets?: number | null;
    Net_Goodwill?: number | null;
    Other_LT_Assets?: number | null;
    Long_Term_Borrowings?: number | null;
    Total_LT_Liabilities?: number | null;
    Total_Liabilities_and_Equity?: number | null;
  }
  