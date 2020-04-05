import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.math.BigDecimal;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;
import java.util.StringTokenizer;

public class BinarySearch {

    static class FastScanner {
        BufferedReader br;
        StringTokenizer st;

        FastScanner(InputStream stream) {
            try {
                br = new BufferedReader(new InputStreamReader(stream));
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        String next() {
            while (st == null || !st.hasMoreTokens()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }
    }

    static class BinarySearchService {
        
        public static final int search(final long k, final long[] a, final int left, final int right) {
            if(left > right) { return -1; }

            final int mid = left + (right - left ) / 2;
            if(a[mid] == k) { return mid; } 
            if (k == a[left]) { return left; }
            if (k == a[right]) { return right; }

            if (a[mid] > k) {
                return search(k, a, left + 1, mid - 1);
            } else {
                return search(k, a, mid + 1, right - 1);
            }
        }

        public static final int searchIt(final long k, final long[] a, int left, int right) {
            int mid;
            long vMid;

            if(a.length == 0 || k < a[left] || k > a[right]) {
                return -1;
            } 
            if (k == a[left]) { return left; }
            if (k == a[right]) { return right; }

            while(left <= right) {
                mid = left + (right - left ) / 2;
                vMid = a[mid];

                if(vMid == k) { return mid; }
                if (vMid > k) { 
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }

            return -1;
        }
    }

    static class BinarySearchTestCases {

        public static void test() {
            //testEmptyArray();
            testEvenArray();
            testOddArray();
            findEdgesOnOddArray();
            findEdgesOnEvenArray();
            notFoundAboveAndBelow();
            notFoundMiddle();
            arrayLimitValues();
            findArrayRepeatedValues();
            findInLargeArray();
        }
        private static void testEmptyArray() {
            long[] a = {};
            long[] b = {1, 3};

            for(int i = 0; i < b.length; i++) {
                System.out.println(String.format("Found %d at %d.", b[i], BinarySearchService.search(b[i], a, 0, 0)));
            }
        }

        private static void testEvenArray() {
            long[] a = {1, 2, 3, 4};
            long[] b = {1, 3};

            for(int i = 0; i < b.length; i++) {
                System.out.println(String.format("Found %d at %d.", b[i], BinarySearchService.search(b[i], a, 0, a.length - 1)));
            }
        }

        private static void testOddArray() {
            long[] a = {1, 2, 3, 4, 5};
            long[] b = {1, 3};

            for(int i = 0; i < b.length; i++) {
                System.out.println(String.format("Found %d at %d.", b[i], BinarySearchService.search(b[i], a, 0, a.length - 1)));
            }
        }

        private static void findEdgesOnOddArray() {
            long[] a = {1, 2, 3, 4, 5};
            long[] b = {1, 5};

            for(int i = 0; i < b.length; i++) {
                System.out.println(String.format("Found %d at %d.", b[i], BinarySearchService.search(b[i], a, 0, a.length - 1)));
            }
        }

        private static void findEdgesOnEvenArray() {
            long[] a = {1, 2, 3, 4};
            long[] b = {1, 4};

            for(int i = 0; i < b.length; i++) {
                System.out.println(String.format("Found %d at %d.", b[i], BinarySearchService.search(b[i], a, 0, a.length - 1)));
            }
        }

        private static void notFoundAboveAndBelow() {
            long[] a = {1, 2, 3, 4};
            long[] b = {-10, 10};

            for(int i = 0; i < b.length; i++) {
                System.out.println(String.format("Found %d at %d.", b[i], BinarySearchService.search(b[i], a, 0, a.length - 1)));
            }
        }

        private static void notFoundMiddle() {
            long[] a = {1, 2, 5, 6};
            long[] b = {4};

            for(int i = 0; i < b.length; i++) {
                System.out.println(String.format("Found %d at %d.", b[i], BinarySearchService.search(b[i], a, 0, a.length - 1)));
            }
        }

        private static void arrayLimitValues() {
            System.out.println(">arrayLimitValues>>>>>>>>>>>>>>>>>>>>>");
            long[] a = {1, 2, 5, (long) Math.pow(10, 9)};
            long[] b = {3,4,6,7, (long) Math.pow(10, 9),999999};

            for(int i = 0; i < b.length; i++) {
                System.out.println(String.format("Found %d at %d.", b[i], BinarySearchService.search(b[i], a, 0, a.length - 1)));
            }
        }

        private static void findArrayRepeatedValues() {

            System.out.println(">findArrayRepeatedValues>>>>>>>>>>>>>>>>>>>>>");
            long[] a = {1, 1, 2, 3, 4, 5, 5};
            long[] b = {0, 3, 1, 6, 1, 3};

            for(int i = 0; i < b.length; i++) {
                System.out.println(String.format("Found %d at %d.", b[i], BinarySearchService.search(b[i], a, 0, a.length - 1)));
            }
        }

        private static void findInLargeArray() {
            final int n = (int) Math.pow(10, 4);
            final long[] a = new long[n];
            for(int i = 0; i < n;i++) {
                a[i] = (long) (Math.pow(10, 9) * Math.random());
            }
            Arrays.sort(a);
            final long[] b = {a[2] , a[10*10*10], 16, a[10*10*10*10 - 1],a[0]};
            for(int i = 0; i < b.length; i++) {
                System.out.println(String.format("Found %d at %d.", b[i], BinarySearchService.search(b[i], a, 0, a.length - 1)));
            }
        }
    }

    public static void main(String[] args) {
        
        boolean testMode = false;

        if(true == testMode) {
            BinarySearchTestCases.test();
        } else{
            final FastScanner scanner = new FastScanner(System.in);
        
            final int n = scanner.nextInt();
            final long[] a = new long[n];

            for (int i = 0; i < n; i++) {
                a[i] = scanner.nextLong();
            }

            final int m = scanner.nextInt();
            for (int i = 0; i < m; i++) {
                System.out.print(
                    "" + BinarySearchService.search(scanner.nextLong(), a, 0, n - 1) + " "
                );
            }
        }
    }
}