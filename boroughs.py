#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 13 Warmup Task 01 module"""


import json


GRADES = {
    'A': 1.00,
    'B': .90,
    'C': .80,
    'D': .70,
    'F': .60
    }


def get_score_summary(filename):
    """Open and read a CSV file found on the local filesystem and return a
        summarized version of the data in dictionary.

    Args:
        filename(string): The filename whose data will be read and interpreted.

    Returns:
        dictionary: A dictionary with the boro-average score from NYC Restaurant
        Inspection data.

    Examples:

        >>> get_score_summary('inspection_results.csv')
        {'BRONX': (156, 0.9762820512820514), 'BROOKLYN': (417, 0.974580335731414
        1), 'STATEN ISLAND': (46, 0.9804347826086955), 'MANHATTAN': (748, 0.9771
        390374331531), 'QUEENS': (414, 0.9719806763285017)}

    """
    newdict = {}
    newdict2 = {}
    newdict3 = {}

    fhandler = open(filename, 'r')
    templine = fhandler.readline()

    for line in fhandler:
        templine = line.split(',')
        camis_id = templine[0]

        if newdict.get(camis_id, None):
            pass
        else:
            boro = templine[1]
            grade = templine[10]
            if grade != '' and grade != 'P':
                newdict[camis_id] = [boro, grade]

    fhandler.close()

    for value in newdict.itervalues():
        boro_temp = value[0]
        grade_temp = value[1]
        grade_convert = GRADES[grade_temp]

        if newdict2.get(boro_temp, None):
            temp_count = newdict2[boro_temp][0] + 1
            newdict2[boro_temp][0] = temp_count
            temp_total = newdict2[boro_temp][1] + grade_convert
            newdict2[boro_temp][1] = temp_total
        else:
            newdict2[boro_temp] = [1, grade_convert]

    for key, value2 in newdict2.iteritems():
        count = value2[0]
        avg_score = value2[1] / count
        newdict3[key] = (count, avg_score)

    return newdict3


def get_market_density(filename):
    """Open and read a JSON file found on the local filesystem and return a
        summarized version of the data in dictionary.

    Args:
        filename(string): The filename whose data will be read and interpreted.

    Returns:
        dictionary: A dictionary with the count of green markets per borough.

    Examples:

        >>> get_market_density('green_markets.json')
        {u'BRONX': 32, u'BROOKLYN': 48, u'STATEN ISLAND': 2, u'MANHATTAN': 39,
        u'QUEENS': 16}

    """
    greendict = {}

    fhandler = open(filename, 'r')
    mydata = json.load(fhandler)
    fhandler.close()

    newdata = mydata['data']

    for line in newdata:
        boro_temp = line[8].upper().rstrip()
        if greendict.get(boro_temp, None):
            temp_count = greendict[boro_temp] + 1
            greendict[boro_temp] = temp_count
        else:
            greendict[boro_temp] = 1

    return greendict
