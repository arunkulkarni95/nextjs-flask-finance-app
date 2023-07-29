'use client'
// pages/page.tsx

import { useState } from 'react';
import axios from 'axios';

interface CompanyData {
  [key: string]: string;
}

const StockTicker: React.FC = () => {
  const [ticker, setTicker] = useState('');
  const [fiscalYear, setFiscalYear] = useState<string>('');
  const [jsonData, setJsonData] = useState<CompanyData | null>(null);
  const [error, setError] = useState('');

  const handleTickerChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setTicker(e.target.value);
    setError('');
  };

  const handleFiscalYearChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFiscalYear(e.target.value);
    setError('');
  };

  const fetchData = async () => {
    try {
      if (!ticker || !fiscalYear || isNaN(parseInt(fiscalYear))) {
        setError('Please enter a valid stock ticker and fiscal year.');
        return;
      }

      const response = await axios.post('/api/financials/company-concepts', {
        ticker,
        fiscal_year: fiscalYear,
      });
      setJsonData(response.data);
      setError('');
    } catch (error) {
      console.error('Error fetching data:', error);
      setError('Error fetching data. Please try again later.');
    }
  };

  return (
    <div className="container mx-auto p-4">
      <div className="flex items-center mb-4">
        <input
          type="text"
          className="border border-gray-300 p-2 mr-2"
          placeholder="Enter stock ticker"
          value={ticker}
          onChange={handleTickerChange}
        />
        <input
          type="text" // Change input type to text
          className="border border-gray-300 p-2 mr-2"
          placeholder="Enter fiscal year"
          value={fiscalYear}
          onChange={handleFiscalYearChange}
        />
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded"
          onClick={fetchData}
        >
          Get Data
        </button>
      </div>

      {error && (
        <div className="text-red-600 mb-4">{error}</div>
      )}

      {jsonData && (
        <table className="border-collapse border border-gray-400 w-full">
          <thead>
            <tr className="bg-gray-200">
              <th className="border border-gray-400 px-4 py-2">Key</th>
              <th className="border border-gray-400 px-4 py-2">Value</th>
            </tr>
          </thead>
          <tbody>
            {Object.entries(jsonData).map(([key, value]) => (
              <tr key={key}>
                <td className="border border-gray-400 px-4 py-2">{key}</td>
                <td className="border border-gray-400 px-4 py-2">
                  {String(value)} {/* Convert to string to handle any type */}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default StockTicker;
