import java.lang.String;

public class BinarySearch {

    // l - left
    // r - right
    // x - element you are searching for
    public static String binarySearch(int[] arr, int l, int r, int x) {
        while (l <= r) {
            // (r-l) - current search interval
            // (r-l)//2 - finds the middle point of the interval NB! floor division
            // l + (r-l)//2 - finds the index of subarray midpoint in the entire array
            int mid = l + (r - l) / 2;

            if (arr[mid] == x) {
                return "The number '" + x + "' exists in the array.";
            }

            // if x is greater, ignore left half
            else if (arr[mid] < x) {
                l = mid + 1;
            }

            // if x is smaller, ignore right half
            else {
                r = mid - 1;
            }
        }

        // if we reach here, then the element was not present
        return "No such number in the array.";
    }

    public static void main(String[] args) {
        // Example usage:
        int[] arr = {1, 2, 7, 9, 15, 37, 55, 90, 101, 176, 400, 923};
        int x = 176;
        String result = binarySearch(arr, 0, arr.length - 1, x);
        System.out.println(result);
    }
}
