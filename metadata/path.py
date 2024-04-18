import os


class Path:

    folder = os.path.dirname(__file__)
    """Path principal del proyecto"""

    input_ = os.path.join(folder, '..', 'input')
    """Path con los datos de entrada"""

    out_ = os.path.join(folder, '..', 'output')
    """Path con los datos de salida"""

    templates = os.path.join(input_, 'templates_textfsm')
    """Path donde se encuentran los template textfsm"""

    bgp = os.path.join(templates, 'template_bgp.template')
    """Ruta del template bgp"""

    route_table = os.path.join(templates, 'template_route_table.template')
    """Ruta del template route table"""

    mpls_prelines = os.path.join(templates, 'template_mpls_prelines.template')
    """Ruta del template mlps prelines"""

    mpls_deteils = os.path.join(templates, 'template_mpls_deteils.template')
    """Ruta del template mlps deteils"""

    data = os.path.join(input_, 'comandos')
    """Path con el resultado del comando"""

    data_bgp = os.path.join(data, 'bgp.txt')
    """Data del comando"""

    data_route_table = os.path.join(data, 'route_table.txt')
    """Data del comando"""

    data_mpls_prelines = os.path.join(data, 'mpls_prelines.txt')
    """Data del comando"""

    data_mpls_deteils = os.path.join(data, 'mpls_deteils.txt')
    """Data del comando"""
