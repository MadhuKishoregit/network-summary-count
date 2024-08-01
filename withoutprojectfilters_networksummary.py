import logging
from googleapiclient.discovery import build
from google.auth import default
from google.cloud import storage
from google.cloud import resourcemanager_v3

# Configure logging to send logs to the console and a log sink
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to console
    ]
)

# Configure Cloud Storage
storage_client = storage.Client()
bucket_name = 'metric-count'  # Replace with your Cloud Storage bucket name
blob_name = 'vpn_tunnel_counts.txt'  # Replace with your desired blob name

def count_vpn_tunnels(target_project_id):
    """Counts VPN Tunnels in the target project and writes the count to the log."""
    try:
        # Authenticate with Google Cloud (using default credentials)
        credentials, project_id = default()

        # Build the Compute Engine service
        service = build('compute', 'v1', credentials=credentials)

        # Specify the region for VPN Tunnels
        region = 'us-central1'  # Replace with your actual region

        # List VPN Tunnels in the target project and region
        response = service.vpnTunnels().list(project=target_project_id, region=region).execute()
        vpn_tunnel_count = len(response.get('items', []))

        # Log the VPN Tunnel count to the console
        logging.info(f"VPN Tunnel Count in {target_project_id}: {vpn_tunnel_count}")

        # Write the VPN Tunnel count to Cloud Storage
        blob = storage_client.bucket(bucket_name).blob(blob_name)
        blob.upload_from_string(f"VPN Tunnel Count in {target_project_id}: {vpn_tunnel_count}\n",
                                 content_type='text/plain')

    except Exception as e:
        # Log the error to the console
        logging.error(f"Error counting VPN Tunnels in {target_project_id}: {e}")

def count_vpcs(target_project_id):
    """Counts VPCs in the target project and writes the count to the log."""
    try:
        # Authenticate with Google Cloud (using default credentials)
        credentials, project_id = default()

        # Build the Compute Engine service
        service = build('compute', 'v1', credentials=credentials)

        # List VPCs in the target project
        response = service.networks().list(project=target_project_id).execute()
        vpc_count = len(response.get('items', []))

        # Log the VPC count to the console
        logging.info(f"VPC Count in {target_project_id}: {vpc_count}")

        # Write the VPC count to Cloud Storage
        blob = storage_client.bucket(bucket_name).blob(blob_name)
        blob.upload_from_string(f"VPC Count in {target_project_id}: {vpc_count}\n",
                                 content_type='text/plain')

    except Exception as e:
        # Log the error to the console
        logging.error(f"Error counting VPCs in {target_project_id}: {e}")

def count_dns_zones(target_project_id):
    """Counts DNS Zones in the target project and writes the count to the log."""
    try:
        # Authenticate with Google Cloud (using default credentials)
        credentials, project_id = default()

        # Build the DNS service
        service = build('dns', 'v1', credentials=credentials)

        # List DNS Zones in the target project
        response = service.managedZones().list(project=target_project_id).execute()
        dns_zone_count = len(response.get('managedZones', []))

        # Log the DNS Zone count to the console
        logging.info(f"DNS Zone Count in {target_project_id}: {dns_zone_count}")

        # Write the DNS Zone count to Cloud Storage
        blob = storage_client.bucket(bucket_name).blob(blob_name)
        blob.upload_from_string(f"DNS Zone Count in {target_project_id}: {dns_zone_count}\n",
                                 content_type='text/plain')

    except Exception as e:
        # Log the error to the console
        logging.error(f"Error counting DNS Zones in {target_project_id}: {e}")

def count_cloud_routers(target_project_id):
    """Counts Cloud Routers in the target project and writes the count to the log."""
    try:
        # Authenticate with Google Cloud (using default credentials)
        credentials, project_id = default()

        # Build the Compute Engine service
        service = build('compute', 'v1', credentials=credentials)

        # Specify the region for Cloud Routers
        region = 'us-central1'  # Replace with your actual region

        # List Cloud Routers in the target project and region
        response = service.routers().list(project=target_project_id, region=region).execute()
        cloud_router_count = len(response.get('items', []))

        # Log the Cloud Router count to the console
        logging.info(f"Cloud Router Count in {target_project_id}: {cloud_router_count}")

        # Write the Cloud Router count to Cloud Storage
        blob = storage_client.bucket(bucket_name).blob(blob_name)
        blob.upload_from_string(f"Cloud Router Count in {target_project_id}: {cloud_router_count}\n",
                                 content_type='text/plain')

    except Exception as e:
        # Log the error to the console
        logging.error(f"Error counting Cloud Routers in {target_project_id}: {e}")

