/*
ID: carvaja1
PROG: beads
LANG: C++11
*/

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

int mod(int a, int b){
  if(b < 0) //you can check for b == 0 separately and do what you want
     return mod(a, -b);
   int ret = a % b;
   if(ret < 0)
     ret+=b;
   return ret;
}

int main(){
  ifstream fin ("beads.in");
  ofstream fout ("beads.out");
  string beads;
  int n, count, max=0;
  char cr, cl;
  
  fin >> n >> beads;

  for(int i=0; i<n; i++){
    count = 0;
    cl = beads[mod(i-1,n)];
    cr = beads[mod(i,n)];
    for(int j=i-1, k=1; cl == 'w' and k <n; j--, k++) cl = beads[mod(j,n)];
    for(int j=i, k=1; cr == 'w' and k <n; j++, k++) cr = beads[mod(j,n)];

    for(int j=i-1; (beads[mod(j,n)]==cl or beads[mod(j,n)] == 'w') and count<n; j--) count++;

    if(count < n)
      for(int j=i; (beads[mod(j,n)]==cr or beads[mod(j,n)] == 'w') and count<n; j++) count++;

    max = (count > max) ? count : max;
    if (max == n) break;
  }
  
  fout << max << endl;
  return 0;
}
