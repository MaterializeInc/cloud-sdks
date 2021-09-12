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
pub struct PatchedDeploymentRequest {
    #[serde(rename = "name", skip_serializing_if = "Option::is_none")]
    pub name: Option<String>,
    #[serde(rename = "size", skip_serializing_if = "Option::is_none")]
    pub size: Option<Box<crate::models::DeploymentSizeEnum>>,
    #[serde(rename = "storageMb", skip_serializing_if = "Option::is_none")]
    pub storage_mb: Option<i32>,
    #[serde(rename = "materializedExtraArgs", skip_serializing_if = "Option::is_none")]
    pub materialized_extra_args: Option<Vec<String>>,
    #[serde(rename = "mzVersion", skip_serializing_if = "Option::is_none")]
    pub mz_version: Option<String>,
}

impl PatchedDeploymentRequest {
    pub fn new() -> PatchedDeploymentRequest {
        PatchedDeploymentRequest {
            name: None,
            size: None,
            storage_mb: None,
            materialized_extra_args: None,
            mz_version: None,
        }
    }
}


