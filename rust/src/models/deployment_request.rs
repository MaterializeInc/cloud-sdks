/*
 * Materialize Cloud
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 *
 * Generated by: https://openapi-generator.tech
 */

#[derive(Clone, Debug, PartialEq, Serialize, Deserialize)]
pub struct DeploymentRequest {
    #[serde(rename = "name", skip_serializing_if = "Option::is_none")]
    pub name: Option<String>,
    #[serde(rename = "catalogRestoreMode", skip_serializing_if = "Option::is_none")]
    pub catalog_restore_mode: Option<bool>,
    #[serde(rename = "size", skip_serializing_if = "Option::is_none")]
    pub size: Option<Box<crate::models::DeploymentSizeEnum>>,
    #[serde(rename = "storageMb", skip_serializing_if = "Option::is_none")]
    pub storage_mb: Option<i32>,
    #[serde(rename = "disableUserIndexes", skip_serializing_if = "Option::is_none")]
    pub disable_user_indexes: Option<bool>,
    #[serde(
        rename = "materializedExtraArgs",
        skip_serializing_if = "Option::is_none"
    )]
    pub materialized_extra_args: Option<Vec<String>>,
    #[serde(rename = "mzVersion", skip_serializing_if = "Option::is_none")]
    pub mz_version: Option<String>,
    #[serde(rename = "releaseTrack", skip_serializing_if = "Option::is_none")]
    pub release_track: Option<Box<crate::models::ReleaseTrackEnum>>,
    #[serde(rename = "enableTailscale", skip_serializing_if = "Option::is_none")]
    pub enable_tailscale: Option<bool>,
    #[serde(rename = "tailscaleAuthKey", skip_serializing_if = "Option::is_none")]
    pub tailscale_auth_key: Option<String>,
    #[serde(rename = "cloudProviderRegion")]
    pub cloud_provider_region: Box<crate::models::SupportedCloudRegionRequest>,
}

impl DeploymentRequest {
    pub fn new(
        cloud_provider_region: crate::models::SupportedCloudRegionRequest,
    ) -> DeploymentRequest {
        DeploymentRequest {
            name: None,
            catalog_restore_mode: None,
            size: None,
            storage_mb: None,
            disable_user_indexes: None,
            materialized_extra_args: None,
            mz_version: None,
            release_track: None,
            enable_tailscale: None,
            tailscale_auth_key: None,
            cloud_provider_region: Box::new(cloud_provider_region),
        }
    }
}
