
from bloqade.qasm2.emit import QASM2 # the QASM2 target

def write_to_qasm_file(circuit, filename):
    with open(filename, "w") as f:
        qasm_object = QASM2()
        qasm_string = qasm_object.emit_str(circuit)
        f.write(qasm_string)