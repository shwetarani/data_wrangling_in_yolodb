#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a
cleaning idea and then clean it up. In the first exercise we want you to audit
the datatypes that can be found in some particular fields in the dataset.

The possible types of values can be:
- NoneType if the value is a string "NULL" or an empty string ""
- list, if the value starts with "{"
- int, if the value can be cast to int
- float, if the value can be cast to float, but CANNOT be cast to int.
   For example, '3.23e+07' should be considered a float because it can be cast
   as float but int('3.23e+07') will throw a ValueError
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and a
SET of the types that can be found in the field. e.g.
{"field1: set([float, int, str]),
 "field2: set([str]),
  ....
}

All the data initially is a string, so you have to do some checks on the values
first.
"""
import sys
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'

FIELDS = ["name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode",
          "populationTotal", "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat",
          "wgs84_pos#long", "areaLand", "areaMetro", "areaUrban"]


def castable(input_string, input_type):
    try:
        return isinstance(input_type(input_string), input_type)
    except ValueError:
        return False

def audit_row(input_string):

    if input_string.startswith("{"):
        return list
    elif len(input_string) == 0 or input_string == "NULL":
        print("We return None for {}".format(input_string))
        return None
    elif castable(input_string, float):
        if castable(input_string, int):
            return int
        else:
            return float
    else:
        return str


def audit_file(filename, fields):
    fieldtypes = dict()
    # We create an empty set for each field proactively
    for field in FIELDS:
        fieldtypes[field] = set()

    # YOUR CODE HERE
    with open(filename, "r") as input_file:
        reader = csv.DictReader(input_file)
        header = reader.fieldnames
        for row in reader:
            for field in FIELDS:

                row_type_audit = audit_row(row[field])
                print("Field: {}\nRow value: {}\nAudit Type: {}\n".format(field, row[field], row_type_audit))
                #print("type(row)", type(row))
                #print(row[field])
                #fieldtypes[field].add(audit_row(row[field]))
        pprint.pprint(fieldtypes)
        sys.exit()


    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])


if __name__ == "__main__":
    test()
