F1 Tyre Strategy Simulator & Model
A Python Simulation tool that models Formula 1 tyre behaviour, degredation, affects of fuel and pit stop stratergy etc. It is capable of predicting race lap times and identifying th optimal one-stop or two-stop race strategy.

----------------------------------------------------------
Features

Tyre Behaviour Model
 Polynomial regression model trained on sample date
 Predicts lap-time based on:
    -Tyre age
    -Tyre temperature
    -Warmup phase
    -Track evolution
    -Fuel load

Race Stint Simulator
 Accurately simulates each lap by modelling:
  -Tyre degradation per lap
  -Temperature increase
  -Warmup laps
  -Fuel burn and its effect on lap time
  -Pit stop time loss
  -Compound-specific characteristics (soft/medium/hard)

Strategy Optimisation
 Brute-force optimiser evaluates:
  -One-stop strategies
  -Two-stop strategies
  -Three-stop strategies
  -All valid combinations of compounds
  -Hundreds of potential pit windows

 Automatically returns:
  -Best strategy
  -Total predicted race time
  -Lap-by-lap pace curve

Visualisation
 The simulator produces clear race-engineering style figures:
  -Lap-time curves for single strategies
  -Temperature evolution curves
  -Strategy comparison graphs
  -One-stop vs two-stop overlays
  -Lap-time predictions for contrasting pit windows

----------------------------------------------------------
Project Structure
F1-Strategy-Simulator/
│
├── notebooks/
│   └── tyre_model_development.ipynb   # Main modelling & simulation notebook
│
├── src/
│   ├── degradation_model.py                  # Tyre prediction model
│   ├── strategy_sim.py
│   ├── data_loader.py
│   └── visualisations.py
│
│
├── data/
│   └── sample_stint.csv               # Training data for tyre model
│
└── README.md

----------------------------------------------------------
How it works
1. Build the Tyre Model
  A regression model is trained using a dataset containing:
   -Lap number
   -Recorded lap time
   -Tyre temperature
  Output: A predictive function predict(lap, tyre_temp).

2. Simulate a Race Stint
  For every lap:
   -Tyre temp increases
   -Degradation is applied
   -Fuel load decreases
   -Warmup modifiers applied
   -Lap time is computed using the regression model
  Returns a lap-by-lap DataFrame.

3. Optimise Strategy
  The optimiser iterates through:
   -Valid compound combinations
   -All pit stop windows
   -All minimum stint length constraints
  And returns the fastest predicted race time.

4. Visualise the Results
 Using Matplotlib, the notebook produces plots including:
  Tyre pace curves
    -Soft, Medium, Hard degradation profiles
  Optimal two-stop vs one-stop
   -Direct comparison of race time evolution
  Temperature vs lap
   -Shows tyre overheating behaviour

----------------------------------------------------------
Example Output
 Best Two-Stop Strategy:
  -Pit 1: Lap 29
  -Pit 2: Lap 41
  -Compounds: Medium → Hard → Medium
  -Total Predicted Race Time: ~5200 sec
  
----------------------------------------------------------
Installation
git clone https://github.com/<your-name>/F1-Strategy-Simulator.git
cd F1-Strategy-Simulator
pip install -r requirements.txt

Requirements:
numpy
pandas
matplotlib
scikit-learn

----------------------------------------------------------
Usage
Open the main notebook:
notebooks/tyre_model_development.ipynb

 Run the cells to:
  -Train the tyre model
  -Generate stint simulations
  -Run strategy optimisation
  -Plot and compare strategies 

----------------------------------------------------------
Future Improvements

 These will massively impress teams if added later:
  -Import real F1 timing data (FIA timing sheets / Ergast API)
  -Monaco simulation for safety cars / track evolution
  -Dashboard using Streamlit
  -Team-specific car modelling (Williams / Ferrari / etc.)

----------------------------------------------------------
Contributions

Suggestions and improvements welcome — this project will continue evolving into a full race-strategy engine.

----------------------------------------------------------
Contact
Jack Lydon
Email: jackLydon1@icloud.com
Github: jacklydon23

