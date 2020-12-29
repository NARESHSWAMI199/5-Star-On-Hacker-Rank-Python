#include <iostream>
using namespace std;



int *sort(int arr[],int size){
    int value =0;
    for (int i=0; i<size; i++){
        for (int j=i+1; j<size; j++){
            if (arr[i] > arr[j]){
                value = arr[i];
                arr[i] = arr[j];
                arr[j] = value;
            }
        }
    }
    
    return arr;
}
void max_migratory(int arr[],int size){
    int ans_size = 0;
    int answer[ans_size];
    int max = 0;
    int index = 0;
    for (int i=0; i<size; i++){
        int count = 0;
        for (int j=i; j<size; j++){
            if (arr[i] == arr[j]){
                count ++;
                i = j;
            }        
        }
        int count_arr[index];
        count_arr[index] = count;

        for (int k = 1; k<index; k++){
            if (count_arr[index]  > count_arr[k]){
                max = count_arr[index];
            }
        }
        if (count_arr[index]== max){
            answer[ans_size] = arr[i];
            ans_size ++;
        }
        index ++;
    } 
    for (int i = 0; i<ans_size; i++){
         for (int j = 0; j<ans_size; j++){
             if (answer[i] < answer[j]){
                 cout<<answer[i];
             }else{
                 cout<<answer[0];
             }
         }
    }

}
int main(){
    int size;
    cin >> size;
    int arr[size];
    for (int i = 0; i < size; i++){
        int value;
        cin >> value;
        arr[i] = value;
    }
    int *sorted_arr = sort(arr,size);
    max_migratory(sorted_arr,size);
    return 0;
}