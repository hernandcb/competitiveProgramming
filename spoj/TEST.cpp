#include <iostream>

int main()
{
  int n=0;
  
  std::cin >> n;
  while(n != 42)
  {
    std::cout << n << std::endl;
    std::cin >> n;
  }
  
  return 0;
}
