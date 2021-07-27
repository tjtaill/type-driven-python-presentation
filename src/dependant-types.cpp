#include <iostream>
#include <array>

int main(int, char**) {
    std::array<int, 3> nums = {1, 2, 3}; // c++ 11 and later
    std::cout << std::get<4>(nums) << std::endl; // fails to compile
    return 0;
}