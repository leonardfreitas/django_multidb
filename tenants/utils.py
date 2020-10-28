from django.db import connection


def hostname_from_request(request):
    # split on `:` to remove port
    return request.get_host().split(":")[0].lower()


def tenant_db_from_request(request):
    # get hostname
    hostname = hostname_from_request(request)
    # get map of tenants
    tenants_map = get_tenants_map()
    # verify if hostname have tenant
    if tenants_map.get(hostname, False):
        # return tenant
        return tenants_map.get(hostname)
    else:
        return False


def get_tenants_map():
    return {
        "store.localhost": "store",
        "leonardo.localhost": "leonardo",
    }
