# db.NUMBERS.insert_one({'number': data})

# db.COLLECTION.insert_one({column:data})

#COLLECTION = collection
# column
# data


def classifier():
    input ={'pajarito':'gurrup%&%$leta'}
    input_value = [value for value in input.values()]
    string = input_value[0]
    chars = [i for i in string]


    print(chars)
    data_to_save = f'db.COLLECTION.insert_one({input_value})'
    return print(data_to_save)


classifier()

