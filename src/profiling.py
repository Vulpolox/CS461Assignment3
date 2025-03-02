from typing import Callable
import time
import multiprocessing


# Define the wrapper function at the top level
def wrapper(func: Callable, args, return_dict):
    start_time = time.time()
    func(*args)  # Run the target function
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000000  # Convert to microseconds
    return_dict['execution_time'] = execution_time


def get_execution_time(func: Callable, timeout: float, *args) -> None:
    # Create a multiprocessing Manager for shared data
    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    # Create a Process to run the function
    process = multiprocessing.Process(target=wrapper, args=(func, args, return_dict))
    
    process.start()

    # Wait for the process to complete or timeout
    process.join(timeout)

    # If the process is still alive, it means it exceeded the timeout
    if process.is_alive():
        process.terminate()  # Forcefully terminate the process
        print(f"\n---\nTimeout exceeded after {timeout} seconds.\n---\n")
    else:
        # If the process finishes in time, print the execution time
        print(f'\n---\nExecution Time: {return_dict["execution_time"]} μs\n---\n')