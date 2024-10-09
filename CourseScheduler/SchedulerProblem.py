from CSP.Problem import Problem
from CSP.Variable import Variable
from CourseScheduler.Course import Course
from CourseScheduler.CourseConstraint import CourseConstraint
from CourseScheduler.AllDiffConstraint import AllDiffConstraint

class SchedulerProblem(Problem):

    def __init__(self):
        super().__init__([], [], "Scheduler Problem")
        domain = [Course("Logic Circuits", "Dr.Sedaghat", 3), Course("Data Structures", "Dr.Amintoosi", 3), Course("Technical Language", "Dr.Vahedian", 3),
                  Course("Computer Architecture", "Dr.Noori", 4), Course("Languages and Automatas Theory", "Dr.Abrishami", 4), Course("Electronic Electrical Circuits", "Dr.Vahedian", 4),
                  Course("Microprocessor", "Dr.Sedaghat", 5), Course("Compiler Design", "Dr.Amintoosi", 5), Course("Artificial Intelligence", "Dr.Abrishami", 5)] 

        x1 = Variable[Course](domain, 'B32_8')
        x2 = Variable[Course](domain, 'B33_8') 
        x3 = Variable[Course](domain, 'B34_8')
        x4 = Variable[Course](domain, 'B32_10') 
        x5 = Variable[Course](domain, 'B33_10') 
        x6 = Variable[Course](domain, 'B34_10')
        x7 = Variable[Course](domain, 'B32_14')
        x8 = Variable[Course](domain, 'B33_14')
        x9 = Variable[Course](domain, 'B34_14')

        self.variables = [x1, x2, x3, x4, x5, x6, x7, x8, x9]

        # add constraints here ...
        
                
    def print_assignments(self):
        for variable in self.variables:
            print(f"{variable.name} is set to {variable.value.name} and {variable.value.prof} ")