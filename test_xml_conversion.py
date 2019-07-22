import xml.etree.ElementTree as ET


#dic = {'tag' : 'Key-value pair','value' : 'total amount due','key' : '123456'}

a1 = [{'parent' : {'tag' : 'Key-value pair','value' : 'total amount due','key' : '123456'},
     'child' : [{'tag':'Key-value pair','value':'total due','key':'987654'} , {'tag':'Standalone','value':'something','key':'942064'}]}]



#Master : [{'parent': {'key': '"total amount due"', 'value': '"$129.23"', 'tag': 'Total Amount Due'}, 'child': [{'key': '"total due"', 'value': '"$129.23"', 'tag': 'Total Due'}, {'key': '"previous balance"', 'value': '"141.07"', 'tag': 'Previous Balance'}, {'key': '"date due"', 'value': '"02/09/08"', 'tag': 'Date Due'}]}]





#print(a1)


for relation in a1 :
    rel_parent = relation['parent']
    rel_children = relation['child']

    par_tag = rel_parent['tag']
    #p = ''

    if(par_tag == 'Key-value pair') :
        par_key = rel_parent['key']
        par_value = rel_parent['value']
        #p = 'txtNode key=' + str(par_key) + ' value=' + str(par_value) + ' tags=' + str(par_tag)
        a = ET.Element('textNode')
        a.set('key', par_key)
        a.set('value',par_value)
        a.set('tags',par_tag)
    elif((par_tag == 'Standalone') or (par_tag == 'Key-value pair')) :
        par_value = rel_parent['value']
        #p = 'txtNode value=' + str(par_value) + ' tags=' + str(par_tag)
        a = ET.Element('textNode')
        a.set('value', par_value)
        a.set('tags',par_tag)

    #a = ET.Element(p).set('Status','Completed')


    for child in rel_children :
        #c = ''

        child_tag = child['tag']
        if(child_tag == 'Key-value pair') :
            child_key = child['key']
            child_value = child['value']
            #c = 'txtNode key=' + str(child_tag) + ' value=' + str(child_value) + ' tags=' + str(child_tag)
            b = ET.SubElement(a, 'textNode')
            b.set('key', child_key)
            b.set('value', child_value)
            b.set('tags', child_tag)

        elif((child_tag == 'Standalone') or (child_tag == 'Key-value pair')) :
            child_value = child['value']
            #c = 'txtNode value=' + str(child_value) + ' tags=' + str(child_tag)
            b = ET.SubElement(a, 'textNode')
            b.set('value', child_value)
            b.set('tags', child_tag)




    ET.dump(a)









