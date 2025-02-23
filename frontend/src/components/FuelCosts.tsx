import React from "react";
import { Link } from "react-router-dom";
import { Grid, Card, CardContent, Typography, Button } from "@mui/material";

const fuelCostsData = [
    { name: "HFO ISO 8217 (Grades RME to RMK)", price: 460 },
    { name: "MDO & MGO ISO 8217 (Grades DMX to DMB)", price: 700 },
    { name: "LSFO Crude", price: 480 },
    { name: "LNG Otto (Dual Fuel Medium Speed)", price: 750 },
    { name: "LSFO Blend", price: 480 },
    { name: "LNG Otto (Dual Fuel Slow Speed)", price: 750 },
    { name: "ULSFO", price: 650 },
    { name: "LNG Diesel (Dual Fuel Slow Speed)", price: 750 },
    { name: "VLSFO", price: 600 },
    { name: "LNG LBSI", price: 750 },
    { name: "LFO ISO 8217 (Grades RMA to RMD)", price: 490 },
    { name: "LNG Steam Turbine", price: 750 },
    { name: "LPG (Butane)", price: 690 },
    { name: "H2 (From Natural Gas)", price: 2000 },
    { name: "LPG (Propane)", price: 690 },
    { name: "NH3 (From Natural Gas)", price: 1200 },
    { name: "Methanol (From Natural Gas)", price: 1500 }
];

const FuelCosts: React.FC = () => {
    return (
        <div style={{
            padding: "20px",
            backgroundColor: "#f9f9f9",
            borderRadius: "10px",
            boxShadow: "0px 0px 10px rgba(0, 0, 0, 0.1)",
            margin: "auto",
            textAlign: "center",
        }}>
            {/* Header Section */}
            <div style={headerStyle}>
                <Typography variant="h4" style={{ color: "black", fontWeight: "bold" , fontSize: "larger", fontFamily: "Times New Roman",}}>
                    Fuel Costs <span style={{ color: "black" }}>($/mt)</span>
                </Typography>
            </div>

            {/* Fuel Costs Grid */}
            <Grid container spacing={2} style={{ marginTop: "20px"}}>
                {fuelCostsData.map((fuel, index) => (
                    <Grid item xs={12} sm={6} md={4} key={index}>
                        <Card style={{
                            backgroundColor: "white",
                            borderRadius: "10px",
                            padding: "10px",
                            boxShadow: "0px 4px 6px rgba(0, 0, 0, 0.1)",
                            textAlign: "center",
                        }}>
                            <CardContent>
                                <Typography variant="subtitle1" style={fuelLabelStyle}>
                                    {fuel.name}
                                </Typography>
                                <Typography variant="h5" style={fuelPriceStyle}>
                                    {fuel.price}
                                </Typography>
                            </CardContent>
                        </Card>
                    </Grid>
                ))}
            </Grid>

            {/* Return Button */}
            <div style={{ textAlign: "center", marginTop: "30px" }}>
                <Link to="/">
                    <Button variant="contained" style={returnButtonStyle}>
                        ⬅ Return
                    </Button>
                </Link>
            </div>
        </div>
    );
};

// Styles


const headerStyle = {
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "lightgreen",
    padding: "2px",
    borderRadius: "20px",
    color: "black",
    border: "2px solid",
    fontSize: "larger",
}



const fuelLabelStyle = {
    fontSize: "0.9rem",
    fontWeight: "bold",
    color: "#555",
};

const fuelPriceStyle = {
    fontSize: "1.8rem",
    fontWeight: "bold",
    color: "green",
};

const returnButtonStyle = {
    backgroundColor: "green",
    color: "white",
    padding: "10px 20px",
    fontSize: "1.2rem",
    borderRadius: "10px",
};

export default FuelCosts;
