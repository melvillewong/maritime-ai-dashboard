// src/utils/emissionsFactors.ts

export const emissionsFactors = {
  hfo: { factor: 3.114, cost: 460 }, // HFO ISO 8217 (Grades RME to RMK)
  mgo: { factor: 3.206, cost: 700 }, // MDO & MGO ISO 8217 (Grades DMX to DMB)
  lsfoc: { factor: 3.151, cost: 480 }, // LSFO Crude
  lng_otto_medium: { factor: 2.750, cost: 750 }, // LNG Otto (Dual Fuel Medium Speed)
  lsfo_blend: { factor: 3.151, cost: 480 }, // LSFO Blend
  lng_otto_slow: { factor: 2.750, cost: 750 }, // LNG Otto (Dual Fuel Slow Speed)
  ulsfo: { factor: 3.151, cost: 650 }, // ULSFO
  lng_diesel: { factor: 2.750, cost: 750 }, // LNG Diesel (Dual Fuel Slow Speed)
  vlsfo: { factor: 3.151, cost: 600 }, // VLSFO
  lfo: { factor: 3.151, cost: 490 }, // LFO ISO 8217 (Grades RMA to RMD)
  lpg: { factor: 3.000, cost: 690 }, // LPG (Propane)
  hydrogen: { factor: 0, cost: 2000 }, // Hydrogen (Grey - From Natural Gas)
  ammonia: { factor: 0, cost: 1200 },
  bs: { factor: 3.188, cost: 600 }


};
