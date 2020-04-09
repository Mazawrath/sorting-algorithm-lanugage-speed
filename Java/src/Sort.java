import java.io.*;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Sort {

    public static void main(String[] args) throws IOException {
        // Array of 100 because there are 102 files to sort
        long[] timings = new long[102];

        // Randomly sorted
        for (int i = 1; i <= 100; i++) {
            File file = new File(System.getProperty("user.dir") + "\\Test files\\Random\\f" + i + ".txt");
            long timeElapsed = sortArray(file);
            timings[i - 1] = timeElapsed;
            System.out.println("Time spent sorting " + i + ".txt: " + timeElapsed);
        }

        // Best case
        File bestFile = new File(System.getProperty("user.dir") + "\\Test files\\Best\\best.txt");
        long bestTimeElapsed = sortArray(bestFile);
        timings[100] = bestTimeElapsed;
        System.out.println("Time spent sorting best.txt: " + bestTimeElapsed);

        // Worst case
        File worstFile = new File(System.getProperty("user.dir") + "\\Test files\\Worst\\worst.txt");
        long worstTimeElapsed = sortArray(worstFile);
        timings[101] = worstTimeElapsed;
        System.out.println("Time spent sorting worst.txt: " + worstTimeElapsed);

        // Write the results to a file
        DateFormat dateFormat = new SimpleDateFormat("MM-dd-yyyy HH-mm-ss");
        Date date = new Date();
        File output = new File(System.getProperty("user.dir") + "\\results\\" + dateFormat.format(date) + ".txt");
        output.createNewFile();
        BufferedWriter results = new BufferedWriter(new FileWriter(output));

        for (long timing : timings) {
            results.write(timing + "\n");
        }
        results.close();
    }

    private static long sortArray(File file) throws IOException {
        BufferedReader br = new BufferedReader(new FileReader(file));
        int[] nums = new int[15000];

        // Read the input of the file
        int itt = 0;
        String st;
        while ((st = br.readLine()) != null) {
            nums[itt] = Integer.parseInt(st);
            itt++;
        }

        // Sort algorithm via bubble sort and time it
        long start = System.currentTimeMillis();
        int n = nums.length;
        for (int j = 0; j < n-1; j++)
            for (int k = 0; k < n-j-1; k++)
                if (nums[k] > nums[k+1])
                {
                    // swap arr[j+1] and arr[i]
                    int temp = nums[k];
                    nums[k] = nums[k+1];
                    nums[k+1] = temp;
                }
        long finish = System.currentTimeMillis();

        return finish - start;
    }
}
