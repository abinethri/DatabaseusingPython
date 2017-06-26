# a test file that retrieves the names,course titles and roles from json file
import json

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'roster_data_sample.json'

fh = open(fname)
str_data = fh.read()
print "Str_data: ", type(str_data)
json_data = json.loads(str_data)

print "Type of json_data:", type(json_data)
print "Length of json data list:", len(json_data)

user_name = list()
course_id = list()
role = list() 

for entry in json_data:
    user_name.append(str(entry[0]))
    course_id.append(str(entry[1]))
    role.append(entry[2])

print user_name
print course_id
print role
