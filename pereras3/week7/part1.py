
import numpy as np
# Create/add Qubit ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
def pushQubit(weights):
    global workspace
    workspace = np.reshape(workspace,(1,-1)) 
    workspace = np.kron(workspace,weights)

def applyGate(gate):
    global workspace
    workspace = np.reshape(workspace,(-1,gate.shape[0]))     
    np.matmul(workspace,gate.T,out=workspace)
    
# Move Qubit to stack top ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
def tosQubit(k):
    global workspace
    if k > 1:                                               # if non-trivial
        workspace = np.reshape(workspace,(-1,2,2**(k-1)))
        workspace = np.swapaxes(workspace,-2,-1)


# Measure a Qubit ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

def probQubit():
    global workspace
    workspace = np.reshape(workspace,(-1,2)) 
    prob = np.linalg.norm(workspace,axis=0)**2
    print('probability is', prob)
    total_prob = np.sum(prob)
    if total_prob != 1:
        prob /= total_prob
    return prob
    
def measureQubit():
    global workspace
    prob = probQubit()
    measurement = np.random.choice(2,p=prob)         # select 0 or 1 
    workspace = (workspace[:,[measurement]]/
    np.sqrt(prob[measurement])) 
    return str(measurement)


# ===== #
# Gates #
# ===== #
X_gate = np.array([[0, 1],                      # Pauli X gate
                   [1, 0]])                     # = NOT gate

Y_gate = np.array([[ 0,-1j],                    # Pauli Y gate
                   [1j,  0]])                   # = SHZHZS
  
Z_gate = np.array([[1, 0],                      # Pauli Z gate
                   [0,-1]])                     # = P(pi) = S^2
                                                # = HXH

H_gate = np.array([[1, 1],                      # Hadamard gate 
                   [1,-1]]) * np.sqrt(1/2)

S_gate = np.array([[1, 0],                      # Phase gate
                   [0,1j]])                     # = P(pi/2) = T^2
                   
T_gate = np.array([[1,                0],       # = P(pi/4)
                   [0,np.exp(np.pi/-4j)]])
                   
Tinv_gate = np.array([[1, 0],                   # = P(-pi/4) 
                      [0,np.exp(np.pi/4j)]])    # = T^-1
                      
def P_gate(theta):
    # Phase shift gate, even though shift is not the same as rotation,
    # the same angles will be implemented
    return np.array([[1,             0],
                     [0,np.exp(theta*1j)]])
                     
def Rx_gate(theta):                             # Y rotation gate
    return np.array([[np.cos(theta/2),-1j*np.sin(theta/2)],
                     [-1j*np.sin(theta/2),np.cos(theta/2)]])
                     
def Ry_gate(theta):                             # Y rotation gate return 
    return np.array([[np.cos(theta/2),-np.sin(theta/2)],
              [np.sin(theta/2), np.cos(theta/2)]])
              
def Rz_gate(theta):                             # Z rotation gate 
    return np.array([[np.exp(-1j*theta/2),0],
                     [0,np.exp(1j*theta/2)]])
                     
CNOT_gate = np.array([[1, 0, 0, 0],             # Ctled NOT gate
                      [0, 1, 0, 0],             #=XORgate
                      [0, 0, 0, 1],
                      [0, 0, 1, 0]])
                      
CZ_gate = np.array([[1, 0, 0, 0],               # Ctled Z gate
                    [0, 1, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0,-1]])
                    
SWAP_gate = np.array([[1, 0, 0, 0],             # Swap gate
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 1]])
                      
TOFF_gate = np.array([[1, 0, 0, 0, 0, 0, 0, 0], # Toffoli gate
                     [0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1],
                     [0, 0, 0, 0, 0, 0, 1, 0]])



''' Create a qubic and append more '''

workspace = np.array([[1.]])       # create empty qubit stack pushQubit([1,0])
pushQubit([1,0])
print(workspace)
pushQubit([0,1])               # push a 2nd qubit print(workspace)
print(workspace)

workspace = np.array([[1.]], dtype = complex)       # create empty qubit stack pushQubit([1,0])
pushQubit(np.array([1,0], dtype = complex))
original = workspace



# ==================== #
# Gates implementation #
# ==================== #

# prove that the shortcut and the definition are the same
print(np.matmul(X_gate,[1,0]))
print("input x-gate",workspace)
applyGate(X_gate)                  # = NOT 
print("output x-gate",workspace)


# loop to try all the gates and with differeen thetas if they are defined by one to the original workspace

gate_list = (X_gate, Y_gate, Z_gate, H_gate, S_gate, T_gate, Tinv_gate)
gate_name = ('X_gate', 'Y_gate', 'Z_gate', 'H_gate', 'S_gate', 'T_gate', 'Tinv_gate')
print("initial input for all gates {}".format(original))


# loop to implemente all no angled gates to the same workspace
for gate, name in zip(gate_list, gate_name):
    workspace = original.copy()
    applyGate(gate)
    print(' output for {} is {}'.format(name, workspace))


# loop to implemente all angled gates to the same workspace
gate_angle = (P_gate, Rx_gate, Ry_gate, Rz_gate)
name_gate_angle = ('P_gate', 'Rx_gate', 'Ry_gate', 'Rz_gate')
theta_deg = (45, 90, 180)

for gate_a, name_a in zip(gate_angle, name_gate_angle):
    for angle in theta_deg:
        theta = np.deg2rad(angle)
        workspace = original.copy()
        gate = gate_a(theta)
        applyGate(gate)
        print('output for {} with angle {} (deg) is {}'.format(name_a, angle, workspace))






# ==================================== #
# Move a qubit to the top of the stack #
# ==================================== #

workspace = np.array([[1.]])
pushQubit([1,0])
pushQubit([0.6,0.8])
print(workspace)
tosQubit(2)
print(workspace)
print(np.reshape(workspace,(1,-1)))


# =============== #
# Measure a Qubit #
# =============== #

meas_qubit = []
workspace = np.array([[1. ]])
for n in range(30):
    pushQubit(np.array([0.6,0.8], dtype = complex))
    meas_qubit.append(measureQubit())
print(meas_qubit)

result_q = []
workspace = np.array([[1.]]) 
for i in range(16):
    pushQubit([1,0])                      # push a zero qubit
    applyGate(H_gate)                     # set equal 0 and 1 probability
    pushQubit([1,0])                      # push a 2nd zero qubit
    applyGate(H_gate)                     # set equal 0 and 1 probability
    pushQubit([1,0])                      # push a dummy zero qubit
    applyGate(TOFF_gate)                  # compute Q3 = Q1 AND Q2
    q3 = measureQubit()                   # pop qubit 3
    q2 = measureQubit()                   # pop qubit 2
    q1 = measureQubit()                   # pop qubit 1
    result_q.append(q1+q2+q3)
print(result_q[0])
print(result_q[1:-1])
