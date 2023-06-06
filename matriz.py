# -*- coding: utf8 -*-

# TODO: Mover o read_sequence para próximo do main.
# TODO: Mover o comentário para uma docstring
# TODO: Melhorar o nome read_sequence
# TODO: Separar as responsabilidades do read_sequence para garantir leitura
# TODO: Verificar se faz sentido ter um parser único para o comando validado
def read_sequence():  # Read and validate a sequence of commands.
    # TODO: Melhorar o nome charValid para algo mais semântico.
    # TODO: Remover os parêntesis desnecessários.
    charValid = ("ICLVHKFSX")
    # TODO: Melhorar o nome sqc. Sugestão: cmd
    # TODO: Separar a obtenção do comando, do tratamento do comando.
    sqc = input("Digite um comando: ").upper()
    sqc = sqc.split()

    for char in charValid:
        # TODO: Verificar a real necessidade desse "and.
        if char == sqc[0] and not "":
            return sqc
    else:
        print("\nComando Inválido!\n")
        return sqc
    # TODO: Implementar um único return.

# TODO: Mover o comentário para docstring.
# TODO: Extrair o print do print_board.
# TODO: print_board deveria ser ...
def print_board(board):  # Print the Board.
    print("\n")
    for row in board:
        print("".join(row))
    print("\n")

# TODO: Move o comentário para um docstring
# TODO: Expandir o argument cmd para comtemplar as partes específicas.
# TODO: Mudar "col" e "line" para "width" e "height".
# TODO: Idealmente width e height já deveriam chegar como int.
# TODO: Mudar o nome create_array para algo ligado ao board.
def create_array(cmd):  # Create a array - 'I' Command.
    board = []
    col, line = cmd

    # TODO: Renomear x par algo mais semântico.
    # TODO: Trocar o for por uma listcomp.
    for x in range(int(line)):
        board.append(["O"] * int(col))
    return board

# TODO: Mover o comentário para docstring.
# TODO: Renomear clean_array para algo melhor.
def clean_array(board):  # Clean a array - 'C' Command.
    # TODO: Extrair len(board) e len(board[line]) para variáveis.
    # TODO: Remover o "0" do range.
    for line in range(0, len(board)):
        for col in range(0, len(board[line])):
            board[line][col] = "O"
    return board

# TODO: Mover comentários para docstring.
# TODO: Expandir o cmd em parâmetros.
# TODO: Receber os parâmetros já no tipo correto.
# TODO: Verificar se faz sentido implementar um objeto Cooernada/Cell/etc
#       que encapsule os comandos em índices do board: board[Coord(1, 2)] = color - __set_item__
# TODO: Renomear color_pixel para color.
def color_pixel(cmd, board):  # Change the color of one pixel - 'L' Command.
    col, line, color = cmd

    board[int(line) - 1][int(col) - 1] = color
    return board

# TODO: Mover comentário para docstring.
# TODO: Renomear ver_pixel par algo como vertical_line.
# TODO: Expandir cmd em parâmetros que devem ser recebidos já nos tipos corretos.
def ver_pixel(cmd, board):  # Change the color of a column - 'V' Command.
    # TODO: Manter as variáveis alinhadas com o range. lineIni -> start e lineEnd -> stop
    # TODO: C é um nome ruim.
    col, lineIni, lineEnd, C = cmd

    # TODO: Renomear ver para line ou algo assim.
    # TODO: Computar as coordenadas e passá-las para algum método do board que atribui valor a múltiplas coordenadas.
    for ver in range(int(lineIni) - 1, int(lineEnd)):
        board[int(ver)][int(col) - 1] = C
    return board

