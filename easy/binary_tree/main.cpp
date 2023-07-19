#include "tree.cpp"
#include <iostream>

// g++ -std=c++11 -o add_two_numbers main.cpp

int main() {
    TreeNode* tree = new TreeNode(0, new TreeNode(1, new TreeNode(3), nullptr), new TreeNode(2));

    std::cout << "tree size : " << tree->getHeight() << std::endl;


    return 0;
}