'use client'

// pages/page.tsx
import React, { useState } from 'react';
import axios from 'axios';
import CompanyConceptsTable from './components/CompanyConceptTable';

interface FinancialData {
  fy: number;
  [key: string]: number | string;
}

const Page: React.FC = () => {
  const [ticker, setTicker] = useState<string>('');
  const [fiscalYear, setFiscalYear] = useState<string>('');
  const [numYears, setNumYears] = useState<string>('');
  const [financialData, setFinancialData] = useState<FinancialData[]>([]);
  const [error, setError] = useState<string>('');

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
    } catch (error) {
      console.error('Error fetching financial data:', error);
      setError('Error fetching financial data. Please try again later.');
    }
  };

  return (
    <div className="p-4">
      <form onSubmit={handleSubmit}>
        <div className="flex flex-col items-center justify-center mb-4 rounded-lg shadow-lg p-4 space-y-4">
          <div className="flex flex-col">
            <label className="text-gray-600 mb-2">Ticker:</label>
            <input
              type="text"
              className="px-4 py-2 border rounded-lg"
              value={ticker}
              onChange={(e) => setTicker(e.target.value.toUpperCase())}
              required
              autoFocus // Set autoFocus for the first input
            />
          </div>
          <div className="flex flex-col">
            <label className="text-gray-600 mb-2">Fiscal Year:</label>
            <input
              type="number"
              className="px-4 py-2 border rounded-lg"
              value={fiscalYear}
              onChange={(e) => setFiscalYear(e.target.value)}
              required
            />
          </div>
          <div className="flex flex-col">
            <label className="text-gray-600 mb-2">Number of Years:</label>
            <input
              type="number"
              className="px-4 py-2 border rounded-lg"
              value={numYears}
              onChange={(e) => setNumYears(e.target.value)}
              required
            />
          </div>
          <button
            type="submit"
            className="px-6 py-2 bg-blue-500 text-white rounded-lg"
          >
            Submit
          </button>
        </div>
      </form>

      {/* Add shadow above the table */}
      <div className="shadow-lg">
        {financialData.length > 0 && <CompanyConceptsTable data={financialData} />}
      </div>

      {error && <p className="text-red-600 mt-2">{error}</p>}
    </div>
  );
};

export default Page;
