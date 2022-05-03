import contextlib
import json
from typing import List


query=""" 
    SELECT
        `status_history`.`id`,
        `status_history`.`property_id`,
        `status_history`.`status_id`,
        `status_history`.`update_date`,
        `property`.`id`, 
        `property`.`address`,
        `property`.`city`,
        `property`.`price`,
        `property`.`description`,
        `property`.`year`,
        `status`.`id`,
        `status`.`name`,
        `status`.`label`
    FROM `status_history` INNER JOIN `status` ON (`status_history`.`status_id` = `status`.`id`)
    INNER JOIN `property` ON (`status_history`.`property_id` = `property`.`id`) WHERE `status`.`id` IN (3, 4, 5)
"""


long_query="""
    SELECT
        `status_history`.`id`,
        `status_history`.`property_id`,
        `status_history`.`status_id`,
        `status_history`.`update_date`,
        `property`.`id`, 
        `property`.`address`,
        `property`.`city`,
        `property`.`price`,
        `property`.`description`,
        `property`.`year`,
        `status`.`id`,
        `status`.`name`,
        `status`.`label`
    FROM `status_history` INNER JOIN `status` ON (`status_history`.`status_id` = `status`.`id`)
    INNER JOIN `property` ON (`status_history`.`property_id` = `property`.`id`)
    WHERE 
"""

VALID_FILTER_KEY = ['year','city','status']
VALID_KEY_STATUS = [3,4,5]

key_query_map = {
    'year': "`property`.`year`",
    'city': "`property`.`city`",
    'status':"`status`.`id`"
}

def query_in_numbers(string:str,list_query_numbers:str) -> str:
    """_This function only return a string to be added to 
        long query for filtration when a list is provided  
    _

    Args:
        string (str): _description_
        list_query_numbers (str): _description_

    Returns:
        str:  property.name in (list_query_numbers)
    """
    if isinstance(list_query_numbers,str):
        with contextlib.suppress(Exception):
            list_query_numbers = json.loads(list_query_numbers)
            
    list_query_numbers = [x for x in list_query_numbers if x in VALID_KEY_STATUS]
    final_str = ",".join(str(x) for x in list_query_numbers) if list_query_numbers else ''
    if final_str != '':
        return f"{string} IN ({final_str}) "
    return final_str

def get_queryset_raw(long_query:str,key_queries:List, query_params: List[object]) -> str:
    
    """ 
        This function return a string to concatante to long_query 
        only to add all parameters need for filtration to a RAW SQL
        
        This return something like : Where property.id=1  AND property.city=medellin 
    """
   
    flag_status = False
    cont = 0
    key_queries = [q for q in key_queries if q in key_query_map and query_params[q]]
    for key in key_queries:
        if key == 'status':
            if cont > 0 :
                long_query+=" AND "
            flag_status=True
            string = key_query_map['status']
            list_id = query_params['status']
            final_str = query_in_numbers(string,list_id)
            long_query +=final_str
        else:
            if flag_status is True:
                cont += 1
            if cont > 0 :
                long_query+=" AND "
            key_query=key_query_map[key]
            long_query+=key_query 
            long_query+="="
            long_query+=query_params[key] if key != 'city' else f"'{query_params[key]}'"
            cont += 1
    
    
    long_query +="ORDER BY  `property`.`year` DESC"
    return long_query  
            
    

    
    