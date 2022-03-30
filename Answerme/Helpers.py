import datetime

def queryset_to_json(queryset):
    json = []
    item = {}

    for i in queryset.values():
        for j in i.keys():
            i[j] = i[j].strftime("%d/%m/%Y") if isinstance(i[j], datetime.datetime) else i[j]

        json.append(i)

    return json