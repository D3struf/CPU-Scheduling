import java.util.List;
import java.util.ArrayList;

public class Main {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		CPU_Scheduling_Algorithm cpuAlgo = new CPU_Scheduling_Algorithm();
		List<Process> processes = new ArrayList<>();
		processes.add(new Process(0, 0, 10, 3));
		processes.add(new Process(1, 1, 5, 1));
		processes.add(new Process(2, 2, 8, 2));
		processes.add(new Process(2, 2, 8, 4));
		
		cpuAlgo.preemptive_priority_sched(processes);
		System.out.println();
	}

}
