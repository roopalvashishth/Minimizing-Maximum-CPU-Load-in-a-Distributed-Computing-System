import heapq
import os

class JobProcessor:
    def __init__(self):
        # List to store all tasks (start time, end time, CPU load)
        self.task_list = []
        # Min-heap to track active overlapping tasks based on end times
        self.min_heap = []

    def add_task(self, task):
        """Adds a task to the list of tasks, validates CPU load and time."""
        start, end, cpu_load = task

        # Validation: CPU load cannot be negative
        if cpu_load < 0:
            raise ValueError("Error: Negative CPU load cannot be entered.") 

        # Validation: Start time cannot be greater than end time
        if start > end:
            raise ValueError("Error: Start time is greater than end time, which is not possible.")

        self.task_list.append(task)

    def find_max_cpu_load(self):
        """Calculates the minimum possible maximum CPU load."""
        # Sort tasks by their start time for processing in chronological order
        self.task_list.sort(key=lambda x: x[0])

        max_load = 0  # Maximum CPU load at any time
        current_load = 0  # Current CPU load based on active tasks

        for start, end, cpu_load in self.task_list:
            # Remove tasks from the heap whose end time is <= the current task's start time
            while self.min_heap and self.min_heap[0][0] <= start:
                _, old_cpu = heapq.heappop(self.min_heap)
                current_load -= old_cpu

            # Add the current task to the heap
            heapq.heappush(self.min_heap, (end, cpu_load))
            current_load += cpu_load

            # Update the maximum CPU load if needed
            max_load = max(max_load, current_load)

        return max_load

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the input and output file paths
input_file_path = os.path.join(current_dir, "inputPS06.txt")
output_file_path = os.path.join(current_dir, "outputPS06.txt")

# Read input from input file
try:
    with open(input_file_path, "r") as input_file:
        tasks = eval(input_file.read().strip())  # Read and parse the tasks list

    # Process tasks
    processor = JobProcessor()
    for task in tasks:
        processor.add_task(task)

    # Calculate the minimum maximum CPU load
    result = processor.find_max_cpu_load()

    # Write the result to output file
    with open(output_file_path, "w") as output_file:
        output_file.write(f"Minimum Max CPU Load: {result}\n")
        print("Output file generated successfully.")

except ValueError as e:
    # Write the error message to output file
    with open(output_file_path, "w") as output_file:
        output_file.write(f"{str(e)}\n")
        print(f"{str(e)}\n")
except FileNotFoundError:
    print(f"Error: '{input_file_path}' not found in the directory.")
except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")
