/*
ID: carvaja1
PROG: milk2
LANG: C++11
*/
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <utility>
using namespace std;

int main(){
  ifstream fin("milk2.in");
  ofstream fout("milk2.out");
  
  vector<pair<int, int>> times;
  int n, a, b, tmp, work=0, gap=0;
  bool chained=false;
  
  fin >> n;
  for(int i=0; i<n; i++){
    fin >> a >> b;
    if(b>a){
      tmp=b; b=a; b=tmp;
    } 
    times.push_back(make_pair(a,b));
  }
  sort(times.begin(), times.end());
  
  for(int j=0; j<times.size(); j++){
    if(j>0){
      gap = (times[j].first-times[j-1].second>gap)? times[j].first-times[j-1].second : gap;
      if(times[j].first <= times[j-1].second)
        times[j].first = times[j-1].first;
      
      if(times[j].second < times[j-1].second)
        times[j].second = times[j-1].second;
    }
    
    work = (times[j].second-times[j].first > work) ? times[j].second-times[j].first : work;
  }
  
  fout << work << " " << gap << endl;
  
  
  return 0;
}
