import logging
from googleapiclient.discovery import build
from google.auth import default
from google.cloud import storage
import time
import logging
import warnings
from google.cloud import logging as cloud_logging

logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)
warnings.filterwarnings("ignore", category=DeprecationWarning)


# Configure logging to send logs to the console and a log sink
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Log to console
    ]
)

# Configure Cloud Logging
logging_client = cloud_logging.Client()
logger = logging_client.logger('network-summary')  # Replace with your desired logger name

# Configure Cloud Storage
storage_client = storage.Client()
bucket_name = 'metric-count'  
blob_name = 'vpn_tunnel_counts.txt'  

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

        # Log the VPN Tunnel count to Cloud Logging
        logger.log_text(f"VPN Tunnel Count in {target_project_id}: {vpn_tunnel_count}")

        # Log the VPN Tunnel count to the console
        logging.info(f"VPN Tunnel Count in {target_project_id}: {vpn_tunnel_count}")

        return vpn_tunnel_count

    except Exception as e:
        # Log the error to Cloud Logging
        logger.log_text(f"Error counting VPN Tunnels in {target_project_id}: {e}")

        # Log the error to the console
        logging.error(f"Error counting VPN Tunnels in {target_project_id}: {e}")
        return None

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

        # Log the VPC count to Cloud Logging
        logger.log_text(f"VPC Count in {target_project_id}: {vpc_count}")

        # Log the VPC count to the console
        logging.info(f"VPC Count in {target_project_id}: {vpc_count}")

        return vpc_count

    except Exception as e:
        # Log the error to Cloud Logging
        logger.log_text(f"Error counting VPCs in {target_project_id}: {e}")

        # Log the error to the console
        logging.error(f"Error counting VPCs in {target_project_id}: {e}")
        return None

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

        # Log the DNS Zone count to Cloud Logging
        logger.log_text(f"DNS Zone Count in {target_project_id}: {dns_zone_count}")

        # Log the DNS Zone count to the console
        logging.info(f"DNS Zone Count in {target_project_id}: {dns_zone_count}")

        return dns_zone_count

    except Exception as e:
        # Log the error to Cloud Logging
        logger.log_text(f"Error counting DNS Zones in {target_project_id}: {e}")

        # Log the error to the console
        logging.error(f"Error counting DNS Zones in {target_project_id}: {e}")
        return None

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

        # Log the Cloud Router count to Cloud Logging
        logger.log_text(f"Cloud Router Count in {target_project_id}: {cloud_router_count}")

        # Log the Cloud Router count to the console
        logging.info(f"Cloud Router Count in {target_project_id}: {cloud_router_count}")

        return cloud_router_count

    except Exception as e:
        # Log the error to Cloud Logging
        logger.log_text(f"Error counting Cloud Routers in {target_project_id}: {e}")

        # Log the error to the console
        logging.error(f"Error counting Cloud Routers in {target_project_id}: {e}")
        return None

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

        # Log the VPC Peering count to Cloud Logging
        logger.log_text(f"VPC Peering Count in {target_project_id}: {vpc_peering_count}")

        # Log the VPC Peering count to the console
        logging.info(f"VPC Peering Count in {target_project_id}: {vpc_peering_count}")

        return vpc_peering_count

    except Exception as e:
        # Log the error to Cloud Logging
        logger.log_text(f"Error counting VPC Peerings in {target_project_id}: {e}")

        # Log the error to the console
        logging.error(f"Error counting VPC Peerings in {target_project_id}: {e}")
        return None

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

        # Log the Firewall count to Cloud Logging
        logger.log_text(f"Firewall Count in {target_project_id}: {firewall_count}")

        # Log the Firewall count to the console
        logging.info(f"Firewall Count in {target_project_id}: {firewall_count}")

        return firewall_count

    except Exception as e:
        # Log the error to Cloud Logging
        logger.log_text(f"Error counting Firewalls in {target_project_id}: {e}")

        # Log the error to the console
        logging.error(f"Error counting Firewalls in {target_project_id}: {e}")
        return None

def count_private_service_access_ranges(target_project_id):
    """Counts Private Service Access Ranges in the target project and writes the count to the log."""
    try:
        # Authenticate with Google Cloud (using default credentials)
        credentials, project_id = default()

        # Build the Compute Engine service
        service = build('compute', 'v1', credentials=credentials)

        # List subnets in all regions for the target project
        request = service.subnetworks().aggregatedList(project=target_project_id)
        response = request.execute()

        # Count PSA subnets
        private_service_access_range_count = 0
        for region, subnets_scoped_list in response.get('items', {}).items():
            for subnet in subnets_scoped_list.get('subnetworks', []):
                if 'purpose' in subnet and subnet['purpose'] == 'PRIVATE_SERVICE_CONNECT':
                    private_service_access_range_count += 1

        # Log the Private Service Access Range count to Cloud Logging
        logger.log_text(f"Private Service Access Range Count in {target_project_id}: {private_service_access_range_count}")

        # Log the Private Service Access Range count to the console
        logging.info(f"Private Service Access Range Count in {target_project_id}: {private_service_access_range_count}")

        return private_service_access_range_count

    except Exception as e:
        # Log the error to Cloud Logging
        logger.log_text(f"Error counting Private Service Access Ranges in {target_project_id}: {e}")

        # Log the error to the console
        logging.error(f"Error counting Private Service Access Ranges in {target_project_id}: {e}")
        return None

def write_to_storage(data):
    """Writes the collected data to Cloud Storage."""
    try:
        blob = storage_client.bucket(bucket_name).blob(blob_name)
        blob.upload_from_string(data, content_type='text/plain')
    except Exception as e:
        logging.error(f"Error writing to Cloud Storage: {e}")

if __name__ == "__main__":
    # Define the projects you want to monitor
    projects = [
        'eighth-duality-429108-h0',
        'mgmt-hst-tst-8',
        'tfci-hst-tst-6'
    ]

    # Collect counts for all projects
    data = ""
    for project in projects:
        vpn_tunnel_count = count_vpn_tunnels(project)
        vpc_count = count_vpcs(project)
        dns_zone_count = count_dns_zones(project)
        cloud_router_count = count_cloud_routers(project)
        vpc_peering_count = count_vpc_peerings(project)
        firewall_count = count_firewalls(project)
        private_service_access_range_count = count_private_service_access_ranges(project)

        if all(
            [
                vpn_tunnel_count is not None,
                vpc_count is not None,
                dns_zone_count is not None,
                cloud_router_count is not None,
                vpc_peering_count is not None,
                firewall_count is not None,
                private_service_access_range_count is not None,
            ]
        ):
            data += (
                f"VPN Tunnel Count in {project}: {vpn_tunnel_count}\n"
                f"VPC Count in {project}: {vpc_count}\n"
                f"DNS Zone Count in {project}: {dns_zone_count}\n"
                f"Cloud Router Count in {project}: {cloud_router_count}\n"
                f"VPC Peering Count in {project}: {vpc_peering_count}\n"
                f"Firewall Count in {project}: {firewall_count}\n"
                f"Private Service Access Range Count in {project}: {private_service_access_range_count}\n"
            )
        else:
            logging.warning(f"Skipping project {project} due to errors during counting.")

        # Introduce a delay to avoid rate limiting
        time.sleep(1)  # Adjust the delay as needed

    # Write all counts to Cloud Storage in a single operation
    write_to_storage(data)
