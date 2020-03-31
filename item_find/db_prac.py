import psycopg2
from helper import unique
from database import create_new_store
# function to get unique values 

#connect to the db
con = psycopg2.connect(
            host = "localhost",
            database="app",
            user = "danya",
            password="khairpuri",
            port=5432)

cur = con.cursor()

name = 'Target'
location = [42.350903, -71.114086]
slat = str(location[0])
slong = str(location[1])
com_str = "SELECT * FROM app WHERE store_lat='"+slat+"' AND store_long='"+slong+"';"
cur.execute(com_str)

#cur.execute("SELECT * FROM app")
rows = cur.fetchall()

if rows==[]:
    rows = create_new_store(cur,name,slat,slong)


area = []
for r in rows:
    area.append(r[4])
    print(r)

area,ind = unique(area)
#print(area)
#print(ind)

con.commit()
cur.close()
con.close()


# <article class="media content-section">
#     <div class="media-body">
#       <p class="article-content">{{ r }}</p>
#     </div>
# </article>

# cur.execute("insert into app (store_id,store_name,area,item,if_there) values ('42.350903-71.114086', 'Target', 'bathroom', 'towel', '0'); \
#             insert into app (store_id,store_name,area,item,if_there) values ('42.350903-71.114086', 'Target', 'bathroom', 'toilet', '0'); \
#             insert into app (store_id,store_name,area,item,if_there) values ('42.350903-71.114086', 'Target', 'bathroom', 'shampoo', '1');")


#starmarket 42.352399, -71.123364   '42.352399-71.123364'
#trader joes 42.342306, -71.120524   '42.342306-71.120524'
#target 42.350903, -71.114086      '42.350903-71.114086'