# TODO: Mover comentário para docstring.
# TODO: Renomear hor_pixel para algo mais horizontal_line
# TODO: Expandir cmd em parâmetros que devem ser recebidos já nos tipos corretos.
# TODO: Verificar se é possível uniformizar a assinatura de ver_pixel e hor_pixel.
def hor_pixel(cmd, board):  # Change the color of a line - 'H' Command.
    # TODO: Manter as variáveis alinhadas com o range. colIni -> start e colEnd -> stop
    colIni, colEnd, line, color = cmd

    # TODO: Renomear ver para line ou algo assim.
    # TODO: Computar as coordenadas e passá-las para algum método do board que atribui valor a múltiplas coordenadas.
    for hor in range(int(colIni) - 1, int(colEnd)):
        board[int(line) - 1][int(hor)] = color
    return board

# TODO: Mover comentários para docstring
# TODO: Melhorar nome block_pixel
# TODO: Expandir o cmd em parâmetros que devem ser recebidos já nos tipos corretos.
# TODO: Uniformizar os parâmetros com vertical_line e horizontal_line.

def block_pixel(cmd, board):  # Change color of an entire block - 'K' Command.
    # TODO: Alinhas os nomes dos parâmetros como na função range.
    colIni, lineIni, colEnd, lineEnd, color = cmd

    # TODO: Simplificar esse códigos com as abstrações de Coordenada, Region e Board.
    for hor in range(int(colIni) - 1, int(colEnd)):
        for ver in range(int(lineIni) - 1, int(lineEnd)):
            board[int(ver)][int(hor)] = color
    return board


def out_range(board, Y, X):  # Check if a cmd is out of list range.
    line = len(board)
    col = len(board[0])

    if (X >= 0 and X < col) and (Y >= 0 and Y < line):
        return True
    else:
        return False


def fill_pixel(cmd, board):  # Fill a continuous region 'F' command.
    col, line, chgColor = cmd

    color = board[line][col]

    if out_range(board, line, col):
        board[line][col] = chgColor

        if out_range(board, line, col - 1):
            if board[line][col - 1] == color:
                fill_pixel([col - 1, line, chgColor], board)

        if out_range(board, line, col + 1):
            if board[line][col + 1] == color:
                fill_pixel([col + 1, line, chgColor], board)

        if out_range(board, line - 1, col):
            if board[line - 1][col] == color:
                fill_pixel([col, line - 1, chgColor], board)

        if out_range(board, line + 1, col):
            if board[line + 1][col] == color:
                fill_pixel([col, line + 1, chgColor], board)

    return board


def save_array(name, board):  # Save the array with the 'S' command.
    with open(name.lower(), "w") as my_file:
        for item in board:
            my_file.write("".join(item) + "\n")



def main():
    # TODO: Substituir o uso do if/elif por um mapeamento com dicionário.
    # TODO: Encapsular os detalhes do comando sem vazar para o main.
    # TODO: Extrair a definição do board para o início do processamento.
    # TODO: Verificar a possibilidade do board ser uma instância de uma classe.
    while True:
        try:
            cmd = read_sequence()

            if cmd[0] == "X":
                break

            elif cmd[0] == "I":
                board = create_array(cmd[1:3])

            elif cmd[0] == "L":
                board = color_pixel(cmd[1:4], board)

            elif cmd[0] == "V":
                board = ver_pixel(cmd[1:5], board)

            elif cmd[0] == "H":
                board = hor_pixel(cmd[1:5], board)

            elif cmd[0] == "K":
                board = block_pixel(cmd[1:6], board)

            elif cmd[0] == "F":
                # TODO: Encapsulara a conversão de índices do board.
                cmd[1] = int(cmd[1]) - 1
                cmd[2] = int(cmd[2]) - 1
                board = fill_pixel(cmd[1:4], board)

            elif cmd[0] == "S":
                save_array(cmd[1], board)

            elif cmd[0] == "C":
                board = clean_array(board)

            else:
                # TODO: Remover quando a validação do comando for encapsulada no read_sequence.
                continue

            # TODO: Extrair o print do print_board.
            print_board(board)

        except:
            # TODO: Especificar as exception que serão tratadas.
            # TODO: Verificar como isolar a validação do comando no read_sequence.
            print("\nComando inválido!\n")


if __name__ == '__main__':
    main()
