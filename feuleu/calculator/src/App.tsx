// src/App.tsx
import React, { useState } from 'react';
import FuelInput from './components/FuelInput';
import EmissionsCalculation from './components/EmissionsCalculation';
import FuelCosts from "./components/FuelCosts";
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

const App: React.FC = () => {
    const [vesselData, setVesselData] = useState<any>(null);

    const handleVesselDataSubmit = (data: any) => {
        setVesselData(data);
    };

    return (
        <Router>
            <div style={{ padding: 20 }}>
                <h1 style={{
                    fontFamily: "Times New Roman",
                    border: "2px solid black",
                    borderRadius: "20px",
                    backgroundColor: "green",
                    color: "white",
                    fontSize: "xx-large",
                    textAlign: "center",
                    padding: "5px"
                }}>
                    FuelEU Calculator
                </h1>

                <Routes>
                    {/* Home Page - Includes Fuel Input & Emissions Calculation */}
                    <Route path="/" element={
                        <>

                            <FuelInput onSubmit={handleVesselDataSubmit} />
                            {vesselData && <EmissionsCalculation vesselData={vesselData} />}

                            {/* Button to navigate to Fuel Costs page */}
                            <div style={{ textAlign: "center", marginTop: "20px" }}>
                                <Link to="/fuel-costs" style={{
                                    display: "inline-block",
                                    marginTop: "20px",
                                    padding: "10px 15px",
                                    backgroundColor: "green",
                                    color: "white",
                                    textDecoration: "none",
                                    borderRadius: "5px",
                                    textAlign: "center",
                                    width: "150px",
                                    fontWeight: "bold",
                                    fontFamily: "Times New Roman",
                                    fontSize: "x- large"
                                }}>View Fuel Costs</Link>
                            </div>
                        </>
                    } />

                    {/* Fuel Costs Page */}
                    <Route path="/fuel-costs" element={<FuelCosts />} />
                </Routes>
            </div>
        </Router>
    );
};

// Styling for the but

export default App;
