from CSP.Solver import Solver
from States.StatesProblem import StatesProblem

if __name__ == '__main__':

    states = StatesProblem()
    s = Solver(states)
    s.solve()
    states.print_assignments()
