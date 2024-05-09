data "aws_ami" "this" {
  most_recent = true
}


resource "aws_instance" "my_instance" {
  instance_type = "t3.micro"
  ami           = data.aws_ami.this.id
}

provider "aws" {
  region = "us-east-1"
}
