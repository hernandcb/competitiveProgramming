//	Author: hernandcb
//	Date: 20/04/2016

#include <iostream>

int reverseNumber(int n)
{
  int reverse = 0;
  while(n != 0)
  {
    int remainder = n%10;
    reverse = reverse*10 + remainder;
    n /= 10;
  }
  return reverse;
}

int main(void)
{
  int n=0;
  std::cin >> n;
  
  for(int i = 0; i < n; i++){
    int a, b, result;
    std::cin >> a >> b;
    result = reverseNumber(reverseNumber(a) + reverseNumber(b));
    std::cout << result << std::endl;
  }
  return 0;
}

