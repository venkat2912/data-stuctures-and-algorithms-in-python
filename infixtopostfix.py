# User function Template for python3
class Solution:
    
    # Function to get the priority of operators
    def priority(self, s):
        if s == '^':
            return 3
        elif s in ('/', '*'):
            return 2
        elif s in ('+', '-'):
            return 1
        else: 
            return -1
            
    # Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, s):
        ans = ''
        st = []

        for c in s:
            # If the character is an operand, add it to the result
            if c.isalnum():
                ans += c
               
            elif c == '(':
                st.append(c)
                
            elif c == ')':
                while st and st[-1] != '(':
                    ans += st.pop()
                st.pop()  # Pop the '(' from stack
                
            else:
                while st and self.priority(c) <= self.priority(st[-1]) and c != '^':
                    ans += st.pop()
                st.append(c)

        # Pop all remaining elements from the stack
        while st:
            ans += st.pop()
        
        return ans    
