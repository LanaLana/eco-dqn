import copy
import numpy as np
import random


class Action:

    def __init__(self, vertex_left, negation_left, vertex_right, negation_right):
        self.vertex_left = vertex_left
        self.negation_left = negation_left
        self.vertex_right = vertex_right
        self.negation_right = negation_right


class Circuit:


class Environment:
    def __init__(self, num_vars):
        self.num_vertices = num_vars
        self.score = 0
        self.best_score = 0
        self.best_circuit = None

    def calculate_score(self):
        # number of equal
        return 0

    def step(self, action):
        # 1. Performs the action and calculates the score change.
        if action is None:
            action = Action(
                vertex_left=random.randint(0, self.num_vertices - 1),
                negation_left=random.choice([True, False]),
                vertex_right=random.randint(action.vertex_left, self.num_vertices - 1),
                negation_right=random.choice([True, False])
            )

        #2. Calculate reward for action
        new_score = self.calculate_score()
        reward = new_score - self.score
        self.score = new_score

        if self.score > self.best_score:
            self.best_score = self.score
            self.best_circuit = copy.deepcopy(self.circuit)

        # 3. Updates the state of the system









