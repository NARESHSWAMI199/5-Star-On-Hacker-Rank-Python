
// import java.util.*;
// class CirculalArray{
//     public static void main(String[] args) {
//         Scanner in = new Scanner(System.in);
//         int n = in.nextInt();
//         int k = in.nextInt();
//         int q = in.nextInt();
//         int[] a = new int[n];
//         for(int a_i=0; a_i < n; a_i++){
//             a[a_i] = in.nextInt();
//         }
//         // for (int x : a){
//         //     System.out.println("the element : "+x);
//         // }

//         for(int a0 = 0; a0 < q; a0++){
//             int m = in.nextInt();
//             System.out.println(a[(n - (k % n)+ m) % n]);
//         }               
//     }
// }


public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int N = in.nextInt();
    int K = in.nextInt();
    int Q = in.nextInt();
    int rot = K % N;
    // appending the arr elements in arr
    int[] arr = new int[N];
    for (int i = 0; i < N; i++)
        arr[i] = in.nextInt();

    for (int i = 0; i < Q; i++) {
        // indexs which we want 
        int idx = in.nextInt();
        if (idx - rot >= 0)
            System.out.println(arr[idx - rot]);
        else
            System.out.println(arr[idx - rot + arr.length]);
		}
	}







