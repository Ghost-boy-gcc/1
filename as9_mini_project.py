# Code
# Implementation of Job Scheduling using Topological Sort (Kahn's Algorithm)
from collections import deque

def find_job_schedule(jobs, dependencies):

    # --- 1. Model the Graph and In-Degrees ---

    # Adjacency list to represent the graph, e.g., {'A': ['B', 'C']}
    adj_list = {job: [] for job in jobs}

    # Dictionary to store the in-degree of each job
    in_degree = {job: 0 for job in jobs}

    # Populate the adjacency list and in-degree map from the dependencies
    for prereq, job in dependencies:
        adj_list[prereq].append(job)
        in_degree[job] += 1

    # --- 2. Use Kahn's Algorithm ---

    # Initialize a queue with all jobs that have an in-degree of 0
    queue = deque([job for job in jobs if in_degree[job] == 0])

    # This list will store the final sorted job schedule
    scheduled_order = []

    while queue:
        # Dequeue a job that can be executed
        current_job = queue.popleft()
        scheduled_order.append(current_job)

        # "Complete" the job by updating its neighbors' in-degrees
        for dependent_job in adj_list[current_job]:
            in_degree[dependent_job] -= 1
            # If a dependent job now has no prerequisites, add it to the queue
            if in_degree[dependent_job] == 0:
                queue.append(dependent_job)

    # --- 3. Handle Cycles ---

    # If the scheduled order has fewer jobs than the total, there was a cycle
    if len(scheduled_order) == len(jobs):
        return scheduled_order
    else:
        return "Error: A cycle was detected in the dependencies. No valid schedule exists."

# --- Example Usage ---

# Example 1: A valid set of jobs (getting dressed)
print("--- Example 1: Getting Dressed ---")
jobs_1 = ['underwear', 'socks', 'pants', 'shoes', 'shirt', 'belt', 'jacket']
dependencies_1 = [
    ('underwear', 'pants'),
    ('socks', 'shoes'),
    ('pants', 'shoes'),
    ('pants', 'belt'),
    ('shirt', 'belt'),
    ('belt', 'jacket')
]

schedule_1 = find_job_schedule(jobs_1, dependencies_1)
print(f"A valid job schedule is: {schedule_1}\n")


# Example 2: An impossible schedule with a cycle
print("--- Example 2: Impossible Schedule with a Cycle ---")
jobs_2 = ['Task A', 'Task B', 'Task C']
dependencies_2 = [
    ('Task A', 'Task B'),
    ('Task B', 'Task C'),
    ('Task C', 'Task A') # This creates a cycle
]

schedule_2 = find_job_schedule(jobs_2, dependencies_2)
print(f"Result: {schedule_2}")