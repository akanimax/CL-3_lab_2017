
public class ConcurrentQuicksort implements Runnable{

	int array[], lo, hi, id;
	public ConcurrentQuicksort(int array[], int lo, int hi, int id) {
		this.array = array;
		this.lo = lo;
		this.hi = hi;
		this.id = id;
	}
	public void quicksort() {
		if(lo<hi) {
			int p = partition();
			/*
			 * now spawn new threads here
			*/
			new Thread(new ConcurrentQuicksort(array, lo, p-1, id*2)).start();
			new Thread(new ConcurrentQuicksort(array, p+1, hi, id*2+1)).start();
		}
	}
	public int partition() {
		int pivot = array[hi];
		int i = lo;
		for(int j=lo; j<=hi-1; j++) {
			if(array[j]<=pivot) {
				swap(j,i);
				i++;
			}
		}
		swap(i,hi);
		return i;
	}
	public void swap(int x, int y) {
		if(x!=y) {
			int temp = array[x];
			array[x] = array[y];
			array[y] = temp;
		}
	}
	public String print(int lo, int hi) {
		String s = "array["+lo+".."+hi+"] = ";
		for(int i=lo; i<=hi; i++) {
			s += array[i]+ " ";
		}
		s+="\n";
		return s;
	}
	public void run() {
		System.out.print("Thread"+id+" is now sorting: "+print(lo,hi));
		quicksort();
	}
}
