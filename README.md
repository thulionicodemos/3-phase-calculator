# Three-Phase Circuit Analysis Toolkit

### 3-Phase Circuit Calculator (Y and Δ Networks)

This project provides a complete toolkit for analyzing three-phase electrical circuits, including balanced and unbalanced **Δ (Delta)** and **Y (Star)** configurations.  
It includes:

- A fully interactive **Streamlit-based GUI** (`painel.py`)
- Calculation modules for currents, voltages, and power
- Conversion utilities (rectangular ↔ polar)
- A `Circuito` class encapsulating all electrical parameters
- A CLI version (`main.py`) for console-based execution

This tool is designed for academic, engineering, and educational use.

---

## Project Structure

├── painel.py # Streamlit interface (main application)  
├── main.py # CLI version of the analysis tool  
├── circuito_trifasico.py # Core class for system parameters and utilities  
├── calc_circuito_eq_desesq_Y.py # Y-connected (star) analysis (balanced & unbalanced)  
├── calc_circuito_eq_DD.py # Balanced Δ analysis  
├── calc_circuito_deseq_D.py # Unbalanced Δ analysis  
├── calc_corrente.py # Phase currents (Y)  
├── calc_corrente_linha_carga.py # Line currents (Δ)  
├── calc_tensao_carga.py # Phase voltages (star)  
├── calc_tensao_linha_carga.py # Line voltages  
├── calc_potencia.py # Complex, active, reactive, and apparent power  
├── convert.py # Complex number conversions  
├── imprime_polar.py # Polar-format printing utilities  
└── requirements.txt # Dependencies  

---

## Features

### Supported Circuit Types

- **Balanced Y (star)**
- **Unbalanced Y (star)**
- **Balanced Δ (delta)**
- **Unbalanced Δ (delta)**

### Computed Quantities

- Phase currents
- Line currents
- Phase voltages
- Line voltages
- Neutral current (4-wire systems)
- Neutral displacement voltage (3-wire systems)
- Load powers (S, P, Q, |S|)
- Total system power
- Power factor (pf)

### Interface Features

- Modern and responsive Streamlit layout
- All circuit parameters editable via UI
- Results displayed immediately under calculation button
- Output formatted using polar notation (r∠θ)

---

## Running the Streamlit App

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run painel.py
```

Access in your browser:[text](http://localhost:8501)

---

## Running the CLI Version

Fill in the circuit parameters in the "main.py" file.

Run:

```bash
python main.py
```

---

Author

Thulio Nicodemos
Electrical Engineering • Power Systems • Python Development
