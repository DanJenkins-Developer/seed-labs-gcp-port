# Automating the creation of SEED lab VMs in GCP via Cloud Shell

This document provides instructions on configuring your GCP cloud environment to run preconfigured SEED lab VMs. Original instructions for creating a SEED lab VM in the Cloud were provided by kevin-w-du on [Github](https://github.com/seed-labs/seed-labs/blob/master/manuals/cloud/seedvm-cloud.md). 

Following the instructions, (minus the firewall rules since these are created via terraform later) I made an initial VM in GCP, ran the provided startup script, enabled ssh password authentication for the seed user (vnc is also enabled technically, see issues section). Then I created the image using this VM as the source disk. 

The the `main.tf` file automates setting up a Seed Labs VM from an image of VM created above (see the `boot_disk` block in the `google_compute_instance` resource). It also sets up a VNC (`google_compute_network` resource) and firewall rules for a VNC and SSH (`google_compute_firewall` resource). These (Google Cloud Docs)[https://cloud.google.com/docs/terraform/get-started-with-terraform] helped me set up the VPC and Subnet.

Keep in mind Our ultimate goal project is to convert this setup to be used in Apache CloudStack. At this point configuration takes place within GCP and the terraform file is ran inside the cloud shell. There is a configuration using the ("provider" resource)[https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/google-cloud-platform-build] which would allow this setup to be ran from a local envrionment (as opposed to directly cloud shell), but this is an easy switch and doesn't matter for now. 

A basic use case for this terraform set up could go like this:
```
1. User clicks start lab (in vscode extension, web interface, whatever), the terraform config runs and creates a vm, vpc, and subnet for that user's new vm.
2. Same user or different user wants to create another lab.
```
The way terraform works, you don't simply destroy the existing configuration and apply a new vm instance, vpc, subnet, etc. That would disrupt any other user's current VMs. Each terraform file sets up one infrastructure (there's probably a more elegant way to put that, but I don't know all the terminology right now). Meaning, each time a new lab is required a separate infrastructure must be set up. That is the purpose of `main.py` which will eventually create a new directory for each lab a user wants to run and be able to configure the resources in a unique way. So don't mind `main.py` for now, stick to the /init_vm directory. This means you'll only be able to set up one vm at a time for now (should be fine for testing maybe) unless you physically copy the terraform files to a separate directory.

## Step 1: Download custom SEED labs image

First download the custom SEED labs image we created onto your local machine. See me for image or check discord (CSCI 422 people)

## Step 2: Upload the .vmdk image to a bucket via the Cloud Storage API

- [Cloud Storage API](https://cloud.google.com/storage)

In order to create an image in Compute Engine from the .vmdk file it has to be stored in a bucket first within GCP. 

## Step 3  Create an image in Compute Engine

Go to images in Compute Engine and click the create image button. Choose the .vmdk file as the source. You will have to select it from the bucket you just uploaded it to. Name this image "seed-labs-ubuntu" (or just make sure the name of the image matches whatever you have in main.tf) so that it is the same as the boot disk parmeter in the terraform file.

## Step 4 Clone this repository in Cloud Shell and run start_terraform_script.sh 

```
git clone https://github.com/DanJenkins-Developer/seed-labs-gcp-port.git
```
Change directories into the /create_from_image directory
```
cd ~/seed-labs-gcp-port/init_vm
```
Make the script executable and run it
```
chmod +x start_terraform_script.sh
./start_terraform_script.sh
```

It will take a bit for the VM to start, maybe 4-5 minutes. After it starts you may need to give it another 1-2 minutes to be able to actually SSH into the seed user (just try a couple times, should work eventually). 
## Step 5 Log in to the new Seed Labs VM

Navigate back to your VM instaces and you should see one called "custom-instance.." Log in via SSH using putty or whatever client you like with the following credentials:
```
 Username: `seed` 
 Password `dees`
```

## Issues

- VNC probably won't work right now. I've noticed that it will work on inital setup of a Seed Labs VM, but if you 1) stop the vm and then start if again or 2) create a Seed Labs VM from the image it won't.

## Notes

The hardest part of this set up is uploading the image to GCP via the bucket method described above, but we won't have to do this everytime once we have the image in cloudstack.

It seems like converting from a GCP to CloudStack terraform config might be pretty easy. Just look at this [article](https://www.shapeblue.com/automating-infrastructure-with-cloudstack-and-terraform/) on Automating Infrastructure with CloudStack and Terraform. Seems like all the resources we are using in the configs currently have equivilents in cloud stack. 

It will most likely involve creating an [instance](https://docs.cloudstack.apache.org/en/latest/adminguide/templates.html#:~:text=When%20Users%20launch%20Instances%2C%20they,who%20can%20use%20the%20Template.) of the Seed Lab VM manually and then replicating this instance with Terraform for each user who starts a lab. 


