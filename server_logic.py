import random
from typing import List, Dict


def choose_move(data: dict) -> str:
    my_head = data["you"]["head"]
    my_body = data["you"]["body"]
    possible_moves = ["up", "down", "left", "right"]
    possible_moves = avoid_my_neck(my_head, my_body, possible_moves)
    # possible_moves = mybody(my_head, my_body, possible_moves)
    possible_moves = borders(data, possible_moves)

    # last move under this line
    move = random.choice(possible_moves)
    print(f"{data['game']['id']} MOVE {data['turn']}: {move} picked from all valid options in {possible_moves}")
    return move


def avoid_my_neck(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:
    my_neck = my_body[1]  # The segment of body right after the head is the 'neck'

    if my_neck["x"] < my_head["x"]:  # my neck is left of my head
        possible_moves.remove("left")
    elif my_neck["x"] > my_head["x"]:  # my neck is right of my head
        possible_moves.remove("right")
    elif my_neck["y"] < my_head["y"]:  # my neck is below my head
        possible_moves.remove("down")
    elif my_neck["y"] > my_head["y"]:  # my neck is above my head
        possible_moves.remove("up")

    return possible_moves


def borders(data: dict, possible_moves: List[str]) -> List[str]:
    bh = data["board"]["height"] - 1  # y axis
    bw = data["board"]["width"] - 1  # x axis
    my_head = data["you"]["head"]

    if my_head["x"] == bw:
        possible_moves.remove("right")
    elif my_head["x"] == 0:
        possible_moves.remove("left")

    if my_head["y"] == bh:
        possible_moves.remove("up")
    elif my_head["y"] == 0:
        possible_moves.remove("down")

    return possible_moves


# TODO Using information from 'data', don't let your Battlesnake pick a move that would hit its own body
def mybody(my_head: Dict[str, int], my_body: List[dict], possible_moves: List[str]) -> List[str]:
    head = my_head
    body = my_body
    print(head, body)
    return possible_moves

    # TODO: Using information from 'data', don't let your Battlesnake pick a move that would collide with
    #  another Battlesnake
    # TODO: Using information from 'data', make your Battlesnake move towards a piece of food on the board
    # TODO: Explore new strategies for picking a move that are better than random
    # TODO: an array with all blocked fields for easy evaluation. one x, one y
    # TODO: uncomment the lines below so you can see what this data looks like in your output!
    # print(f"~~~ Turn: {data['turn']}  Game Mode: {data['game']['ruleset']['name']} ~~~")
    # print(f"All board data this turn: {data}")
    # print(f"My Battlesnakes head this turn is: {my_head}")
    # print(f"My Battlesnakes body this turn is: {my_body}")


'''
data = {
    "game": {
    "id": "game-00fe20da-94ad-11ea-bb37",
    "ruleset": {
    "name": "standard",
    "version": "v.1.2.3"
    },
    "timeout": 500
    },
    "turn": 14,
    "board": {
        "height": 11,
        "width": 11,
        "food": [
            {"x": 5, "y": 5},
            {"x": 9, "y": 0},
            {"x": 2, "y": 6}
        ],
        "hazards": [
            {"x": 3, "y": 2}
        ],
        "snakes": [
            {
                "id": "snake-508e96ac-94ad-11ea-bb37",
                "name": "My Snake",
                "health": 54,
                "body": [
                    {"x": 0, "y": 0},
                    {"x": 1, "y": 0},
                    {"x": 2, "y": 0}
                ],
                "latency": "111",
                "head": {"x": 0, "y": 0},
                "length": 3,
                "shout": "why are we shouting??",
                "squad": ""
            },
            {
                "id": "snake-b67f4906-94ae-11ea-bb37",
                "name": "Another Snake",
                "health": 16,
                "body": [
                    {"x": 5, "y": 4},
                    {"x": 5, "y": 3},
                    {"x": 6, "y": 3},
                    {"x": 6, "y": 2}
                ],
                "latency": "222",
                "head": {"x": 5, "y": 4},
                "length": 4,
                "shout": "I'm not really sure...",
                "squad": ""
            }
        ]
    },
    "you": {
        "id": "snake-508e96ac-94ad-11ea-bb37",
        "name": "My Snake",
        "health": 54,
        "body": [
            {"x": 0, "y": 0},
            {"x": 1, "y": 0},
            {"x": 2, "y": 0}
        ],
        "latency": "111",
        "head": {"x": 0, "y": 0},
        "length": 3,
        "shout": "why are we shouting??",
        "squad": ""
    }
}

print(choose_move(data))
'''