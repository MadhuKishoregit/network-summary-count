from google.cloud import monitoring_v3

def delete_custom_metrics(project_id):
    """Deletes all custom metrics in the specified project."""
    try:
        # Authenticate with Google Cloud
        client = monitoring_v3.MetricServiceClient()
        project_name = f"projects/{project_id}"

        # List all custom metrics
        for descriptor in client.list_metric_descriptors(name=project_name):
            # Check if the metric type starts with "custom.googleapis.com/"
            if descriptor.type.startswith("custom.googleapis.com/"):
                # Delete the custom metric
                client.delete_metric_descriptor(name=descriptor.name)
                print(f"Deleted custom metric: {descriptor.name}")

    except Exception as e:
        print(f"Error deleting custom metrics: {e}")

if __name__ == "__main__":
    project_id = "eighth-duality-429108-h0"  # Replace with your project ID
    delete_custom_metrics(project_id)
