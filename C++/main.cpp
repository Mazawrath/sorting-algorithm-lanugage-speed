#include <fstream>
#include <iostream>
#include <chrono>

void swap(int *xp, int *yp) {
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

// A function to implement bubble sort
long sortArray(std::string fileName, int n) {
    std::ifstream file;
    file.open(fileName);

    int arr[15000];
    int itt = 0;
    std::string line;
    while (std::getline(file, line)) {
        arr[itt++] = std::stoi(line);
    }

    int i, j;
    using namespace std::chrono;
    milliseconds start = duration_cast<milliseconds>(
            system_clock::now().time_since_epoch()
    );
    for (i = 0; i < n - 1; i++)

        // Last i elements are already in place
        for (j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1])
                swap(&arr[j], &arr[j + 1]);
    milliseconds finish = duration_cast<milliseconds>(
            system_clock::now().time_since_epoch()
    );
    return finish.count() - start.count();
}

int main() {
    // Array of 100 because there are 102 files to sort
    long timings[102];

    // Randomly sorted
    for (int i = 1; i <= 100; i++) {
        std::string fileName = (R"(..\Test files\Random\f)" + std::to_string(i) + ".txt");

        long timeElapsed = sortArray(fileName, 15000);
        timings[i - 1] = timeElapsed;
        std::cout << timeElapsed << "\n";
    }

    // Best case
    std::string bestFileName = (R"(..\Test files\Best\best.txt)");

    long bestTimeElapsed = sortArray(bestFileName, 15000);
    timings[100] = bestTimeElapsed;
    std::cout << bestTimeElapsed << "\n";

    // Worst case
    std::string worstFileName = (R"(..\Test files\Best\worst.txt)");

    long worstTimeElapsed = sortArray(worstFileName, 15000);
    timings[101] = worstTimeElapsed;
    std::cout << worstTimeElapsed << "\n";
    return 0;

}
