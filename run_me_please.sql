# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# UNCOMMENT when pushing to prod
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Creates a temporary user for the project (I suppose UFOP has its own admin users already)
# -----------------------------------------------

# create user tempdelete identified by ‘temp123’;
# grant all on ufop.* to ‘dbadmin’@’%’;
# flush privileges;

# !!!!!!!!!!!!!!!
# UNCOMMENT ABOVE
# !!!!!!!!!!!!!!!

# TODO: dont forget to delete this and put the database/schema in my project's folder
# if it doesnt work: CREATE SCHEMA 'ufop';