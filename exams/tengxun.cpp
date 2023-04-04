#include <iostream>
#include <stdio.h>
#include <unordered_map>
using namespace std;

#define MAX 1000001
int A[MAX];     //存储数据
int Q[MAX];    //队列
int P[MAX];    //存储A[i]中的下标i
int Min[MAX];  //输出最小
int Max[MAX];  //输出最大
int n,k;

void get_min()
{
    int i;
    int head=1,tail=0;
    for(i=0; i<k-1; i++)                       //先把前两个入队
    {
        while(head<=tail && Q[tail]>=A[i])      //队尾元素大于要插入的数
            --tail;
        Q[++tail]=A[i];
        P[tail]=i;
    }

    for(; i<n; i++)
    {
        while(head<=tail && Q[tail]>=A[i])
            --tail;
        Q[++tail]=A[i];
        P[tail]=i;
        while(P[head]<i-k+1)                            //判断数是否过时，即窗口是否已经划过这个数，我这是从0开始计数的。
        {
            head++;
        }
        Min[i-k+1]=Q[head];
    }
}


void get_max()
{
    int i;
    int head=1,tail=0;
    for(i=0; i<k-1; i++)
    {
        while(head<=tail && Q[tail]<=A[i])   //队尾元素小于要插入的值
            --tail;
        Q[++tail]=A[i];
        P[tail]=i;
    }

    for(; i<n; i++)
    {
        while(head<=tail && Q[tail]<=A[i])   //队尾元素小于要插入的值
            --tail;
        Q[++tail]=A[i];
        P[tail]=i;
        while(P[head]<i-k+1)
            {
            head++;
        }
        Max[i-k+1]=Q[head];
    }
}
 
int main()
{
    int i;
    int coun;
    cin >> n >> k;
    coun=0;
    for(i=0; i<n; i++)
        scanf("%d",&A[i]);
    get_min();
    get_max();
    unordered_map<int, int> map;
    for(int i=0;i<k-1;i++){
        if(map.count(A[i])){
            map[A[i]] ++;
        }else{
            map[A[i]] = 1;
        }
    }
    for(int i=0;i<n-k+1;i++){
        if(map.count(A[i+k-1])){
            map[A[i+k-1]] ++;
        }else{
            map[A[i+k-1]] = 1;
        }
        if(i>0){
            map[A[i-1]] --;
            if(map[A[i-1]] == 0){
                map.erase(A[i-1]);
            }
        }

        if((Max[i]-Min[i])==(k-1) && map.size() == k)
            coun++;
        
    }
    printf("%d\n",coun);
    return 0;
}