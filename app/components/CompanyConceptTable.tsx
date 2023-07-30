// components/CompanyConceptsTable.tsx

import React from 'react';

interface FinancialData {
  FY: number;
  [key: string]: number | string;
}

interface CompanyConceptsTableProps {
  data: FinancialData[];
}

const CompanyConceptsTable: React.FC<CompanyConceptsTableProps> = ({ data }) => {
  const getColumns = () => {
    return data.map((item) => item.FY);
  };

  const getRows = () => {
    const metrics = Object.keys(data[0]).filter((key) => key !== 'FY');
    return metrics;
  };

  return (
    <div className="overflow-x-auto">
      <table className="table-auto border-collapse w-full">
        <thead>
          <tr className="bg-gray-200 text-gray-600 uppercase text-sm leading-normal">
            <th className="py-3 px-6 text-left"></th>
            {getColumns().map((fy) => (
              <th key={fy} className="py-3 px-6 text-left">
                {fy}
              </th>
            ))}
          </tr>
        </thead>
        <tbody className="text-gray-600 text-sm font-light">
          {getRows().map((row) => (
            <tr key={row} className="border-b border-gray-200 hover:bg-gray-100">
              <td className="py-3 px-6 text-left whitespace-nowrap">
                {row}
              </td>
              {data.map((item) => (
                <td key={item.fy} className="py-3 px-6 text-left whitespace-nowrap">
                  {item[row]}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default CompanyConceptsTable;
