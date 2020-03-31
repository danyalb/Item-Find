create table app (
	id BIGSERIAL NOT NULL PRIMARY KEY,
	store_lat VARCHAR(200) NOT NULL,
	store_long VARCHAR(200) NOT NULL,
    store_name VARCHAR(200) NOT NULL,
	area VARCHAR(150) NOT NULL,
	item VARCHAR(150) NOT NULL,
	if_there INTEGER NOT NULL
);
insert into app (store_lat,store_long,store_name,area,item,if_there) values ('42.352399','-71.123364', 'Star Market', 'Kitchen', 'Bread', '1');
insert into app (store_lat,store_long,store_name,area,item,if_there) values ('42.352399','-71.123364', 'Star Market', 'Kitchen', 'Bananas', '-1');
insert into app (store_lat,store_long,store_name,area,item,if_there) values ('42.352399','-71.123364', 'Star Market', 'Kitchen', 'Apple', '1');

insert into app (store_lat,store_long,store_name,area,item,if_there) values ('42.352399','-71.123364', 'Star Market', 'Bathroom', 'Towel', '1');
insert into app (store_lat,store_long,store_name,area,item,if_there) values ('42.352399','-71.123364', 'Star Market', 'Bathroom', 'Toilet', '1');
insert into app (store_lat,store_long,store_name,area,item,if_there) values ('42.352399','-71.123364', 'Star Market', 'Bathroom', 'Shampoo', '-1');


insert into app (store_lat,store_long,store_name,area,item,if_there) values ('42.342306','-71.120524', 'Trader Joes', 'Kitchen', 'Bread', '1');
insert into app (store_lat,store_long,store_name,area,item,if_there) values ('42.342306','-71.120524', 'Trader Joes', 'Kitchen', 'Bananas', '1');
insert into app (store_lat,store_long,store_name,area,item,if_there) values ('42.342306','-71.120524', 'Trader Joes', 'Kitchen', 'Apple', '1');

insert into app (store_lat,store_long,store_name,area,item,if_there) values ('42.342306','-71.120524', 'Trader Joes', 'Bathroom', 'Towel', '-1');
insert into app (store_lat,store_long,store_name,area,item,if_there) values ('42.342306','-71.120524', 'Trader Joes', 'Bathroom', 'Toilet', '-1');
insert into app (store_lat,store_long,store_name,area,item,if_there) values ('42.342306','-71.120524', 'Trader Joes', 'Bathroom', 'Shampoo', '-1');

