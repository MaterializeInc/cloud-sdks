/*
 * Materialize Cloud
 *
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * API version: 0.1.0
 */

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package mzcloud

import (
	"encoding/json"
)

// PrometheusMetrics Serializer for the prometheus metrics.
type PrometheusMetrics struct {
	Metrics []PrometheusMetric `json:"metrics"`
}

// NewPrometheusMetrics instantiates a new PrometheusMetrics object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewPrometheusMetrics(metrics []PrometheusMetric) *PrometheusMetrics {
	this := PrometheusMetrics{}
	this.Metrics = metrics
	return &this
}

// NewPrometheusMetricsWithDefaults instantiates a new PrometheusMetrics object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewPrometheusMetricsWithDefaults() *PrometheusMetrics {
	this := PrometheusMetrics{}
	return &this
}

// GetMetrics returns the Metrics field value
func (o *PrometheusMetrics) GetMetrics() []PrometheusMetric {
	if o == nil {
		var ret []PrometheusMetric
		return ret
	}

	return o.Metrics
}

// GetMetricsOk returns a tuple with the Metrics field value
// and a boolean to check if the value has been set.
func (o *PrometheusMetrics) GetMetricsOk() (*[]PrometheusMetric, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Metrics, true
}

// SetMetrics sets field value
func (o *PrometheusMetrics) SetMetrics(v []PrometheusMetric) {
	o.Metrics = v
}

func (o PrometheusMetrics) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if true {
		toSerialize["metrics"] = o.Metrics
	}
	return json.Marshal(toSerialize)
}

type NullablePrometheusMetrics struct {
	value *PrometheusMetrics
	isSet bool
}

func (v NullablePrometheusMetrics) Get() *PrometheusMetrics {
	return v.value
}

func (v *NullablePrometheusMetrics) Set(val *PrometheusMetrics) {
	v.value = val
	v.isSet = true
}

func (v NullablePrometheusMetrics) IsSet() bool {
	return v.isSet
}

func (v *NullablePrometheusMetrics) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullablePrometheusMetrics(val *PrometheusMetrics) *NullablePrometheusMetrics {
	return &NullablePrometheusMetrics{value: val, isSet: true}
}

func (v NullablePrometheusMetrics) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullablePrometheusMetrics) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


