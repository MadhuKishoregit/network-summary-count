from google.cloud import monitoring_v3
from google.api import metric_pb2 as ga_metric
from google.api import label_pb2 as ga_label

def create_custom_metric():
    client = monitoring_v3.MetricServiceClient()

    project_name = client.project_path("your-gcp-project-id")

    descriptor = ga_metric.MetricDescriptor()
    descriptor.type = "custom.googleapis.com/vpc_count"
    descriptor.metric_kind = ga_metric.MetricDescriptor.MetricKind.GAUGE
    descriptor.value_type = ga_metric.MetricDescriptor.ValueType.INT64
    descriptor.description = "VPC Count"
    descriptor.display_name = "VPC Count"

    label_descriptor = ga_label.LabelDescriptor()
    label_descriptor.key = "project_id"
    label_descriptor.value_type = ga_label.LabelDescriptor.ValueType.STRING
    label_descriptor.description = "ID of the GCP Project"

    descriptor.labels.append(label_descriptor)

    descriptor = client.create_metric_descriptor(name=project_name, metric_descriptor=descriptor)
    print("Created {}.".format(descriptor.name))

if __name__ == "__main__":
    create_custom_metric()
