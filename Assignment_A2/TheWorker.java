
public class TheWorker implements Runnable{
	int id;
	public TheWorker(int n) {
		id = n;
	}
	public void run() {
		
		System.out.println("This is thread with id "+id);
		if(id>4) return;
		int left = id*2;
		int right = id*2+1;
		System.out.println(id+ " is now spawning "+left+" and "+right);
		new Thread(new TheWorker(left)).start();
		new Thread(new TheWorker(right)).start();
		
	}

}
