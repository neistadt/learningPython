import pkg_resources


def resource(name):
    resource_package = __name__
    resource_path = '/'.join(('..', 'resources', name))
    return pkg_resources.resource_stream(resource_package, resource_path)