def count_vpc_peerings(target_project_id):
    """Counts VPC Peerings in the target project and writes the count to the log."""
    try:
        # Authenticate with Google Cloud (using default credentials)
        credentials, project_id = default()

        # Build the Compute Engine service
        service = build('compute', 'v1', credentials=credentials)

        # List VPC Peerings in the target project
        response = service.globalAddresses().list(project=target_project_id).execute()
        vpc_peering_count = len(response.get('items', []))

        # Log the VPC Peering count to the console
        logging.info(f"VPC Peering Count in {target_project_id}: {vpc_peering_count}")

        # Write the VPC Peering count to Cloud Storage
        blob = storage_client.bucket(bucket_name).blob(blob_name)
        blob.upload_from_string(f"VPC Peering Count in {target_project_id}: {vpc_peering_count}\n",
                                 content_type='text/plain')

    except Exception as e:
        # Log the error to the console
        logging.error(f"Error counting VPC Peerings in {target_project_id}: {e}")

def count_firewalls(target_project_id):
    """Counts Firewalls in the target project and writes the count to the log."""
    try:
        # Authenticate with Google Cloud (using default credentials)
        credentials, project_id = default()

        # Build the Compute Engine service
        service = build('compute', 'v1', credentials=credentials)

        # List Firewalls in the target project
        response = service.firewalls().list(project=target_project_id).execute()
        firewall_count = len(response.get('items', []))

        # Log the Firewall count to the console
        logging.info(f"Firewall Count in {target_project_id}: {firewall_count}")

        # Write the Firewall count to Cloud Storage
        blob = storage_client.bucket(bucket_name).blob(blob_name)
        blob.upload_from_string(f"Firewall Count in {target_project_id}: {firewall_count}\n",
                                 content_type='text/plain')

    except Exception as e:
        # Log the error to the console
        logging.error(f"Error counting Firewalls in {target_project_id}: {e}")

def count_private_service_access_ranges(target_project_id):
    """Counts Private Service Access Ranges in the target project and writes the count to the log."""
    try:
        # Authenticate with Google Cloud (using default credentials)
        credentials, project_id = default()

        # Build the Service Networking service
        service = build('servicenetworking', 'v1', credentials=credentials)

        # List Private Service Access Ranges in the target project
        response = service.services().list(parent=f"projects/{target_project_id}").execute()
        private_service_access_range_count = len(response.get('services', []))

        # Log the Private Service Access Range count to the console
        logging.info(f"Private Service Access Range Count in {target_project_id}: {private_service_access_range_count}")

        # Write the Private Service Access Range count to Cloud Storage
        blob = storage_client.bucket(bucket_name).blob(blob_name)
        blob.upload_from_string(f"Private Service Access Range Count in {target_project_id}: {private_service_access_range_count}\n",
                                 content_type='text/plain')

    except Exception as e:
        # Log the error to the console
        logging.error(f"Error counting Private Service Access Ranges in {target_project_id}: {e}")

if __name__ == "__main__":
    # Define the projects you want to monitor
    projects = [
        'eighth-duality-429108-h0',
        'mgmt-hst-tst-8',
        'tfci-hst-tst-6'
    ]

    for project in projects:
        count_vpn_tunnels(project)  # Count VPN Tunnels in each project
        count_vpcs(project)  # Count VPCs in each project
        count_dns_zones(project)  # Count DNS Zones in each project
        count_cloud_routers(project)  # Count Cloud Routers in each project
        count_vpc_peerings(project)  # Count VPC Peerings in each project
        count_firewalls(project)  # Count Firewalls in each project
        count_private_service_access_ranges(project)  # Count Private Service Access Ranges in each project
