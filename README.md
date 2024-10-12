# Artificial-Intelligence-Course CSP Project

This project provides a framework for solving different problems using Constraint Satisfaction Problem (CSP) techniques. It includes two distinct problem modules: **Course Scheduling** and **States Problem**, both of which leverage a common CSP core.

## Project Structure

- **main.py**: The main entry point for solving CSP problems. This file allows users to switch between different problem domains (e.g., Course Scheduling, States).
- **CSP/**: Contains the core CSP algorithms and classes, used as the foundation for solving different problems.
- **CourseScheduler/**: A module that defines the Course Scheduling problem, with specific constraints and logic to assign courses to time slots and rooms.
- **States/**: A module that defines the States problem, focusing on constraints specific to state-based logic (e.g., map coloring or state assignments).
- **Scheduling Problem.pdf**: A document describing the Course Scheduling Problem in detail.
- **README.md**: Project documentation (this file).


## Problem Descriptions

### 1. Course Scheduling Problem
The Course Scheduling Problem aims to assign courses to classrooms and time slots while satisfying various constraints, such as:
- No room can have more than one course at the same time.
- Courses should be assigned to appropriate professors and time slots based on availability.

### 2. States Problem
The States Problem involves constraints specific to a set of states (e.g., map coloring), where:
- No two neighboring states can share the same color.
- The CSP core ensures efficient assignment of colors or labels based on constraints.

## CSP Core

The **CSP** folder contains the core implementation of the Constraint Satisfaction Problem, including:
- **Constraint propagation** techniques.
- **Backtracking** search for finding solutions.
- General utilities for defining variables, domains, and constraints.

## Contributing

Contributions are welcome! If you have any suggestions, issues, or improvements, please open a pull request or issue on the GitHub repository.
