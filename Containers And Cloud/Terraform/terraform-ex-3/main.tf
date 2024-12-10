terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.13.0"
    }
  }
}

provider "azurerm" {
  subscription_id = "59f109cd-dc2a-4348-b16c-34007e9c3ea9"
  features {
  }
}

resource "random_integer" "randomInteger" {
  min = 10000
  max = 99999
}

resource "azurerm_resource_group" "TerraformResourceGroup" {
  name     = "TerraformResourceGroup-${random_integer.randomInteger.result}"
  location = "North Europe"
}

resource "azurerm_service_plan" "TerraformServicePlan" {
  name                = "TerraformServicePlan-${random_integer.randomInteger.result}"
  resource_group_name = azurerm_resource_group.TerraformResourceGroup.name
  os_type             = "Linux"
  sku_name            = "F1"
  location            = azurerm_resource_group.TerraformResourceGroup.location
}

resource "azurerm_linux_web_app" "Taskboard" {
  name                = "Taskboard-${random_integer.randomInteger.result}"
  resource_group_name = azurerm_resource_group.TerraformResourceGroup.name
  location            = azurerm_resource_group.TerraformResourceGroup.location
  service_plan_id     = azurerm_service_plan.TerraformServicePlan.id
  site_config {
    application_stack {
      dotnet_version = "6.0"
    }
    always_on = false
  }
  connection_string {
    name  = "DefaultConnection"
    type  = "SQLAzure"
    value = "Data Source=tcp:${azurerm_mssql_server.SQLServerTaskboard.fully_qualified_domain_name},1433;Initial Catalog=${azurerm_mssql_database.SQLDatabaseTaskboard.name};User ID=${azurerm_mssql_server.SQLServerTaskboard.administrator_login};Password=${azurerm_mssql_server.SQLServerTaskboard.administrator_login_password};Trusted_Connection=False; MultipleActiveResultSets=True;"
  }
}

resource "azurerm_mssql_server" "SQLServerTaskboard" {
  name                         = "sqlservertaskboard"
  resource_group_name          = azurerm_resource_group.TerraformResourceGroup.name
  location                     = azurerm_resource_group.TerraformResourceGroup.location
  version                      = "12.0"
  administrator_login          = "4dm1n157r470r"
  administrator_login_password = "4-v3ry-53cr37-p455w0rd"
}

resource "azurerm_mssql_database" "SQLDatabaseTaskboard" {
  name           = "TaskboardDB"
  server_id      = azurerm_mssql_server.SQLServerTaskboard.id
  collation      = "SQL_Latin1_General_CP1_CI_AS"
  license_type   = "LicenseIncluded"
  max_size_gb    = 2
  sku_name       = "S0"
  zone_redundant = false
}

resource "azurerm_app_service_source_control" "TerraformSourceControl" {
  app_id                 = azurerm_linux_web_app.Taskboard.id
  repo_url               = "https://github.com/dimosoftuni/azure-web-app-with-database-taskboard"
  branch                 = "main"
  use_manual_integration = true
}

resource "azurerm_mssql_firewall_rule" "GithubFirewallRule" {
  name             = "TaskboardFirewallRule"
  server_id        = azurerm_mssql_server.SQLServerTaskboard.id
  start_ip_address = "0.0.0.0"
  end_ip_address   = "0.0.0.0"
}
