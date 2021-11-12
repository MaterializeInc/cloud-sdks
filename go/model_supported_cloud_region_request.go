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

// SupportedCloudRegionRequest struct for SupportedCloudRegionRequest
type SupportedCloudRegionRequest struct {
	Provider ProviderEnum `json:"provider"`
	Region string `json:"region"`
}

// NewSupportedCloudRegionRequest instantiates a new SupportedCloudRegionRequest object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewSupportedCloudRegionRequest(provider ProviderEnum, region string) *SupportedCloudRegionRequest {
	this := SupportedCloudRegionRequest{}
	this.Provider = provider
	this.Region = region
	return &this
}

// NewSupportedCloudRegionRequestWithDefaults instantiates a new SupportedCloudRegionRequest object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewSupportedCloudRegionRequestWithDefaults() *SupportedCloudRegionRequest {
	this := SupportedCloudRegionRequest{}
	return &this
}

// GetProvider returns the Provider field value
func (o *SupportedCloudRegionRequest) GetProvider() ProviderEnum {
	if o == nil {
		var ret ProviderEnum
		return ret
	}

	return o.Provider
}

// GetProviderOk returns a tuple with the Provider field value
// and a boolean to check if the value has been set.
func (o *SupportedCloudRegionRequest) GetProviderOk() (*ProviderEnum, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Provider, true
}

// SetProvider sets field value
func (o *SupportedCloudRegionRequest) SetProvider(v ProviderEnum) {
	o.Provider = v
}

// GetRegion returns the Region field value
func (o *SupportedCloudRegionRequest) GetRegion() string {
	if o == nil {
		var ret string
		return ret
	}

	return o.Region
}

// GetRegionOk returns a tuple with the Region field value
// and a boolean to check if the value has been set.
func (o *SupportedCloudRegionRequest) GetRegionOk() (*string, bool) {
	if o == nil  {
		return nil, false
	}
	return &o.Region, true
}

// SetRegion sets field value
func (o *SupportedCloudRegionRequest) SetRegion(v string) {
	o.Region = v
}

func (o SupportedCloudRegionRequest) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if true {
		toSerialize["provider"] = o.Provider
	}
	if true {
		toSerialize["region"] = o.Region
	}
	return json.Marshal(toSerialize)
}

type NullableSupportedCloudRegionRequest struct {
	value *SupportedCloudRegionRequest
	isSet bool
}

func (v NullableSupportedCloudRegionRequest) Get() *SupportedCloudRegionRequest {
	return v.value
}

func (v *NullableSupportedCloudRegionRequest) Set(val *SupportedCloudRegionRequest) {
	v.value = val
	v.isSet = true
}

func (v NullableSupportedCloudRegionRequest) IsSet() bool {
	return v.isSet
}

func (v *NullableSupportedCloudRegionRequest) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullableSupportedCloudRegionRequest(val *SupportedCloudRegionRequest) *NullableSupportedCloudRegionRequest {
	return &NullableSupportedCloudRegionRequest{value: val, isSet: true}
}

func (v NullableSupportedCloudRegionRequest) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullableSupportedCloudRegionRequest) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}


