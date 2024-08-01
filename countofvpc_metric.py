from google.cloud import monitoring_v3
from google.api import metric_pb2 as ga_metric
from google.api import label_pb2 as ga_label
from googleapiclient.discovery import build
from google.auth import default
from google.protobuf.timestamp_pb2 import Timestamp

def create_custom_metric():
    """Creates a custom metric for VPC count in Cloud Monitoring."""
    try:
        # Authenticate with Google Cloud
        credentials, project_id = default()

        # Create the Monitoring client
        client = monitoring_v3.MetricServiceClient()
        project_name = f"projects/{project_id}"  # Corrected line

        # Construct the MetricDescriptor
        descriptor = ga_metric.MetricDescriptor(
            type="custom.googleapis.com/vpc_count",
            metric_kind=ga_metric.MetricDescriptor.MetricKind.GAUGE,
            value_type=ga_metric.MetricDescriptor.ValueType.INT64,
            description="VPC Count in the project",
            display_name="VPC Count",
            labels=[
                ga_label.LabelDescriptor(
                    key="project_id",
                    value_type=ga_label.LabelDescriptor.ValueType.STRING,
                    description="ID of the GCP Project"
                )
            ]
        )

        # Create the metric descriptor
        descriptor = client.create_metric_descriptor(name=project_name, metric_descriptor=descriptor)
        print(f"Created custom metric: {descriptor.name}")

    except Exception as e:
        print(f"Error creating custom metric: {e}")

def count_vpcs():
    """Counts VPCs in the project and writes the count to the custom metric."""
    try:
        # Authenticate with Google Cloud
        credentials, project_id = default()

        # Build the Compute Engine service
        service = build('compute', 'v1', credentials=credentials)

        # List VPCs in the project
        response = service.networks().list(project=project_id).execute()
        vpc_count = len(response.get('items', []))

        # Create the Monitoring client
        client = monitoring_v3.MetricServiceClient()
        project_name = f"projects/{project_id}"  # Corrected line

        # Prepare the custom metric data
        series = monitoring_v3.TimeSeries()
        series.metric.type = "custom.googleapis.com/vpc_count"  # Your custom metric type
        series.resource.type = "global"

        # Initialize the point and interval
        point = monitoring_v3.Point()
        point.value.int64_value = vpc_count

        # Get the current time
        now = Timestamp()
        now.GetCurrentTime()

        # Set the same start and end time for gauge metric
        interval = monitoring_v3.TimeInterval(end_time=now, start_time=now)
        point.interval = interval

        # Append the point to the series
        series.points.append(point)

        # Send the data to Cloud Monitoring
        client.create_time_series(name=project_name, time_series=[series])

        print(f"VPC Count: {vpc_count}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_custom_metric()  # Create the custom metric first
    count_vpcs()  # Then count VPCs and write to the metric
