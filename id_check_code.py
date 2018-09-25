"""Check if given ID code is valid."""


def check_your_id(id_code: str):
    """
    Check if given ID code is valid and return the result.

    :param id_code: str
    :return: boolean
    """
    gender_number = int(id_code[0])
    ab = 0
    if gender_number == 1 or gender_number == 2:
        ab = 18
    elif gender_number == 3 or gender_number == 4:
        ab = 19
    elif gender_number == 5 or gender_number == 6:
        ab = 20

    year = int(id_code[1:3])
    year_number = str(ab) +
    month_number = int(id_code[3:5])
    day_number = int(id_code[5:7])
    born_order = int(id_code[7:10])
    control_number = int(id_code[10])

    if check_gender_number(gender_number) == True and check_year_number_two_digits(
            year_number) == True and check_month_number(month_number) == True and check_day_number(year_number,
                                                                                                   month_number,
                                                                                                   day_number) == True and check_born_order(
            born_order) == True and check_control_number(control_number) == True:
        return True
    else:
        return False


# korras
def check_gender_number(gender_number: int):
    """
    Check if given value is correct for gender number in ID code.

    :param gender_number: int
    :return: boolean
    """
    if gender_number in range(1, 7):
        return True
    else:
        return False


# korras
def check_year_number_two_digits(year_number: int):
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """

    if year_number in range(0, 100):
        return True
    else:
        return False


def check_month_number(month_number: int):
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """

    if month_number in range(1, 13):
        return True
    else:
        return False


# korras
def check_day_number(year_number: int, month_number: int, day_number: int):
    """
    Check if given value is correct for day number in ID code.
    Also, consider leap year and which month has 30 or 31 days.

    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """

    month31 = [1, 3, 5, 7, 8, 10, 12]
    month30 = [4, 6, 9, 11]

    for i in month31:
        if month_number == i and day_number in range(1, 32):
            return True

    for j in month30:
        if month_number == j and day_number in range(1, 31):
            return True

    if month_number == 2:
        if day_number in range(1, 29):
            return True
        elif check_leap_year(year_number) == True and day_number in range(1, 30):
            return True
        else:
            return False


# korras
def check_leap_year(year_number: int):
    """
    Check if given year is a leap year. If True, it is a leap year

    :param year_number: int
    :return: boolean
    """

    if (int(year_number) % 400) == 0:
        return True
    elif (int(year_number) % 100) == 0:
        return False
    elif (int(year_number) % 4) == 0:
        return True
    else:
        return False


# korras
def check_born_order(born_order: int):
    """
    Check if given value is correct for born order number in ID code.

    :param born_order: int
    :return: boolean
    """
    if born_order in range(0, 1000):
        return True
    else:
        return False


def check_control_number(id_code: str):
    """
    Check if given value is correct for control number in ID code.
    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """

    multipliers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    multipliers_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    id_code_numbers = [int(id_code[0]), int(id_code[1]), int(id_code[2]), int(id_code[3]), int(id_code[4]),
                       int(id_code[5]), int(id_code[6]), int(id_code[7]), int(id_code[8]), int(id_code[9])]

    multipliers_1. * id_code_numbers

    control_number = id_code[-1]

    control_number_calc_first = (
                (int(id_code[0]) * 1) + (int(id_code[1]) * 2) + (int(id_code[2]) * 3) + (int(id_code[3]) * 4) + (
                    int(id_code[4]) * 5) + (int(id_code[5]) * 6) + (int(id_code[6]) * 7) + (int(id_code[7]) * 8) + (
                            int(id_code[8]) * 9) + (int(id_code[9]) * 1))
    control_number_calc_second = (
                (int(id_code[0]) * 3) + (int(id_code[1]) * 4) + (int(id_code[2]) * 5) + (int(id_code[3]) * 6) + (
                    int(id_code[4]) * 7) + (int(id_code[5]) * 8) + (int(id_code[6]) * 9) + (int(id_code[7]) * 1) + (
                            int(id_code[8]) * 2) + (int(id_code[9]) * 3))
    if control_number_calc_first % 11 == control_number:
        return True
    elif control_number_calc_first % 11 == 10:
        if control_number_calc_second % 11 == control_number:
            return True
        elif control_number_calc_second % 11 == 10 and control_number == 0
            return True
    else:
        return False

    elif control_number_calc_first % 11 == 10 and control_number_cal_second % 11 == control_number:
    return True

    elif control_number_cal_second % 11 == 10 and control_number == 0:
    return True
    else:
    return False


def get_data_from_id(id_code: str):
    """
    Get possible information about the person.
    Use given ID code and return a short message.
    Follow the template - This is a (gender) born on (DD.MM.YYYY).
    :param id_code: str
    :return: str
    """

    # get_gender = "male" or "female"
    # if id_code[0] == 1 or id_code[] == 3 or id_code[1] == 5:
    #     get_gender = male
    # elif id_code[1] == 2 or id_code[1] == 4 or id_code[1] == 6:
    #     get_gender = female

    birth_date = str(id_code[5:7]) + "." + str(id_code[3:5]) + "." + str(get_full_year(gender_number, year))

    if check_your_id() == False:
        return ("Given invalid ID code!")
    elif id_code[1] == 1 or id_code[1] == 3 or id_code[1] == 5:
        return ("This is a" + get_gender(gender_number) + "born on" + birth_date


def get_gender(gender_number):
    """
    Define the gender according to the number from ID code.

    :param gender_number: int
    :return: str
    """

    male = [1, 3, 5]
    female = [2, 4, 6]

    for i in male:
        if gender_number == i:
            return "male"

    for j in female:
        if gender_number == j:
            return "female"


# korras
def get_full_year(gender_number: int, year: int):
    """
    Define the 4-digit year when given person was born.
    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year: int
    :return: int
    """

    year_nr_start = 0
    if gender_number == 1 or gender_number == 2:
        year_nr_start = 18
    elif gender_number == 3 or gender_number == 4:
        year_nr_start = 19
    elif gender_number == 5 or gender_number == 6:
        year_nr_start = 20
    year_number = str(year_nr_start) + str(year)
    return year_number
