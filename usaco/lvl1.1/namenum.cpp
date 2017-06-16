/*
ID: carvaja1
PROG: namenum
LANG: C++11
*/

#include<iostream>
#include<fstream>
#include<string>

using namespace std;

string dial[] = {"ABC", "DEF", "GHI", "JKL", "MNO", "PRS", "TUV", "WXY"};
string tmp ="";

int isValidWord(ifstream& dict, string word){
  if(tmp.size()==0) dict>>tmp;
  while(tmp.compare(word) <0 && !dict.eof())dict >> tmp;

  return word.compare(tmp);
}

int main(){
  ifstream fin("namenum.in");
  ofstream fout("namenum.out");
  ifstream dict("dict.txt");
  
  string number, tmp;
  fin >> number;
  dict >> tmp;
  
  int n = number.size();
  string word (n, 'a'); // Create a string with n 'a's
  int indices[n] = {};
  int num =0, valid=0;

  for(int i=0; i<n; i++){
    num = number[i]-'0'-2;
    word[i] = dial[num][0];
  }
  int j=n-1;
  
  while(j>=0){
    indices[j] = (indices[j]+1)%3;
    
    if(indices[j] == 0){
      j--;
    } else {
      for(int i=n-1; i>=0; i--)
        word[i] = dial[number[i]-'0'-2][indices[i]];
      
      if(isValidWord(dict, word)==0){
        fout << word << endl;
        valid++;
      } 
      j=n-1;
    }
  }
  
  if(valid ==0) fout << "NONE" << endl;
  
  return 0;
}


