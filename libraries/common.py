
class Utils():

    def cleanse_data(self, data):
        date_list = []
        price_list = []
        for item in data:
            x = item.split('\n')
            if len(x) > 1:
                date_list.append(x[0])
                price_list.append(x[1])
            else:
                date_list.append(x[0])
                price_list.append(x[0])
        return date_list, price_list


    def find_min_value_index(self, data):
        """
        This function finds the minumum value from the given list
        :param data: list of data
        :return: minimum value, list of indexes contains minimum valuue
        """
        smallest = min(data)
        return smallest, [index for index, element in enumerate(data)
                        if smallest == element]


    def process_data(self, data):
        """
        This function reads the data provided and process it into required fashion
        :param data: data list
        :return: list which doesnt contains weekend and blank data
        """
        outer_list = []
        inner_list = []
        inner_list_without_empty_data = []
        final_list = []
        memory_count = 0
        counter = 0
        while len(data) > 0:
            for index, pos in enumerate(range(memory_count, len(data))):
                counter += 1
                inner_list.append(data[pos])
                if (index == 6) or (counter == len(data)):
                    if len(inner_list) == 7:
                        inner_list = inner_list[1:-1]
                    else:
                        inner_list = inner_list[1:]
                    for val in inner_list:
                        if val != '':
                            inner_list_without_empty_data.append(val)
                    outer_list.append(inner_list_without_empty_data)
                    inner_list = []
                    inner_list_without_empty_data = []
                    memory_count = pos + 1
                    break
            if len(data) == counter:
                break
        for val in outer_list:
            final_list.extend(val)
        return final_list
