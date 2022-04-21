import datetime


'''
This function convert a QuerySet to a Dict
@author Luis GP
@param QuerySet
@return Dict
'''
def queryset_to_json(queryset):
    json = []

    for i in queryset.values():
        for j in i.keys():
            i[j] = i[j].strftime("%d/%m/%Y") if isinstance(i[j], datetime.datetime) else i[j]

        json.append(i)

    return json





'''
This function clean de HTML code and retrn only the HTML code of the question
@author Luis GP
@param String
@return String
'''
def clean_description(description):

    description = str(description).replace('<pre class="ql-syntax"', '<pre class="pre-code"')
    description = description.replace('<div class="ql-clipboard" contenteditable="true" tabindex="-1"></div><div class="ql-tooltip ql-hidden"><a class="ql-preview" target="_blank" href="about:blank"></a><input type="text" data-formula="e=mc^2" data-link="https://quilljs.com" data-video="Embed URL"><a class="ql-action"></a><a class="ql-remove"></a></div>', "")
    description = description.replace('contenteditable="true"', '')
    description = description.replace('class="ql-editor"', '')

    return description