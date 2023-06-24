import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;

public class CPU_Scheduling_Algorithm {
	public void preemptive_priority_sched(List<Process> processes) {
		PriorityQueue<Process> queue = new PriorityQueue<>(Comparator.comparingInt(Process::getPriority));
        int currentTime = 0;

        // Enqueue processes based on arrival time and priority
        for (Process process : processes) {
            queue.add(process);
        }

        // Execute processes based on priority
        while (!queue.isEmpty()) {
            Process currentProcess = queue.poll();
            currentTime += currentProcess.getBurstTime();
            currentProcess.setCompletionTime(currentTime);
            System.out.println("Process " + currentProcess.getProcessId() + " completed at time " + currentTime);
        }
	}
}
