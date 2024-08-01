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

if __name__ == "__main__":
    # Get all projects from the GCP
    client = resourcemanager_v3.ProjectsClient()

    # Listing all projects (without parent)
    projects = [project.project_id for project in client.list_projects()]

    # Filter projects based on "hst-tst" prefix
    filtered_projects = [project for project in projects if "hst-tst" in project]

    for project in filtered_projects:
        count_vpn_tunnels(project)  # Count VPN Tunnels in each project
