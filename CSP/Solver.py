import time
from collections import deque
from typing import Optional

from CSP.Problem import Problem
from CSP.Variable import Variable


class Solver:

    def __init__(self, problem: Problem):
        """
        Initializes the Solver object with the given problem instance and optional parameters.

        Args:
            problem (Problem): The problem instance to be solved.
        """
        self.problem = problem
        self.back_up = deque()

    def is_finished(self) -> bool:
        """
        Determines if the problem has been solved.

        Returns:
            bool: True if the problem has been solved, False otherwise.
        """
        return all([x.is_satisfied() for x in self.problem.constraints]) and len(
            self.problem.get_unassigned_variables()) == 0

    def solve(self):
        """
        Solves the problem instance using the backtracking algorithm with optional heuristics.
        """
        start = time.time()
        result = self.backtracking()
        end = time.time()
        time_elapsed = (end - start) * 1000
        if result:
            print(f'Solved after {time_elapsed} ms')
        else:
            print(f'Failed to solve after {time_elapsed} ms')

    def backtracking(self) -> bool:
        """
        Implements the backtracking algorithm.

        Returns:
            bool: True if the problem has been solved, False otherwise.
        """
        if self.is_finished():
            return True
        var = self.problem.get_unassigned_variables()[0]
        for value in var.domain:
            var.value = value
            if self.is_consistent(var): 
                result = self.backtracking()
                if result:
                    return True
            var.value = None
        return False
    
    def is_consistent(self, var: Variable) -> bool:
        """
        Determines if the given variable is consistent with all constraints.

        Args:
            var (Variable): The variable to be checked for consistency.

        Returns:
            bool: True if the variable is consistent with all constraints, False otherwise.
        """
        return all(constraint.is_satisfied() for constraint in self.problem.constraints if var in constraint.variables)

    def forward_check(self, var: Variable) -> bool:
        """
        Implements the Forward Checking algorithm.

        """
        pass

    def mrv(self) -> Optional[Variable]:
        """
        Implements the Minimum Remaining Values heuristic.

        Returns:
            Optional[Variable]: The variable with the smallest domain or None if all variables have been assigned.
        """
        pass    


    def lcv(self, var: Variable):
        """
        Implements the Least Constraining Values heuristic.

        Args:
            var (Variable): The variable whose domain values are to be ordered.

        Returns:
            List: The domain values of the variable ordered according to the number of conflicts they cause.
        """
        pass
    
    def save_domain(self, vars: list[Variable]):
        self.back_up.append([var.domain.copy() for var in vars])
    
    def load_domain(self, problem: Problem):
        domains = self.back_up.pop()
        for i in range(len(problem.variables)):
            problem.variables[i].domain = domains[i]
