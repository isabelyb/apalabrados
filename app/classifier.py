

# db.NUMBERS.insert_one({'number': data})

# db.COLLECTION.insert_one({column:data})

#COLLECTION = collection
# column
# data


# def classifier():
#     input ={'pajarito':'gurrup%&%$leta'}
#     input_value = [value for value in input.values()]
#     string = input_value[0]
#     chars = [i for i in string]


#     print(chars)
#     data_to_save = f'db.COLLECTION.insert_one({input_value})'
#     return print(data_to_save)


# classifier()





data = '54$654%&589'


def accumulate():
    pass


if type(data) == int:
    accumulate()
    data_to_save = 'numbers'
    
elif data.isalnum() == False:
    #data_to_save = []
#    datas = [data_to_save.append(data[i]) for i in range(0, len(data)) if data[i].isalnum() == False]
    datas = ''.join([data[i] for i in range(0, len(data)) if data[i].isalnum() == False])
    #datas = ''.join(datas)


else:
    data_to_save = 'chars'


print(datas)

