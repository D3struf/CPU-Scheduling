
public class Process {
	private int process_id;
	private int arrival_time;
	private int burst_time;
	private int priority;
	private int completion_time;
	
	Process (int process_id, int arrival_time, int burst_time, int priority) {
		this.setProcessId(process_id);
		this.setArrivalTime(arrival_time);
		this.setBurstTime(burst_time);
		this.setPriority(priority);
		this.setCompletionTime(0);
	}
	
	// Getter Methods
	public int getProcessId() {
		return process_id;
	}
	
	public int getArrivalTime() {
		return arrival_time;
	}
	
	public int getBurstTime() {
		return burst_time;
	}
	
	public int getPriority() {
		return priority;
	}
	
	public int getCompletionTime() {
		return completion_time;
	}
	
	// Setter Methods
	public void setProcessId(int process_id) { 
		this.process_id = process_id;
	}
	
	public void setArrivalTime(int arrival_time) {
		this.arrival_time = arrival_time;
	}
	
	public void setBurstTime(int burst_time) {
		this.burst_time = burst_time;
	}
	
	public void setPriority(int priority) {
		this.priority = priority;
	}
	
	public void setCompletionTime(int completion_time) {
		this.completion_time = completion_time;
	}
}
