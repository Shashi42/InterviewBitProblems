#############REDUNDANT BRACES################
class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        i=0
        res=0
        while(i<len(A)):
            if(A[i]=='('):
                openBraces='('
                i=i+1
                while(A[i]=='('):
                    i=i+1
                    openBraces=openBraces+'('
                if(len(openBraces)!=1):
                    closedBraces=''
                    for j in range(0,len(openBraces)):
                        closedBraces=closedBraces+')'
                    val=A.find(closedBraces)
                    temp=A[i:val]
                    B=A[i:]
                    if(B.find(closedBraces)!=-1 & temp.find(')')==-1):
                        res=1
                else:
                    temp=A[i:]
                    index=temp.find(')')
                    if(index<2):
                        res=1
            i=i+1
        return res
#######################################
# testcase = "((a+b))"
# print(Solution.redundantbraces(testcase))
