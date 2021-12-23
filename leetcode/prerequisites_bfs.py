from queue import LifoQueue, Queue
from typing import Dict, Set, List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        # numCourses courses from [0, numCourses-1]
        # prerequisites where [a, b]
        # graph problem
        
        # return ordering of courses to finish all courses
        # return any valid answer
        # return empty array if not possible
        
        # edge cases
        # num_courses == 0
        # prerequisites is empty, misshaped
        if numCourses == 0:
            return []
        if not prerequisites:
            return [_ for _ in range(numCourses)]
        
        # Space O(N + E + N + N + N) ~ O(N + E)
        # Time O(1 + 1 + E + N) ~ O(N + E)
        
        # connectivity of graph is defined in prerequisites
        # prerequisites is only pairs [a, b] connectivity is B -> A
        # path of length numCourses through graph
        course_path: List = []
        to_take: Queue = Queue()
        taken: Set = set()

        # Make from prerequisites
        connectivity: Dict = {}
        for course2, course1 in prerequisites:
            if connectivity.get(course2, None) is None:
                connectivity[course2] = [course1]
            else:
                connectivity[course2].append(course1)
            if (connectivity.get(course1, None) is not None) and \
                course2 in connectivity[course1]:
                # Cycle detected
                return []
                
        # Take any courses without pre-reqs
        for course in range(numCourses):
            to_take.put(course)
            if connectivity.get(course, None) is None:
                taken.add(course)
                course_path.append(course)


        # BFS
        while not to_take.empty():
            course = to_take.get()
            if (not course in taken) and \
               (connectivity.get(course, None) is not None) and \
               all(c in taken for c in connectivity[course]):
                taken.add(course)
                course_path.append(course)
                if len(course_path) > numCourses:
                    break
                if connectivity.get(course, None) is not None:
                    for _course in connectivity[course]:
                        to_take.put(_course)
            
        if len(course_path) < numCourses:
            return []
        else:
            return course_path
        
        
        
        
        
        
