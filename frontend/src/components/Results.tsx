// src/components/Results.tsx
import React from 'react';
import { Button } from '@mui/material';

type ResultsProps = {
    emissions: number;
};

const Results: React.FC<ResultsProps> = ({ emissions }) => {
    const downloadReport = () => {
        const report = `Emissions Report\n\nTotal CO2 Emissions: ${emissions.toFixed(2)} kg CO2`;
        const blob = new Blob([report], { type: 'text/plain' });
        const link = document.createElement('a');
        link.href = URL.createObjectURL(blob);
        link.download = 'emissions_report.txt';
        link.click();
    };

    return (
        <div>
            <h2>Results</h2>
            <p>Total CO2 Emissions: {emissions.toFixed(2)} kg CO2</p>
            <Button variant="contained" onClick={downloadReport}>
                Download Report
            </Button>
        </div>
    );
};

export default Results;
