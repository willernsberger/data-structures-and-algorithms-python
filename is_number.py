from enum import Enum
# given a string, determine if the string represents a valid number


# finite state machine
class StateMachine(Enum):
    # states
    START = 0
    NEGATIVE = 1
    DIGIT = 2
    DECIMAL = 3
    DECIMAL_DIGIT = 4
    POWER = 5
    POWER_NEGATIVE = 6
    POWER_DIGIT = 7
    POWER_DECIMAL = 8
    POWER_DECIMAL_DIGIT = 9


# transitions between states
NEXT_STATES_MAP = {
    StateMachine.START: [StateMachine.NEGATIVE, StateMachine.DIGIT, StateMachine.DECIMAL],
    StateMachine.NEGATIVE: [StateMachine.DIGIT],
    StateMachine.DIGIT: [StateMachine.DIGIT, StateMachine.DECIMAL, StateMachine.POWER],
    StateMachine.DECIMAL: [StateMachine.DECIMAL_DIGIT],
    StateMachine.DECIMAL_DIGIT: [StateMachine.DECIMAL_DIGIT, StateMachine.POWER],
    StateMachine.POWER: [StateMachine.POWER_NEGATIVE, StateMachine.POWER_DIGIT],
    StateMachine.POWER_NEGATIVE: [StateMachine.POWER_DIGIT],
    StateMachine.POWER_DIGIT: [StateMachine.POWER_DIGIT, StateMachine.POWER_DECIMAL],
    StateMachine.POWER_DECIMAL: [StateMachine.POWER_DECIMAL_DIGIT],
    StateMachine.POWER_DECIMAL_DIGIT: [StateMachine.POWER_DECIMAL_DIGIT]
}

# validation
STATE_VALIDATOR = {
    StateMachine.START: lambda x: True,
    StateMachine.NEGATIVE: lambda x: x == '-',
    StateMachine.DIGIT: lambda x: x.isdigit(),
    StateMachine.DECIMAL: lambda x: x == '.',
    StateMachine.DECIMAL_DIGIT: lambda x: x.isdigit(),
    StateMachine.POWER: lambda x: x == 'e',
    StateMachine.POWER_NEGATIVE: lambda x: x == '-',
    StateMachine.POWER_DIGIT: lambda x: x.isdigit(),
    StateMachine.POWER_DECIMAL: lambda x: x == '.',
    StateMachine.POWER_DECIMAL_DIGIT: lambda x: x.isdigit()
}

VALID_END_STATE = {
    StateMachine.START: False,
    StateMachine.NEGATIVE: False,
    StateMachine.DIGIT: True,
    StateMachine.DECIMAL: False,
    StateMachine.DECIMAL_DIGIT: True,
    StateMachine.POWER: False,
    StateMachine.POWER_NEGATIVE: False,
    StateMachine.POWER_DIGIT: True,
    StateMachine.POWER_DECIMAL: False,
    StateMachine.POWER_DECIMAL_DIGIT: True
}


def is_number(number_string):
    state = StateMachine.START
    # evaluate the string
    for c in number_string:
        # fetch the next states
        transitions = NEXT_STATES_MAP[state]
        # check if there is a valid transition
        # if so, update the state
        # otherwise return False
        valid = False
        for transition in transitions:
            if STATE_VALIDATOR[transition](c):
                state = transition
                valid = True
        if not valid:
            return False
    # check the end state for invalid ending states
    return VALID_END_STATE[state]


# driver
test_string = '-12.3e-4.56'
print(is_number(test_string))
