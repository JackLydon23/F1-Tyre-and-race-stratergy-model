import numpy as np

def run_strategy_sim(model, lap_20_df, lap_30_df, n=5000):
    results = []
    for _ in range(n):
        total_20 = lap_20_df["lap_time"].sum() + np.random.normal(0, 0.2)
        total_30 = lap_30_df["lap_time"].sum() + np.random.normal(0, 0.2)
        results.append(total_20 < total_30)
    return sum(results) / len(results)
