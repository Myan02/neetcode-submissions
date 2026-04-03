class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # create an empty hashmap that maps each course to an empty array
        preMap = {i: [] for i in range(numCourses)}

        # populate the courses with their prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()

        def dfs(crs):
            # cycle exists
            if crs in visiting:
                return False
            
            # course has not prereqs
            if preMap[crs] == []:
                return True
            
            visiting.add(crs)

            # for each prereq, run dfs
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        