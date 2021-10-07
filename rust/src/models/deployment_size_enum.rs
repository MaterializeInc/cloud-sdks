/*
 * Materialize Cloud
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 * Generated by: https://openapi-generator.tech
 */


/// 
#[derive(Clone, Copy, Debug, Eq, PartialEq, Ord, PartialOrd, Hash, Serialize, Deserialize)]
pub enum DeploymentSizeEnum {
    #[serde(rename = "XS")]
    XS,
    #[serde(rename = "S")]
    S,
    #[serde(rename = "M")]
    M,
    #[serde(rename = "L")]
    L,
    #[serde(rename = "XL")]
    XL,

}

impl ToString for DeploymentSizeEnum {
    fn to_string(&self) -> String {
        match self {
            Self::XS => String::from("XS"),
            Self::S => String::from("S"),
            Self::M => String::from("M"),
            Self::L => String::from("L"),
            Self::XL => String::from("XL"),
        }
    }
}



