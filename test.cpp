#include <iostream>
using namespace std;

    int red = 5;
    int blu = 5;
    int yel = 5;
    int res[20]={0};
    int count = 0;
    int total_count = 0;

void calc() {
    if (count==15) {
        total_count++;
        return;
    }
        if (red>0 && res[count-1]!=1) {
            res[count++] = 1;
            red--;
            calc();
            red++;
            count--;
        }
        if (blu>0 && res[count-1]!=2) {
            res[count++] = 2;
            blu--;
            calc();
            blu++;
            count--;
        }
        if (yel>0 && res[count-1]!=3) {
            res[count++] = 3;
            yel--;
            calc();
            yel++;
            count--;
        }
        return;
    }

int main() {
    count = 1;
    res[0] = 1; red--;
    calc();

    count = 1;
    res[0] = 2; blu--;
    calc();

    count = 1;
    res[0] = 3; yel--;
    calc();
    
    cout<<"Total : "<<total_count;
}