import numpy as np 
import matplotlib.pyplot as plt 
c =-1
plt.style.use("dark_background")
def f(z):
    return np.square(z)+c

selected_values = np.array([0.4 + 0.4j, 0.41 + 0.4j, 0.4 + 0.41j])
num_iter = 9

outputs = np.zeros((num_iter+1, selected_values.shape[0]), dtype=complex)
outputs[0] = selected_values

for i in range(num_iter):
    outputs[i+1] = f(outputs[i])  # Apply 10 iterations, save each output

fig, axes = plt.subplots(1, selected_values.shape[0], figsize=(16, 6))
axes[1].set_xlabel('Real axis')
axes[0].set_ylabel('Imaginary axis')
ans=[
    [0.4,-1.,-0.1024,-1.39911424,0.94034079,-0.250279,-1.41315199,0.87778501,-1.18177046,-2.53836105],
    [0.4,0.32,-0.64,0.131072,-0.3667694,-0.68977646,0.34527312,-0.9758468,-1.71316738,4.0491412],
    [0.41,-0.9919,-0.12371839,-1.40808655,0.95678553,-0.29014609,-1.66861566,1.53078095,-1.47993742,-25.27235411],
    [0.4,0.328,-0.6506864,0.16100375,-0.45341442,-0.86764072,0.50348513,-1.68024633,-5.14417815,15.22612345],
    [0.4,-1.0081,-0.09131839,-1.42899663,1.02744351,-0.06351525,-1.49910679,1.23920212,0.46263738,-1.23427319],
    [0.41,0.328,-0.6613136,0.12078019,-0.34518896,-0.70932431,0.09010582,-0.27015648,-0.66955697,-0.61952416]
]
i=0
for ax, data in zip(axes, outputs.T):
    cycle = ax.scatter(data.real, data.imag, c=range(data.shape[0]), alpha=0.6)
    ax.set_title(f'Mapping of iterations on {data[0]}')
    i+=2

fig.colorbar(cycle, ax=axes, location="bottom", label='Iteration');
plt.show()

