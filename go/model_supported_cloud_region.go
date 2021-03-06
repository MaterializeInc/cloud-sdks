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

// SupportedCloudRegion struct for SupportedCloudRegion
type SupportedCloudRegion struct {
	Provider ProviderEnum `json:"provider"`
	Region string `json:"region"`
}

// NewSupportedCloudRegion instantiates a new SupportedCloudRegion object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewSupportedCloudRegion(provider ProviderEnum, region string) *SupportedCloudRegion {
	this := SupportedCloudRegion{}
	this.Provider = provider
	this.Region = region
	return &this
}

// NewSupportedCloudRegionWithDefaults instantiates a new SupportedCloudRegion object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewSupportedCloudRegionWithDefaults() *SupportedCloudRegion {
	this := SupportedCloudRegion{}
	return &this
}

// GetProvider returns the Provider field value
func (o *SupportedCloudRegion) GetProvider() ProviderEnum {
	if o == nil {
		var ret ProviderEnum
		return ret
	}

	return o.Provider
}

// GetProviderOk returns a tuple with the Provider field value
// and a boolean to check if the value has been set.
func (o *SupportedCloudRegion) GetProviderOk() (*ProviderEnum, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Provider, true
}

// SetProvider sets field value
func (o *SupportedCloudRegion) SetProvider(v ProviderEnum) {
	o.Provider = v
}

// GetRegion returns the Region field value
func (o *SupportedCloudRegion) GetRegion() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Region
}

// GetRegionOk returns a tuple with the Region field value
// and a boolean to check if the value has been set.
func (o *SupportedCloudRegion) GetRegionOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Region, true
}

// SetRegion sets field value
func (o *SupportedCloudRegion) SetRegion(v string) {
	o.Region = v
}

func (o SupportedCloudRegion) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if true {
		toSerialize["provider"] = o.Provider
	}
	if true {
		toSerialize["region"] = o.Region
	}
	return json.Marshal(toSerialize)
}

type NullableSupportedCloudRegion struct {
	value *SupportedCloudRegion
	isSet bool
}

func (v NullableSupportedCloudRegion) Get() *SupportedCloudRegion {
	return v.value
}

func (v *NullableSupportedCloudRegion) Set(val *SupportedCloudRegion) {
	v.value = val
	v.isSet = true
}

func (v NullableSupportedCloudRegion) IsSet() bool {
	return v.isSet
}

func (v *NullableSupportedCloudRegion) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableSupportedCloudRegion(val *SupportedCloudRegion) *NullableSupportedCloudRegion {
	return &NullableSupportedCloudRegion{value: val, isSet: true}
}

func (v NullableSupportedCloudRegion) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableSupportedCloudRegion) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


