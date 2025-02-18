// src/App.tsx
import React, { useState } from 'react';
import FuelInput from './components/FuelInput';
import EmissionsCalculation from './components/EmissionsCalculation';

const App: React.FC = () => {
    const [vesselData, setVesselData] = useState<any>(null);

    const handleVesselDataSubmit = (data: any) => {
        setVesselData(data);
    };

    return (
        <div style={{ padding: 20 }}>
            <h1 style={{fontFamily: "Times New Roman", border: "2px solid black", borderRadius: "20px", backgroundColor: "green", color: "white", fontSize: "xx-large", textAlign: "center", padding: "5px"}}>FuelEU Calculator</h1>
            <FuelInput onSubmit={handleVesselDataSubmit} />
            {vesselData && <EmissionsCalculation vesselData={vesselData} />}
        </div>
    );
};

export default App;
