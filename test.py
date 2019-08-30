from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient

compute_client = get_client_from_cli_profile(ComputeManagementClient)
network_client = get_client_from_cli_profile(NetworkManagementClient)

maquinas = compute_client.virtual_machines.list('DataArts')
for m in maquinas:
    print(m.name)
