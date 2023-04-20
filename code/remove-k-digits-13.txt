/*
    time: O(n)       
    space: O(n)
        O(n) for the stack, O(n) for the list
*/

public class Solution {
    public string RemoveKdigits(string num, int k) {
        
        Stack<char> stack = new Stack<char>();
        
        // O(n + k)
        foreach(char c in num)
        {
            while(stack.Count > 0 && stack.Peek() > c && k > 0)
            {
                stack.Pop();
                k--;
            }
            stack.Push(c);
        }
        
        // handle cases where digits are in non-descending order (12345, 11111)
        while(k > 0)
        {
            stack.Pop();
            k--;
        }
        
        List<char> res = new List<char>();
        while(stack.Count > 0)
        {
            res.Add(stack.Pop());
        }
        
        // handle cases where there are leading zeros after removing digits 
        // num = "98002", k =2. result string should be "2" instead of "002"
        // num = "98002" -> res = "200", so we need to removing ending zeros before reversing.
        int idx = res.Count - 1;
        while(idx >= 0)
        {
            if(res[idx] == '0')
            {
                res.RemoveAt(idx);
                idx--;
            }
            else
                break;
        }
        
        // if all digits are removed, return "0"
        if(res.Count == 0)
            return "0";
        
        char[] arr = res.ToArray();
        Array.Reverse(arr);       
        return new string(arr);
    }
}