# Rust API client for mzcloud

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

## Overview

This API client was generated by the [OpenAPI Generator](https://openapi-generator.tech) project.  By using the [openapi-spec](https://openapis.org) from a remote server, you can easily generate an API client.

- API version: 0.1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.RustClientCodegen

## Installation

Put the package under your project folder and add the following to `Cargo.toml` under `[dependencies]`:

```
    openapi = { path = "./generated" }
```

## Documentation for API Endpoints

All URIs are relative to *https://cloud.materialize.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CloudProvidersApi* | [**cloud_providers_list**](docs/CloudProvidersApi.md#cloud_providers_list) | **GET** /api/cloud-providers | 
*DeploymentsApi* | [**deployments_certs_retrieve**](docs/DeploymentsApi.md#deployments_certs_retrieve) | **GET** /api/deployments/{id}/certs | 
*DeploymentsApi* | [**deployments_changes_list**](docs/DeploymentsApi.md#deployments_changes_list) | **GET** /api/deployments/{id}/changes | 
*DeploymentsApi* | [**deployments_create**](docs/DeploymentsApi.md#deployments_create) | **POST** /api/deployments | 
*DeploymentsApi* | [**deployments_destroy**](docs/DeploymentsApi.md#deployments_destroy) | **DELETE** /api/deployments/{id} | 
*DeploymentsApi* | [**deployments_ip_retrieve**](docs/DeploymentsApi.md#deployments_ip_retrieve) | **GET** /api/deployments/{id}/ip | 
*DeploymentsApi* | [**deployments_list**](docs/DeploymentsApi.md#deployments_list) | **GET** /api/deployments | 
*DeploymentsApi* | [**deployments_logs_retrieve**](docs/DeploymentsApi.md#deployments_logs_retrieve) | **GET** /api/deployments/{id}/logs | 
*DeploymentsApi* | [**deployments_metrics_cpu_retrieve**](docs/DeploymentsApi.md#deployments_metrics_cpu_retrieve) | **GET** /api/deployments/{id}/metrics/cpu/{period} | 
*DeploymentsApi* | [**deployments_metrics_memory_retrieve**](docs/DeploymentsApi.md#deployments_metrics_memory_retrieve) | **GET** /api/deployments/{id}/metrics/memory/{period} | 
*DeploymentsApi* | [**deployments_partial_update**](docs/DeploymentsApi.md#deployments_partial_update) | **PATCH** /api/deployments/{id} | 
*DeploymentsApi* | [**deployments_retrieve**](docs/DeploymentsApi.md#deployments_retrieve) | **GET** /api/deployments/{id} | 
*DeploymentsApi* | [**deployments_secrets_create**](docs/DeploymentsApi.md#deployments_secrets_create) | **POST** /api/deployments/{id}/secrets/{secret} | 
*DeploymentsApi* | [**deployments_secrets_destroy**](docs/DeploymentsApi.md#deployments_secrets_destroy) | **DELETE** /api/deployments/{id}/secrets/{secret} | 
*DeploymentsApi* | [**deployments_secrets_list**](docs/DeploymentsApi.md#deployments_secrets_list) | **GET** /api/deployments/{id}/secrets | 
*DeploymentsApi* | [**deployments_tailscale_logs_retrieve**](docs/DeploymentsApi.md#deployments_tailscale_logs_retrieve) | **GET** /api/deployments/{id}/tailscale_logs | 
*HealthApi* | [**health_retrieve**](docs/HealthApi.md#health_retrieve) | **GET** /api/health | 
*MzVersionsApi* | [**mz_versions_latest_retrieve**](docs/MzVersionsApi.md#mz_versions_latest_retrieve) | **GET** /api/mz-versions/latest | 
*MzVersionsApi* | [**mz_versions_list**](docs/MzVersionsApi.md#mz_versions_list) | **GET** /api/mz-versions | 
*OrganizationsApi* | [**organizations_retrieve**](docs/OrganizationsApi.md#organizations_retrieve) | **GET** /api/organizations/{id} | 
*RegionsApi* | [**regions_list**](docs/RegionsApi.md#regions_list) | **GET** /api/regions/{providerName} | 
*SchemaApi* | [**schema_retrieve**](docs/SchemaApi.md#schema_retrieve) | **GET** /api/schema | 


## Documentation For Models

 - [Deployment](docs/Deployment.md)
 - [DeploymentRequest](docs/DeploymentRequest.md)
 - [DeploymentSizeEnum](docs/DeploymentSizeEnum.md)
 - [HistoricalDeploymentChange](docs/HistoricalDeploymentChange.md)
 - [HistoricalDeploymentDelta](docs/HistoricalDeploymentDelta.md)
 - [HistoricalDeploymentMetadata](docs/HistoricalDeploymentMetadata.md)
 - [ModifiedBoolean](docs/ModifiedBoolean.md)
 - [ModifiedSize](docs/ModifiedSize.md)
 - [ModifiedString](docs/ModifiedString.md)
 - [ModifiedStringList](docs/ModifiedStringList.md)
 - [OperationEnum](docs/OperationEnum.md)
 - [Organization](docs/Organization.md)
 - [PatchedDeploymentUpdateRequest](docs/PatchedDeploymentUpdateRequest.md)
 - [PrometheusMetric](docs/PrometheusMetric.md)
 - [PrometheusMetrics](docs/PrometheusMetrics.md)
 - [ProviderEnum](docs/ProviderEnum.md)
 - [ReleaseTrackEnum](docs/ReleaseTrackEnum.md)
 - [SupportedCloudRegion](docs/SupportedCloudRegion.md)
 - [SupportedCloudRegionRequest](docs/SupportedCloudRegionRequest.md)


To get access to the crate's generated documentation, use:

```
cargo doc --open
```

## Author



