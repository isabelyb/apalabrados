

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





data = '54654589'


def accumulate():
    pass
    #GET THE LAST OBJECT_ID in MONGO
    #db.dataset2.find().sort( {'_id': -1 } ).limit(1); WRONG (TypeError: if no direction is specified, key_or_list must be an instance of the list)
    #db.demo141.find().sort({_id:-1}).limit(1);
    #db.dataset2.find().sort('_id', pymongo.DESCENDING).limit(1)[0]['_id'];
    #db.dataset2.find().sort('_id', -1).limit(1)[0]['_id'];
    
    # obtain number
    # sum number
    # return acummulated

if type(data) == int:
    accumulate()
    data_to_save = 'numbers'
    
elif data.isalnum() == False:
    data_to_save = 'special_char'
    #save_input()
else:
    data_to_save = 'chars'
    # save data[0] in initial
    #save data[-1] in final


print(data_to_save)




    # print(chars)
    # data_to_save = f'db.COLLECTION.insert_one({input_value})'
    # return print(data_to_save)


#{"_id":{"$oid":"616a13b8546f11ba27b9069d"},"number":{"$numberInt":"999"}}