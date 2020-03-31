def create_new_store(cur,name,slat,slong):
    
    com_add = "insert into app (store_lat,store_long,store_name,area,item,if_there) values ('"+slat+"','"+slong+"', '"+name+"', 'Bathroom', 'Towel', '0'); \
                insert into app (store_lat,store_long,store_name,area,item,if_there) values ('"+slat+"','"+slong+"', '"+name+"', 'Bathroom', 'Toilet', '0'); \
                insert into app (store_lat,store_long,store_name,area,item,if_there) values ('"+slat+"','"+slong+"', '"+name+"', 'Bathroom', 'Shampoo', '0');"
    cur.execute(com_add)

    com_str = "SELECT * FROM app WHERE store_lat='"+slat+"' AND store_long='"+slong+"';"
    cur.execute(com_str)
    rows = cur.fetchall()
    return rows

def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
    ind = []
    # traverse for all elements 
    for ii,x in enumerate(list1): 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
            ind.append(ii)
    return unique_list, ind

def database_retrieve(name,location):

    import psycopg2

    #connect to the db
    con = psycopg2.connect(
                host = "localhost",
                database="app",
                user = "danya",
                password="khairpuri",
                port=5432)

    cur = con.cursor()

    slat = str(location[0])
    slong = str(location[1])
    com_str = "SELECT * FROM app WHERE store_lat='"+slat+"' AND store_long='"+slong+"';"
    cur.execute(com_str)

    rows = cur.fetchall()

    if rows==[]:
        rows = create_new_store(cur,name,slat,slong)

    area = []
    for r in rows:
        area.append(r[4])    

    area,ind = unique(area)

    con.commit()
    cur.close()
    con.close()

    return rows, area









