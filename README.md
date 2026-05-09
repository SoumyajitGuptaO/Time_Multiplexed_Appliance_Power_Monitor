# Time-Multiplexed Appliance Power Monitoring & Processing

This repository contains simulation models and data processing pipelines for a centralized, time-division multiplexed (TDM) energy monitoring system. The project evaluates the power consumption of four independent household appliances (such as washing machine motor sub-systems or resistive loads) using a shared power measurement architecture to reduce hardware redundancy.

It includes hardware-level circuit simulations in **LTspice** and synthetic data processing scripts in **Python** (handling data generated via MATLAB/Simulink).

## 📐 System Architecture

The core of the simulation tests a TDM approach to power monitoring, capturing both dedicated continuous data and multiplexed data.

**Hardware Signal Chain (LTspice Simulation):**
1. **Loads:** 4 independent AC loads.
2. **Current Sensing:** Dedicated ACS712 Hall-effect current sensors isolate and measure the current drawn by each load.
3. **Multiplexing:** A DG408 8-channel analog multiplexer routes the sensed current signals.
4. **Switching Logic:** The DG408 is configured to give each load exactly **1 second of attention** before switching to the next channel.
5. **Power Calculation:** The multiplexed signal is fed into an MCP39F521 power monitoring IC to calculate active power, reactive power, and RMS values.

## 📂 Repository Structure

```text
├── LTspice_Simulations/
│   ├── models/                     # .lib files for ACS712, MCP39F521, DG408
│   └── tdm_power_monitor.cir       # Main executable text netlist 
├── Simulink_Pipeline/
│   └── simulink_data_processor.py  # Python script for data processing
└── README.md