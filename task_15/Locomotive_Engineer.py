
def get_list_of_wagons(*args):
    """Return a list of wagons.
 
    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [el for el in args if el > 0 and el % 1 == 0]
  
def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.
 
    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    each_wagons_id = each_wagons_id[2:] + each_wagons_id[0:2]
    return each_wagons_id[:1] + missing_wagons[0:] + each_wagons_id[1:]
  
def add_missing_stops(self, **kwargs):
    """Add missing stops to route dict.
 
    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    list_ = []
    for el in kwargs.values():
        list_.append(el)
    self["stops"] = list_
    return self
  
def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.
 
    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    new_route = route | more_route_information
    return new_route
  
def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.
 
    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    new_list = []
    [*content] = zip(wagons_rows[0], wagons_rows[1], wagons_rows[2])
    for el in content:
      new_list.append(list(el))
    return new_list
