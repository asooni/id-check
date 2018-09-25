"""Check if given ID code is valid."""
id_code = str(49211130281)
gender_number = int(id_code[0])
year_number = int(id_code[1:3])
month_number = int(id_code[3:5])
day_number = int(id_code[5:7])
born_order = int(id_code[7:10])
control_number = int(id_code[-1])

def check_your_id(id_code):
    """
    Check if given ID code is valid and return the result.

    :param id_code: str
    :return: boolean
    """
    if check_gender_number(gender_number) is True and check_year_number_two_digits(year_number) is True and check_month_number(month_number) is True and check_day_number(year_number, month_number, day_number) is True and check_born_order(born_order) is True and check_control_number(control_number) is True:
        return True
    else:
        return False


# korras
def check_gender_number(gender_number):
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
def check_year_number_two_digits(year_number):
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    if year_number in range(0, 100):
        return True
    else:
        return False


# korras
def check_month_number(month_number):
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
def check_day_number(year_number, month_number, day_number):
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
        elif check_leap_year(year_number) is True and day_number in range(1, 30):
            return True
        else:
            return False


# korras
def check_leap_year(year_number):
    """
    Check if given year is a leap year. If True, it is a leap year.

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
def check_born_order(born_order):
    """
    Check if given value is correct for born order number in ID code.

    :param born_order: int
    :return: boolean
    """
    if born_order in range(0, 1000):
        return True
    else:
        return False

# korras
def check_control_number(id_code):
    """
    Check if given value is correct for control number in ID code.

    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """

    # tee list idcodest
    # id_array = map(int, id_code) # see toimib ka
    id_array = [int(x) for x in id_code]
    # eemalda viimane kontrollnumber
    del id_array[-1]

    # loopi l2bi iga kordajaga ja liida saadu kokku
    i = 0
    kordaja = 1
    korrutis = 0

    while i < len(id_array):
        korrutis += id_array[i] * kordaja
        i += 1
        kordaja += 1

        if kordaja == 10:
            kordaja = 1
            continue

    control_number = korrutis % 11

    # if 10, siis teisiti.
    if control_number == 10:
        i = 0
        kordaja = 3
        korrutis = 0

        while i < len(id_array):
            korrutis += id_array[i] * kordaja
            i += 1
            kordaja += 1

            if kordaja == 10:
                kordaja = 1
                continue

    control_number = korrutis % 11

    # ja kui uuesti 10 siis 0
    if control_number == 10:
        control_number = 0


    # kontolli kas sai 6igesti
    id_last_nr = [int(x) for x in id_code].pop()
    if id_last_nr == control_number:
        return True
    else:
        return False


def get_data_from_id(id_code):
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

    gender_number = int(id_code[0])
    year = int(id_code[1:3])
    birth_date = str(id_code[5:7]) + "." + str(id_code[3:5]) + "." + str(get_full_year(gender_number, year))

    if check_your_id(id_code) is False:
        return "Given invalid ID code!"
    elif id_code[1] == 1 or id_code[1] == 3 or id_code[1] == 5:
        return "This is a" + get_gender(gender_number) + "born on" + birth_date + "."


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
def get_full_year(gender_number, year):
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
