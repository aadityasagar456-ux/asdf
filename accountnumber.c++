#include <iostream>
using namespace std;

class account {
    public :
    int accountnumber ;
    float balance ;
        
    };
int main() {
    account a;
    a.accountnumber = 122540;
    a.balance = 10000;
    cout<<"account number:"<<a.accountnumber<<endl;
    cout<<"balance:"<<a.balance;
    return 0;
}