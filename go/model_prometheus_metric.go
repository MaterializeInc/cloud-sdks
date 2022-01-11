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

// PrometheusMetric struct for PrometheusMetric
type PrometheusMetric struct {
	Name string `json:"name"`
	Values [][]string `json:"values"`
}

// NewPrometheusMetric instantiates a new PrometheusMetric object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewPrometheusMetric(name string, values [][]string) *PrometheusMetric {
	this := PrometheusMetric{}
	this.Name = name
	this.Values = values
	return &this
}

// NewPrometheusMetricWithDefaults instantiates a new PrometheusMetric object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewPrometheusMetricWithDefaults() *PrometheusMetric {
	this := PrometheusMetric{}
	return &this
}

// GetName returns the Name field value
func (o *PrometheusMetric) GetName() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Name
}

// GetNameOk returns a tuple with the Name field value
// and a boolean to check if the value has been set.
func (o *PrometheusMetric) GetNameOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Name, true
}

// SetName sets field value
func (o *PrometheusMetric) SetName(v string) {
	o.Name = v
}

// GetValues returns the Values field value
func (o *PrometheusMetric) GetValues() [][]string {
	if o == nil {
		var ret [][]string
		return ret
	}

	return o.Values
}

// GetValuesOk returns a tuple with the Values field value
// and a boolean to check if the value has been set.
func (o *PrometheusMetric) GetValuesOk() (*[][]string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Values, true
}

// SetValues sets field value
func (o *PrometheusMetric) SetValues(v [][]string) {
	o.Values = v
}

func (o PrometheusMetric) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if true {
		toSerialize["name"] = o.Name
	}
	if true {
		toSerialize["values"] = o.Values
	}
	return json.Marshal(toSerialize)
}

type NullablePrometheusMetric struct {
	value *PrometheusMetric
	isSet bool
}

func (v NullablePrometheusMetric) Get() *PrometheusMetric {
	return v.value
}

func (v *NullablePrometheusMetric) Set(val *PrometheusMetric) {
	v.value = val
	v.isSet = true
}

func (v NullablePrometheusMetric) IsSet() bool {
	return v.isSet
}

func (v *NullablePrometheusMetric) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullablePrometheusMetric(val *PrometheusMetric) *NullablePrometheusMetric {
	return &NullablePrometheusMetric{value: val, isSet: true}
}

func (v NullablePrometheusMetric) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullablePrometheusMetric) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}

