interface Assumptions {
    lastReportedYear: number;
    ticker: string;
    number_years: number;
    operatingCashPercent?: number;
    wacc?: number;
    cvNoplat?: number;
    cvRoiv?: number;
    cvG?: number;
    sharesOutstanding?: number;
  }
  
  export default Assumptions;
  