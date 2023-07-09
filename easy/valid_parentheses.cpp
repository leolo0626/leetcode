class Solution {
public:
    bool isValid(string s) {
        stack<char> p_stack;
        for (char c: s ) {
            if ( c == ')' || c == ']' || c== '}') {
                if (!p_stack.empty()) {
                    if (c == ')' && p_stack.top() != '(') {
                        return false;
                    } else if  (c == ']' && p_stack.top() != '[')  {
                        return false;
                    } else if (c == '}' && p_stack.top() != '{')  {
                        return false;
                    }
                    p_stack.pop();
                } else { 
                    return false;
                }
            } else {
                p_stack.push(c);
            }
        }
        if (p_stack.size()) {
            return false;
        }

        return true;
    }
};