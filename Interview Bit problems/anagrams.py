############# ANAGRAMS ################
class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(A):
        # A is a tuple of strings
        ana_groups = {}
        #Iterating through every string in given tuple
        for anapos,ana in enumerate(A,start=1):
            #making a list of characters of string and sorting it to make a base structure
            ana_base_struct = list(ana)
            ana_base_struct.sort()
            ana_base_struct = str(list(ana_base_struct)) 
            #check if the base structure is present as key in groups dictionary
            if ana_base_struct in ana_groups:
                #if present then add index of the string to the common base structure
                ana_groups[ana_base_struct].append(anapos)
            #add new key value pair of new group to anagrams groups dictionary
            else:
                ana_groups[ana_base_struct] = [anapos]
        return(list(ana_groups.values()))

#######################################
# testcase = ("abbbaabbbabbbbabababbbbbbbaabaaabbaaababbabbabbaababbbaaabbabaabbaabbabbbbbababbbababbbbaabababba", "abaaabbbabaaabbbbabaabbabaaaababbbbabbbaaaabaababbbbaaaabbbaaaabaabbaaabbaabaaabbabbaaaababbabbaa", "babbabbaaabbbbabaaaabaabaabbbabaabaaabbbbbbabbabababbbabaabaabbaabaabaabbaabbbabaabbbabaaaabbbbab", "bbbabaaabaaaaabaabaaaaaaabbabaaaabbababbabbabbaabbabaaabaabbbabbaabaabaabaaaabbabbabaaababbaababb", "abbbbbbbbbbbbabaabbbbabababaabaabbbababbabbabaaaabaabbabbaaabbaaaabbaabbbbbaaaabaaaaababababaabab", "aabbbbaaabbaabbbbabbbbbaabbababbbbababbbabaabbbbbbababaaaabbbabaabbbbabbbababbbaaabbabaaaabaaaaba", "abbaaababbbabbbbabababbbababbbaaaaabbbbbbaaaabbaaabbbbbbabbabbabbaabbbbaabaabbababbbaabbbaababbaa", "aabaaabaaaaaabbbbaabbabaaaabbaababaaabbabbaaaaababaaabaabbbabbababaabababbaabaababbaabbabbbaaabbb")
# print(Solution.anagrams(testcase))
