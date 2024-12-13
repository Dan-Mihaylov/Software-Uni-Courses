output "app_ips" {
  value       = azurerm_linux_web_app.alwa.outbound_ip_address_list
  description = "The IP of the application"
}

output "app_url" {
  value       = azurerm_linux_web_app.alwa.default_hostname
  description = "The url of the application"
}