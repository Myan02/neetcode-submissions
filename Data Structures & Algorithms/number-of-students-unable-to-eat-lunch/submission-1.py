class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_dict = Counter(students)

        for i in range(len(sandwiches)):
            if student_dict[sandwiches[i]] > 0:
                student_dict[sandwiches[i]] -= 1
            else:
                return len(sandwiches) - i
        
        return 0
