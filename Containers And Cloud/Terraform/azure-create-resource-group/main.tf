terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "4.13.0"
    }
  }
}

provider "azurerm" {
  subscription_id = ""
  features {
    
  }
}

resource "azurerm_resource_group" "TerraformResourseGroup" {
  name     = "TerraformResourceGroup"
  location = "West Europe"
}
