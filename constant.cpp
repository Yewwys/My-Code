#include <iostream>
#include <cmath>
using namespace std;

int main() {
    //หาPv=nrt
    const float R = 0.082;
    int v = 10;
    int n = 2;
    int t = 15;
    cout << "Finding P value= "<< (n*R*t) / v<<endl;
    cout << "Thank you !!";
}