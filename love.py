#include <iostream>
#include <cmath>
#include <thread>
#include <chrono>

using namespace std;

int main() {
    const string red = "\033[31m"; // Red color
    const string reset = "\033[0m"; // Reset color

    for (int y = 15; y > -15; y--) {
        for (int x = -30; x < 30; x++) {
            float x_scaled = x * 0.05;
            float y_scaled = y * 0.1;
            float a = x_scaled * x_scaled + y_scaled * y_scaled - 1;
            float condition = a * a * a - x_scaled * x_scaled * y_scaled * y_scaled * y_scaled;

            if (condition <= 0.0) {
                cout << red << "*" << reset;
            } else {
                cout << " ";
            }
        }
        cout << endl;
        this_thread::sleep_for(chrono::milliseconds(50)); // Slow reveal effect
    }

    this_thread::sleep_for(chrono::milliseconds(500));
    cout << red << "\n" << string(30 - 7, ' ') << "i love you <3\n" << reset;

    return 0;
}
