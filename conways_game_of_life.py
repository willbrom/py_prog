#!/bin/python3

initial_state = [
        [{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []}],
        [{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []}],
        [{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []}],
        [{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []}],
        [{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []}],
        [{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []},{'v': 0, 'l': []}]
        ]

initial_state[0][0]['l'].append(initial_state[0][1]['v'])
initial_state[0][0]['l'].append(initial_state[1][0]['v'])
initial_state[0][0]['l'].append(initial_state[1][1]['v'])

initial_state[-1][0]['l'].append(initial_state[-1][1]['v'])
initial_state[-1][0]['l'].append(initial_state[-2][0]['v'])
initial_state[-1][0]['l'].append(initial_state[-2][1]['v'])

initial_state[0][-1]['l'].append(initial_state[0][-2]['v'])
initial_state[0][-1]['l'].append(initial_state[1][-1]['v'])
initial_state[0][-1]['l'].append(initial_state[1][-2]['v'])

print(initial_state[-1])

print(id(initial_state[0][0]['l'][0]),id(initial_state[0][1]['v']), sep=',')

print(initial_state[0])
