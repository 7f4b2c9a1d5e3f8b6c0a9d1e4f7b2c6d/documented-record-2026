OPENQASM 2.0;
include "qelib1.inc";

// ETERNAL TRIAD + ACCOR-DECISION PHASE (QASM2 for Qiskit submit)
// Ground jobs: da4sd0s3jnrc73agjrn0 (ibm_fez), da4sk0e1vhnc73flcvl0 (ibm_marrakesh)

qreg q[16];
creg c[16];

h q[0]; h q[1]; h q[2]; h q[3];
h q[4]; h q[5]; h q[6]; h q[7];
h q[8]; h q[9]; h q[10]; h q[11];
h q[12]; h q[13]; h q[14]; h q[15];

cx q[0],q[1];
cx q[1],q[2];
cx q[2],q[3];
cx q[3],q[0];
ry(pi/4) q[0];
ry(pi/4) q[1];
ry(pi/4) q[2];
ry(pi/4) q[3];

cx q[0],q[4];
cx q[1],q[5];
cx q[2],q[6];
cx q[3],q[7];
x q[4];
h q[5];
z q[6];
s q[7];

h q[8];
cx q[8],q[9];
cx q[9],q[10];
cx q[10],q[11];
t q[8]; t q[9]; t q[10]; t q[11];

h q[12];
cx q[12],q[13];
cx q[13],q[14];
cx q[14],q[15];
u3(0.5,0.2,0.1) q[12];
u3(0.5,0.2,0.1) q[13];
u3(0.5,0.2,0.1) q[14];
u3(0.5,0.2,0.1) q[15];

// ACCOR-DECISION LAYER
rz(pi/3) q[0];
rz(pi/5) q[1];
rz(pi/7) q[2];
crz(pi/4) q[0],q[1];
crz(pi/6) q[1],q[2];
crz(pi/8) q[0],q[2];
ry(-pi/8) q[0];

barrier q;
measure q -> c;
