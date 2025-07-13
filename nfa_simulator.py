import sys
from collections import deque

def parse_input():
    lines = []
    for line in sys.stdin:
        lines.append(line.strip())

    inputs = lines[0].split('|')
    states = lines[1].split(',')       
    start_state = lines[4]
    transitions = {}

    for line in lines[5:]:
        if not line:
            continue

        left, right = line.split('->')
        current_state, symbol = left.split(',')

        if current_state not in transitions:
            transitions[current_state] = {}

        if symbol not in transitions[current_state]:
            transitions[current_state][symbol] = set()
        
        if right == '#':
            next_states = set()
        else:
            next_states = set(right.split(','))

        for state in next_states:
            transitions[current_state][symbol].add(state)

    return inputs, start_state, transitions

def process_epsilon_closure(state_set, transitions):
    closure = set(state_set)
    queue = deque(state_set)  

    while queue:
        current = queue.popleft()

        if current in transitions and '$' in transitions[current]:
            for next_state in transitions[current]['$']:
                if next_state not in closure:
                    closure.add(next_state)
                    queue.append(next_state)

    return closure

def nfa_result(inputs, start_state, transitions): 
    results = []

    for input_str in inputs:
        symbols = input_str.split(',') if input_str else []
        start_set = set()
        start_set.add(start_state)
        current_states = process_epsilon_closure(start_set, transitions)  

        if current_states:
            sorted_states = sorted(current_states)
            first_entry = ','.join(sorted_states)
        else:
            first_entry = '#'

        result_sequence = [first_entry]

        for symbol in symbols:
            next_states = set()

            for state in current_states:
                if state in transitions and symbol in transitions[state]:
                    next_states.update(transitions[state][symbol])

            current_states = process_epsilon_closure(next_states, transitions)

            if current_states:
                sorted_states = sorted(current_states)
                new_entry = ','.join(sorted_states)
            else:
                new_entry = '#'

            result_sequence.append(new_entry)
        
        results.append('|'.join(result_sequence))

    return results

def main():
    inputs, start_state, transitions = parse_input()
    results = nfa_result(inputs, start_state, transitions)

    for result_line in results:
        print(result_line)

if __name__ == "__main__": 
    main()
