import os
from qiskit.test.reference_circuits import ReferenceCircuits
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler

token = os.environ["IBM_AUTH_TOKEN"]
service = QiskitRuntimeService(channel="ibm_quantum", token=token)

backend = service.backend("ibmq_qasm_simulator")
job = Sampler(backend).run(ReferenceCircuits.bell())

print(f"job id: {job.job_id()}")
result = job.result()
print(result)
