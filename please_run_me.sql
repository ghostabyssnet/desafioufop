# Creates a temporary user for the project (I suppose UFOP has its own admin users already)
# You can also do this manually, your call.

create schema UFOP
create user tempdelete identified by ‘temp123’;
grant all on ufop.* to ‘dbadmin’@’%’;
flush privileges;
