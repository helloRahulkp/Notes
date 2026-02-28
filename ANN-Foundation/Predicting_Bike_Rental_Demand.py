# ===============================
# Standard Python Libraries
# ===============================
import os
import random
import pickle     # for saving/loading model weights
import math

# ===============================
# Data Handling & Visualization
# ===============================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ===============================
# To access Custom micrograd ANN Packages
# ===============================
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# ===============================
# Custom micrograd ANN Packages
# ===============================
from micrograd.engine import Value      # Core Value class for autograd
from micrograd.nn import Neuron, Layer, MLP  # ANN building blocks
from micrograd.utils import draw_dot    # For visualizing computation graph

# ===============================
# Optional: For dataset splitting
# ===============================
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Set seed for reproducibility
np.random.seed(42)

# Number of samples (e.g., 1000 hours of data)
N = 1000

# ----------------------------
# Features
# ----------------------------
hour = np.random.randint(0, 24, size=N)               # Hour of the day: 0-23
temperature = np.random.uniform(0, 35, size=N)       # Temperature in Celsius
humidity = np.random.uniform(10, 90, size=N)         # Humidity in %
weather = np.random.randint(0, 4, size=N)            # 0: Clear, 1: Mist, 2: Light rain, 3: Heavy rain
working_day = np.random.randint(0, 2, size=N)        # 0: Non-working, 1: Working day
windspeed = np.random.uniform(0, 35, size=N)         # Wind speed in km/h

# ----------------------------
# Target: Bike rentals
# ----------------------------
# Assume more rentals during working hours (7-9am, 4-6pm) and good weather
base_rentals = 50 + hour*2 - 0.5*temperature - 0.3*humidity
weather_factor = np.array([10 if w==0 else -5 if w==1 else -15 if w==2 else -25 for w in weather])
working_day_factor = working_day * 20
noise = np.random.normal(0, 5, size=N)

bike_rentals = base_rentals + weather_factor + working_day_factor + noise
bike_rentals = np.clip(bike_rentals, 0, None)  # rentals cannot be negative

# ----------------------------
# Create DataFrame
# ----------------------------
df = pd.DataFrame({
    'hour': hour,
    'temperature': temperature,
    'humidity': humidity,
    'weather': weather,
    'working_day': working_day,
    'windspeed': windspeed,
    'bike_rentals': bike_rentals
})

# Preview
print(df.head())

# Prepare Data for ANN

# Select Features & Target
features = ['hour', 'temperature', 'humidity', 'weather', 'working_day', 'windspeed']
target = 'bike_rentals'
X = df[features].values
y = df[target].values

# Normalize Features
scaler_X = StandardScaler()
X_scaled = scaler_X.fit_transform(X)

# Normalize Target (bike_rentals)
scaler_y = StandardScaler()
y_scaled = scaler_y.fit_transform(y.reshape(-1,1)).flatten()  # scale to ~0 mean, 1 std

# Split Train/Test
X_train, X_test, y_train_scaled, y_test_scaled = train_test_split(
    X_scaled, y_scaled, test_size=0.2, random_state=42
)

# Convert to Value objects for micrograd
X_train_val = [list(map(Value, xrow)) for xrow in X_train]
y_train_val = [Value(yi) for yi in y_train_scaled]

X_test_val = [list(map(Value, xrow)) for xrow in X_test]
y_test_val = [Value(yi) for yi in y_test_scaled]

# Initialize MLP
model = MLP(len(features), [32, 32, 1])  # 2 hidden layers with 16 neurons each

# Train Model & Save Weights
# Training parameters
epochs = 100
learning_rate = 1e-2

# Try to load weights first
if os.path.exists("bike_model_weights.pkl"):
    with open("bike_model_weights.pkl", "rb") as f:
        weights = pickle.load(f)
    # assign saved weights
    for p, w in zip(model.parameters(), weights):
        p.data = w
    print("Loaded saved weights.")
else:
    # Training loop
    for k in range(epochs):
        total_loss = Value(0.0)
        for xi, yi in zip(X_train_val, y_train_val):
            pred = model(xi) # MLP returns list of Value
            loss = (pred - yi)**2
            total_loss += loss

        # Backward
        model.zero_grad()
        total_loss.backward()

        # Update weights
        for p in model.parameters():
            p.data -= learning_rate * p.grad

        if k % 10 == 0:
            print(f"Epoch {k} Loss: {total_loss.data:.2f}")

    # Save weights
    weights = [p.data for p in model.parameters()]
    with open("bike_model_weights.pkl", "wb") as f:
        pickle.dump(weights, f)
    print("Training finished and weights saved.")

# Evaluate on test set (scaled)
preds = []
for xi in X_test_val:
    pred = model(xi)
    preds.append(pred.data)

# Compute MSE on scaled targets
mse_scaled = np.mean((np.array(preds) - y_test_scaled)**2)
print(f"Test MSE (scaled targets): {mse_scaled:.4f}")

# Convert predictions back to original scale
preds_real = scaler_y.inverse_transform(np.array(preds).reshape(-1,1)).flatten()

# Original unscaled test targets
y_test_original = scaler_y.inverse_transform(y_test_scaled.reshape(-1,1)).flatten()

# Compute MSE in original units
mse_real = np.mean((preds_real - y_test_original)**2)
print(f"Test MSE (real bike rentals): {mse_real:.2f}")

# Visualize predictions vs actuals
plt.figure(figsize=(8,5))
plt.scatter(range(len(y_test_original)), y_test_original, label="Actual")
plt.scatter(range(len(y_test_original)), preds_real, label="Predicted", alpha=0.7)
plt.xlabel("Test sample index")
plt.ylabel("Bike rentals")
plt.legend()
plt.show()

# Calculate Prediction Accuracy
# Compute absolute percentage error
percentage_errors = np.abs(preds_real - y_test_original) / y_test_original * 100

from sklearn.metrics import r2_score

r2 = r2_score(y_test_original, preds_real)
print(f"R² Score: {r2:.4f}")  # Closer to 1 → better


# ===============================
# Custom Input Prediction
# ===============================
# Define a custom input sample with real-world values
# Features: ['hour', 'temperature', 'humidity', 'weather', 'working_day', 'windspeed']
# Example: 2 PM, 25°C, 50% humidity, clear weather, working day, windspeed 10 km/h
custom_input = [14, 25.0, 50.0, 0, 1, 10.0]

# ===============================
# Scale the Custom Input
# ===============================
# Apply the same scaling transformation used on training data
# StandardScaler requires 2D input, so we wrap in a list
custom_input_scaled = scaler_X.transform([custom_input])

# ===============================
# Convert to Value Objects
# ===============================
# Convert scaled features to micrograd Value objects for the neural network
from micrograd.engine import Value
custom_input_val = list(map(Value, custom_input_scaled[0]))

# ===============================
# Make Prediction (Scaled)
# ===============================
# Pass scaled input through the trained model to get scaled prediction
pred_scaled = model(custom_input_val).data

# ===============================
# Inverse Scale the Prediction
# ===============================
# Convert prediction from scaled units back to original bike rental units
pred_real = scaler_y.inverse_transform([[pred_scaled]])[0,0]

# ===============================
# Calculate Relative Prediction
# ===============================
# Compute prediction as a percentage of average daily rentals for context
average_rentals = df['bike_rentals'].mean()
pred_percentage = (pred_real / average_rentals) * 100

# ===============================
# Display Results
# ===============================
# Print the predicted bike rentals in real-world units and as percentage of average
print(f"Predicted bike rentals: {pred_real:.2f}")
print(f"Predicted rentals (% of average day): {pred_percentage:.2f}%")