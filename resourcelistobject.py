import boto3
# Resources represent an object-oriented interface to AWS. They provide a
# higher-level abstraction than the raw, low-level calls made by service clients
s3resource = boto3.resource('s3')

bucket = s3resource.Bucket('course-demo-mybucket')

# in this case you do not have to make a second API call to get the objects; they're available to you as a collection on the bucket.
# These collections of sub-resources are lazily-loaded.
for object in bucket.objects.all():
    print(object.key, object.last_modified)