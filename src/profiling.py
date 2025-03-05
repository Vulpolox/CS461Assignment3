from typing import Callable
import time
import multiprocessing


def wrapper(func: Callable, args, return_dict):
    start_time = time.perf_counter()  # Use high-resolution timer
    func(*args)  # Run the target function
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000000  # Convert to microseconds
    return_dict['execution_time'] = execution_time


def get_execution_time(func: Callable, timeout: float, *args) -> None:
    # Create a new multiprocessing Manager for shared data
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
        process.join()  # Ensure the process is fully terminated
        print(f"\n---\nTimeout exceeded after {timeout} seconds.\n---\n")
    else:
        # Add a small delay to ensure the return_dict is updated
        time.sleep(0.001)
        
        # If the process finishes in time, print the execution time
        if 'execution_time' in return_dict:
            print(f'\n---\nExecution Time: {return_dict["execution_time"]:.0f} μs\n---\n')
        else:
            print('\n---\nError: Execution time not found.\n---\n')

    # Clean up the manager and process
    manager.shutdown()