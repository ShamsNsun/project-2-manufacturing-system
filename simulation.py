import simpy
import random
from models import Machine, Operator, Operation

def process_operation(env, machine, operator, operation_time, failure_rate):
    while True:
        try:
            yield env.timeout(operation_time)
            if random.random() < failure_rate:
                print(f"Machine {machine.id} failed at time {env.now}")
                yield env.timeout(random.randint(1, 5))
            print(f"Operation completed by Machine {machine.id} at time {env.now}")
        except simpy.Interrupt:
            print(f"Machine {machine.id} interrupted at time {env.now}")

def machine_process(env, machine, operator):
    while True:
        operation_time = machine.operation.duration
        failure_rate = machine.failure_rate
        yield env.process(process_operation(env, machine, operator, operation_time, failure_rate))

def create_machines(processing_times, failure_rates):
    return [Machine(i, Operation('machining', processing_times['machining']), failure_rates['machining']) for i in range(5)]

def create_operators(shift_patterns):
    return [Operator(i, 'shift_1') for i in range(3)] + [Operator(i, 'shift_2') for i in range(3, 6)]

def run_simulation(env, machines, operators, runtime):
    for machine in machines:
        for operator in operators:
            env.process(machine_process(env, machine, operator))
    env.run(until=runtime)
