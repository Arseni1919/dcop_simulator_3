from simulators.nodes import *


def scenario_n_1():
    targets = [
        TargetNode('target0', 0, req=30, cells_near_me=['pos0']),
    ]
    robots = [
        RobotNode('robot0', 0, cred=10, domain=['pos0', 'pos1']),
        RobotNode('robot1', 1, cred=10, domain=['pos0', 'pos2'])
    ]
    positions = [
        PositionNode('pos0', 0, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos1', 1, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos2', 2, dict_of_weights=create_dict_of_weights(robots)),
    ]

    targets[0].neighbours = [robots[0], robots[1]]
    robots[0].neighbours = [targets[0], positions[0], positions[1]]
    robots[1].neighbours = [targets[0], positions[0], positions[2]]
    positions[0].neighbours = [*robots]
    positions[1].neighbours = [robots[0]]
    positions[2].neighbours = [robots[1]]

    return [*targets, *robots, *positions]


def scenario_n_2():
    targets = [
        TargetNode('target0', 0, req=10, cells_near_me=['pos0']),
    ]
    robots = [
        RobotNode('robot0', 0, cred=7, domain=['pos0', 'pos1']),
        RobotNode('robot1', 1, cred=6, domain=['pos0', 'pos1'])
    ]
    positions = [
        PositionNode('pos0', 0, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos1', 1, dict_of_weights=create_dict_of_weights(robots)),
    ]

    targets[0].neighbours = [robots[0], robots[1]]
    robots[0].neighbours = [targets[0], positions[0], positions[1]]
    robots[1].neighbours = [targets[0], positions[0], positions[1]]
    positions[0].neighbours = [*robots]
    positions[1].neighbours = [*robots]

    return [*targets, *robots, *positions]


def scenario_n_3():
    targets = [
        TargetNode('target0', 0, req=30, cells_near_me=['pos0']),
        TargetNode('target1', 1, req=30, cells_near_me=['pos0']),
    ]
    robots = [
        RobotNode('robot0', 0, cred=25, domain=['pos0', 'pos1']),
        RobotNode('robot1', 1, cred=13, domain=['pos0', 'pos2'])
    ]
    positions = [
        PositionNode('pos0', 0, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos1', 1, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos2', 2, dict_of_weights=create_dict_of_weights(robots)),
    ]

    targets[0].neighbours = [robots[0], robots[1]]
    targets[1].neighbours = [robots[0], robots[1]]
    robots[0].neighbours = [targets[0], targets[1], positions[0], positions[1]]
    robots[1].neighbours = [targets[0], targets[1], positions[0], positions[2]]
    positions[0].neighbours = [*robots]
    positions[1].neighbours = [robots[0]]
    positions[2].neighbours = [robots[1]]

    return [*targets, *robots, *positions]


def scenario_n_4():
    targets = [
        TargetNode('target0', 0, req=30, cells_near_me=['pos0']),
        TargetNode('target1', 1, req=30, cells_near_me=['pos1']),
    ]
    robots = [
        RobotNode('robot0', 0, cred=25, domain=['pos0', 'pos1']),
        RobotNode('robot1', 1, cred=13, domain=['pos0', 'pos1'])
    ]
    positions = [
        PositionNode('pos0', 0, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos1', 1, dict_of_weights=create_dict_of_weights(robots)),
    ]

    targets[0].neighbours = [robots[0], robots[1]]
    targets[1].neighbours = [robots[0], robots[1]]
    robots[0].neighbours = [targets[0], targets[1], positions[0], positions[1]]
    robots[1].neighbours = [targets[0], targets[1], positions[0], positions[1]]
    positions[0].neighbours = [*robots]
    positions[1].neighbours = [*robots]

    return [*targets, *robots, *positions]


def scenario_n_5():
    targets = [
        TargetNode('target0', 0, req=30, cells_near_me=['pos1']),
    ]
    robots = [
        RobotNode('robot0', 0, cred=10, domain=['pos0', 'pos1']),
        RobotNode('robot1', 1, cred=10, domain=['pos0', 'pos2']),
        RobotNode('robot2', 2, cred=10, domain=['pos1', 'pos4']),
        RobotNode('robot3', 3, cred=10, domain=['pos2', 'pos3'])
    ]
    positions = [
        PositionNode('pos0', 0, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos1', 1, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos2', 2, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos3', 3, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos4', 4, dict_of_weights=create_dict_of_weights(robots)),
    ]

    targets[0].neighbours = [robots[0], robots[2]]
    robots[0].neighbours = [targets[0], positions[0], positions[1]]
    robots[1].neighbours = [positions[0], positions[2]]
    robots[2].neighbours = [targets[0], positions[1], positions[4]]
    robots[3].neighbours = [positions[2], positions[3]]
    positions[0].neighbours = [robots[0], robots[1]]
    positions[1].neighbours = [robots[0], robots[2]]
    positions[2].neighbours = [robots[1], robots[3]]
    positions[3].neighbours = [robots[3]]
    positions[4].neighbours = [robots[2]]

    return [*targets, *robots, *positions]



def scenario_n_6():
    targets = [
        TargetNode('target0', 0, req=30, cells_near_me=['pos1']),
    ]
    robots = [
        RobotNode('robot0', 0, cred=20, domain=['pos0', 'pos1', 'pos4']),
        RobotNode('robot1', 1, cred=22, domain=['pos0', 'pos2']),
        RobotNode('robot2', 2, cred=24, domain=['pos1', 'pos4']),
        RobotNode('robot3', 3, cred=26, domain=['pos2', 'pos3'])
    ]
    positions = [
        PositionNode('pos0', 0, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos1', 1, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos2', 2, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos3', 3, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos4', 4, dict_of_weights=create_dict_of_weights(robots)),
    ]

    targets[0].neighbours = [robots[0], robots[2]]
    robots[0].neighbours = [targets[0], positions[0], positions[1], positions[4]]
    robots[1].neighbours = [positions[0], positions[2]]
    robots[2].neighbours = [targets[0], positions[1], positions[4]]
    robots[3].neighbours = [positions[2], positions[3]]
    positions[0].neighbours = [robots[0], robots[1]]
    positions[1].neighbours = [robots[0], robots[2]]
    positions[2].neighbours = [robots[1], robots[3]]
    positions[3].neighbours = [robots[3]]
    positions[4].neighbours = [robots[2], robots[0]]

    return [*targets, *robots, *positions]









