import turtle


def read_coords(file):
    henrydraper = []
    coords = []
    magnitudes = []
    names = {}

    # Opens file and creates lists for HD number, coordinates, and magnitudes
    data = open(file, 'r')
    for line in data:
        data_list = line.split(' ', maxsplit=6)
        henrydraper += [int(data_list[3])]
        coords += [(float(data_list[0]), float(data_list[1]))]
        magnitudes += [float(data_list[4])]

        # Creates dictionary for star names
        if len(data_list) == 7 and ';' in data_list[6]:
            data_list[6] = data_list[6].split(';')
            data_list[6][1] = data_list[6][1].strip("\n").lstrip()
            names.update({data_list[6][0]: data_list[3],
                          data_list[6][1]: data_list[3]})
        elif len(data_list) == 7:
            data_list[6] = data_list[6].strip("\n")
            names.update({data_list[6]: data_list[3]})

    # Creates coordinate and magnitude dictionaries
    coordinates_dict = dict(zip(henrydraper, coords))
    magnitudes_dict = dict(zip(henrydraper, magnitudes))
    dictionaries = (coordinates_dict, magnitudes_dict, names)
    return dictionaries


def draw_square(size):
    turtle.speed(0)
    turtle.penup()
    turtle.bgcolor('black')
    turtle.pencolor('white')
    turtle.fillcolor('white')
    turtle.begin_fill()
    turtle.pendown()
    for i in range(4):
        turtle.fd(size)
        turtle.rt(90)
    turtle.penup()
    turtle.end_fill()


def plot_plain_stars(picture_size, coordinates_dict):
    turtle.setup(picture_size, picture_size)
    turtle.ht()
    for i in coordinates_dict:
        turtle.penup()
        turtle.goto(coordinates_dict[i][0] * picture_size / 2.1,
                    coordinates_dict[i][1] * picture_size / 2.1)
        draw_square(1)


def plot_by_magnitude(picture_size, coordinates_dict, magnitudes_dict):
    turtle.screensize(picture_size, picture_size)
    turtle.ht()
    for i in coordinates_dict:
        turtle.penup()
        turtle.goto(coordinates_dict[i][0] * picture_size / 2,
                    coordinates_dict[i][1] * picture_size / 2)
        star_size = round(10.0 / (magnitudes_dict[i] + 2))
        if star_size > 8:
            star_size = 8
        draw_square(star_size)


def main():
    dictionaries = read_coords('stars.txt')
    coordinates_dict = dictionaries[0]
    magnitudes_dict = dictionaries[1]
    names_dict = dictionaries[2]
    # plot_plain_stars(700, coordinates_dict)
    plot_by_magnitude(700, coordinates_dict, magnitudes_dict)


main()
