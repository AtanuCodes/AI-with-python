from functools import wraps

def require_admin(func):
    @wraps(func)
    def admin_auth(user_role):
        if user_role != 'admin':
            print('Access Denied!')
            return None
        else:
            print('Access Granted!')
            return user_role
    return admin_auth

@require_admin

def tea_inventory(role):
    print(f'Accessing tea inventory with role: {role}')

tea_inventory('user')
tea_inventory('admin')

# tea_inventory = require_admin(tea_inventory)
# print(tea_inventory('user'))
# print(tea_inventory('admin'))
