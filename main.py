from queue import PriorityQueue, Queue
from typing import List


class Process:
    def __init__(self, process_id, arrival_time, burst_time, priority):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.remaining_time = burst_time

    def __lt__(self, other):
        if self.priority < other.priority:
            return self.priority < other.priority
        if self.burst_time == other.burst_time:
            return self.process_id < other.process_id
        if self.arrival_time == 0 and other.arrival_time != 0:
            return True
        elif self.arrival_time != 0 and other.arrival_time == 0:
            return False
        elif self.arrival_time == other.arrival_time:
            return self.burst_time < other.burst_time
        return self.burst_time < other.burst_time


def priority_preemptive(processes):
    def find_max_prior_arrived(currTime, lst):
        available_processes = []
        for process in lst:
            if process.arrival_time <= currTime and process.remaining_time > 0:
                available_processes.append(process)
        if available_processes:
            available_processes.sort(key=lambda x: x.priority)
            return available_processes[0], True
        return None, False

    def all_done(lst):
        for process in lst:
            if process.remaining_time != 0:
                return False
        return True

    curr_time = 0
    while not all_done(processes):
        process, has_arrived = find_max_prior_arrived(curr_time, processes)
        if not has_arrived:
            curr_time += 1
            continue

        process.remaining_time -= 1
        curr_time += 1
        if process.remaining_time == 0:
            process.completion_time = curr_time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time

    return processes


def round_robin(processes: List[Process], time_quantum: int) -> List[Process]:
    queue = Queue()
    total_time = 0
    total_time_counted = 0
    wait_time = 0
    turnaround_time = 0
    completed_processes = []

    for process in processes:
        total_time += process.burst_time
        queue.put(process)

    while not queue.empty():
        current_process = queue.get()

        if current_process.remaining_time <= time_quantum:
            total_time_counted += current_process.remaining_time
            total_time -= current_process.remaining_time
            current_process.completion_time = total_time_counted
            current_process.turnaround_time = total_time_counted - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
            completed_processes.append(current_process)
            current_process.remaining_time = 0
        else:
            total_time_counted += time_quantum
            total_time -= time_quantum
            current_process.remaining_time -= time_quantum
            queue.put(current_process)

    return completed_processes


def shortest_job_first(processes):
    sjf = PriorityQueue()
    curr_time = 0

    for process in processes:
        if process.arrival_time <= curr_time:
            sjf.put((process.burst_time, process))
        else:
            while not sjf.empty() and process.arrival_time < curr_time + sjf.queue[0][0]:
                _, current_process = sjf.get()
                current_process.completion_time = curr_time + current_process.burst_time
                current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
                current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
                curr_time = current_process.completion_time

            sjf.put((process.burst_time, process))

    while not sjf.empty():
        _, current_process = sjf.get()
        current_process.completion_time = curr_time + current_process.burst_time
        current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
        current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
        curr_time = current_process.completion_time

    return processes


def average_turnaround_time(processes):
    averageTurnaroundTime = 0
    sum_turnaroundTime = 0
    for i in range(len(processes)):
        sum_turnaroundTime += processes[i].turnaround_time

    averageTurnaroundTime = sum_turnaroundTime / len(processes)
    return averageTurnaroundTime


def average_waiting_time(processes):
    averageWaitingTime = 0
    sum_waitingTime = 0
    for i in range(len(processes)):
        sum_waitingTime += processes[i].waiting_time

    averageWaitingTime = sum_waitingTime / len(processes)
    return averageWaitingTime


def cpu_Utilization(processes):
    sum_burstTime = 0
    for i in range(len(processes)):
        sum_burstTime += processes[i].burst_time

    cpu_utilization = (sum_burstTime / float(processes[-1].completion_time)) * 100
    return cpu_utilization


def system_Throughput(processes):
    length = len(processes)
    system_throughput = length / float(processes[-1].completion_time)
    return system_throughput


