import React, { useEffect, useState } from "react";
import api from "../services/api";
import { emissionsFactors } from "../utils/emissionsFactors";

type EmissionsProps = {
  vesselData: {
    fuelType: string;
    ballastVLSFO: number;
    ladenVLSFO: number;
    ballastSpeed: number;
    ladenSpeed: number;
    dwt: number;
    sector: string;
    fuelCost: number;
  };
};

type VesselProp = {
  deadweight_mt: number;
  fuel_type: string;
  ballast_speed_knts: number;
  ballast_vlsfo_mt_day: number;
  laden_speed_knts: number;
  laden_vlsfo_mt_day: number;
  sector: string;
};

const postVessel = async (vessel: VesselProp): Promise<string> => {
  try {
    const res = await api.post(`/vessels`, vessel);
    return res.status >= 200 && res.status < 300 ? "OK" : res.statusText;
  } catch (error) {
    throw new Error("Error: " + error);
  }
};

const EmissionsCalculation: React.FC<EmissionsProps> = ({ vesselData }) => {
  const {
    fuelType,
    ballastVLSFO,
    ladenVLSFO,
    ballastSpeed,
    ladenSpeed,
    dwt,
    sector,
  } = vesselData;

  const vessel_data = {
    deadweight_mt: dwt,
    fuel_type: fuelType,
    ballast_speed_knts: ballastSpeed,
    ballast_vlsfo_mt_day: ballastVLSFO,
    laden_speed_knts: ladenSpeed,
    laden_vlsfo_mt_day: ladenVLSFO,
    sector: sector,
  };

  // State to store the emissions factor
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // Fetch the emissions factor when the component mounts or fuelType changes
  useEffect(() => {
    const postVesselData = async () => {
      try {
        const status = await postVessel(vessel_data);
        if (status !== "OK") throw error;
        setLoading(false);
      } catch (err) {
        setError("Error posting vessel's data");
        setLoading(false);
      }
    };
    postVesselData();
  }, [vessel_data]);

  if (loading) return <div>Loading...</div>; // Show loading state while fetching data
  if (error) return <div>{error}</div>; // Show error if fetch fails

  // Retrieve emissions factor & default fuel cost
  const fuelData = emissionsFactors[fuelType as keyof typeof emissionsFactors];
  const emissionsFactor = fuelData.factor;
  // const defaultFuelCost = fuelData.cost;

  // Adjust consumption based on DWT (assuming 50,000 DWT is the baseline)
  const dwtAdjustment = dwt / 50000;

  // Sector-based fuel consumption adjustment
  let sectorMultiplier = 1;
  if (sector === "dt" || sector === "ct")
    sectorMultiplier = 1.2; // Tankers consume more
  else if (sector === "lng") sectorMultiplier = 0.8; // LNG vessels consume less

  // Calculate fuel consumption
  const ballastConsumption =
    ballastVLSFO * ballastSpeed * dwtAdjustment * sectorMultiplier;
  const ladenConsumption =
    ladenVLSFO * ladenSpeed * dwtAdjustment * sectorMultiplier;
  const totalConsumption = ballastConsumption + ladenConsumption;

  // Emissions & Fuel Cost Calculations
  const emissions = emissionsFactor * totalConsumption;
  // const finalFuelCost = fuelCost > 0 ? fuelCost : defaultFuelCost; // Allow user to override fuel cost
  //const totalFuelCost = totalConsumption * finalFuelCost;

  return (
    <div
      style={{
        padding: "20px",
        backgroundColor: "#f9f9f9",
        borderRadius: "10px",
        boxShadow: "0px 0px 10px rgba(0, 0, 0, 0.1)",
        maxWidth: "600px",
        margin: "auto",
        textAlign: "center",
      }}
    >
      <h2 style={headerStyle}>Emissions Calculation</h2>

      <div
        style={{
          backgroundColor: "white",
          borderRadius: "10px",
          padding: "10px",
          margin: "10px 0",
          boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.1)",
          textAlign: "center",
        }}
      >
        <h3>Total CO₂ Emissions:</h3>
        <p style={valueStyle}>{emissions.toFixed(2)} kg CO₂</p>
      </div>

      <div
        style={{
          backgroundColor: "white",
          borderRadius: "10px",
          padding: "10px",
          margin: "10px 0",
          boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.1)",
          textAlign: "center",
        }}
      ></div>
    </div>
  );
};

const headerStyle = {
  fontFamily: "Arial, sans-serif",
  color: "#333",
  fontSize: "1.8rem",
};

const valueStyle = {
  fontSize: "1.5rem",
  fontWeight: "bold",
  color: "#003366",
};

export default EmissionsCalculation;
