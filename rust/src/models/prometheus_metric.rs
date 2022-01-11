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
pub struct PrometheusMetric {
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "values")]
    pub values: Vec<Vec<String>>,
}

impl PrometheusMetric {
    pub fn new(name: String, values: Vec<Vec<String>>) -> PrometheusMetric {
        PrometheusMetric { name, values }
    }
}