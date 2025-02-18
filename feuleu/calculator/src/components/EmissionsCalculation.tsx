// src/components/EmissionsCalculation.tsx
import React from 'react';
import { emissionsFactors } from '../utils/emissionsFactors';

type EmissionsProps = {
    vesselData: any;
};

const EmissionsCalculation: React.FC<EmissionsProps> = ({ vesselData }) => {
    const { ballastSpeed, ballastVLSFO, ladenSpeed, ladenVLSFO, dwt, sector, fuelType, fuelCost } = vesselData;

    const emissionsFactor = emissionsFactors[fuelType as keyof typeof emissionsFactors];

    // Adjust ballast and laden consumption based on speed, DWT, and sector type
    let ballastConsumption = ballastVLSFO * (ballastSpeed / 11) * (dwt / 50000);
    let ladenConsumption = ladenVLSFO * (ladenSpeed / 11) * (dwt / 50000);

    // Adjustments based on sector type (example: tanker sectors consume more)
    if (sector === 'dt' || sector === 'ct') {
        ballastConsumption *= 1.2; // Example multiplier for tankers
        ladenConsumption *= 1.2;   // Example multiplier for tankers
    } else if (sector === 'lng') {
        ballastConsumption *= 0.8; // Example adjustment for LNG sector
        ladenConsumption *= 0.8;
    }

    const totalConsumption = ballastConsumption + ladenConsumption;

    // Emissions calculation
    const emissions = emissionsFactor * totalConsumption;

    return (
        <div>
            <h2 style={{fontFamily: "Times New Roman", border: "2px solid", borderRadius: "20px", backgroundColor: "lightgreen", color: "black", fontSize: "large", textAlign: "center", padding: "2px"}}>Emissions Calculation</h2>
            <p style={{fontFamily: "Times New Roman", color: "#333", fontSize: "medium", padding: "2px",  marginBottom: "15px", lineHeight: "1.6", paddingLeft: "10px"}}>Total CO2 Emissions: {emissions.toFixed(2)} kg CO2</p>

            <h3 style={{fontFamily: "Times New Roman", border: "2px solid", borderRadius: "20px", backgroundColor: "lightgreen", color: "black", fontSize: "large", textAlign: "center", padding: "2px"}}>Fuel Consumption Details</h3>
            <p style={{fontFamily: "Times New Roman",color: "#333", fontSize: "medium", padding: "2px",  marginBottom: "15px", lineHeight: "1.6", paddingLeft: "10px"}}>Ballast Fuel Consumption: {ballastConsumption.toFixed(2)} mt/day</p>
            <p style={{fontFamily: "Times New Roman",color: "#333", fontSize: "medium", padding: "2px",  marginBottom: "15px", lineHeight: "1.6", paddingLeft: "10px"}}>Laden Fuel Consumption: {ladenConsumption.toFixed(2)} mt/day</p>

            <h3 style={{fontFamily: "Times New Roman",border: "2px solid", borderRadius: "20px", backgroundColor: "lightgreen", color: "black", fontSize: "large", textAlign: "center", padding: "2px"}}>Fuel Cost Calculation</h3>
            <p style={{fontFamily: "Times New Roman",color: "#333", fontSize: "medium", padding: "2px",  marginBottom: "15px", lineHeight: "1.6", paddingLeft: "10px"}}>Total Fuel Cost: {(fuelCost * totalConsumption * 365).toFixed(2)} USD/year</p>

            <h3 style={{fontFamily: "Times New Roman",border: "2px solid", borderRadius: "20px", backgroundColor: "lightgreen", color: "black", fontSize: "large", textAlign: "center", padding: "2px"}}>FuelEU Penalty</h3>
            <p style={{fontFamily: "Times New Roman",color: "#333", fontSize: "medium", padding: "2px",  marginBottom: "15px", lineHeight: "1.6", paddingLeft: "10px"}}>Penalty: {emissions > 10000 ? 'High Penalty' : 'Low Penalty'}</p>
        </div>
    );
};

export default EmissionsCalculation;
