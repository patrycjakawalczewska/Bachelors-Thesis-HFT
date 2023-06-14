import numpy as np
import matplotlib.pyplot as plt

# set parameters
T = 1000
x0 = 100
r = 0.05
sigma = 0.2
kappa = 0.1
theta = 100
epsilon = 0.01

# simulate paths
np.random.seed(123)
dt = 0.01
t = np.linspace(0, T*dt, T+1)
dw = np.random.randn(2, T+1)
x = np.zeros((2, T+1))
x[:, 0] = x0
for i in range(1, T+1):
    x[0, i] = x[0, i-1] + kappa*(theta-x[0, i-1])*dt + sigma*dw[0, i]*np.sqrt(dt)
    x[1, i] = x[1, i-1] + kappa*(theta-x[1, i-1])*dt + sigma*dw[1, i]*np.sqrt(dt) - epsilon*np.abs(dw[1, i])*np.sqrt(dt)

# plot results
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(t, x[0], label='without transaction costs')
ax.plot(t, x[1], label='with transaction costs')
ax.set_title('Impact of Transaction Costs on HFT')
ax.set_xlabel('Number of Trades')
ax.set_ylabel('Price')
ax.legend()
plt.show()
