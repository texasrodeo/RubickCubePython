import xml.etree.ElementTree as xml


def createXMLFile(game, file_name, mainForm):
    if not mainForm.game_started:
        pass
    else:
        root = write_game_info(game)
        write_color_matrix(root, game.get_matrix)
        tree = xml.ElementTree(root)
        tree.write(open(file_name, 'w'), encoding='unicode')

def write_color_matrix(root, matr):
    str = 'matrix'
    matrix = xml.SubElement(root, str)
    for x in matr:
        for k in x:
            elem = xml.SubElement(matrix, "elem")
            elem.set("COLOR", k)

def write_game_info(game):
    root = xml.Element("game")
    root.set("difficulty", to_string(game.get_difficulty))
    root.set("turns_left", to_string(game.get_turns_left))
    root.set("game_ended", to_string(game.is_game_ended))
    return root



def to_string(value):
    return str(value)



def readXMLFile(file_name):
    tree = xml.parse(file_name)
    root = tree.getroot()
    args = {}

    difficulty = int(root.attrib.get("difficulty"))
    args['difficulty'] = difficulty

    if root.attrib.get("game_endend") == "True":
        args['game_ended'] = True
    else:
        args['game_ended'] = False
    turns_left = int(root.attrib.get("turns_left"))
    args['turns_left'] = turns_left
    colors = []
    for elem in root.find('matrix'):

        COLOR = elem.attrib.get("COLOR")
        colors.append(COLOR)
    args['COLORS'] = colors
    return args