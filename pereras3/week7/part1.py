
import numpy as np

def pushQubit(weights):
    global workspace
    workspace = np.reshape(workspace,(1,-1)) 
    workspace = np.kron(workspace,weights)

def applyGate(gate):
    global workspace
    workspace = np.reshape(workspace,(-1,gate.shape[0]))     
    np.matmul(workspace,gate.T,out=workspace)


''' Gates '''

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
                      
def P_gate(phi):                                # Phase shift gate
    return np.array([[1,             0],
                     [0,np.exp(phi*1j)]])
                     
def Rx_gate(theta):                             # Y rotation gate
    return np.array([[np.cos(theta/2),-1j*np.sin(theta/2)],
                     [-1j*np.sin(theta/2),np.cos(theta/2)]])
                     
def Ry_gate(theta):                             # Y rotation gate return 
    np.array([[np.cos(theta/2),-np.sin(theta/2)],
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
pushQubit([3/5,4/5])               # push a 2nd qubit print(workspace)
print(workspace)
original = workspace

''' Gates implementation ''''
theta = (45, 90, 180)
gate_list = (X_gate, Y_gate, Z_gate, H_gate, S_gate, T_gate, Tinv_gate)

# prove that the shortcut and the definition are the same
print(np.matmul(X_gate,workspace))
print("input x-gate",workspace)
applyGate(X_gate)                  # = NOT 
print("output x-gate",workspace)


# loop to try all the gates and with differeen thetas if they are defined by one to the original workspace
print('initial input for all gates')
for gate in gate_list:
  applyGate(gate)
  print(f' output for {gate} is {workspace}'


