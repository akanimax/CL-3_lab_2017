
public class TheMaster {
	public static int mThreadCounter = 1;
	public static void main(String args[]) {
		TheWorker firstWorker = new TheWorker(mThreadCounter++);
		Thread t = new Thread(firstWorker);
		t.start();
	}
}
