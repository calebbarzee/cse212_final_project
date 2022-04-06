def main():
    """
    In the previous example we saw how sets are unordered and don't allow duplicates.
    In python you can think of the keys in a dictionary like a set, only they link to a value.
    The key must always be unique in a python dictionary, while there can be duplicate values.
    (As of Python 3.6 dictionaries are ordered, this is where the analogy breaks down a bit.)

    Try to use this concept to create a dictionary with all company employee ID's.
    Then find Caleb Barzee in the set of employees and remove him.
    """
    employee_id_list = [63273897,
                        56606641,
                        90673643,
                        60686942,
                        54207291,
                        67738108,
                        73425830,
                        81941762,
                        57233646,
                        70110851,
                        64047293,
                        13759397,
                        13898753, ]
    employee_name_list = ["Coby Parsons",
                          "Ayana Robles",
                          "Silas Clements",
                          "Wyatt Walter",
                          "Johanna Clarke",
                          "Madden Ball",
                          "Vaughn Taylor",
                          "Bianca Hancock",
                          "Makhi Armstrong",
                          "Tanner Mullins",
                          "Eden Lloyd",
                          "Clinton Carrell",
                          "Caleb Barzee"]

    employees = dict()
    # Use the update() method to add items to the dictionary.

    # Solution Code #
    for i in range(len(employee_id_list)):
        employees.update({employee_id_list[i]: employee_name_list[i]})
    print(employees)

    # Refer to a specific employee by key, then use the pop() method to remove both key and value.
    employees.pop(13898753)
    print(employees)


if __name__ == "__main__":
    main()
