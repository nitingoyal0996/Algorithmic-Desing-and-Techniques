#include<iostream>
using namespace std;


//function to add two numbers
int sum(int a, int b){
    return a  + b;
}

//main function
int main(){
    int a, b;
    cin >> a >> b;
    cout << sum(a,b)<< endl;
}
