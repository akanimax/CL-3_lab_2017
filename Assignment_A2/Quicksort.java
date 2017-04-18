
public class Quicksort {

	public static void main(String[] args) throws InterruptedException {
		System.out.println("Enter the array to be sorted(space separated): ");
		InputParser parser = new InputParser();
		int array[] = parser.getInput();
		
		ConcurrentQuicksort qs = new ConcurrentQuicksort(array, 0, array.length-1, 1);
		new Thread(qs).start();
		Thread.sleep(1000);
		
		//too lazy to use join or other methods to wait for all the threads to complete
		
		System.out.println("\nThe sorted array is:");
		for(int i=0; i<array.length; i++) {
			System.out.print(array[i]+ " ");
		}
		
		System.out.println();
	}
}
/*
--------Output--------:
Enter the array to be sorted(space separated): 
3 1 2 7 5 6 4
Thread1 is now sorting: array[0..6] = 3 1 2 7 5 6 4 
Thread2 is now sorting: array[0..2] = 3 1 2 
Thread3 is now sorting: array[4..6] = 5 6 7 
Thread4 is now sorting: array[0..0] = 1 
Thread5 is now sorting: array[2..2] = 3 
Thread6 is now sorting: array[4..5] = 5 6 
Thread7 is now sorting: array[7..6] = 
Thread13 is now sorting: array[6..5] = 
Thread12 is now sorting: array[4..4] = 5 

The sorted array is:
1 2 3 4 5 6 7 
*/
