from django_q.tasks import async, result


def sync_server_pull(user_id, server_id, technique):
    """Pull new information from a remote MISP server.

    user_id: user with permission to sync
    server_id: remote server config
    technique: either 'full' or 'incremental' but only 'full' is implemented atm.
    """
    pass


def sync_server_push(user_id, server_id):
    pass