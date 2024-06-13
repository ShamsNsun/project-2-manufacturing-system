import simpy
from data import processing_times, failure_rates, shift_patterns
from simulation import run_simulation, create_machines, create_operators

def main():
    env = simpy.Environment()
    
    machines = create_machines(processing_times, failure_rates)
    operators = create_operators(shift_patterns)
    
    runtime = 100  # Define simulation runtime
    run_simulation(env, machines, operators, runtime)

if __name__ == "__main__":
    main()
