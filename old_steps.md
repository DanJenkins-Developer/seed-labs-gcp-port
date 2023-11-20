Steps for creating vm from seed labs image:



2. Download the Seedlabs .vmdk image from https://storage.cloud.google.com/seed-labs-bucket/seed-labs-ubuntu.vmdk
3. Upload the .vmdk image to a bucket via the Cloud Storage API at https://cloud.google.com/storage 
4. Create an image in Compute Engine and use the .vmdk file as the source. You will have to select it from the bucket you just uploaded to. Name this image "seed-labs-ubuntu".
5. Activate Cloud Shell and set current project with "gcloud config set project PROJECT_ID"
6. git clone https://github.com/DanJenkins-Developer/seedlabs-cloud-port.git into your prefered directory
7. Run "terraform init" to add the necessary plugins and build the .terraform directory.
8. Run "terraform plan" to verrify syntx
9. Run "terraform apply" to create the VM.
