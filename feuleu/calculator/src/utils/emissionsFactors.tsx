// src/utils/emissionsFactors.ts

export const emissionsFactors = {
    vlsfo: { factor: 3.188, cost: 600 },       // Very Low Sulfur Fuel Oil
    mgo: { factor: 3.206, cost: 700 },         // Marine Gas Oil
    lngst: { factor: 2.75, cost: 750 },        // LNG Stream Turbine
    bs: { factor: 3.188, cost: 600 },          // Baltic Standard (assuming similar to VLSFO)
    hfo: { factor: 3.114, cost: 460 },         // Heavy Fuel Oil
    lsfoc: { factor: 3.114, cost: 480 },       // Low Sulfur Fuel Oil Crude
    lngd: { factor: 2.75, cost: 750 },         // LNG Diesel
    lngo: { factor: 2.75, cost: 750 },         // LNG Otto
    lpg: { factor: 3.02, cost: 690 },         // Liquefied Petroleum Gas
    methanol: { factor: 1.375, cost: 1500 },   // Methanol
};
