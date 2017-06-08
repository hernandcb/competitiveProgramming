/*
ID: carvaja1
PROG: friday
LANG: C++11
*/

#include <iostream>
#include <fstream>

using namespace std;

int main(){
  ifstream fin ("friday.in");
  ofstream fout ("friday.out");
  
  int counts[7] ={};
  int years, year, month, day, weekday;
  fin >> years;
  
  weekday=2;
  for(int year=1900; year<1900+years; year++){
    month = 1; day=1;
    for(int j=1; j<=365; j++){
      if(day == 13)
        counts[weekday]++;
      
      
      if(month == 2){
        int d = (year%100 == 0)?400 : 4; // Is a century ?
        if( year%d == 0 and day == 29){ // Is leap year
          day = 1; month++;
          --j;
        } else if (year%d != 0 and day == 28){
          day = 1; month++;
        } else{
          day ++;
        }
      } else if (day == 30 and (month==4 or month==6 or month==9 or month == 11)){
        day = 1; month++;
      } else if (day == 31) {
        day = 1; month++;
      }else{
        day++;
      }
      weekday = (weekday+1)%7;
    }
  }
  
  for(int i=0; i<7; i++){
    if(i==0)
      fout << counts[i];
    else
      fout << " " << counts[i];
  }
  fout << endl;
  
  return 0;
}
