import logging
import config


def is_admin(config, user_id: int, log_no_admin=False) -> bool:
    """
    Checks if the user is the admin of the bot.
    The first user in the user list is the admin.
    """
    if config.admin_user_ids == '-':
        if log_no_admin:
            logging.info('No admin user defined.')
        return False

    admin_user_ids = config.admin_user_ids.split(',')

    # Check if user is in the admin user list
    if str(user_id) in admin_user_ids:
        return True

    return False