/*
ID: carvaja1
PROG: ride
LANG: C++11
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
  ofstream fout ("ride.out");
  ifstream fin ("ride.in");
  
  string comet, group;
  fin >> comet >> group;
  
  int cometC = 1, groupC =1;
  
  for(char& c : comet){
    cometC *= ((int)c) - 64;
  }

  for(char& c : group){
    groupC *= ((int)c) - 64;
  }
  
  if(cometC %47 == groupC % 47)
    fout << "GO" << endl;
  else
    fout << "STAY" << endl;
  
  return 0;
}
