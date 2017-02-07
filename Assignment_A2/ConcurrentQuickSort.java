import java.util.Scanner;


public class ConcurrentQuickSort {

	int A[];
	public ConcurrentQuickSort() {
		System.out.println("Enter the array (space separated): ");
		Scanner sc = new Scanner(System.in);
		//String input = sc.nextLine();
		String input = "4 3 6 1 2 5 7";
		populateArray(input);
		quicksort(0,A.length-1);
		print(0, A.length-1);
	}
	public void populateArray(String input) {
		String arr[] = input.split(" ");
		A = new int[arr.length];
		for(int i=0; i<arr.length; i++) {
			A[i] = Integer.parseInt(arr[i]);
		}
	}
	public void quicksort(int lo, int hi) {
		System.out.print("Now sorting: ");
		print(lo, hi);
		if(lo<hi) {
			int p = partition(lo, hi);
			quicksort(lo, p-1);
			quicksort(p+1, hi);
			print(lo, hi);
		}
	}
	public int partition(int lo, int hi) {
		int pivot = A[hi];
		int i = lo;
		for(int j=lo; j<=hi-1; j++) {
			if(A[j]<=pivot) {
				swap(j,i);
				i++;
			}
		}
		swap(i,hi);
		return i;
	}
	public void swap(int x, int y) {
		if(x!=y) {
			int temp = A[x];
			A[x] = A[y];
			A[y] = temp;
		}
	}
	public void print(int lo, int hi) {
		for(int i=lo; i<=hi; i++) {
			System.out.print(A[i]+ " ");
		}
		System.out.println();
	}
	public static void main(String[] args) {
		ConcurrentQuickSort qs = new ConcurrentQuickSort();
	}

}
