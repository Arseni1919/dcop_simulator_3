from simulators.nodes import *


def scenario_n_1():
    agents = {
        'target0': {
            'num': 0,
            'req': 30,
            'cells_near_me': [0]
        },
        'robot0': {
            'num': 0,
            'cred': 28,
            'domain': [0, 1]
        },
        'robot1': {
            'num': 1,
            'cred': 10,
            'domain': [0, 2]
        },
    }
    return create_scenario(agents)


def scenario_n_2():
    targets = [
        TargetNode('target0', 0, req=30, cells_near_me=['pos0']),
    ]
    robots = [
        RobotNode('robot0', 0, cred=28, domain=['pos0', 'pos1']),
        RobotNode('robot1', 1, cred=10, domain=['pos0', 'pos1'])
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


def scenario_n_7():
    targets = [
        TargetNode('target0', 0, req=21, cells_near_me=['pos0']),
    ]
    robots = [
        RobotNode('robot0', 0, cred=3, domain=['pos0', 'pos1']),
        RobotNode('robot1', 1, cred=10, domain=['pos0', 'pos2']),
        RobotNode('robot2', 2, cred=10, domain=['pos0', 'pos3']),
    ]
    positions = [
        PositionNode('pos0', 0, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos1', 1, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos2', 2, dict_of_weights=create_dict_of_weights(robots)),
        PositionNode('pos3', 3, dict_of_weights=create_dict_of_weights(robots)),
    ]

    robots[0].neighbours = [targets[0], positions[0], positions[1]]
    robots[1].neighbours = [targets[0], positions[0], positions[2]]
    robots[2].neighbours = [targets[0], positions[0], positions[3]]
    targets[0].neighbours = [robots[0], robots[1], robots[2]]
    positions[0].neighbours = [*robots]
    positions[1].neighbours = [robots[0]]
    positions[2].neighbours = [robots[1]]
    positions[3].neighbours = [robots[2]]

    return [*targets, *robots, *positions]


def scenario_n_8():
    agents = {
        'target0': {
            'num': 0,
            'req': 70,
            'cells_near_me': [0, 3]
        },
        'robot0': {
            'num': 0,
            'cred': 30,
            'domain': [0, 1]
        },
        'robot1': {
            'num': 1,
            'cred': 31,
            'domain': [2, 3]
        },
        'robot2': {
            'num': 2,
            'cred': 29,
            'domain': [0, 3]
        },
    }
    return create_scenario(agents)


def scenario_n_9():
    agents = {
        'target0': {
            'num': 0,
            'req': 70,
            'cells_near_me': [0, 3]
        },
        'target1': {
            'num': 1,
            'req': 68,
            'cells_near_me': [2, 3]
        },
        'robot0': {
            'num': 0,
            'cred': 30,
            'domain': [0, 1]
        },
        'robot1': {
            'num': 1,
            'cred': 31,
            'domain': [2, 3]
        },
        'robot2': {
            'num': 2,
            'cred': 29,
            'domain': [0, 3]
        },
    }
    return create_scenario(agents)


def create_scenario(agents):
    targets, robots, positions = [], [], []
    positions_dict = {}
    # create positions
    for agent_name, agent_dict in agents.items():
        list_to_check = []
        if 'target' in agent_name:
            list_to_check = agent_dict['cells_near_me']
        if 'robot' in agent_name:
            list_to_check = agent_dict['domain']
        for cell in list_to_check:
            if cell not in positions_dict:
                positions_dict[cell] = PositionNode(f'pos{cell}', cell, dict_of_weights={})
                positions.append(positions_dict[cell])
    # create robots and targets
    for agent_name, agent_dict in agents.items():
        if 'target' in agent_name:
            targets.append(TargetNode(agent_name, agent_dict['num'],  req=agent_dict['req'],
                                      cells_near_me=[positions_dict[cell].name for cell in agent_dict['cells_near_me']])
                           )
        if 'robot' in agent_name:
            robots.append(RobotNode(agent_name, agent_dict['num'], cred=agent_dict['cred'],
                                    domain=[positions_dict[cell].name for cell in agent_dict['domain']]))
    # update positions
    for pos_nun, pos_node in positions_dict.items():
        pos_node.dict_of_weights = create_dict_of_weights(robots)
    # neighbours
    # targets - robots
    for target in targets:
        for robot in robots:
            if len(set(target.cells_near_me) & set(robot.domain)) > 0:
                if target not in robot.neighbours:
                    robot.neighbours.append(target)
                if robot not in target.neighbours:
                    target.neighbours.append(robot)
    # positions - robots
    for robot in robots:
        agent_dict = agents[robot.name]
        for cell in agent_dict['domain']:
            cell_node = positions_dict[cell]
            robot.neighbours.append(cell_node)
            cell_node.neighbours.append(robot)
    return [*targets, *robots, *positions]




