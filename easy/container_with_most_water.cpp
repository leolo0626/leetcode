#include <vector>
#include <algorithm>

using namespace std;
// https://leetcode.com/problems/container-with-most-water/editorial/
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0 ;
        int right = height.size() - 1 ;
        int result = 0 ;
        while (left < right) {
            int distance =  right - left;
            if (height[left] <= height[right]) {
                result = max(result, height[left] * distance);
                left ++ ;
            } else {
                result = max(result, height[right] * distance);
                right -- ;
            }
        }
        return result;
    }
};