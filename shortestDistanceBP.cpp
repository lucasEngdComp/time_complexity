#include <bits/stdc++.h>


using namespace std;

int sum(vector<int>& a,int mid){
    vector<int>::iterator it;
    int s = 0;
    for(*it = mid - 1; *it < mid+1; it++){
        s +=*it;
    }

    return s;

}

/**
 * @brief 
 * 
 * @param v1 vector number 1 
 * @param v2 vector number 2
 * @param size size of vector
 * @return int return the median of array
 */                                 
int calcMed(vector<int>& v1, vector<int>& v2, int size, int mid){

    int valuemidV1;
    int valuemidV2;
    vector<int> vectorAux;
    size = v1.size();
    if(size == 1){
        return (v1[0] + v2[0]) / 2;
    }
    else{
        mid = size / 2;
        if( size %2 != 0){
            valuemidV1 = v1[mid]; // middle v1
        }else{
            sum(v1,mid);
        }
        if(size % 2 != 0){
            valuemidV2 = v2[mid]; // middle v2
        }else{
            sum(v2,mid);
        }
        if(valuemidV1 == valuemidV2){
            return valuemidV1;
        }
        else{
            if(size  % 2 != 0){
                for(size_t i = mid + 1; i < v1.size(); i++){
                    vectorAux.push_back(v1[i]);   
                }
            }
            
        }
        
        

    }

}
/*
 * @brief 
 * 
 * Function for generate random values to vector 

*/
 vector<int> vrandom(vector<int>& v1, int tam){

    for(int i = 0; i < tam; i++){
        v1.push_back(rand() % 100);
    }

    return v1;

}

int main(){

    vector<int> v1 ={};
    vector<int> v2 ={1,2,3,4,5};

    v1 = vrandom(v1,6);

    for(int i = 0; i<v1.size(); i++){
        cout << v1[i] << " ";
    }

    int mid = v2.size() / 2;
    int soma = sum(v1,mid);
    cout << soma << endl;

    return 0;
}