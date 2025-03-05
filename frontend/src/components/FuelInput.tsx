// src/components/FuelInput.tsx
import React, { useState } from "react";
import {
  TextField,
  MenuItem,
  Button,
  Select,
  InputLabel,
  FormControl,
} from "@mui/material";

// Sample fuel types and sectors
const fuelTypes = [
  { label: "VLSFO", value: "vlsfo" },
  { label: "MDO & MGO ISO 8217 (Grades DMX to DMB)", value: "mgo" },
  { label: "Baltic Standard", value: "bs" },
  { label: "HFO ISO 8217 (Grades RME to RMK)", value: "hfo" },
  { label: "LSFO Crude", value: "lsfoc" },
  { label: "LNG Diesel (Dual Fuel Slow Speed)", value: "lng_diesel" },
  { label: "LNG Otto (Dual Fuel Medium Speed)", value: "lng_otto_medium" },
  { label: "LPG (Propane)", value: "lpg" },
  {label: "LSFO Blend", value: "lsfo_blend" },
  {label: "LNG Otto (Dual Fuel Slow Speed)", value: "lng_otto_slow" },
  {label: "ULSFO", value: "ulsfo" },
  {label: "LFO ISO 8217 (Grades RMA to RMD)", value: "lfo" },
  {label: "Hydrogen (Grey - From Natural Gas)", value: "hydrogen" },
  {label: "Ammonia (Grey - From Natural Gas)", value: "ammonia" },











];


const sectors = [
  { label: "Dry Physical", value: "dp" },
  { label: "Dirty Tanker", value: "dt" },
  { label: "Clean Tanker", value: "ct" },
  { label: "LNG", value: "lng" },
  { label: "LPG", value: "lpg" },
];

const FuelInput: React.FC<{ onSubmit: (vesselData: any) => void }> = ({
  onSubmit,
}) => {
  const [dwt, setDwt] = useState<number>(50000);
  const [ballastSpeed, setBallastSpeed] = useState<number>(12);
  const [ballastVLSFO, setBallastVLSFO] = useState<number>(16.8);
  const [ladenSpeed, setLadenSpeed] = useState<number>(11);
  const [ladenVLSFO, setLadenVLSFO] = useState<number>(18);
  const [sector, setSector] = useState<string>("dp");
  const [fuelType, setFuelType] = useState<string>("bs");
  const [fuelCost, setFuelCost] = useState<number>();

  const handleSubmit = () => {
    onSubmit({
      dwt,
      ballastSpeed,
      ballastVLSFO,
      ladenSpeed,
      ladenVLSFO,
      sector,
      fuelType,
      fuelCost,
    });
  };

  return (
    <div>
      <h2
        style={{
          fontFamily: "Times New Roman",
          border: "2px solid",
          borderRadius: "20px",
          backgroundColor: "lightgreen",
          color: "black",
          fontSize: "larger",
          textAlign: "center",
          padding: "2px",
        }}
      >
        Your Vessel Details
      </h2>
      <TextField
        label="Deadweight (mt)"
        type="number"
        fullWidth
        value={dwt}
        onChange={(e) => setDwt(Number(e.target.value))}
        margin="normal"
      />
      <TextField
        label="Ballast Speed (knts)"
        type="number"
        fullWidth
        value={ballastSpeed}
        onChange={(e) => setBallastSpeed(Number(e.target.value))}
        margin="normal"
      />
      <TextField
        label="Ballast VLSFO Equivalent (mt/day)"
        type="number"
        fullWidth
        value={ballastVLSFO}
        onChange={(e) => setBallastVLSFO(Number(e.target.value))}
        margin="normal"
      />
      <TextField
        label="Laden Speed (knts)"
        type="number"
        fullWidth
        value={ladenSpeed}
        onChange={(e) => setLadenSpeed(Number(e.target.value))}
        margin="normal"
      />
      <TextField
        label="Laden VLSFO Equivalent (mt/day)"
        type="number"
        fullWidth
        value={ladenVLSFO}
        onChange={(e) => setLadenVLSFO(Number(e.target.value))}
        margin="normal"
      />
      <TextField
        label="Fuel Cost ($/mt)"
        type="number"
        fullWidth
        value={fuelCost}
        onChange={(e) => setFuelCost(Number(e.target.value))}
      />

      <h3
        style={{
          fontFamily: "Times New Roman",
          border: "2px solid",
          borderRadius: "20px",
          backgroundColor: "lightgreen",
          color: "black",
          fontSize: "larger",
          textAlign: "center",
          padding: "2px",
        }}
      >
        Route Configuration
      </h3>
      <FormControl fullWidth margin="normal">
        <InputLabel>Sector</InputLabel>
        <Select
          value={sector}
          onChange={(e) => setSector(e.target.value)}
          label="Sector"
        >
          {sectors.map((sector) => (
            <MenuItem key={sector.value} value={sector.value}>
              {sector.label}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      <FormControl fullWidth margin="normal">
        <InputLabel>Main Fuel Type</InputLabel>
        <Select
          value={fuelType}
          onChange={(e) => setFuelType(e.target.value)}
          label="Main Fuel Type"
        >
          {fuelTypes.map((fuel) => (
            <MenuItem key={fuel.value} value={fuel.value}>
              {fuel.label}
            </MenuItem>
          ))}
        </Select>
      </FormControl>

      <Button variant="contained" color="success" onClick={handleSubmit}>
        Calculate
      </Button>
    </div>
  );
};

export default FuelInput;
