class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> u;
        for (int i = 0; i< nums.size() ; i++ ){ 
            int another = target - nums[i];
            if (auto search = u.find(another); search != u.end()) {

                return {i, search->second};
            } else {
                u.insert({nums[i], i});
            }
        }
        return {};
    }
};