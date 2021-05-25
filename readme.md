This services for loylty bonus programms.

Service bonus API:
all API work for authenticated users.

  for admin:
    users/ - show users list all information;
    users/<int:pk> - show user all information by id;

  user:
    balance/ - show balance for user;
    operations/ - show list all operations with bonuses for user;
    operations/<int:pk> - show operation with bonuses for user by id;
