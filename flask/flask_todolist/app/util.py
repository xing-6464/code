def database_to_dict(database):
    data = []
    for d in database:
        map = {}
        map['ID'] = d.ID
        map['title'] = d.title
        map['isEdit'] = d.isEdit
        map['isDone'] = d.isDone
        data.append(map)

    return data
