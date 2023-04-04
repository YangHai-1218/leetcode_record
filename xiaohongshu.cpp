#include <iostream> 
#include <vector> 
using namespace std;

void op_1(vector<int>& nums, int l, int r, int x) { 
    for (int i = l-1; i < r; i++){
        nums[i] = nums[i] | x; 
    } 
}
void op_2(vector<int>& nums, int l, int r, int x) {
    for (int i = l-1; i < r; i++) {
        nums[i] = nums[i] & x; 
    } 
}
void op_3(vector<int>& nums, int l, int r, int x) {
    for (int i = l-1; i < r; i++) { 
        nums[i] = x; 
    } 
}
int main() { 
    int len_input, op_nums; 
    cin >> len_input;
    vector<int> input_nums;
    for (int i = 0; i < len_input; i++) {
        int num;
        cin >> num;
        input_nums.push_back(num);
    }

    cin >> op_nums;

    vector<int> seq_l;
    vector<int> seq_r;
    vector<char> seq_op;
    vector<int> seq_x;

    for (int i = 0; i < op_nums; i++) {
        int l;
        cin >> l;
        seq_l.push_back(l);
    }
    for (int i = 0; i < op_nums; i++) {
        int r;
        cin >> r;
        seq_r.push_back(r);
    }
    for (int i = 0; i < op_nums; i++) {
        char op;
        cin >> op;
        seq_op.push_back(op);
    }

    for (int i = 0; i < op_nums; i++) {
        int x;
        cin >> x;
        seq_x.push_back(x);
    }

    for (int i = 0; i < op_nums; i++) {
        if (seq_op[i] == '|') {
            op_1(input_nums, seq_l[i], seq_r[i], seq_x[i]);
        }
        else if (seq_op[i] == '&') {
            op_2(input_nums, seq_l[i], seq_r[i], seq_x[i]);
        }
        else if (seq_op[i] == '=') {
            op_3(input_nums, seq_l[i], seq_r[i], seq_x[i]);
        }
    }

    string result = "";
    for (int n: input_nums) {
        result += " " + to_string(n);
    }

    cout << result.substr(1) << endl;

    return 0;
}