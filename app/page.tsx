'use client'
// pages/page.tsx
import React, { useState } from 'react';
import axios from 'axios';
import CompanyConceptsTable from './components/CompanyConceptTable'; // Corrected import path

interface FinancialData {
  fy: number;
  [key: string]: number | string;
}

interface StockPriceResponse {
  ticker: string;
  stock_price: number;
}

const Page: React.FC = () => {
  const [ticker, setTicker] = useState<string>('');
  const [fiscalYear, setFiscalYear] = useState<string>('');
  const [numYears, setNumYears] = useState<string>('');
  const [financialData, setFinancialData] = useState<FinancialData[]>([]);
  const [error, setError] = useState<string>('');
  const [stockPrice, setStockPrice] = useState<number | null>(null); // New state for stock price

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!ticker.match(/^[A-Za-z]+$/)) {
      setError('Ticker must contain only letters (uppercase or lowercase).');
      return;
    }

    const currentYear = new Date().getFullYear();
    const lastYear = currentYear - 1;
    if (parseInt(fiscalYear) > lastYear) {
      setError(`Fiscal Year cannot be greater than ${lastYear}.`);
      return;
    }

    const numYearsInt = parseInt(numYears);
    if (numYearsInt <= 0 || numYearsInt > 10) {
      setError('Number of historical years must be between 1 and 10.');
      return;
    }

    try {
      // Updated API endpoint with correct URL
      const response = await axios.post<FinancialData[]>('/api/company-concepts', {
        ticker: ticker.toUpperCase(),
        fiscal_year: fiscalYear,
        num_years: numYears,
      });
      setFinancialData(response.data);
      setError('');

      const stockPriceResponse = await axios.post<StockPriceResponse>('/api/stock-price', {
        ticker: ticker.toUpperCase(),
      });
      setStockPrice(stockPriceResponse.data.stock_price);
    } catch (error) {
      console.error('Error fetching financial data:', error);
      setError('Error fetching financial data. Please try again later.');
    }
  };

  const currentYear = new Date().getFullYear();
  const authorWebsite = 'https://arunkulkarni.io';

  const sortedFinancialData = financialData.slice().sort((a, b) => a.fy - b.fy);

  return (
    <div className="p-4 bg-white">
      <form onSubmit={handleSubmit} className="max-w-md mx-auto p-6 bg-white shadow-lg rounded-lg">
        <div className="mb-4">
          <label className="block text-gray-600 mb-2">Stock Ticker:</label>
          <input
            type="text"
            className="w-full px-4 py-2 border rounded-lg text-black"
            value={ticker}
            onChange={(e) => setTicker(e.target.value.toUpperCase())}
            required
            autoFocus // Set autoFocus for the first input
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-600 mb-2">Latest Fiscal Year:</label>
          <input
            type="number"
            className="w-full px-4 py-2 border rounded-lg text-black"
            value={fiscalYear}
            onChange={(e) => setFiscalYear(e.target.value)}
            required
          />
        </div>
        <div className="mb-4">
          <label className="block text-gray-600 mb-2">Number of Historical Years:</label>
          <input
            type="number"
            className="w-full px-4 py-2 border rounded-lg text-black"
            value={numYears}
            onChange={(e) => setNumYears(e.target.value)}
            required
          />
        </div>
        <button
          type="submit"
          className="w-full bg-blue-500 text-white rounded-lg py-2 hover:bg-blue-600 transition-colors duration-300"
        >
          Submit
        </button>
      </form>

      {stockPrice !== null && (
        <div className="text-center mt-4">
          <p className="text-lg font-semibold">Current Share Price: ${stockPrice}</p>
        </div>
      )}

      {/* Add shadow above the table */}
      <div className="shadow-lg mt-4 bg-white">
        {sortedFinancialData.length > 0 && <CompanyConceptsTable data={sortedFinancialData} />}
      </div>

      {error && <p className="text-red-600 mt-2">{error}</p>}

       {/* Copyright notice and link to the author's website */}
       <div className="text-center mt-4 text-sm text-gray-500">
        <span>&copy; {currentYear} Arun Kulkarni</span>
        <span className="mx-2">|</span>
        <a href={authorWebsite} target="_blank" rel="noopener noreferrer" className="text-blue-500 underline">
          Learn more about Arun!
        </a>
      </div>
    </div>
  );
};

export default Page;
