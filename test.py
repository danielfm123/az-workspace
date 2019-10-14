from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import ResourceManagementClient

compute_client = get_client_from_cli_profile(ComputeManagementClient)
network_client = get_client_from_cli_profile(NetworkManagementClient)
resource_client = get_client_from_cli_profile(ResourceManagementClient)

maquinas = compute_client.virtual_machines.list('DataArts')
for m in maquinas:
    if m.name == 'dfischer2':
        break


network_client.network_interfaces.get('DataArts','dfischer2235').as_dict()

ip = network_client.public_ip_addresses.get('DataArts','dfischer2-ip')
ip.as_dict()