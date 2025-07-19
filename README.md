# Minimizing-Maximum-CPU-Load-in-a-Distributed-Computing-System
Using a min-heap to efficiently calculate the minimum possible maximum CPU load in distributed systems, ensuring scalability for managing thousands of concurrent tasks with specific start times, end times, and CPU loads.

Input:
A list of tasks, where each task is represented as a tuple (start_time, end_time, cpu_load).
Given Input: [(1, 4, 3), (2, 5, 4), (7, 9, 6)]

Output:
The minimum possible maximum CPU load at any time.
Desired Output: 7

Explanation:
At time 2, two tasks are running with a total CPU load of 3 + 4 = 7.
At time 7, only one task is running with a CPU load of 6.
Hence, the peak CPU load is 7.

Solution Design:
The solution uses a min-heap to efficiently track overlapping tasks and calculate the peak CPU load.

Algorithm:
1. Sort Jobs: Sort the jobs by their start time to process them in chronological order.
2. Process Jobs: For each job:
• Remove completed jobs from the min-heap.
• Add the current job to the min-heap.
• Update the current CPU load by adding the current job's CPU load and track the maximum
CPU load.
3. Return Result: The maximum CPU load observed during the processing of jobs is the result.

Complexity Analysis:
1. Time Complexity:
• Sorting tasks: O(n log n), where n is the number of tasks.
• Processing tasks: Each task is pushed and popped from the min-heap once, resulting
in O(n log n).
• Total Time Complexity: O(n log n).

2. Space Complexity:
• The min-heap stores at most n tasks.
• Total Space Complexity: O(n).

Assumptions:
The solution assumes that tasks are valid if start_time < end_time and cpu_load >= 0.

Conclusion:
The proposed solution efficiently calculates the minimum possible maximum CPU load in a distributed computing system using a min-heap. It is scalable, dynamic, and suitable for systems managing thousands of concurrent tasks.
