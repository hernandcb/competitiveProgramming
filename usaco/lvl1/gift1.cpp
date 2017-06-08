/*
ID: carvaja1
PROG: gift1
LANG: C++11
*/

#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main(){
  ifstream fin("gift1.in");
  ofstream fout("gift1.out");

  map<string, int> friends;
  string name;
  int np, amount, money, receivers;
  fin >> np;

  string names[np];

  for(int i=0; i<np; i++){
    fin >> name;
    names[i] = name;
    friends[name] = 0;
  }

  for(int i=0; i<np; i++){
    fin >> name;
    fin >> money >> receivers;
    
    friends[name] -= money;
    if(receivers >0){
      amount = (int) money / receivers;
      friends[name] += money % receivers;
    }
    else
      amount = 0;
    for(int j=0; j< receivers; j++){
      fin >> name;
      friends[name] += amount;
    }
  }

  for(auto const & name : names){
    fout << name << " " << friends[name] << endl;
  }
  
  return 0;
}
