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
pub struct Deployment {
    #[serde(rename = "id")]
    pub id: String,
    #[serde(rename = "organization")]
    pub organization: String,
    #[serde(rename = "tlsAuthority")]
    pub tls_authority: Option<String>,
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "hostname")]
    pub hostname: Option<String>,
    #[serde(rename = "flaggedForDeletion")]
    pub flagged_for_deletion: bool,
    #[serde(rename = "flaggedForUpdate")]
    pub flagged_for_update: bool,
    #[serde(rename = "catalogRestoreMode")]
    pub catalog_restore_mode: bool,
    #[serde(rename = "size")]
    pub size: Box<crate::models::DeploymentSizeEnum>,
    #[serde(rename = "storageMb")]
    pub storage_mb: i32,
    #[serde(rename = "disableUserIndexes")]
    pub disable_user_indexes: bool,
    #[serde(rename = "materializedExtraArgs")]
    pub materialized_extra_args: Vec<String>,
    #[serde(rename = "clusterId")]
    pub cluster_id: Option<String>,
    #[serde(rename = "mzVersion")]
    pub mz_version: String,
    #[serde(rename = "releaseTrack")]
    pub release_track: Box<crate::models::ReleaseTrackEnum>,
    #[serde(rename = "status")]
    pub status: String,
    #[serde(rename = "enableTailscale")]
    pub enable_tailscale: bool,
    #[serde(rename = "cloudProviderRegion")]
    pub cloud_provider_region: Box<crate::models::SupportedCloudRegion>,
}

impl Deployment {
    pub fn new(
        id: String,
        organization: String,
        tls_authority: Option<String>,
        name: String,
        hostname: Option<String>,
        flagged_for_deletion: bool,
        flagged_for_update: bool,
        catalog_restore_mode: bool,
        size: crate::models::DeploymentSizeEnum,
        storage_mb: i32,
        disable_user_indexes: bool,
        materialized_extra_args: Vec<String>,
        cluster_id: Option<String>,
        mz_version: String,
        release_track: crate::models::ReleaseTrackEnum,
        status: String,
        enable_tailscale: bool,
        cloud_provider_region: crate::models::SupportedCloudRegion,
    ) -> Deployment {
        Deployment {
            id,
            organization,
            tls_authority,
            name,
            hostname,
            flagged_for_deletion,
            flagged_for_update,
            catalog_restore_mode,
            size: Box::new(size),
            storage_mb,
            disable_user_indexes,
            materialized_extra_args,
            cluster_id,
            mz_version,
            release_track: Box::new(release_track),
            status,
            enable_tailscale,
            cloud_provider_region: Box::new(cloud_provider_region),
        }
    }
}
