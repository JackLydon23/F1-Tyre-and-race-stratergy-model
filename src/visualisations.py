import matplotlib.pyplot as plt

def plot_lap_times(df):
    plt.figure(figsize=(8,4))
    plt.plot(df["lap"], df["lap_time"], marker='o')
    plt.xlabel("Lap")
    plt.ylabel("Lap Time (s)")
    plt.title("Lap Times vs Lap Number")
    plt.grid()