def get_input(prompt):
    while True:
        try:
            num_process = int(input(prompt))
            if num_process < 0:
                print("Input Invalid, Try Again!")
            else:
                return num_process
        except ValueError:
            print("Input Invalid, Try Again!")


def main():
    list_processes = []
    print("CPU Scheduling Algorithms")
    print("[1] Shortest Job First")
    print("[2] Round Robin")
    print("[3] Preemptive Priority")
    algo = int(input("Choose your Algorithm: "))

    if algo > 3 or algo <= 0:
        print("Input Invalid, Try Again!")
    elif algo == 1:
        print("Shortest Job First")
        num = get_input("Enter the number of Processes: ")
        for i in range(1, num + 1):
            print(f"Process {i}:")
            AT = get_input("Enter Arrival Time: ")
            BT = get_input("Enter Burst Time: ")
            process = Process(i, AT, BT, i)
            list_processes.append(process)

        result = shortest_job_first(list_processes)
        avg_turnaroundTime = average_turnaround_time(list_processes)
        avg_waitingTime = average_waiting_time(list_processes)
        cpuUtilization = cpu_Utilization(list_processes)
        systemThroughput = system_Throughput(list_processes)
        print("\nShortest Job First Result:")
        print(f"Process ID\t\tArrival Time\t\tBurst Time\t\tCompletion Time\t\tTurnaround Time\t\tWaiting Time\t\t")
        for process in result:
            print(f"Process {process.process_id}\t\t\t{process.arrival_time}\t\t\t\t\t{process.burst_time}\t\t\t\t\t{process.completion_time}\t\t\t\t{process.turnaround_time}\t\t\t\t\t{process.waiting_time}")
        print()
        print(f"======================================================>  Average:\t\t\t{avg_waitingTime}\t\t\t\t{avg_turnaroundTime}")
        print("CPU Utilization:", cpuUtilization, '%')
        print("System Throughput:", systemThroughput)
        print()
    elif algo == 2:
        print("Round Robin")
        num = get_input("Enter the number of Processes: ")
        for i in range(1, num + 1):
            print(f"Process {i}:")
            AT = get_input("Enter Arrival Time: ")
            BT = get_input("Enter Burst Time: ")
            process = Process(i, AT, BT, i)
            list_processes.append(process)
        time_quantum = get_input("Enter Time Quantum: ")

        result = round_robin(list_processes, time_quantum)
        avg_turnaroundTime = average_turnaround_time(list_processes)
        avg_waitingTime = average_waiting_time(list_processes)
        cpuUtilization = cpu_Utilization(list_processes)
        systemThroughput = system_Throughput(list_processes)
        print("\nRound Robin Result:")
        print(f"Process ID\t\tArrival Time\t\tBurst Time\t\tCompletion Time\t\tTurnaround Time\t\tWaiting Time\t\t")
        for process in result:
            print(
                f"Process {process.process_id}\t\t\t{process.arrival_time}\t\t\t\t\t{process.burst_time}\t\t\t\t\t{process.completion_time}\t\t\t\t{process.turnaround_time}\t\t\t\t\t{process.waiting_time}")
        print()
        print(
            f"======================================================>  Average:\t\t\t{avg_waitingTime}\t\t\t\t\t{avg_turnaroundTime}")
        print("CPU Utilization:", cpuUtilization, '%')
        print("System Throughput:", systemThroughput)
        print()
    else:
        print("Preemptive Priority")
        num = get_input("Enter the number of Processes: ")
        for i in range(1, num + 1):
            print(f"Process {i}:")
            AT = get_input("Enter Arrival Time: ")
            BT = get_input("Enter Burst Time: ")
            Prio = get_input("Enter Priority: ")
            process = Process(i, AT, BT, Prio)
            list_processes.append(process)

        result = priority_preemptive(list_processes)
        avg_turnaroundTime = average_turnaround_time(list_processes)
        avg_waitingTime = average_waiting_time(list_processes)
        cpuUtilization = cpu_Utilization(list_processes)
        systemThroughput = system_Throughput(list_processes)
        print("\nPreemptive Priority:")
        print(f"Process ID\t\tArrival Time\t\tBurst Time\t\tPriority\t\tCompletion Time\t\tTurnaround Time\t\tWaiting Time\t\t")
        for process in result:
            print(
                f"Process {process.process_id}\t\t\t{process.arrival_time}\t\t\t\t\t{process.burst_time}\t\t\t\t{process.priority}\t\t\t\t\t{process.completion_time}\t\t\t\t{process.turnaround_time}\t\t\t\t\t{process.waiting_time}")
        print()
        print(
            f"======================================================================>  Average:\t\t\t{avg_waitingTime}\t\t\t\t{avg_turnaroundTime}")
        print("CPU Utilization:", cpuUtilization, '%')
        print("System Throughput:", systemThroughput)
        print()

    # processes = [
    #     Process(1, 0, 5, 4),
    #     Process(2, 0, 6, 3),
    #     Process(3, 0, 7, 2),
    #     Process(4, 0, 8, 1)
    # ]
    #
    # time_quantum = 4

    # result = shortest_job_first(processes)
    # avg_turnaroundTime = average_turnaround_time(processes)
    # avg_waitingTime = average_waiting_time(processes)
    # cpuUtilization = cpu_Utilization(processes)
    # systemThroughput = system_Throughput(processes)
    # print("\nShortest Job First Result:")
    # for process in result:
    #     print("Process ID:", process.process_id, '|', process.arrival_time, '|', process.burst_time, '|', process.priority)
    #     print("Completion Time:", process.completion_time)
    #     print("Waiting Time:", process.waiting_time)
    #     print("Turnaround Time:", process.turnaround_time)
    #     print()
    # print("Average Waiting Time:", avg_waitingTime)
    # print("Average Turnaround Time:", avg_turnaroundTime)
    # print("CPU Utilization:", cpuUtilization, '%')
    # print("System Throughput:", systemThroughput)
    # print()
    #
    # result = round_robin(processes, time_quantum)
    # avg_turnaroundTime = average_turnaround_time(processes)
    # avg_waitingTime = average_waiting_time(processes)
    # cpuUtilization = cpu_Utilization(processes)
    # systemThroughput = system_Throughput(processes)
    # print("\nRound Robin Result:")
    # for process in result:
    #     print("Process ID:", process.process_id, '|', process.arrival_time, '|', process.burst_time, '|',
    #           process.priority)
    #     print("Completion Time:", process.completion_time)
    #     print("Waiting Time:", process.waiting_time)
    #     print("Turnaround Time:", process.turnaround_time)
    #     print()
    # print("Average Waiting Time:", avg_waitingTime)
    # print("Average Turnaround Time:", avg_turnaroundTime)
    # print("CPU Utilization:", cpuUtilization, '%')
    # print("System Throughput:", systemThroughput)
    # print()

    # result = priority_preemptive(processes)
    # avg_turnaroundTime = average_turnaround_time(processes)
    # avg_waitingTime = average_waiting_time(processes)
    # cpuUtilization = cpu_Utilization(processes)
    # systemThroughput = system_Throughput(processes)
    # print("\nPreemptive Priority:")
    # for process in result:
    #     print("Process ID:", process.process_id, '|', process.arrival_time, '|', process.burst_time, '|',
    #           process.priority)
    #     print("Completion Time:", process.completion_time)
    #     print("Waiting Time:", process.waiting_time)
    #     print("Turnaround Time:", process.turnaround_time)
    #     print()
    # print("Average Waiting Time:", avg_waitingTime)
    # print("Average Turnaround Time:", avg_turnaroundTime)
    # print("CPU Utilization:", cpuUtilization, '%')
    # print("System Throughput:", systemThroughput)
    # print()


# Call the main function
main()
