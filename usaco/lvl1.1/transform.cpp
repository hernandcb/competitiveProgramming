/*
ID: carvaja1
PROG: transform
LANG: C++11
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

vector<string> rotate90(vector<string> square){
  int n = square.size();
  vector<string> result(square);
  for(int i=0; i<n; i++){
    for(int j=0; j<n; j++)
      result[i][j] = square[n-j-1][i];
  }
  return result;
}

vector<string> reflect(vector<string> square){
  int n = square.size();
  vector<string> result(square);
  for(int i=0; i<n; i++){
    for(int j=0; j<n; j++)
      result[i][j] = square[i][n-j-1];
  }
  return result;
}


int main(){
  ifstream fin("transform.in");
  ofstream fout("transform.out");
  int n, transformation;

  fin >> n;
  string tmp;
  vector<string> squareA, squareB, t1, t2, t3, r, rt1, rt2;
  for(int i=0; i<n; i++){
    fin >> tmp;
    squareA.push_back(tmp);
  }
  for(int i=0; i<n; i++){
    fin >> tmp;
    squareB.push_back(tmp);
  }
  
  
  t1 = rotate90(squareA);
  t2 = rotate90(t1);
  t3 = rotate90(t2);
  r  = reflect(squareA);
  if(squareB == t1) transformation = 1;
  else if(squareB == t2) transformation = 2;
  else if(squareB == t3) transformation = 3;
  else if(squareB == r)  transformation = 4;
  else if(squareB == (rt1=rotate90(r)) || squareB == (rt2=rotate90(rt1)) || squareB == rotate90(rt2)) transformation = 5;
  else if(squareA == squareB) transformation = 6;
  else transformation = 7;
  
  fout << transformation<<endl;
  
  return 0;
}
