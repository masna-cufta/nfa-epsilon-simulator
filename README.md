# NFA Simulator with Epsilon Transitions

This is a Python program that simulates a Non-deterministic Finite Automaton (NFA) with support for epsilon ($) transitions. It reads the automaton definition and input strings from standard input (stdin), processes each input, and prints the set of current states after each step.

## Features:

Supports multiple input strings separated by '|'

Handles epsilon ($) transitions

Prints the epsilon closure at the beginning and after each symbol

Outputs '#' when no states are reachable

## Input Format:
The input should be given via standard input in the following order:

Line 1: Input strings separated by '|'

Line 2: List of states (e.g. q0,q1,q2)

Line 3: Input alphabet (e.g. a,b)

Line 4: Symbol for epsilon (always '$')

Line 5: Start state (e.g. q0)

Line 6 and onward: Transitions in the format currentState,symbol->nextState1,nextState2,...
Use '#' on the right side if there are no reachable states.

## Example Input:
a,b
q0,q1,q2
a,b
$
q0
q0,a->q1
q1,$->q2
q2,b->q0

## Example Output:
q0,q1,q2|q1,q2|q0,q1,q2

## Explanation:

The output shows the reachable states after each input symbol (including epsilon closures).

States are sorted alphabetically and separated by commas.

'#' means that no states are reachable at that point.

## How to Run:
Save the Python script as e.g. nfa_simulator.py, then run:

python3 nfa_simulator.py < input.txt

Where input.txt contains the properly formatted input.
