resource "google_compute_network" "vpc_network" {
  #name                    = "my-custom-mode-network"
  name                    = var.vpc_network_name
  auto_create_subnetworks = false
  mtu                     = 1460
}

resource "google_compute_subnetwork" "default" {
  #name          = "my-custom-subnet"
  name          = var.subnet_name
  ip_cidr_range = "10.0.1.0/24"
  region        = "us-west1"
  network       = google_compute_network.vpc_network.id
}

# Create a single Compute Engine instance
resource "google_compute_instance" "default" {
  #name         = "seed-labs-ubuntu-vm"
  name = var.instance_name
  machine_type = "e2-medium"
  zone         = "us-west1-a"
  tags         = ["ssh"]

  boot_disk {
    initialize_params {
      #image = "ubuntu-os-cloud/ubuntu-2004-lts"
      image = "seed-labs-ubuntu"
      size  = 20  # 20GB boot disk size
    }
  }

  metadata_startup_script = "cd /home/seed/Desktop/; wget https://seedsecuritylabs.org/Labs_20.04/Files/ICMP_Redirect/ICMP_Redirect.pdf; wget https://seedsecuritylabs.org/Labs_20.04/Files/ICMP_Redirect/Labsetup.zip; unzip Labsetup.zip; cd Labsetup;"
  network_interface {
    subnetwork = google_compute_subnetwork.default.id

    access_config {
      # Include this section to give the VM an external IP address
    }
  }

  metadata = {
   ssh-keys = "ubuntu:${file("/home/admin_/.ssh/id_rsa.pub")}"  
}

connection {
  type        = "ssh"
  host        = self.network_interface[0].access_config[0].nat_ip
  user        = "ubuntu"  # or the appropriate username
  private_key = file("/home/admin_/.ssh/id_rsa")  # path to your private key
}
}

output "instance_startup_script" {
  value = google_compute_instance.default.metadata_startup_script
  description = "The startup script used by the instance"
}
output "instance_ips" {
  value = "${join(" ", google_compute_instance.default.*.network_interface.0.access_config.0.nat_ip)}"
  description = "The public IP address of the newly created instance"
}


resource "google_compute_firewall" "ssh" {
  name = "${var.instance_name}-allow-ssh"
  allow {
    ports    = ["22"]
    protocol = "tcp"
  }
  direction     = "INGRESS"
  network       = google_compute_network.vpc_network.id
  priority      = 1000
  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["ssh"]
}

resource "google_compute_firewall" "vnc" {
  name = "${var.instance_name}-allow-vnc"
  #name = "allow-vnc-again"
  allow {
    ports    = ["5901-5910"]
    protocol = "tcp"
  }
  direction     = "INGRESS"
  network       = google_compute_network.vpc_network.id
  priority      = 1000
  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["vnc"]
}
