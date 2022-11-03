#include <bits/stdc++.h>
using namespace std;

vector<vector<int> > performOps(vector<vector<int> > &A) {
    vector<vector<int> > B;
    B.resize(A.size());
    for (int i = 0; i < A.size(); i++) {
        B[i].resize(A[i].size());
        for (int j = 0; j < A[i].size(); j++) {
            B[i][A[i].size() - 1 - j] = A[i][j];
        }
    }
    return B;
}


vector<int> partition(vector<int> &A,int p,int r) {
    int mid = (A.size()/2) - 1;
    int mid2 = (A.size()/2) + 1;
    
    vector<int> aux;
    aux.push_back(mid);
    aux.push_back(mid2);
    return aux;
}

int part(int *arr, int p, int r){
    int x = arr[r]; // choice my pivot; the best choice?
    int i = p - 1; // left side, maybe.
    for(int j = p; j < r - 1; j++) {
        if(arr[j] <= x){
            i = i + 1;
            swap(arr[i],arr[j]);
        }
    }
    swap(arr[i+1],arr[r]);
    return i + 1;

}

int quicksort(int *arr,int p, int r){
    if(p < r){
        int q = part(arr,p,r);
        quicksort(arr,p,q-1);
        quicksort(arr, q+1,r);
    }    
}

int main(){

	/*vector<vector<int>> A = {
		{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}
		
	};
	vector<vector<int> > B = performOps(A);

	for (int i = 0; i < B.size(); i++) {
		for (int j = 0; j < B[i].size(); j++) 
			cout<<B[i][j]<<" ";
	}
    */


   /*  vector<int> vet = {1,2,3,4,5};
    vector<int> res = partition(vet);

    for(int i = 0; i < res.size(); i++){
        cout<< res[i]<<endl;
    }
 */
    int arr[] = {10,2,30,20,60,14,22};
    int n = sizeof(arr)/sizeof(arr[0]);
    quicksort(arr,0,n);

    for(int i = 0; i < n; i++){
        cout << arr[i] << endl;
    }
    
    return 0;
}
